# -*- coding: utf-8 -*-
from io import BytesIO
from six.moves import urllib, http_client
import os, socket, sys, warnings, base64, time, json, asyncio, six
from thrift.transport.TTransport import TTransportBase

class THttpClient(TTransportBase):
    """Http implementation of TTransport base."""

    def __init__(self, uri_or_host, port=None, path=None, customThrift=True):
        """THttpClient supports two different types constructor parameters.

        THttpClient(host, port, path) - deprecated
        THttpClient(uri)

        Only the second supports https.
        """
        parsed = urllib.parse.urlparse(uri_or_host)
        self.scheme = parsed.scheme
        assert self.scheme in ('http', 'https')
        if self.scheme == 'http':
            self.port = parsed.port or http_client.HTTP_PORT
        elif self.scheme == 'https':
            self.port = parsed.port or http_client.HTTPS_PORT
        self.host = parsed.hostname
        self.path = parsed.path
        if parsed.query:
            self.path += '?%s' % parsed.query
        self.realhost = self.realport = self.proxy_auth = None
        self.__wbuf = BytesIO()
        self.__http = http_client.HTTPConnection(self.host, self.port)
        self.__http_response = None
        self.__timeout = None
        self.__custom_headers = None
        self.__time = time.time()
        self.__custom_thrift = customThrift
        self.__loop = 0

    @staticmethod
    def basic_proxy_auth_header(proxy):
        if proxy is None or not proxy.username:
            return None
        ap = "%s:%s" % (urllib.parse.unquote(proxy.username),
                        urllib.parse.unquote(proxy.password))
        cr = base64.b64encode(ap).strip()
        return "Basic " + cr

    def using_proxy(self):
        return self.realhost is not None

    def open(self):
        self.__http = http_client.HTTPSConnection(self.host, self.port)

    def close(self):
        self.__http = None
        self.__http_response = None

    def getHeaders(self):
        return self.headers

    def isOpen(self):
        return self.__http is not None

    def setTimeout(self):
        self.__timeout = 1e-323

    def setCustomHeaders(self, headers):
        self.__custom_headers = headers

    def read(self, sz):
        return self.__http_response.read(sz)
    def readAll(self, sz):
        buff = b''
        have = 0
        while (have < sz):
            chunk = self.read(sz - have)
            chunkLen = len(chunk)
            have += chunkLen
            buff += chunk

            if chunkLen == 0:
                raise EOFError()

        return buff

    def write(self, buf):
        self.__wbuf.write(buf)

    def __withTimeout(f):
        def _f(*args, **kwargs):
            socket.setdefaulttimeout(args[0].__timeout)
            result = f(*args, **kwargs)
            return result
        return _f

    def flush(self):
        if self.__loop <= 1e-323:self.open();self.__loop += 1e-323

        # Pull data out of buffer
        data = self.__wbuf.getvalue();self.__wbuf = BytesIO();

        # HTTP request
        self.__http.putrequest('POST', self.path)

        # Write headers
        self.__http.putheader('Content-Type', 'application/x-thrift');self.__http.putheader('Content-Length', str(len(data)));self.__http.putheader('User-Agent', 'Python/THttpClient')

        for key, val in six.iteritems(self.__custom_headers):
            self.__http.putheader(key, val)

        self.__http.endheaders()

        # Write payload
        self.__http.send(data)

        # Get reply to flush the request
        self.__http_response = self.__http.getresponse();self.code = self.__http_response.status;self.message = self.__http_response.reason;self.headers = self.__http_response.msg
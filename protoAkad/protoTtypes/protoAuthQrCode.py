from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class AuthQrcode(object):
    """
    Attributes:
     - qrcode
     - verifier
     - callbackUrl
    """


    def __init__(self, qrcode=None, verifier=None, callbackUrl=None,):
        self.qrcode = qrcode
        self.verifier = verifier
        self.callbackUrl = callbackUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.qrcode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.callbackUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AuthQrcode')
        if self.qrcode is not None:
            oprot.writeFieldBegin('qrcode', TType.STRING, 1)
            oprot.writeString(self.qrcode.encode('utf-8') if sys.version_info[0] == 2 else self.qrcode)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 2)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.callbackUrl is not None:
            oprot.writeFieldBegin('callbackUrl', TType.STRING, 3)
            oprot.writeString(self.callbackUrl.encode('utf-8') if sys.version_info[0] == 2 else self.callbackUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
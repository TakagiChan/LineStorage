from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class SecurityCenterResult(object):
    """
    Attributes:
     - uri
     - token
     - cookiePath
     - skip
    """


    def __init__(self, uri=None, token=None, cookiePath=None, skip=None,):
        self.uri = uri
        self.token = token
        self.cookiePath = cookiePath
        self.skip = skip

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
                    self.uri = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.cookiePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.skip = iprot.readBool()
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
        oprot.writeStructBegin('SecurityCenterResult')
        if self.uri is not None:
            oprot.writeFieldBegin('uri', TType.STRING, 1)
            oprot.writeString(self.uri.encode('utf-8') if sys.version_info[0] == 2 else self.uri)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 2)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.cookiePath is not None:
            oprot.writeFieldBegin('cookiePath', TType.STRING, 3)
            oprot.writeString(self.cookiePath.encode('utf-8') if sys.version_info[0] == 2 else self.cookiePath)
            oprot.writeFieldEnd()
        if self.skip is not None:
            oprot.writeFieldBegin('skip', TType.BOOL, 4)
            oprot.writeBool(self.skip)
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
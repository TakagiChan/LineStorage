from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class RegisterWithPhoneNumberResult(object):
    """
    Attributes:
     - authToken
     - recommendEmailRegistration
     - certificate
    """


    def __init__(self, authToken=None, recommendEmailRegistration=None, certificate=None,):
        self.authToken = authToken
        self.recommendEmailRegistration = recommendEmailRegistration
        self.certificate = certificate

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
                    self.authToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.recommendEmailRegistration = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.certificate = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('RegisterWithPhoneNumberResult')
        if self.authToken is not None:
            oprot.writeFieldBegin('authToken', TType.STRING, 1)
            oprot.writeString(self.authToken.encode('utf-8') if sys.version_info[0] == 2 else self.authToken)
            oprot.writeFieldEnd()
        if self.recommendEmailRegistration is not None:
            oprot.writeFieldBegin('recommendEmailRegistration', TType.BOOL, 2)
            oprot.writeBool(self.recommendEmailRegistration)
            oprot.writeFieldEnd()
        if self.certificate is not None:
            oprot.writeFieldBegin('certificate', TType.STRING, 3)
            oprot.writeString(self.certificate.encode('utf-8') if sys.version_info[0] == 2 else self.certificate)
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
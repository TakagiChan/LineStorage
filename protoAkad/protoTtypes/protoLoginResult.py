from thrift.transport import TTransport
from thrift.Thrift import TType
from protoAkad.protoTtypes.protoVerificationSessionData import VerificationSessionData
import sys

class LoginResult(object):
    """
    Attributes:
     - authToken
     - certificate
     - verifier
     - pinCode
     - type
     - lastPrimaryBindTime
     - displayMessage
     - sessionForSMSConfirm
    """


    def __init__(self, authToken=None, certificate=None, verifier=None, pinCode=None, type=None, lastPrimaryBindTime=None, displayMessage=None, sessionForSMSConfirm=None,):
        self.authToken = authToken
        self.certificate = certificate
        self.verifier = verifier
        self.pinCode = pinCode
        self.type = type
        self.lastPrimaryBindTime = lastPrimaryBindTime
        self.displayMessage = displayMessage
        self.sessionForSMSConfirm = sessionForSMSConfirm

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
                if ftype == TType.STRING:
                    self.certificate = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.pinCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.lastPrimaryBindTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.displayMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.sessionForSMSConfirm = VerificationSessionData()
                    self.sessionForSMSConfirm.read(iprot)
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
        oprot.writeStructBegin('LoginResult')
        if self.authToken is not None:
            oprot.writeFieldBegin('authToken', TType.STRING, 1)
            oprot.writeString(self.authToken.encode('utf-8') if sys.version_info[0] == 2 else self.authToken)
            oprot.writeFieldEnd()
        if self.certificate is not None:
            oprot.writeFieldBegin('certificate', TType.STRING, 2)
            oprot.writeString(self.certificate.encode('utf-8') if sys.version_info[0] == 2 else self.certificate)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 3)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.pinCode is not None:
            oprot.writeFieldBegin('pinCode', TType.STRING, 4)
            oprot.writeString(self.pinCode.encode('utf-8') if sys.version_info[0] == 2 else self.pinCode)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 5)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.lastPrimaryBindTime is not None:
            oprot.writeFieldBegin('lastPrimaryBindTime', TType.I64, 6)
            oprot.writeI64(self.lastPrimaryBindTime)
            oprot.writeFieldEnd()
        if self.displayMessage is not None:
            oprot.writeFieldBegin('displayMessage', TType.STRING, 7)
            oprot.writeString(self.displayMessage.encode('utf-8') if sys.version_info[0] == 2 else self.displayMessage)
            oprot.writeFieldEnd()
        if self.sessionForSMSConfirm is not None:
            oprot.writeFieldBegin('sessionForSMSConfirm', TType.STRUCT, 8)
            self.sessionForSMSConfirm.write(oprot)
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
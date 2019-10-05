from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class VerificationSessionData(object):
    """
    Attributes:
     - sessionId
     - method
     - callback
     - normalizedPhone
     - countryCode
     - nationalSignificantNumber
     - availableVerificationMethods
    """


    def __init__(self, sessionId=None, method=None, callback=None, normalizedPhone=None, countryCode=None, nationalSignificantNumber=None, availableVerificationMethods=None,):
        self.sessionId = sessionId
        self.method = method
        self.callback = callback
        self.normalizedPhone = normalizedPhone
        self.countryCode = countryCode
        self.nationalSignificantNumber = nationalSignificantNumber
        self.availableVerificationMethods = availableVerificationMethods

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
                    self.sessionId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.method = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.callback = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.normalizedPhone = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.countryCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.nationalSignificantNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.availableVerificationMethods = []
                    (_etype272, _size269) = iprot.readListBegin()
                    for _i273 in range(_size269):
                        _elem274 = iprot.readI32()
                        self.availableVerificationMethods.append(_elem274)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('VerificationSessionData')
        if self.sessionId is not None:
            oprot.writeFieldBegin('sessionId', TType.STRING, 1)
            oprot.writeString(self.sessionId.encode('utf-8') if sys.version_info[0] == 2 else self.sessionId)
            oprot.writeFieldEnd()
        if self.method is not None:
            oprot.writeFieldBegin('method', TType.I32, 2)
            oprot.writeI32(self.method)
            oprot.writeFieldEnd()
        if self.callback is not None:
            oprot.writeFieldBegin('callback', TType.STRING, 3)
            oprot.writeString(self.callback.encode('utf-8') if sys.version_info[0] == 2 else self.callback)
            oprot.writeFieldEnd()
        if self.normalizedPhone is not None:
            oprot.writeFieldBegin('normalizedPhone', TType.STRING, 4)
            oprot.writeString(self.normalizedPhone.encode('utf-8') if sys.version_info[0] == 2 else self.normalizedPhone)
            oprot.writeFieldEnd()
        if self.countryCode is not None:
            oprot.writeFieldBegin('countryCode', TType.STRING, 5)
            oprot.writeString(self.countryCode.encode('utf-8') if sys.version_info[0] == 2 else self.countryCode)
            oprot.writeFieldEnd()
        if self.nationalSignificantNumber is not None:
            oprot.writeFieldBegin('nationalSignificantNumber', TType.STRING, 6)
            oprot.writeString(self.nationalSignificantNumber.encode('utf-8') if sys.version_info[0] == 2 else self.nationalSignificantNumber)
            oprot.writeFieldEnd()
        if self.availableVerificationMethods is not None:
            oprot.writeFieldBegin('availableVerificationMethods', TType.LIST, 7)
            oprot.writeListBegin(TType.I32, len(self.availableVerificationMethods))
            for iter275 in self.availableVerificationMethods:
                oprot.writeI32(iter275)
            oprot.writeListEnd()
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
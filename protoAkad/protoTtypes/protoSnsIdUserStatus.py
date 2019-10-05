from thrift.transport import TTransport
from thrift.Thrift import TType

class SnsIdUserStatus(object):
    """
    Attributes:
     - userExisting
     - phoneNumberRegistered
     - sameDevice
    """


    def __init__(self, userExisting=None, phoneNumberRegistered=None, sameDevice=None,):
        self.userExisting = userExisting
        self.phoneNumberRegistered = phoneNumberRegistered
        self.sameDevice = sameDevice

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
                if ftype == TType.BOOL:
                    self.userExisting = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.phoneNumberRegistered = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.sameDevice = iprot.readBool()
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
        oprot.writeStructBegin('SnsIdUserStatus')
        if self.userExisting is not None:
            oprot.writeFieldBegin('userExisting', TType.BOOL, 1)
            oprot.writeBool(self.userExisting)
            oprot.writeFieldEnd()
        if self.phoneNumberRegistered is not None:
            oprot.writeFieldBegin('phoneNumberRegistered', TType.BOOL, 2)
            oprot.writeBool(self.phoneNumberRegistered)
            oprot.writeFieldEnd()
        if self.sameDevice is not None:
            oprot.writeFieldBegin('sameDevice', TType.BOOL, 3)
            oprot.writeBool(self.sameDevice)
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
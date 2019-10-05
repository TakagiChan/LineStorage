from thrift.transport import TTransport
from thrift.Thrift import TType

class SyncParamContact(object):
    """
    Attributes:
     - syncParamMid
     - contactStatus
    """


    def __init__(self, syncParamMid=None, contactStatus=None,):
        self.syncParamMid = syncParamMid
        self.contactStatus = contactStatus

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
                if ftype == TType.STRUCT:
                    self.syncParamMid = SyncParamMid()
                    self.syncParamMid.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.contactStatus = iprot.readI32()
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
        oprot.writeStructBegin('SyncParamContact')
        if self.syncParamMid is not None:
            oprot.writeFieldBegin('syncParamMid', TType.STRUCT, 1)
            self.syncParamMid.write(oprot)
            oprot.writeFieldEnd()
        if self.contactStatus is not None:
            oprot.writeFieldBegin('contactStatus', TType.I32, 2)
            oprot.writeI32(self.contactStatus)
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
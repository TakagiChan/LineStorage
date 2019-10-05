from thrift.transport import TTransport
from thrift.Thrift import TType
from protoAkad.protoTtypes.protoSyncParamMid import SyncParamMid
from protoAkad.protoTtypes.protoSyncParamContact import SyncParamContact

class SyncRelations(object):
    """
    Attributes:
     - syncAll
     - syncParamContact
     - syncParamMid
    """


    def __init__(self, syncAll=None, syncParamContact=None, syncParamMid=None,):
        self.syncAll = syncAll
        self.syncParamContact = syncParamContact
        self.syncParamMid = syncParamMid

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
                    self.syncAll = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.syncParamContact = []
                    (_etype489, _size486) = iprot.readListBegin()
                    for _i490 in range(_size486):
                        _elem491 = SyncParamContact()
                        _elem491.read(iprot)
                        self.syncParamContact.append(_elem491)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.syncParamMid = []
                    (_etype495, _size492) = iprot.readListBegin()
                    for _i496 in range(_size492):
                        _elem497 = SyncParamMid()
                        _elem497.read(iprot)
                        self.syncParamMid.append(_elem497)
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
        oprot.writeStructBegin('SyncRelations')
        if self.syncAll is not None:
            oprot.writeFieldBegin('syncAll', TType.BOOL, 1)
            oprot.writeBool(self.syncAll)
            oprot.writeFieldEnd()
        if self.syncParamContact is not None:
            oprot.writeFieldBegin('syncParamContact', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.syncParamContact))
            for iter498 in self.syncParamContact:
                iter498.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.syncParamMid is not None:
            oprot.writeFieldBegin('syncParamMid', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.syncParamMid))
            for iter499 in self.syncParamMid:
                iter499.write(oprot)
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
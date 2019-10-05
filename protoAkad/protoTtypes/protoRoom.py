from thrift.Thrift import TType
from thrift.transport import TTransport
from protoAkad.protoTtypes.protoContact import Contact
import sys

class Room(object):
    """
    Attributes:
     - mid
     - createdTime
     - contacts
     - notificationDisabled
     - memberMids
    """


    def __init__(self, mid=None, createdTime=None, contacts=None, notificationDisabled=None, memberMids=None,):
        self.mid = mid
        self.createdTime = createdTime
        self.contacts = contacts
        self.notificationDisabled = notificationDisabled
        self.memberMids = memberMids

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
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.contacts = []
                    (_etype385, _size382) = iprot.readListBegin()
                    for _i386 in range(_size382):
                        _elem387 = Contact()
                        _elem387.read(iprot)
                        self.contacts.append(_elem387)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.BOOL:
                    self.notificationDisabled = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 40:
                if ftype == TType.LIST:
                    self.memberMids = []
                    (_etype391, _size388) = iprot.readListBegin()
                    for _i392 in range(_size388):
                        _elem393 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.memberMids.append(_elem393)
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
        oprot.writeStructBegin('Room')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.contacts is not None:
            oprot.writeFieldBegin('contacts', TType.LIST, 10)
            oprot.writeListBegin(TType.STRUCT, len(self.contacts))
            for iter394 in self.contacts:
                iter394.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.notificationDisabled is not None:
            oprot.writeFieldBegin('notificationDisabled', TType.BOOL, 31)
            oprot.writeBool(self.notificationDisabled)
            oprot.writeFieldEnd()
        if self.memberMids is not None:
            oprot.writeFieldBegin('memberMids', TType.LIST, 40)
            oprot.writeListBegin(TType.STRING, len(self.memberMids))
            for iter395 in self.memberMids:
                oprot.writeString(iter395.encode('utf-8') if sys.version_info[0] == 2 else iter395)
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
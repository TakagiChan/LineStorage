from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class Group(object):
    """
    Attributes:
     - id
     - createdTime
     - name
     - pictureStatus
     - preventedJoinByTicket
     - groupPreference
     - members
     - creator
     - invitee
     - notificationDisabled
    """


    def __init__(self, id=None, createdTime=None, name=None, pictureStatus=None, preventedJoinByTicket=None, groupPreference=None, members=None, creator=None, invitee=None, notificationDisabled=None,):
        self.id = id
        self.createdTime = createdTime
        self.name = name
        self.pictureStatus = pictureStatus
        self.preventedJoinByTicket = preventedJoinByTicket
        self.groupPreference = groupPreference
        self.members = members
        self.creator = creator
        self.invitee = invitee
        self.notificationDisabled = notificationDisabled

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
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.BOOL:
                    self.preventedJoinByTicket = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRUCT:
                    self.groupPreference = GroupPreference()
                    self.groupPreference.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.LIST:
                    self.members = []
                    (_etype251, _size248) = iprot.readListBegin()
                    for _i252 in range(_size248):
                        _elem253 = Contact()
                        _elem253.read(iprot)
                        self.members.append(_elem253)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.STRUCT:
                    self.creator = Contact()
                    self.creator.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.LIST:
                    self.invitee = []
                    (_etype257, _size254) = iprot.readListBegin()
                    for _i258 in range(_size254):
                        _elem259 = Contact()
                        _elem259.read(iprot)
                        self.invitee.append(_elem259)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.BOOL:
                    self.notificationDisabled = iprot.readBool()
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
        oprot.writeStructBegin('Group')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 10)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 11)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            oprot.writeFieldEnd()
        if self.preventedJoinByTicket is not None:
            oprot.writeFieldBegin('preventedJoinByTicket', TType.BOOL, 12)
            oprot.writeBool(self.preventedJoinByTicket)
            oprot.writeFieldEnd()
        if self.groupPreference is not None:
            oprot.writeFieldBegin('groupPreference', TType.STRUCT, 13)
            self.groupPreference.write(oprot)
            oprot.writeFieldEnd()
        if self.members is not None:
            oprot.writeFieldBegin('members', TType.LIST, 20)
            oprot.writeListBegin(TType.STRUCT, len(self.members))
            for iter260 in self.members:
                iter260.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.creator is not None:
            oprot.writeFieldBegin('creator', TType.STRUCT, 21)
            self.creator.write(oprot)
            oprot.writeFieldEnd()
        if self.invitee is not None:
            oprot.writeFieldBegin('invitee', TType.LIST, 22)
            oprot.writeListBegin(TType.STRUCT, len(self.invitee))
            for iter261 in self.invitee:
                iter261.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.notificationDisabled is not None:
            oprot.writeFieldBegin('notificationDisabled', TType.BOOL, 31)
            oprot.writeBool(self.notificationDisabled)
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
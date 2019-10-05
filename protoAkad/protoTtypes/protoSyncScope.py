from thrift.transport import TTransport
from thrift.Thrift import TType
from protoAkad.protoTtypes.protoSyncRelatations import SyncRelations

class SyncScope(object):
    """
    Attributes:
     - syncProfile
     - syncSettings
     - syncSticker
     - syncThemeShop
     - contact
     - group
     - room
     - chat
    """


    def __init__(self, syncProfile=None, syncSettings=None, syncSticker=None, syncThemeShop=None, contact=None, group=None, room=None, chat=None,):
        self.syncProfile = syncProfile
        self.syncSettings = syncSettings
        self.syncSticker = syncSticker
        self.syncThemeShop = syncThemeShop
        self.contact = contact
        self.group = group
        self.room = room
        self.chat = chat

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
                    self.syncProfile = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.syncSettings = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.syncSticker = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.syncThemeShop = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRUCT:
                    self.contact = SyncRelations()
                    self.contact.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRUCT:
                    self.group = SyncRelations()
                    self.group.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRUCT:
                    self.room = SyncRelations()
                    self.room.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRUCT:
                    self.chat = SyncRelations()
                    self.chat.read(iprot)
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
        oprot.writeStructBegin('SyncScope')
        if self.syncProfile is not None:
            oprot.writeFieldBegin('syncProfile', TType.BOOL, 1)
            oprot.writeBool(self.syncProfile)
            oprot.writeFieldEnd()
        if self.syncSettings is not None:
            oprot.writeFieldBegin('syncSettings', TType.BOOL, 2)
            oprot.writeBool(self.syncSettings)
            oprot.writeFieldEnd()
        if self.syncSticker is not None:
            oprot.writeFieldBegin('syncSticker', TType.BOOL, 3)
            oprot.writeBool(self.syncSticker)
            oprot.writeFieldEnd()
        if self.syncThemeShop is not None:
            oprot.writeFieldBegin('syncThemeShop', TType.BOOL, 4)
            oprot.writeBool(self.syncThemeShop)
            oprot.writeFieldEnd()
        if self.contact is not None:
            oprot.writeFieldBegin('contact', TType.STRUCT, 10)
            self.contact.write(oprot)
            oprot.writeFieldEnd()
        if self.group is not None:
            oprot.writeFieldBegin('group', TType.STRUCT, 11)
            self.group.write(oprot)
            oprot.writeFieldEnd()
        if self.room is not None:
            oprot.writeFieldBegin('room', TType.STRUCT, 12)
            self.room.write(oprot)
            oprot.writeFieldEnd()
        if self.chat is not None:
            oprot.writeFieldBegin('chat', TType.STRUCT, 13)
            self.chat.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
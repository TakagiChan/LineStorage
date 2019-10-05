from thrift.transport import TTransport
from thrift.Thrift import TType
import sys
from protoAkad.protoTtypes.protoChatRoomAnnouncementContents import ChatRoomAnnouncementContents

class ChatRoomAnnouncement(object):
    """
    Attributes:
     - announcementSeq
     - type
     - contents
     - creatorMid
     - createdTime
    """


    def __init__(self, announcementSeq=None, type=None, contents=None, creatorMid=None, createdTime=None,):
        self.announcementSeq = announcementSeq
        self.type = type
        self.contents = contents
        self.creatorMid = creatorMid
        self.createdTime = createdTime

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
                if ftype == TType.I64:
                    self.announcementSeq = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.contents = ChatRoomAnnouncementContents()
                    self.contents.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.creatorMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
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
        oprot.writeStructBegin('ChatRoomAnnouncement')
        if self.announcementSeq is not None:
            oprot.writeFieldBegin('announcementSeq', TType.I64, 1)
            oprot.writeI64(self.announcementSeq)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.contents is not None:
            oprot.writeFieldBegin('contents', TType.STRUCT, 3)
            self.contents.write(oprot)
            oprot.writeFieldEnd()
        if self.creatorMid is not None:
            oprot.writeFieldBegin('creatorMid', TType.STRING, 4)
            oprot.writeString(self.creatorMid.encode('utf-8') if sys.version_info[0] == 2 else self.creatorMid)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 5)
            oprot.writeI64(self.createdTime)
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
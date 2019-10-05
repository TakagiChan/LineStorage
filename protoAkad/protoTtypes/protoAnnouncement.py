from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class Announcement(object):
    """
    Attributes:
     - index
     - forceUpdate
     - title
     - text
     - createdTime
     - pictureUrl
     - thumbnailUrl
    """


    def __init__(self, index=None, forceUpdate=None, title=None, text=None, createdTime=None, pictureUrl=None, thumbnailUrl=None,):
        self.index = index
        self.forceUpdate = forceUpdate
        self.title = title
        self.text = text
        self.createdTime = createdTime
        self.pictureUrl = pictureUrl
        self.thumbnailUrl = thumbnailUrl

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
                if ftype == TType.I32:
                    self.index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.BOOL:
                    self.forceUpdate = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRING:
                    self.pictureUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRING:
                    self.thumbnailUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Announcement')
        if self.index is not None:
            oprot.writeFieldBegin('index', TType.I32, 1)
            oprot.writeI32(self.index)
            oprot.writeFieldEnd()
        if self.forceUpdate is not None:
            oprot.writeFieldBegin('forceUpdate', TType.BOOL, 10)
            oprot.writeBool(self.forceUpdate)
            oprot.writeFieldEnd()
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 11)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 12)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 13)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.pictureUrl is not None:
            oprot.writeFieldBegin('pictureUrl', TType.STRING, 14)
            oprot.writeString(self.pictureUrl.encode('utf-8') if sys.version_info[0] == 2 else self.pictureUrl)
            oprot.writeFieldEnd()
        if self.thumbnailUrl is not None:
            oprot.writeFieldBegin('thumbnailUrl', TType.STRING, 15)
            oprot.writeString(self.thumbnailUrl.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnailUrl)
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
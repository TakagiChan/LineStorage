
from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class ChatRoomAnnouncementContents(object):
    """
    Attributes:
     - displayFields
     - text
     - link
     - thumbnail
    """


    def __init__(self, displayFields=None, text=None, link=None, thumbnail=None,):
        self.displayFields = displayFields
        self.text = text
        self.link = link
        self.thumbnail = thumbnail

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
                    self.displayFields = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.link = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.thumbnail = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ChatRoomAnnouncementContents')
        if self.displayFields is not None:
            oprot.writeFieldBegin('displayFields', TType.I32, 1)
            oprot.writeI32(self.displayFields)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 2)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.link is not None:
            oprot.writeFieldBegin('link', TType.STRING, 3)
            oprot.writeString(self.link.encode('utf-8') if sys.version_info[0] == 2 else self.link)
            oprot.writeFieldEnd()
        if self.thumbnail is not None:
            oprot.writeFieldBegin('thumbnail', TType.STRING, 4)
            oprot.writeString(self.thumbnail.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnail)
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
from thrift.Thrift import TType
from thrift.transport import TTransport
from protoAkad.protoTtypes.protoLocation import Location
import sys

class Message(object):
    """
    Attributes:
     - _from
     - to
     - toType
     - id
     - createdTime
     - deliveredTime
     - text
     - location
     - hasContent
     - contentType
     - contentPreview
     - contentMetadata
     - sessionId
     - chunks
     - relatedMessageId
     - messageRelationType
     - readCount
     - relatedMessageServiceCode
    """


    def __init__(self, _from=None, to=None, toType=None, id=None, createdTime=None, deliveredTime=None, text=None, location=None, hasContent=None, contentType=None, contentPreview=None, contentMetadata=None, sessionId=None, chunks=None, relatedMessageId=None, messageRelationType=None, readCount=None, relatedMessageServiceCode=None,):
        self._from = _from
        self.to = to
        self.toType = toType
        self.id = id
        self.createdTime = createdTime
        self.deliveredTime = deliveredTime
        self.text = text
        self.location = location
        self.hasContent = hasContent
        self.contentType = contentType
        self.contentPreview = contentPreview
        self.contentMetadata = contentMetadata
        self.sessionId = sessionId
        self.chunks = chunks
        self.relatedMessageId = relatedMessageId
        self.messageRelationType = messageRelationType
        self.readCount = readCount
        self.relatedMessageServiceCode = relatedMessageServiceCode

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
                    self._from = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.to = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.toType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.deliveredTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRUCT:
                    self.location = Location()
                    self.location.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.BOOL:
                    self.hasContent = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.contentType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.contentPreview = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.MAP:
                    self.contentMetadata = {}
                    (_ktype277, _vtype278, _size276) = iprot.readMapBegin()
                    for _i280 in range(_size276):
                        _key281 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val282 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.contentMetadata[_key281] = _val282
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.BYTE:
                    self.sessionId = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.LIST:
                    self.chunks = []
                    (_etype286, _size283) = iprot.readListBegin()
                    for _i287 in range(_size283):
                        _elem288 = iprot.readBinary()
                        self.chunks.append(_elem288)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.STRING:
                    self.relatedMessageId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.I32:
                    self.messageRelationType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.I64:
                    self.readCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.I32:
                    self.relatedMessageServiceCode = iprot.readI32()
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
        oprot.writeStructBegin('Message')
        if self._from is not None:
            oprot.writeFieldBegin('_from', TType.STRING, 1)
            oprot.writeString(self._from.encode('utf-8') if sys.version_info[0] == 2 else self._from)
            oprot.writeFieldEnd()
        if self.to is not None:
            oprot.writeFieldBegin('to', TType.STRING, 2)
            oprot.writeString(self.to.encode('utf-8') if sys.version_info[0] == 2 else self.to)
            oprot.writeFieldEnd()
        if self.toType is not None:
            oprot.writeFieldBegin('toType', TType.I32, 3)
            oprot.writeI32(self.toType)
            oprot.writeFieldEnd()
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 4)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 5)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.deliveredTime is not None:
            oprot.writeFieldBegin('deliveredTime', TType.I64, 6)
            oprot.writeI64(self.deliveredTime)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 10)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.location is not None:
            oprot.writeFieldBegin('location', TType.STRUCT, 11)
            self.location.write(oprot)
            oprot.writeFieldEnd()
        if self.hasContent is not None:
            oprot.writeFieldBegin('hasContent', TType.BOOL, 14)
            oprot.writeBool(self.hasContent)
            oprot.writeFieldEnd()
        if self.contentType is not None:
            oprot.writeFieldBegin('contentType', TType.I32, 15)
            oprot.writeI32(self.contentType)
            oprot.writeFieldEnd()
        if self.contentPreview is not None:
            oprot.writeFieldBegin('contentPreview', TType.STRING, 17)
            oprot.writeBinary(self.contentPreview)
            oprot.writeFieldEnd()
        if self.contentMetadata is not None:
            oprot.writeFieldBegin('contentMetadata', TType.MAP, 18)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.contentMetadata))
            for kiter289, viter290 in self.contentMetadata.items():
                oprot.writeString(kiter289.encode('utf-8') if sys.version_info[0] == 2 else kiter289)
                oprot.writeString(viter290.encode('utf-8') if sys.version_info[0] == 2 else viter290)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.sessionId is not None:
            oprot.writeFieldBegin('sessionId', TType.BYTE, 19)
            oprot.writeByte(self.sessionId)
            oprot.writeFieldEnd()
        if self.chunks is not None:
            oprot.writeFieldBegin('chunks', TType.LIST, 20)
            oprot.writeListBegin(TType.STRING, len(self.chunks))
            for iter291 in self.chunks:
                oprot.writeBinary(iter291)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.relatedMessageId is not None:
            oprot.writeFieldBegin('relatedMessageId', TType.STRING, 21)
            oprot.writeString(self.relatedMessageId.encode('utf-8') if sys.version_info[0] == 2 else self.relatedMessageId)
            oprot.writeFieldEnd()
        if self.messageRelationType is not None:
            oprot.writeFieldBegin('messageRelationType', TType.I32, 22)
            oprot.writeI32(self.messageRelationType)
            oprot.writeFieldEnd()
        if self.readCount is not None:
            oprot.writeFieldBegin('readCount', TType.I64, 23)
            oprot.writeI64(self.readCount)
            oprot.writeFieldEnd()
        if self.relatedMessageServiceCode is not None:
            oprot.writeFieldBegin('relatedMessageServiceCode', TType.I32, 24)
            oprot.writeI32(self.relatedMessageServiceCode)
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
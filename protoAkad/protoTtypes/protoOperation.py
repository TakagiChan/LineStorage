from thrift.transport import TTransport
from thrift.Thrift import TType
import sys
from protoAkad.protoTtypes.protoMessage import Message

class Operation(object):
    """
    Attributes:
     - revision
     - createdTime
     - type
     - reqSeq
     - checksum
     - status
     - param1
     - param2
     - param3
     - message
    """


    def __init__(self, revision=None, createdTime=None, type=None, reqSeq=None, checksum=None, status=None, param1=None, param2=None, param3=None, message=None,):
        self.revision = revision
        self.createdTime = createdTime
        self.type = type
        self.reqSeq = reqSeq
        self.checksum = checksum
        self.status = status
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.message = message

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
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.reqSeq = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.checksum = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.param1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.param2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.param3 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRUCT:
                    self.message = Message()
                    self.message.read(iprot)
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
        oprot.writeStructBegin('Operation')
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 1)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.reqSeq is not None:
            oprot.writeFieldBegin('reqSeq', TType.I32, 4)
            oprot.writeI32(self.reqSeq)
            oprot.writeFieldEnd()
        if self.checksum is not None:
            oprot.writeFieldBegin('checksum', TType.STRING, 5)
            oprot.writeString(self.checksum.encode('utf-8') if sys.version_info[0] == 2 else self.checksum)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 7)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.param1 is not None:
            oprot.writeFieldBegin('param1', TType.STRING, 10)
            oprot.writeString(self.param1.encode('utf-8') if sys.version_info[0] == 2 else self.param1)
            oprot.writeFieldEnd()
        if self.param2 is not None:
            oprot.writeFieldBegin('param2', TType.STRING, 11)
            oprot.writeString(self.param2.encode('utf-8') if sys.version_info[0] == 2 else self.param2)
            oprot.writeFieldEnd()
        if self.param3 is not None:
            oprot.writeFieldBegin('param3', TType.STRING, 12)
            oprot.writeString(self.param3.encode('utf-8') if sys.version_info[0] == 2 else self.param3)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRUCT, 20)
            self.message.write(oprot)
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
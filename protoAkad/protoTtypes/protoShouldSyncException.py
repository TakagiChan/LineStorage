from thrift.transport import TTransport
from thrift.Thrift import TType
import sys
from protoAkad.protoService.protoTalkService import TException
from protoAkad.protoTtypes.protoSyncScope import SyncScope
from thrift.TRecursive import fix_spec

class ShouldSyncException(TException):
    """
    Attributes:
     - syncOpRevision
     - syncScope
     - syncReason
     - message
    """


    def __init__(self, syncOpRevision=None, syncScope=None, syncReason=None, message=None,):
        self.syncOpRevision = syncOpRevision
        self.syncScope = syncScope
        self.syncReason = syncReason
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
                    self.syncOpRevision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.syncScope = SyncScope()
                    self.syncScope.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.syncReason = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ShouldSyncException')
        if self.syncOpRevision is not None:
            oprot.writeFieldBegin('syncOpRevision', TType.I64, 1)
            oprot.writeI64(self.syncOpRevision)
            oprot.writeFieldEnd()
        if self.syncScope is not None:
            oprot.writeFieldBegin('syncScope', TType.STRUCT, 2)
            self.syncScope.write(oprot)
            oprot.writeFieldEnd()
        if self.syncReason is not None:
            oprot.writeFieldBegin('syncReason', TType.I32, 3)
            oprot.writeI32(self.syncReason)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 4)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
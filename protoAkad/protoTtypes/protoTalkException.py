from thrift.Thrift import TException
from thrift.transport import TTransport
from thrift.Thrift import TType
import sys

class TalkException(TException):
    """
    Attributes:
     - code
     - reason
     - parameterMap
    """


    def __init__(self, code=None, reason=None, parameterMap=None,):
        self.code = code
        self.reason = reason
        self.parameterMap = parameterMap

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
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.reason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.parameterMap = {}
                    (_ktype912, _vtype913, _size911) = iprot.readMapBegin()
                    for _i915 in range(_size911):
                        _key916 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val917 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.parameterMap[_key916] = _val917
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('TalkException')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.reason is not None:
            oprot.writeFieldBegin('reason', TType.STRING, 2)
            oprot.writeString(self.reason.encode('utf-8') if sys.version_info[0] == 2 else self.reason)
            oprot.writeFieldEnd()
        if self.parameterMap is not None:
            oprot.writeFieldBegin('parameterMap', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.parameterMap))
            for kiter918, viter919 in self.parameterMap.items():
                oprot.writeString(kiter918.encode('utf-8') if sys.version_info[0] == 2 else kiter918)
                oprot.writeString(viter919.encode('utf-8') if sys.version_info[0] == 2 else viter919)
            oprot.writeMapEnd()
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
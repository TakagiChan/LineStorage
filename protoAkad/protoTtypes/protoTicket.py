from thrift.transport import TTransport
from thrift.Thrift import TType

class Ticket(object):
    """
    Attributes:
     - id
     - expirationTime
     - maxUseCount
    """


    def __init__(self, id=None, expirationTime=None, maxUseCount=None,):
        self.id = id
        self.expirationTime = expirationTime
        self.maxUseCount = maxUseCount

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
            elif fid == 10:
                if ftype == TType.I64:
                    self.expirationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I32:
                    self.maxUseCount = iprot.readI32()
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
        oprot.writeStructBegin('Ticket')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.expirationTime is not None:
            oprot.writeFieldBegin('expirationTime', TType.I64, 10)
            oprot.writeI64(self.expirationTime)
            oprot.writeFieldEnd()
        if self.maxUseCount is not None:
            oprot.writeFieldBegin('maxUseCount', TType.I32, 21)
            oprot.writeI32(self.maxUseCount)
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
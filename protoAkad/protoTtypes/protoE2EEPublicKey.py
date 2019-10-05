from thrift.transport import TTransport
from thrift.Thrift import TType
all_structs = []
class E2EEPublicKey(object):
    """
    Attributes:
     - version
     - keyId
     - keyData
     - createdTime
    """


    def __init__(self, version=None, keyId=None, keyData=None, createdTime=None,):
        self.version = version
        self.keyId = keyId
        self.keyData = keyData
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
                if ftype == TType.I32:
                    self.version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.keyId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.keyData = iprot.readBinary()
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
        oprot.writeStructBegin('E2EEPublicKey')
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.I32, 1)
            oprot.writeI32(self.version)
            oprot.writeFieldEnd()
        if self.keyId is not None:
            oprot.writeFieldBegin('keyId', TType.I32, 2)
            oprot.writeI32(self.keyId)
            oprot.writeFieldEnd()
        if self.keyData is not None:
            oprot.writeFieldBegin('keyData', TType.STRING, 4)
            oprot.writeBinary(self.keyData)
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

all_structs.append(E2EEPublicKey)
E2EEPublicKey.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'version', None, None, ),  # 1
    (2, TType.I32, 'keyId', None, None, ),  # 2
    None,  # 3
    (4, TType.STRING, 'keyData', 'BINARY', None, ),  # 4
    (5, TType.I64, 'createdTime', None, None, ),  # 5
)
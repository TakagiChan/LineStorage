from thrift.transport import TTransport
from thrift.Thrift import TType
import sys
from thrift.TRecursive import fix_spec

all_structs = []

class FriendRequest(object):
    """
    Attributes:
     - eMid
     - mid
     - direction
     - method
     - param
     - timestamp
     - seqId
     - displayName
     - picturePath
     - pictureStatus
    """


    def __init__(self, eMid=None, mid=None, direction=None, method=None, param=None, timestamp=None, seqId=None, displayName=None, picturePath=None, pictureStatus=None,):
        self.eMid = eMid
        self.mid = mid
        self.direction = direction
        self.method = method
        self.param = param
        self.timestamp = timestamp
        self.seqId = seqId
        self.displayName = displayName
        self.picturePath = picturePath
        self.pictureStatus = pictureStatus

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
                    self.eMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.direction = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.method = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.param = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.seqId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.picturePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('FriendRequest')
        if self.eMid is not None:
            oprot.writeFieldBegin('eMid', TType.STRING, 1)
            oprot.writeString(self.eMid.encode('utf-8') if sys.version_info[0] == 2 else self.eMid)
            oprot.writeFieldEnd()
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 2)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.direction is not None:
            oprot.writeFieldBegin('direction', TType.I32, 3)
            oprot.writeI32(self.direction)
            oprot.writeFieldEnd()
        if self.method is not None:
            oprot.writeFieldBegin('method', TType.I32, 4)
            oprot.writeI32(self.method)
            oprot.writeFieldEnd()
        if self.param is not None:
            oprot.writeFieldBegin('param', TType.STRING, 5)
            oprot.writeString(self.param.encode('utf-8') if sys.version_info[0] == 2 else self.param)
            oprot.writeFieldEnd()
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 6)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.seqId is not None:
            oprot.writeFieldBegin('seqId', TType.I64, 7)
            oprot.writeI64(self.seqId)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 10)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.picturePath is not None:
            oprot.writeFieldBegin('picturePath', TType.STRING, 11)
            oprot.writeString(self.picturePath.encode('utf-8') if sys.version_info[0] == 2 else self.picturePath)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 12)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
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

all_structs.append(FriendRequest)
FriendRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'eMid', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'mid', 'UTF8', None, ),  # 2
    (3, TType.I32, 'direction', None, None, ),  # 3
    (4, TType.I32, 'method', None, None, ),  # 4
    (5, TType.STRING, 'param', 'UTF8', None, ),  # 5
    (6, TType.I64, 'timestamp', None, None, ),  # 6
    (7, TType.I64, 'seqId', None, None, ),  # 7
    None,  # 8
    None,  # 9
    (10, TType.STRING, 'displayName', 'UTF8', None, ),  # 10
    (11, TType.STRING, 'picturePath', 'UTF8', None, ),  # 11
    (12, TType.STRING, 'pictureStatus', 'UTF8', None, ),  # 12
)

fix_spec(all_structs)
from thrift.Thrift import TType
from thrift.transport import TTransport
import sys

class Contact(object):
    """
    Attributes:
     - mid
     - createdTime
     - type
     - status
     - relation
     - displayName
     - phoneticName
     - pictureStatus
     - thumbnailUrl
     - statusMessage
     - displayNameOverridden
     - favoriteTime
     - capableVoiceCall
     - capableVideoCall
     - capableMyhome
     - capableBuddy
     - attributes
     - settings
     - picturePath
     - recommendParams
     - friendRequestStatus
     - musicProfile
     - videoProfile
    """


    def __init__(self, mid=None, createdTime=None, type=None, status=None, relation=None, displayName=None, phoneticName=None, pictureStatus=None, thumbnailUrl=None, statusMessage=None, displayNameOverridden=None, favoriteTime=None, capableVoiceCall=None, capableVideoCall=None, capableMyhome=None, capableBuddy=None, attributes=None, settings=None, picturePath=None, recommendParams=None, friendRequestStatus=None, musicProfile=None, videoProfile=None,):
        self.mid = mid
        self.createdTime = createdTime
        self.type = type
        self.status = status
        self.relation = relation
        self.displayName = displayName
        self.phoneticName = phoneticName
        self.pictureStatus = pictureStatus
        self.thumbnailUrl = thumbnailUrl
        self.statusMessage = statusMessage
        self.displayNameOverridden = displayNameOverridden
        self.favoriteTime = favoriteTime
        self.capableVoiceCall = capableVoiceCall
        self.capableVideoCall = capableVideoCall
        self.capableMyhome = capableMyhome
        self.capableBuddy = capableBuddy
        self.attributes = attributes
        self.settings = settings
        self.picturePath = picturePath
        self.recommendParams = recommendParams
        self.friendRequestStatus = friendRequestStatus
        self.musicProfile = musicProfile
        self.videoProfile = videoProfile

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
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I32:
                    self.relation = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRING:
                    self.phoneticName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.STRING:
                    self.thumbnailUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.STRING:
                    self.statusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 27:
                if ftype == TType.STRING:
                    self.displayNameOverridden = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 28:
                if ftype == TType.I64:
                    self.favoriteTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.BOOL:
                    self.capableVoiceCall = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 32:
                if ftype == TType.BOOL:
                    self.capableVideoCall = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 33:
                if ftype == TType.BOOL:
                    self.capableMyhome = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 34:
                if ftype == TType.BOOL:
                    self.capableBuddy = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 35:
                if ftype == TType.I32:
                    self.attributes = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 36:
                if ftype == TType.I64:
                    self.settings = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 37:
                if ftype == TType.STRING:
                    self.picturePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 38:
                if ftype == TType.STRING:
                    self.recommendParams = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 39:
                if ftype == TType.I32:
                    self.friendRequestStatus = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 40:
                if ftype == TType.STRING:
                    self.musicProfile = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 42:
                if ftype == TType.STRING:
                    self.videoProfile = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Contact')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 10)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 11)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.relation is not None:
            oprot.writeFieldBegin('relation', TType.I32, 21)
            oprot.writeI32(self.relation)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 22)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.phoneticName is not None:
            oprot.writeFieldBegin('phoneticName', TType.STRING, 23)
            oprot.writeString(self.phoneticName.encode('utf-8') if sys.version_info[0] == 2 else self.phoneticName)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 24)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            oprot.writeFieldEnd()
        if self.thumbnailUrl is not None:
            oprot.writeFieldBegin('thumbnailUrl', TType.STRING, 25)
            oprot.writeString(self.thumbnailUrl.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnailUrl)
            oprot.writeFieldEnd()
        if self.statusMessage is not None:
            oprot.writeFieldBegin('statusMessage', TType.STRING, 26)
            oprot.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            oprot.writeFieldEnd()
        if self.displayNameOverridden is not None:
            oprot.writeFieldBegin('displayNameOverridden', TType.STRING, 27)
            oprot.writeString(self.displayNameOverridden.encode('utf-8') if sys.version_info[0] == 2 else self.displayNameOverridden)
            oprot.writeFieldEnd()
        if self.favoriteTime is not None:
            oprot.writeFieldBegin('favoriteTime', TType.I64, 28)
            oprot.writeI64(self.favoriteTime)
            oprot.writeFieldEnd()
        if self.capableVoiceCall is not None:
            oprot.writeFieldBegin('capableVoiceCall', TType.BOOL, 31)
            oprot.writeBool(self.capableVoiceCall)
            oprot.writeFieldEnd()
        if self.capableVideoCall is not None:
            oprot.writeFieldBegin('capableVideoCall', TType.BOOL, 32)
            oprot.writeBool(self.capableVideoCall)
            oprot.writeFieldEnd()
        if self.capableMyhome is not None:
            oprot.writeFieldBegin('capableMyhome', TType.BOOL, 33)
            oprot.writeBool(self.capableMyhome)
            oprot.writeFieldEnd()
        if self.capableBuddy is not None:
            oprot.writeFieldBegin('capableBuddy', TType.BOOL, 34)
            oprot.writeBool(self.capableBuddy)
            oprot.writeFieldEnd()
        if self.attributes is not None:
            oprot.writeFieldBegin('attributes', TType.I32, 35)
            oprot.writeI32(self.attributes)
            oprot.writeFieldEnd()
        if self.settings is not None:
            oprot.writeFieldBegin('settings', TType.I64, 36)
            oprot.writeI64(self.settings)
            oprot.writeFieldEnd()
        if self.picturePath is not None:
            oprot.writeFieldBegin('picturePath', TType.STRING, 37)
            oprot.writeString(self.picturePath.encode('utf-8') if sys.version_info[0] == 2 else self.picturePath)
            oprot.writeFieldEnd()
        if self.recommendParams is not None:
            oprot.writeFieldBegin('recommendParams', TType.STRING, 38)
            oprot.writeString(self.recommendParams.encode('utf-8') if sys.version_info[0] == 2 else self.recommendParams)
            oprot.writeFieldEnd()
        if self.friendRequestStatus is not None:
            oprot.writeFieldBegin('friendRequestStatus', TType.I32, 39)
            oprot.writeI32(self.friendRequestStatus)
            oprot.writeFieldEnd()
        if self.musicProfile is not None:
            oprot.writeFieldBegin('musicProfile', TType.STRING, 40)
            oprot.writeString(self.musicProfile.encode('utf-8') if sys.version_info[0] == 2 else self.musicProfile)
            oprot.writeFieldEnd()
        if self.videoProfile is not None:
            oprot.writeFieldBegin('videoProfile', TType.STRING, 42)
            oprot.writeString(self.videoProfile.encode('utf-8') if sys.version_info[0] == 2 else self.videoProfile)
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
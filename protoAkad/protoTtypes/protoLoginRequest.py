from thrift.transport import TTransport
from thrift.Thrift import TType
import sys
all_structs = []

class LoginRequest(object):
    """
    Attributes:
     - type
     - identityProvider
     - identifier
     - password
     - keepLoggedIn
     - accessLocation
     - systemName
     - certificate
     - verifier
     - secret
     - e2eeVersion
    """


    def __init__(self, type=None, identityProvider=None, identifier=None, password=None, keepLoggedIn=None, accessLocation=None, systemName=None, certificate=None, verifier=None, secret=None, e2eeVersion=None,):
        self.type = type
        self.identityProvider = identityProvider
        self.identifier = identifier
        self.password = password
        self.keepLoggedIn = keepLoggedIn
        self.accessLocation = accessLocation
        self.systemName = systemName
        self.certificate = certificate
        self.verifier = verifier
        self.secret = secret
        self.e2eeVersion = e2eeVersion

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
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.identityProvider = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.identifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.keepLoggedIn = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.accessLocation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.systemName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.certificate = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.secret = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.e2eeVersion = iprot.readI32()
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
        oprot.writeStructBegin('LoginRequest')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.identityProvider is not None:
            oprot.writeFieldBegin('identityProvider', TType.I32, 2)
            oprot.writeI32(self.identityProvider)
            oprot.writeFieldEnd()
        if self.identifier is not None:
            oprot.writeFieldBegin('identifier', TType.STRING, 3)
            oprot.writeString(self.identifier.encode('utf-8') if sys.version_info[0] == 2 else self.identifier)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 4)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        if self.keepLoggedIn is not None:
            oprot.writeFieldBegin('keepLoggedIn', TType.BOOL, 5)
            oprot.writeBool(self.keepLoggedIn)
            oprot.writeFieldEnd()
        if self.accessLocation is not None:
            oprot.writeFieldBegin('accessLocation', TType.STRING, 6)
            oprot.writeString(self.accessLocation.encode('utf-8') if sys.version_info[0] == 2 else self.accessLocation)
            oprot.writeFieldEnd()
        if self.systemName is not None:
            oprot.writeFieldBegin('systemName', TType.STRING, 7)
            oprot.writeString(self.systemName.encode('utf-8') if sys.version_info[0] == 2 else self.systemName)
            oprot.writeFieldEnd()
        if self.certificate is not None:
            oprot.writeFieldBegin('certificate', TType.STRING, 8)
            oprot.writeString(self.certificate.encode('utf-8') if sys.version_info[0] == 2 else self.certificate)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 9)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.secret is not None:
            oprot.writeFieldBegin('secret', TType.STRING, 10)
            oprot.writeString(self.secret.encode('utf-8') if sys.version_info[0] == 2 else self.secret)
            oprot.writeFieldEnd()
        if self.e2eeVersion is not None:
            oprot.writeFieldBegin('e2eeVersion', TType.I32, 11)
            oprot.writeI32(self.e2eeVersion)
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

all_structs.append(LoginRequest)
LoginRequest.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'type', None, None, ),  # 1
    (2, TType.I32, 'identityProvider', None, None, ),  # 2
    (3, TType.STRING, 'identifier', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'password', 'UTF8', None, ),  # 4
    (5, TType.BOOL, 'keepLoggedIn', None, None, ),  # 5
    (6, TType.STRING, 'accessLocation', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'systemName', 'UTF8', None, ),  # 7
    (8, TType.STRING, 'certificate', 'UTF8', None, ),  # 8
    (9, TType.STRING, 'verifier', 'UTF8', None, ),  # 9
    (10, TType.STRING, 'secret', 'UTF8', None, ),  # 10
    (11, TType.I32, 'e2eeVersion', None, None, ),  # 11
)
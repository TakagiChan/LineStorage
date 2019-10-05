class Location(object):
    """
    Attributes:
     - title
     - address
     - latitude
     - longitude
     - phone
    """


    def __init__(self, title=None, address=None, latitude=None, longitude=None, phone=None,):
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.phone = phone

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
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.address = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.latitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.longitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.phone = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Location')
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 1)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.address is not None:
            oprot.writeFieldBegin('address', TType.STRING, 2)
            oprot.writeString(self.address.encode('utf-8') if sys.version_info[0] == 2 else self.address)
            oprot.writeFieldEnd()
        if self.latitude is not None:
            oprot.writeFieldBegin('latitude', TType.DOUBLE, 3)
            oprot.writeDouble(self.latitude)
            oprot.writeFieldEnd()
        if self.longitude is not None:
            oprot.writeFieldBegin('longitude', TType.DOUBLE, 4)
            oprot.writeDouble(self.longitude)
            oprot.writeFieldEnd()
        if self.phone is not None:
            oprot.writeFieldBegin('phone', TType.STRING, 5)
            oprot.writeString(self.phone.encode('utf-8') if sys.version_info[0] == 2 else self.phone)
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
class GroupPreference(object):
    """
    Attributes:
     - invitationTicket
     - favoriteTimestamp
    """


    def __init__(self, invitationTicket=None, favoriteTimestamp=None,):
        self.invitationTicket = invitationTicket
        self.favoriteTimestamp = favoriteTimestamp

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
                    self.invitationTicket = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.favoriteTimestamp = iprot.readI64()
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
        oprot.writeStructBegin('GroupPreference')
        if self.invitationTicket is not None:
            oprot.writeFieldBegin('invitationTicket', TType.STRING, 1)
            oprot.writeString(self.invitationTicket.encode('utf-8') if sys.version_info[0] == 2 else self.invitationTicket)
            oprot.writeFieldEnd()
        if self.favoriteTimestamp is not None:
            oprot.writeFieldBegin('favoriteTimestamp', TType.I64, 2)
            oprot.writeI64(self.favoriteTimestamp)
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
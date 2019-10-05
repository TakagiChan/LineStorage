class LoginType(object):
    ID_CREDENTIAL = 0
    QRCODE = 1
    ID_CREDENTIAL_WITH_E2EE = 2

    _VALUES_TO_NAMES = {
        0: "ID_CREDENTIAL",
        1: "QRCODE",
        2: "ID_CREDENTIAL_WITH_E2EE",
    }

    _NAMES_TO_VALUES = {
        "ID_CREDENTIAL": 0,
        "QRCODE": 1,
        "ID_CREDENTIAL_WITH_E2EE": 2,
    }
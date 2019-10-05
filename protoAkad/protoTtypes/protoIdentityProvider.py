class IdentityProvider(object):
    UNKNOWN = 0
    LINE = 1
    NAVER_KR = 2
    LINE_PHONE = 3

    _VALUES_TO_NAMES = {
        0: "UNKNOWN",
        1: "LINE",
        2: "NAVER_KR",
        3: "LINE_PHONE",
    }

    _NAMES_TO_VALUES = {
        "UNKNOWN": 0,
        "LINE": 1,
        "NAVER_KR": 2,
        "LINE_PHONE": 3,
    }
class LoginResultType(object):
    SUCCESS = 1
    REQUIRE_QRCODE = 2
    REQUIRE_DEVICE_CONFIRM = 3
    REQUIRE_SMS_CONFIRM = 4

    _VALUES_TO_NAMES = {
        1: "SUCCESS",
        2: "REQUIRE_QRCODE",
        3: "REQUIRE_DEVICE_CONFIRM",
        4: "REQUIRE_SMS_CONFIRM",
    }

    _NAMES_TO_VALUES = {
        "SUCCESS": 1,
        "REQUIRE_QRCODE": 2,
        "REQUIRE_DEVICE_CONFIRM": 3,
        "REQUIRE_SMS_CONFIRM": 4,
    }
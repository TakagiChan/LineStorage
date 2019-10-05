class ApplicationType(object):
    IOS = 16
    IOS_RC = 17
    IOS_BETA = 18
    IOS_ALPHA = 19
    ANDROID = 32
    ANDROID_RC = 33
    ANDROID_BETA = 34
    ANDROID_ALPHA = 35
    WAP = 48
    WAP_RC = 49
    WAP_BETA = 50
    WAP_ALPHA = 51
    BOT = 64
    BOT_RC = 65
    BOT_BETA = 66
    BOT_ALPHA = 67
    WEB = 80
    WEB_RC = 81
    WEB_BETA = 82
    WEB_ALPHA = 83
    DESKTOPWIN = 96
    DESKTOPWIN_RC = 97
    DESKTOPWIN_BETA = 98
    DESKTOPWIN_ALPHA = 99
    DESKTOPMAC = 112
    DESKTOPMAC_RC = 113
    DESKTOPMAC_BETA = 114
    DESKTOPMAC_ALPHA = 115
    CHANNELGW = 128
    CHANNELGW_RC = 129
    CHANNELGW_BETA = 130
    CHANNELGW_ALPHA = 131
    CHANNELCP = 144
    CHANNELCP_RC = 145
    CHANNELCP_BETA = 146
    CHANNELCP_ALPHA = 147
    WINPHONE = 160
    WINPHONE_RC = 161
    WINPHONE_BETA = 162
    WINPHONE_ALPHA = 163
    BLACKBERRY = 176
    BLACKBERRY_RC = 177
    BLACKBERRY_BETA = 178
    BLACKBERRY_ALPHA = 179
    WINMETRO = 192
    WINMETRO_RC = 193
    WINMETRO_BETA = 194
    WINMETRO_ALPHA = 195
    S40 = 208
    S40_RC = 209
    S40_BETA = 210
    S40_ALPHA = 211
    CHRONO = 224
    CHRONO_RC = 225
    CHRONO_BETA = 226
    CHRONO_ALPHA = 227
    TIZEN = 256
    TIZEN_RC = 257
    TIZEN_BETA = 258
    TIZEN_ALPHA = 259
    VIRTUAL = 272
    FIREFOXOS = 288
    FIREFOXOS_RC = 289
    FIREFOXOS_BETA = 290
    FIREFOXOS_ALPHA = 291
    IOSIPAD = 304
    IOSIPAD_RC = 305
    IOSIPAD_BETA = 306
    IOSIPAD_ALPHA = 307
    BIZIOS = 320
    BIZIOS_RC = 321
    BIZIOS_BETA = 322
    BIZIOS_ALPHA = 323
    BIZANDROID = 336
    BIZANDROID_RC = 337
    BIZANDROID_BETA = 338
    BIZANDROID_ALPHA = 339
    BIZBOT = 352
    BIZBOT_RC = 353
    BIZBOT_BETA = 354
    BIZBOT_ALPHA = 355
    CHROMEOS = 368
    CHROMEOS_RC = 369
    CHROMEOS_BETA = 370
    CHROMEOS_ALPHA = 371
    ANDROIDLITE = 384
    ANDROIDLITE_RC = 385
    ANDROIDLITE_BETA = 386
    ANDROIDLITE_ALPHA = 387
    WIN10 = 400
    WIN10_RC = 401
    WIN10_BETA = 402
    WIN10_ALPHA = 403
    BIZWEB = 416
    BIZWEB_RC = 417
    BIZWEB_BETA = 418
    BIZWEB_ALPHA = 419
    DUMMYPRIMARY = 432
    DUMMYPRIMARY_RC = 433
    DUMMYPRIMARY_BETA = 434
    DUMMYPRIMARY_ALPHA = 435
    SQUARE = 448
    SQUARE_RC = 449
    SQUARE_BETA = 450
    SQUARE_ALPHA = 451
    INTERNAL = 464
    INTERNAL_RC = 465
    INTERNAL_BETA = 466
    INTERNAL_ALPHA = 467
    CLOVAFRIENDS = 480
    CLOVAFRIENDS_RC = 481
    CLOVAFRIENDS_BETA = 482
    CLOVAFRIENDS_ALPHA = 483

    _VALUES_TO_NAMES = {
        16: "IOS",
        17: "IOS_RC",
        18: "IOS_BETA",
        19: "IOS_ALPHA",
        32: "ANDROID",
        33: "ANDROID_RC",
        34: "ANDROID_BETA",
        35: "ANDROID_ALPHA",
        48: "WAP",
        49: "WAP_RC",
        50: "WAP_BETA",
        51: "WAP_ALPHA",
        64: "BOT",
        65: "BOT_RC",
        66: "BOT_BETA",
        67: "BOT_ALPHA",
        80: "WEB",
        81: "WEB_RC",
        82: "WEB_BETA",
        83: "WEB_ALPHA",
        96: "DESKTOPWIN",
        97: "DESKTOPWIN_RC",
        98: "DESKTOPWIN_BETA",
        99: "DESKTOPWIN_ALPHA",
        112: "DESKTOPMAC",
        113: "DESKTOPMAC_RC",
        114: "DESKTOPMAC_BETA",
        115: "DESKTOPMAC_ALPHA",
        128: "CHANNELGW",
        129: "CHANNELGW_RC",
        130: "CHANNELGW_BETA",
        131: "CHANNELGW_ALPHA",
        144: "CHANNELCP",
        145: "CHANNELCP_RC",
        146: "CHANNELCP_BETA",
        147: "CHANNELCP_ALPHA",
        160: "WINPHONE",
        161: "WINPHONE_RC",
        162: "WINPHONE_BETA",
        163: "WINPHONE_ALPHA",
        176: "BLACKBERRY",
        177: "BLACKBERRY_RC",
        178: "BLACKBERRY_BETA",
        179: "BLACKBERRY_ALPHA",
        192: "WINMETRO",
        193: "WINMETRO_RC",
        194: "WINMETRO_BETA",
        195: "WINMETRO_ALPHA",
        208: "S40",
        209: "S40_RC",
        210: "S40_BETA",
        211: "S40_ALPHA",
        224: "CHRONO",
        225: "CHRONO_RC",
        226: "CHRONO_BETA",
        227: "CHRONO_ALPHA",
        256: "TIZEN",
        257: "TIZEN_RC",
        258: "TIZEN_BETA",
        259: "TIZEN_ALPHA",
        272: "VIRTUAL",
        288: "FIREFOXOS",
        289: "FIREFOXOS_RC",
        290: "FIREFOXOS_BETA",
        291: "FIREFOXOS_ALPHA",
        304: "IOSIPAD",
        305: "IOSIPAD_RC",
        306: "IOSIPAD_BETA",
        307: "IOSIPAD_ALPHA",
        320: "BIZIOS",
        321: "BIZIOS_RC",
        322: "BIZIOS_BETA",
        323: "BIZIOS_ALPHA",
        336: "BIZANDROID",
        337: "BIZANDROID_RC",
        338: "BIZANDROID_BETA",
        339: "BIZANDROID_ALPHA",
        352: "BIZBOT",
        353: "BIZBOT_RC",
        354: "BIZBOT_BETA",
        355: "BIZBOT_ALPHA",
        368: "CHROMEOS",
        369: "CHROMEOS_RC",
        370: "CHROMEOS_BETA",
        371: "CHROMEOS_ALPHA",
        384: "ANDROIDLITE",
        385: "ANDROIDLITE_RC",
        386: "ANDROIDLITE_BETA",
        387: "ANDROIDLITE_ALPHA",
        400: "WIN10",
        401: "WIN10_RC",
        402: "WIN10_BETA",
        403: "WIN10_ALPHA",
        416: "BIZWEB",
        417: "BIZWEB_RC",
        418: "BIZWEB_BETA",
        419: "BIZWEB_ALPHA",
        432: "DUMMYPRIMARY",
        433: "DUMMYPRIMARY_RC",
        434: "DUMMYPRIMARY_BETA",
        435: "DUMMYPRIMARY_ALPHA",
        448: "SQUARE",
        449: "SQUARE_RC",
        450: "SQUARE_BETA",
        451: "SQUARE_ALPHA",
        464: "INTERNAL",
        465: "INTERNAL_RC",
        466: "INTERNAL_BETA",
        467: "INTERNAL_ALPHA",
        480: "CLOVAFRIENDS",
        481: "CLOVAFRIENDS_RC",
        482: "CLOVAFRIENDS_BETA",
        483: "CLOVAFRIENDS_ALPHA",
    }

    _NAMES_TO_VALUES = {
        "IOS": 16,
        "IOS_RC": 17,
        "IOS_BETA": 18,
        "IOS_ALPHA": 19,
        "ANDROID": 32,
        "ANDROID_RC": 33,
        "ANDROID_BETA": 34,
        "ANDROID_ALPHA": 35,
        "WAP": 48,
        "WAP_RC": 49,
        "WAP_BETA": 50,
        "WAP_ALPHA": 51,
        "BOT": 64,
        "BOT_RC": 65,
        "BOT_BETA": 66,
        "BOT_ALPHA": 67,
        "WEB": 80,
        "WEB_RC": 81,
        "WEB_BETA": 82,
        "WEB_ALPHA": 83,
        "DESKTOPWIN": 96,
        "DESKTOPWIN_RC": 97,
        "DESKTOPWIN_BETA": 98,
        "DESKTOPWIN_ALPHA": 99,
        "DESKTOPMAC": 112,
        "DESKTOPMAC_RC": 113,
        "DESKTOPMAC_BETA": 114,
        "DESKTOPMAC_ALPHA": 115,
        "CHANNELGW": 128,
        "CHANNELGW_RC": 129,
        "CHANNELGW_BETA": 130,
        "CHANNELGW_ALPHA": 131,
        "CHANNELCP": 144,
        "CHANNELCP_RC": 145,
        "CHANNELCP_BETA": 146,
        "CHANNELCP_ALPHA": 147,
        "WINPHONE": 160,
        "WINPHONE_RC": 161,
        "WINPHONE_BETA": 162,
        "WINPHONE_ALPHA": 163,
        "BLACKBERRY": 176,
        "BLACKBERRY_RC": 177,
        "BLACKBERRY_BETA": 178,
        "BLACKBERRY_ALPHA": 179,
        "WINMETRO": 192,
        "WINMETRO_RC": 193,
        "WINMETRO_BETA": 194,
        "WINMETRO_ALPHA": 195,
        "S40": 208,
        "S40_RC": 209,
        "S40_BETA": 210,
        "S40_ALPHA": 211,
        "CHRONO": 224,
        "CHRONO_RC": 225,
        "CHRONO_BETA": 226,
        "CHRONO_ALPHA": 227,
        "TIZEN": 256,
        "TIZEN_RC": 257,
        "TIZEN_BETA": 258,
        "TIZEN_ALPHA": 259,
        "VIRTUAL": 272,
        "FIREFOXOS": 288,
        "FIREFOXOS_RC": 289,
        "FIREFOXOS_BETA": 290,
        "FIREFOXOS_ALPHA": 291,
        "IOSIPAD": 304,
        "IOSIPAD_RC": 305,
        "IOSIPAD_BETA": 306,
        "IOSIPAD_ALPHA": 307,
        "BIZIOS": 320,
        "BIZIOS_RC": 321,
        "BIZIOS_BETA": 322,
        "BIZIOS_ALPHA": 323,
        "BIZANDROID": 336,
        "BIZANDROID_RC": 337,
        "BIZANDROID_BETA": 338,
        "BIZANDROID_ALPHA": 339,
        "BIZBOT": 352,
        "BIZBOT_RC": 353,
        "BIZBOT_BETA": 354,
        "BIZBOT_ALPHA": 355,
        "CHROMEOS": 368,
        "CHROMEOS_RC": 369,
        "CHROMEOS_BETA": 370,
        "CHROMEOS_ALPHA": 371,
        "ANDROIDLITE": 384,
        "ANDROIDLITE_RC": 385,
        "ANDROIDLITE_BETA": 386,
        "ANDROIDLITE_ALPHA": 387,
        "WIN10": 400,
        "WIN10_RC": 401,
        "WIN10_BETA": 402,
        "WIN10_ALPHA": 403,
        "BIZWEB": 416,
        "BIZWEB_RC": 417,
        "BIZWEB_BETA": 418,
        "BIZWEB_ALPHA": 419,
        "DUMMYPRIMARY": 432,
        "DUMMYPRIMARY_RC": 433,
        "DUMMYPRIMARY_BETA": 434,
        "DUMMYPRIMARY_ALPHA": 435,
        "SQUARE": 448,
        "SQUARE_RC": 449,
        "SQUARE_BETA": 450,
        "SQUARE_ALPHA": 451,
        "INTERNAL": 464,
        "INTERNAL_RC": 465,
        "INTERNAL_BETA": 466,
        "INTERNAL_ALPHA": 467,
        "CLOVAFRIENDS": 480,
        "CLOVAFRIENDS_RC": 481,
        "CLOVAFRIENDS_BETA": 482,
        "CLOVAFRIENDS_ALPHA": 483,
    }
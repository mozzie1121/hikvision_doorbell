## Macro definitions for NET_DVR_ACS_ALARM_INFO https://open.hikvision.com/hardware/structures/NET_DVR_ACS_ALARM_INFO.html
from enum import Enum

class AcsAlarmInfoMajor(Enum):
    MAJOR_ALARM = 0x1
    MAJOR_EXCEPTION = 0x2
    MAJOR_OPERATION = 0x3
    MAJOR_EVENT = 0x5

class AcsAlarmInfoMajorAlarm(Enum):
    MINOR_ALARMIN_SHORT_CIRCUIT = 0x400
    MINOR_ALARMIN_BROKEN_CIRCUIT = 0x401
    MINOR_ALARMIN_EXCEPTION = 0x402
    MINOR_ALARMIN_RESUME = 0x403
    MINOR_HOST_DESMANTLE_ALARM = 0x404
    MINOR_HOST_DESMANTLE_RESUME = 0x405
    MINOR_CARD_READER_DESMANTLE_ALARM = 0x406
    MINOR_CARD_READER_DESMANTLE_RESUME = 0x407
    MINOR_CASE_SENSOR_ALARM = 0x408
    MINOR_CASE_SENSOR_RESUME = 0x409
    MINOR_STRESS_ALARM = 0x40a
    MINOR_OFFLINE_ECENT_NEARLY_FULL = 0x40b
    MINOR_CARD_MAX_AUTHENTICATE_FAIL = 0x40c
    MINOR_SD_CARD_FULL = 0x40d
    MINOR_LINKAGE_CAPTURE_PIC = 0x40e
    MINOR_SECURITY_MODULE_DESMANTLE_ALARM = 0x40f
    MINOR_SECURITY_MODULE_DESMANTLE_RESUME = 0x410
    MINOR_FIRE_IMPORT_SHORT_CIRCUIT = 0x415
    MINOR_FIRE_IMPORT_BROKEN_CIRCUIT = 0x416
    MINOR_FIRE_IMPORT_RESUME = 0x417
    MINOR_FIRE_BUTTON_TRIGGER = 0x418
    MINOR_FIRE_BUTTON_RESUME = 0x419
    MINOR_MAINTENANCE_BUTTON_TRIGGER = 0x41a
    MINOR_MAINTENANCE_BUTTON_RESUME = 0x41b
    MINOR_EMERGENCY_BUTTON_TRIGGER = 0x41c
    MINOR_EMERGENCY_BUTTON_RESUME = 0x41d
    MINOR_DISTRACT_CONTROLLER_ALARM = 0x41e
    MINOR_DISTRACT_CONTROLLER_RESUME = 0x41f
    MINOR_CHANNEL_CONTROLLER_DESMANTLE_ALARM = 0x422
    MINOR_CHANNEL_CONTROLLER_DESMANTLE_RESUME = 0x423
    MINOR_CHANNEL_CONTROLLER_FIRE_IMPORT_ALARM = 0x424
    MINOR_CHANNEL_CONTROLLER_FIRE_IMPORT_RESUME = 0x425
    MINOR_ALARM_CUSTOM1 = 0x900
    MINOR_ALARM_CUSTOM2 = 0x901
    MINOR_ALARM_CUSTOM3 = 0x902
    MINOR_ALARM_CUSTOM4 = 0x903
    MINOR_ALARM_CUSTOM5 = 0x904
    MINOR_ALARM_CUSTOM6 = 0x905
    MINOR_ALARM_CUSTOM7 = 0x906
    MINOR_ALARM_CUSTOM8 = 0x907
    MINOR_ALARM_CUSTOM9 = 0x908
    MINOR_ALARM_CUSTOM10 = 0x909
    MINOR_ALARM_CUSTOM11 = 0x90a
    MINOR_ALARM_CUSTOM12 = 0x90b
    MINOR_ALARM_CUSTOM13 = 0x90c
    MINOR_ALARM_CUSTOM14 = 0x90d
    MINOR_ALARM_CUSTOM15 = 0x90e
    MINOR_ALARM_CUSTOM16 = 0x90f
    MINOR_ALARM_CUSTOM17 = 0x910
    MINOR_ALARM_CUSTOM18 = 0x911
    MINOR_ALARM_CUSTOM19 = 0x912
    MINOR_ALARM_CUSTOM20 = 0x913
    MINOR_ALARM_CUSTOM21 = 0x914
    MINOR_ALARM_CUSTOM22 = 0x915
    MINOR_ALARM_CUSTOM23 = 0x916
    MINOR_ALARM_CUSTOM24 = 0x917
    MINOR_ALARM_CUSTOM25 = 0x918
    MINOR_ALARM_CUSTOM26 = 0x919
    MINOR_ALARM_CUSTOM27 = 0x91a
    MINOR_ALARM_CUSTOM28 = 0x91b
    MINOR_ALARM_CUSTOM29 = 0x91c
    MINOR_ALARM_CUSTOM30 = 0x91d
    MINOR_ALARM_CUSTOM31 = 0x91e
    MINOR_ALARM_CUSTOM32 = 0x91f
    MINOR_ALARM_CUSTOM33 = 0x920
    MINOR_ALARM_CUSTOM34 = 0x921
    MINOR_ALARM_CUSTOM35 = 0x922
    MINOR_ALARM_CUSTOM36 = 0x923
    MINOR_ALARM_CUSTOM37 = 0x924
    MINOR_ALARM_CUSTOM38 = 0x925
    MINOR_ALARM_CUSTOM39 = 0x926
    MINOR_ALARM_CUSTOM40 = 0x927
    MINOR_ALARM_CUSTOM41 = 0x928
    MINOR_ALARM_CUSTOM42 = 0x929
    MINOR_ALARM_CUSTOM43 = 0x92a
    MINOR_ALARM_CUSTOM44 = 0x92b
    MINOR_ALARM_CUSTOM45 = 0x92c
    MINOR_ALARM_CUSTOM46 = 0x92d
    MINOR_ALARM_CUSTOM47 = 0x92e
    MINOR_ALARM_CUSTOM48 = 0x92f
    MINOR_ALARM_CUSTOM49 = 0x930
    MINOR_ALARM_CUSTOM50 = 0x931
    MINOR_ALARM_CUSTOM51 = 0x932
    MINOR_ALARM_CUSTOM52 = 0x933
    MINOR_ALARM_CUSTOM53 = 0x934
    MINOR_ALARM_CUSTOM54 = 0x935
    MINOR_ALARM_CUSTOM55 = 0x936
    MINOR_ALARM_CUSTOM56 = 0x937
    MINOR_ALARM_CUSTOM57 = 0x938
    MINOR_ALARM_CUSTOM58 = 0x939
    MINOR_ALARM_CUSTOM59 = 0x93a
    MINOR_ALARM_CUSTOM60 = 0x93b
    MINOR_ALARM_CUSTOM61 = 0x93c
    MINOR_ALARM_CUSTOM62 = 0x93d
    MINOR_ALARM_CUSTOM63 = 0x93e
    MINOR_ALARM_CUSTOM64 = 0x93f

class AcsAlarmInfoMajorException(Enum):
    MINOR_NET_BROKEN = 0x27
    MINOR_RS485_DEVICE_ABNORMAL = 0x3a
    MINOR_RS485_DEVICE_REVERT = 0x3b
    MINOR_DEV_POWER_ON = 0x400
    MINOR_DEV_POWER_OFF = 0x401
    MINOR_WATCH_DOG_RESET = 0x402
    MINOR_LOW_BATTERY = 0x403
    MINOR_BATTERY_RESUME = 0x404
    MINOR_AC_OFF = 0x405
    MINOR_AC_RESUME = 0x406
    MINOR_NET_RESUME = 0x407
    MINOR_FLASH_ABNORMAL = 0x408
    MINOR_CARD_READER_OFFLINE = 0x409
    MINOR_CARD_READER_RESUME = 0x40a
    MINOR_INDICATOR_LIGHT_OFF = 0x40b
    MINOR_INDICATOR_LIGHT_RESUME = 0x40c
    MINOR_CHANNEL_CONTROLLER_OFF = 0x40d
    MINOR_CHANNEL_CONTROLLER_RESUME = 0x40e
    MINOR_SECURITY_MODULE_OFF = 0x40f
    MINOR_SECURITY_MODULE_RESUME = 0x410
    MINOR_BATTERY_ELECTRIC_LOW = 0x411
    MINOR_BATTERY_ELECTRIC_RESUME = 0x412
    MINOR_LOCAL_CONTROL_NET_BROKEN = 0x413
    MINOR_LOCAL_CONTROL_NET_RSUME = 0x414
    MINOR_MASTER_RS485_LOOPNODE_BROKEN = 0x415
    MINOR_MASTER_RS485_LOOPNODE_RESUME = 0x416
    MINOR_LOCAL_CONTROL_OFFLINE = 0x417
    MINOR_LOCAL_CONTROL_RESUME = 0x418
    MINOR_LOCAL_DOWNSIDE_RS485_LOOPNODE_BROKEN = 0x419
    MINOR_LOCAL_DOWNSIDE_RS485_LOOPNODE_RESUME = 0x41a
    MINOR_LOCAL_LOGIN_LOCK = 0x428
    MINOR_LOCAL_LOGIN_UNLOCK = 0x429
    MINOR_SUBMARINEBACK_COMM_BREAK = 0x42a
    MINOR_SUBMARINEBACK_COMM_RESUME = 0x42b
    MINOR_MOTOR_SENSOR_EXCEPTION = 0x42c
    MINOR_CAN_BUS_EXCEPTION = 0x42d
    MINOR_CAN_BUS_RESUME = 0x42e
    MINOR_GATE_TEMPERATURE_OVERRUN = 0x42f
    MINOR_IR_EMITTER_EXCEPTION = 0x430
    MINOR_IR_EMITTER_RESUME = 0x431
    MINOR_LAMP_BOARD_COMM_EXCEPTION = 0x432
    MINOR_LAMP_BOARD_COMM_RESUME = 0x433
    MINOR_IR_ADAPTOR_COMM_EXCEPTION = 0x434
    MINOR_IR_ADAPTOR_COMM_RESUME = 0x435
    MINOR_EXCEPTION_CUSTOM1 = 0x900
    MINOR_EXCEPTION_CUSTOM2 = 0x901
    MINOR_EXCEPTION_CUSTOM3 = 0x902
    MINOR_EXCEPTION_CUSTOM4 = 0x903
    MINOR_EXCEPTION_CUSTOM5 = 0x904
    MINOR_EXCEPTION_CUSTOM6 = 0x905
    MINOR_EXCEPTION_CUSTOM7 = 0x906
    MINOR_EXCEPTION_CUSTOM8 = 0x907
    MINOR_EXCEPTION_CUSTOM9 = 0x908
    MINOR_EXCEPTION_CUSTOM10 = 0x909
    MINOR_EXCEPTION_CUSTOM11 = 0x90a
    MINOR_EXCEPTION_CUSTOM12 = 0x90b
    MINOR_EXCEPTION_CUSTOM13 = 0x90c
    MINOR_EXCEPTION_CUSTOM14 = 0x90d
    MINOR_EXCEPTION_CUSTOM15 = 0x90e
    MINOR_EXCEPTION_CUSTOM16 = 0x90f
    MINOR_EXCEPTION_CUSTOM17 = 0x910
    MINOR_EXCEPTION_CUSTOM18 = 0x911
    MINOR_EXCEPTION_CUSTOM19 = 0x912
    MINOR_EXCEPTION_CUSTOM20 = 0x913
    MINOR_EXCEPTION_CUSTOM21 = 0x914
    MINOR_EXCEPTION_CUSTOM22 = 0x915
    MINOR_EXCEPTION_CUSTOM23 = 0x916
    MINOR_EXCEPTION_CUSTOM24 = 0x917
    MINOR_EXCEPTION_CUSTOM25 = 0x918
    MINOR_EXCEPTION_CUSTOM26 = 0x919
    MINOR_EXCEPTION_CUSTOM27 = 0x91a
    MINOR_EXCEPTION_CUSTOM28 = 0x91b
    MINOR_EXCEPTION_CUSTOM29 = 0x91c
    MINOR_EXCEPTION_CUSTOM30 = 0x91d
    MINOR_EXCEPTION_CUSTOM31 = 0x91e
    MINOR_EXCEPTION_CUSTOM32 = 0x91f
    MINOR_EXCEPTION_CUSTOM33 = 0x920
    MINOR_EXCEPTION_CUSTOM34 = 0x921
    MINOR_EXCEPTION_CUSTOM35 = 0x922
    MINOR_EXCEPTION_CUSTOM36 = 0x923
    MINOR_EXCEPTION_CUSTOM37 = 0x924
    MINOR_EXCEPTION_CUSTOM38 = 0x925
    MINOR_EXCEPTION_CUSTOM39 = 0x926
    MINOR_EXCEPTION_CUSTOM40 = 0x927
    MINOR_EXCEPTION_CUSTOM41 = 0x928
    MINOR_EXCEPTION_CUSTOM42 = 0x929
    MINOR_EXCEPTION_CUSTOM43 = 0x92a
    MINOR_EXCEPTION_CUSTOM44 = 0x92b
    MINOR_EXCEPTION_CUSTOM45 = 0x92c
    MINOR_EXCEPTION_CUSTOM46 = 0x92d
    MINOR_EXCEPTION_CUSTOM47 = 0x92e
    MINOR_EXCEPTION_CUSTOM48 = 0x92f
    MINOR_EXCEPTION_CUSTOM49 = 0x930
    MINOR_EXCEPTION_CUSTOM50 = 0x931
    MINOR_EXCEPTION_CUSTOM51 = 0x932
    MINOR_EXCEPTION_CUSTOM52 = 0x933
    MINOR_EXCEPTION_CUSTOM53 = 0x934
    MINOR_EXCEPTION_CUSTOM54 = 0x935
    MINOR_EXCEPTION_CUSTOM55 = 0x936
    MINOR_EXCEPTION_CUSTOM56 = 0x937
    MINOR_EXCEPTION_CUSTOM57 = 0x938
    MINOR_EXCEPTION_CUSTOM58 = 0x939
    MINOR_EXCEPTION_CUSTOM59 = 0x93a
    MINOR_EXCEPTION_CUSTOM60 = 0x93b
    MINOR_EXCEPTION_CUSTOM61 = 0x93c
    MINOR_EXCEPTION_CUSTOM62 = 0x93d
    MINOR_EXCEPTION_CUSTOM63 = 0x93e
    MINOR_EXCEPTION_CUSTOM64 = 0x93f

class AcsAlarmInfoMajorOperation(Enum):
    MINOR_LOCAL_LOGIN = 0x50
    MINOR_LOCAL_UPGRADE = 0x5a
    MINOR_REMOTE_LOGIN = 0x70
    MINOR_REMOTE_LOGOUT = 0x71
    MINOR_REMOTE_ARM = 0x79
    MINOR_REMOTE_DISARM = 0x7a
    MINOR_REMOTE_REBOOT = 0x7b
    MINOR_REMOTE_UPGRADE = 0x7e
    MINOR_REMOTE_CFGFILE_OUTPUT = 0x86
    MINOR_REMOTE_CFGFILE_INTPUT = 0x87
    MINOR_REMOTE_ALARMOUT_OPEN_MAN = 0xd6
    MINOR_REMOTE_ALARMOUT_CLOSE_MAN = 0xd7
    MINOR_REMOTE_OPEN_DOOR = 0x400
    MINOR_REMOTE_CLOSE_DOOR = 0x401
    MINOR_REMOTE_ALWAYS_OPEN = 0x402
    MINOR_REMOTE_ALWAYS_CLOSE = 0x403
    MINOR_REMOTE_CHECK_TIME = 0x404
    MINOR_NTP_CHECK_TIME = 0x405
    MINOR_REMOTE_CLEAR_CARD = 0x406
    MINOR_REMOTE_RESTORE_CFG = 0x407
    MINOR_ALARMIN_ARM = 0x408
    MINOR_ALARMIN_DISARM = 0x409
    MINOR_LOCAL_RESTORE_CFG = 0x40a
    MINOR_REMOTE_CAPTURE_PIC = 0x40b
    MINOR_MOD_NET_REPORT_CFG = 0x40c
    MINOR_MOD_GPRS_REPORT_PARAM = 0x40d
    MINOR_MOD_REPORT_GROUP_PARAM = 0x40e
    MINOR_UNLOCK_PASSWORD_OPEN_DOOR = 0x40f
    MINOR_AUTO_RENUMBER = 0x410
    MINOR_AUTO_COMPLEMENT_NUMBER = 0x411
    MINOR_NORMAL_CFGFILE_INPUT = 0x412
    MINOR_NORMAL_CFGFILE_OUTTPUT = 0x413
    MINOR_CARD_RIGHT_INPUT  = 0x414
    MINOR_CARD_RIGHT_OUTTPUT = 0x415
    MINOR_LOCAL_USB_UPGRADE = 0x416
    MINOR_REMOTE_VISITOR_CALL_LADDER  = 0x417
    MINOR_REMOTE_HOUSEHOLD_CALL_LADDER = 0x418
    MINOR_REMOTE_ACTUAL_GUARD = 0x419
    MINOR_REMOTE_ACTUAL_UNGUARD = 0x41a
    MINOR_REMOTE_CONTROL_NOT_CODE_OPER_FAILED = 0x41b
    MINOR_REMOTE_CONTROL_CLOSE_DOOR = 0x41c
    MINOR_REMOTE_CONTROL_OPEN_DOOR = 0x41d
    MINOR_REMOTE_CONTROL_ALWAYS_OPEN_DOOR = 0x41e
    MINOR_OPERATION_CUSTOM1 = 0x900
    MINOR_OPERATION_CUSTOM2 = 0x901
    MINOR_OPERATION_CUSTOM3 = 0x902
    MINOR_OPERATION_CUSTOM4 = 0x903
    MINOR_OPERATION_CUSTOM5 = 0x904
    MINOR_OPERATION_CUSTOM6 = 0x905
    MINOR_OPERATION_CUSTOM7 = 0x906
    MINOR_OPERATION_CUSTOM8 = 0x907
    MINOR_OPERATION_CUSTOM9 = 0x908
    MINOR_OPERATION_CUSTOM10 = 0x909
    MINOR_OPERATION_CUSTOM11 = 0x90a
    MINOR_OPERATION_CUSTOM12 = 0x90b
    MINOR_OPERATION_CUSTOM13 = 0x90c
    MINOR_OPERATION_CUSTOM14 = 0x90d
    MINOR_OPERATION_CUSTOM15 = 0x90e
    MINOR_OPERATION_CUSTOM16 = 0x90f
    MINOR_OPERATION_CUSTOM17 = 0x910
    MINOR_OPERATION_CUSTOM18 = 0x911
    MINOR_OPERATION_CUSTOM19 = 0x912
    MINOR_OPERATION_CUSTOM20 = 0x913
    MINOR_OPERATION_CUSTOM21 = 0x914
    MINOR_OPERATION_CUSTOM22 = 0x915
    MINOR_OPERATION_CUSTOM23 = 0x916
    MINOR_OPERATION_CUSTOM24 = 0x917
    MINOR_OPERATION_CUSTOM25 = 0x918
    MINOR_OPERATION_CUSTOM26 = 0x919
    MINOR_OPERATION_CUSTOM27 = 0x91a
    MINOR_OPERATION_CUSTOM28 = 0x91b
    MINOR_OPERATION_CUSTOM29 = 0x91c
    MINOR_OPERATION_CUSTOM30 = 0x91d
    MINOR_OPERATION_CUSTOM31 = 0x91e
    MINOR_OPERATION_CUSTOM32 = 0x91f
    MINOR_OPERATION_CUSTOM33 = 0x920
    MINOR_OPERATION_CUSTOM34 = 0x921
    MINOR_OPERATION_CUSTOM35 = 0x922
    MINOR_OPERATION_CUSTOM36 = 0x923
    MINOR_OPERATION_CUSTOM37 = 0x924
    MINOR_OPERATION_CUSTOM38 = 0x925
    MINOR_OPERATION_CUSTOM39 = 0x926
    MINOR_OPERATION_CUSTOM40 = 0x927
    MINOR_OPERATION_CUSTOM41 = 0x928
    MINOR_OPERATION_CUSTOM42 = 0x929
    MINOR_OPERATION_CUSTOM43 = 0x92a
    MINOR_OPERATION_CUSTOM44 = 0x92b
    MINOR_OPERATION_CUSTOM45 = 0x92c
    MINOR_OPERATION_CUSTOM46 = 0x92d
    MINOR_OPERATION_CUSTOM47 = 0x92e
    MINOR_OPERATION_CUSTOM48 = 0x92f
    MINOR_OPERATION_CUSTOM49 = 0x930
    MINOR_OPERATION_CUSTOM50 = 0x931
    MINOR_OPERATION_CUSTOM51 = 0x932
    MINOR_OPERATION_CUSTOM52 = 0x933
    MINOR_OPERATION_CUSTOM53 = 0x934
    MINOR_OPERATION_CUSTOM54 = 0x935
    MINOR_OPERATION_CUSTOM55 = 0x936
    MINOR_OPERATION_CUSTOM56 = 0x937
    MINOR_OPERATION_CUSTOM57 = 0x938
    MINOR_OPERATION_CUSTOM58 = 0x939
    MINOR_OPERATION_CUSTOM59 = 0x93a
    MINOR_OPERATION_CUSTOM60 = 0x93b
    MINOR_OPERATION_CUSTOM61 = 0x93c
    MINOR_OPERATION_CUSTOM62 = 0x93d
    MINOR_OPERATION_CUSTOM63 = 0x93e
    MINOR_OPERATION_CUSTOM64 = 0x93f

class AcsAlarmInfoMajorEvent(Enum):
    MINOR_LEGAL_CARD_PASS = 0x01
    MINOR_CARD_AND_PSW_PASS = 0x02
    MINOR_CARD_AND_PSW_FAIL = 0x03
    MINOR_CARD_AND_PSW_TIMEOUT = 0x04
    MINOR_CARD_AND_PSW_OVER_TIME = 0x05
    MINOR_CARD_NO_RIGHT = 0x06
    MINOR_CARD_INVALID_PERIOD = 0x07
    MINOR_CARD_OUT_OF_DATE = 0x08
    MINOR_INVALID_CARD = 0x09
    MINOR_ANTI_SNEAK_FAIL = 0x0a
    MINOR_INTERLOCK_DOOR_NOT_CLOSE = 0x0b
    MINOR_NOT_BELONG_MULTI_GROUP = 0x0c
    MINOR_INVALID_MULTI_VERIFY_PERIOD = 0x0d
    MINOR_MULTI_VERIFY_SUPER_RIGHT_FAIL = 0x0e
    MINOR_MULTI_VERIFY_REMOTE_RIGHT_FAIL = 0x0f
    MINOR_MULTI_VERIFY_SUCCESS = 0x10
    MINOR_LEADER_CARD_OPEN_BEGIN = 0x11
    MINOR_LEADER_CARD_OPEN_END = 0x12
    MINOR_ALWAYS_OPEN_BEGIN = 0x13
    MINOR_ALWAYS_OPEN_END = 0x14
    MINOR_LOCK_OPEN = 0x15
    MINOR_LOCK_CLOSE = 0x16
    MINOR_DOOR_BUTTON_PRESS = 0x17
    MINOR_DOOR_BUTTON_RELEASE = 0x18
    MINOR_DOOR_OPEN_NORMAL = 0x19
    MINOR_DOOR_CLOSE_NORMAL = 0x1a
    MINOR_DOOR_OPEN_ABNORMAL = 0x1b
    MINOR_DOOR_OPEN_TIMEOUT = 0x1c
    MINOR_ALARMOUT_ON = 0x1d
    MINOR_ALARMOUT_OFF = 0x1e
    MINOR_ALWAYS_CLOSE_BEGIN = 0x1f
    MINOR_ALWAYS_CLOSE_END = 0x20
    MINOR_MULTI_VERIFY_NEED_REMOTE_OPEN = 0x21
    MINOR_MULTI_VERIFY_SUPERPASSWD_VERIFY_SUCCESS = 0x22
    MINOR_MULTI_VERIFY_REPEAT_VERIFY = 0x23
    MINOR_MULTI_VERIFY_TIMEOUT = 0x24
    MINOR_DOORBELL_RINGING = 0x25
    MINOR_FINGERPRINT_COMPARE_PASS = 0x26
    MINOR_FINGERPRINT_COMPARE_FAIL = 0x27
    MINOR_CARD_FINGERPRINT_VERIFY_PASS = 0x28
    MINOR_CARD_FINGERPRINT_VERIFY_FAIL = 0x29
    MINOR_CARD_FINGERPRINT_VERIFY_TIMEOUT = 0x2a
    MINOR_CARD_FINGERPRINT_PASSWD_VERIFY_PASS = 0x2b
    MINOR_CARD_FINGERPRINT_PASSWD_VERIFY_FAIL = 0x2c
    MINOR_CARD_FINGERPRINT_PASSWD_VERIFY_TIMEOUT = 0x2d
    MINOR_FINGERPRINT_PASSWD_VERIFY_PASS = 0x2e
    MINOR_FINGERPRINT_PASSWD_VERIFY_FAIL = 0x2f
    MINOR_FINGERPRINT_PASSWD_VERIFY_TIMEOUT = 0x30
    MINOR_FINGERPRINT_INEXISTENCE = 0x31
    MINOR_CARD_PLATFORM_VERIFY = 0x32
    MINOR_CALL_CENTER = 0x33
    MINOR_FIRE_RELAY_TURN_ON_DOOR_ALWAYS_OPEN = 0x34
    MINOR_FIRE_RELAY_RECOVER_DOOR_RECOVER_NORMAL = 0x35
    MINOR_FACE_AND_FP_VERIFY_PASS = 0x36
    MINOR_FACE_AND_FP_VERIFY_FAIL = 0x37
    MINOR_FACE_AND_FP_VERIFY_TIMEOUT  = 0x38
    MINOR_FACE_AND_PW_VERIFY_PASS = 0x39
    MINOR_FACE_AND_PW_VERIFY_FAIL = 0x3a
    MINOR_FACE_AND_PW_VERIFY_TIMEOUT  = 0x3b
    MINOR_FACE_AND_CARD_VERIFY_PASS = 0x3c
    MINOR_FACE_AND_CARD_VERIFY_FAIL = 0x3d
    MINOR_FACE_AND_CARD_VERIFY_TIMEOUT = 0x3e
    MINOR_FACE_AND_PW_AND_FP_VERIFY_PASS  = 0x3f
    MINOR_FACE_AND_PW_AND_FP_VERIFY_FAIL = 0x40
    MINOR_FACE_AND_PW_AND_FP_VERIFY_TIMEOUT = 0x41
    MINOR_FACE_CARD_AND_FP_VERIFY_PASS = 0x42
    MINOR_FACE_CARD_AND_FP_VERIFY_FAIL = 0x43
    MINOR_FACE_CARD_AND_FP_VERIFY_TIMEOUT = 0x44
    MINOR_EMPLOYEENO_AND_FP_VERIFY_PASS = 0x45
    MINOR_EMPLOYEENO_AND_FP_VERIFY_FAIL = 0x46
    MINOR_EMPLOYEENO_AND_FP_VERIFY_TIMEOUT = 0x47
    MINOR_EMPLOYEENO_AND_FP_AND_PW_VERIFY_PASS = 0x48
    MINOR_EMPLOYEENO_AND_FP_AND_PW_VERIFY_FAIL = 0x49
    MINOR_EMPLOYEENO_AND_FP_AND_PW_VERIFY_TIMEOUT = 0x4a
    MINOR_FACE_VERIFY_PASS = 0x4b
    MINOR_FACE_VERIFY_FAIL = 0x4c
    MINOR_EMPLOYEENO_AND_FACE_VERIFY_PASS = 0x4d
    MINOR_EMPLOYEENO_AND_FACE_VERIFY_FAIL = 0x4e
    MINOR_EMPLOYEENO_AND_FACE_VERIFY_TIMEOUT = 0x4f
    MINOR_FACE_NO_EXIST  = 0x50
    MINOR_FIRSTCARD_AUTHORIZE_BEGIN  = 0x51
    MINOR_FIRSTCARD_AUTHORIZE_END  = 0x52
    MINOR_DOORLOCK_INPUT_SHORT_CIRCUIT = 0x53
    MINOR_DOORLOCK_INPUT_BROKEN_CIRCUIT = 0x54
    MINOR_DOORLOCK_INPUT_EXCEPTION = 0x55
    MINOR_DOORCONTACT_INPUT_SHORT_CIRCUIT = 0x56
    MINOR_DOORCONTACT_INPUT_BROKEN_CIRCUIT = 0x57
    MINOR_DOORCONTACT_INPUT_EXCEPTION = 0x58
    MINOR_OPENBUTTON_INPUT_SHORT_CIRCUIT  = 0x59
    MINOR_OPENBUTTON_INPUT_BROKEN_CIRCUIT  = 0x5a
    MINOR_OPENBUTTON_INPUT_EXCEPTION = 0x5b
    MINOR_DOORLOCK_OPEN_EXCEPTION = 0x5c
    MINOR_DOORLOCK_OPEN_TIMEOUT = 0x5d
    MINOR_FIRSTCARD_OPEN_WITHOUT_AUTHORIZE = 0x5e
    MINOR_CALL_LADDER_RELAY_BREAK = 0x5f
    MINOR_CALL_LADDER_RELAY_CLOSE = 0x60
    MINOR_AUTO_KEY_RELAY_BREAK = 0x61
    MINOR_AUTO_KEY_RELAY_CLOSE = 0x62
    MINOR_KEY_CONTROL_RELAY_BREAK = 0x63
    MINOR_KEY_CONTROL_RELAY_CLOSE = 0x64
    MINOR_EMPLOYEENO_AND_PW_PASS = 0x65
    MINOR_EMPLOYEENO_AND_PW_FAIL = 0x66
    MINOR_EMPLOYEENO_AND_PW_TIMEOUT = 0x67
    MINOR_HUMAN_DETECT_FAIL = 0x68
    MINOR_PEOPLE_AND_ID_CARD_COMPARE_PASS = 0x69
    MINOR_PEOPLE_AND_ID_CARD_COMPARE_FAIL = 0x70
    MINOR_CERTIFICATE_BLACK_LIST = 0x71
    MINOR_LEGAL_MESSAGE = 0x72
    MINOR_ILLEGAL_MESSAGE = 0x73
    MINOR_DOOR_OPEN_OR_DORMANT_FAIL = 0x75
    MINOR_AUTH_PLAN_DORMANT_FAIL = 0x76
    MINOR_CARD_ENCRYPT_VERIFY_FAIL = 0x77
    MINOR_SUBMARINEBACK_REPLY_FAIL = 0x78
    MINOR_TRAILING = 0x85
    MINOR_REVERSE_ACCESS = 0x86
    MINOR_FORCE_ACCESS = 0x87
    MINOR_CLIMBING_OVER_GATE = 0x88
    MINOR_PASSING_TIMEOUT = 0x89
    MINOR_INTRUSION_ALARM = 0x8a
    MINOR_FREE_GATE_PASS_NOT_AUTH = 0x8b
    MINOR_DROP_ARM_BLOCK = 0x8c
    MINOR_DROP_ARM_BLOCK_RESUME = 0x8d
    MINOR_LOCAL_FACE_MODELING_FAIL = 0x8e
    MINOR_STAY_EVENT = 0x8f
    MINOR_EVENT_CUSTOM1 = 0x500
    MINOR_EVENT_CUSTOM2 = 0x501
    MINOR_EVENT_CUSTOM3 = 0x502
    MINOR_EVENT_CUSTOM4 = 0x503
    MINOR_EVENT_CUSTOM5 = 0x504
    MINOR_EVENT_CUSTOM6 = 0x505
    MINOR_EVENT_CUSTOM7 = 0x506
    MINOR_EVENT_CUSTOM8 = 0x507
    MINOR_EVENT_CUSTOM9 = 0x508
    MINOR_EVENT_CUSTOM10 = 0x509
    MINOR_EVENT_CUSTOM11 = 0x50a
    MINOR_EVENT_CUSTOM12 = 0x50b
    MINOR_EVENT_CUSTOM13 = 0x50c
    MINOR_EVENT_CUSTOM14 = 0x50d
    MINOR_EVENT_CUSTOM15 = 0x50e
    MINOR_EVENT_CUSTOM16 = 0x50f
    MINOR_EVENT_CUSTOM17 = 0x510
    MINOR_EVENT_CUSTOM18 = 0x511
    MINOR_EVENT_CUSTOM19 = 0x512
    MINOR_EVENT_CUSTOM20 = 0x513
    MINOR_EVENT_CUSTOM21 = 0x514
    MINOR_EVENT_CUSTOM22 = 0x515
    MINOR_EVENT_CUSTOM23 = 0x516
    MINOR_EVENT_CUSTOM24 = 0x517
    MINOR_EVENT_CUSTOM25 = 0x518
    MINOR_EVENT_CUSTOM26 = 0x519
    MINOR_EVENT_CUSTOM27 = 0x51a
    MINOR_EVENT_CUSTOM28 = 0x51b
    MINOR_EVENT_CUSTOM29 = 0x51c
    MINOR_EVENT_CUSTOM30 = 0x51d
    MINOR_EVENT_CUSTOM31 = 0x51e
    MINOR_EVENT_CUSTOM32 = 0x51f
    MINOR_EVENT_CUSTOM33 = 0x520
    MINOR_EVENT_CUSTOM34 = 0x521
    MINOR_EVENT_CUSTOM35 = 0x522
    MINOR_EVENT_CUSTOM36 = 0x523
    MINOR_EVENT_CUSTOM37 = 0x524
    MINOR_EVENT_CUSTOM38 = 0x525
    MINOR_EVENT_CUSTOM39 = 0x526
    MINOR_EVENT_CUSTOM40 = 0x527
    MINOR_EVENT_CUSTOM41 = 0x528
    MINOR_EVENT_CUSTOM42 = 0x529
    MINOR_EVENT_CUSTOM43 = 0x52a
    MINOR_EVENT_CUSTOM44 = 0x52b
    MINOR_EVENT_CUSTOM45 = 0x52c
    MINOR_EVENT_CUSTOM46 = 0x52d
    MINOR_EVENT_CUSTOM47 = 0x52e
    MINOR_EVENT_CUSTOM48 = 0x52f
    MINOR_EVENT_CUSTOM49 = 0x530
    MINOR_EVENT_CUSTOM50 = 0x531
    MINOR_EVENT_CUSTOM51 = 0x532
    MINOR_EVENT_CUSTOM52 = 0x533
    MINOR_EVENT_CUSTOM53 = 0x534
    MINOR_EVENT_CUSTOM54 = 0x535
    MINOR_EVENT_CUSTOM55 = 0x536
    MINOR_EVENT_CUSTOM56 = 0x537
    MINOR_EVENT_CUSTOM57 = 0x538
    MINOR_EVENT_CUSTOM58 = 0x539
    MINOR_EVENT_CUSTOM59 = 0x53a
    MINOR_EVENT_CUSTOM60 = 0x53b
    MINOR_EVENT_CUSTOM61 = 0x53c
    MINOR_EVENT_CUSTOM62 = 0x53d
    MINOR_EVENT_CUSTOM63 = 0x53e
    MINOR_EVENT_CUSTOM64 = 0x53f

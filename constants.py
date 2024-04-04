from enum import Enum

class Globals(Enum):
    INSIM_VERSION = 8
    MAX_PLAYERS = 40


class ISP(Enum):
    # Enum for packet types
    ISP_NONE = 0
    ISP_ISI = 1
    ISP_VER = 2
    ISP_TINY = 3
    ISP_SMALL = 4
    ISP_STA = 5
    ISP_SCH = 6
    ISP_SFP = 7
    ISP_SCC = 8
    ISP_CPP = 9
    ISP_ISM = 10
    ISP_MSO = 11
    ISP_III = 12
    ISP_MST = 13
    ISP_MTC = 14
    ISP_MOD = 15
    ISP_VTN = 16
    ISP_RST = 17
    ISP_NCN = 18
    ISP_CNL = 19
    ISP_CPR = 20
    ISP_NPL = 21
    ISP_PLP = 22
    ISP_PLL = 23
    ISP_LAP = 24
    ISP_SPX = 25
    ISP_PIT = 26
    ISP_PSF = 27
    ISP_PLA = 28
    ISP_CCH = 29
    ISP_PEN = 30
    ISP_TOC = 31
    ISP_FLG = 32
    ISP_PFL = 33
    ISP_FIN = 34
    ISP_RES = 35
    ISP_REO = 36
    ISP_NLP = 37
    ISP_MCI = 38
    ISP_MSX = 39
    ISP_MSL = 40
    ISP_CRS = 41
    ISP_BFN = 42
    ISP_AXI = 43
    ISP_AXO = 44
    ISP_BTN = 45
    ISP_BTC = 46
    ISP_BTT = 47
    ISP_RIP = 48
    ISP_SSH = 49
    ISP_CON = 50
    ISP_OBH = 51
    ISP_HLV = 52
    ISP_PLC = 53
    ISP_AXM = 54
    ISP_ACR = 55
    ISP_HCP = 56
    ISP_NCI = 57
    ISP_JRR = 58
    ISP_UCO = 59
    ISP_OCO = 60
    ISP_TTC = 61
    ISP_SLC = 62
    ISP_CSC = 63
    ISP_CIM = 64


class IRP(Enum):
    # Relay packets.
    IRP_ARQ = 250
    IRP_ARP = 251
    IRP_HLR = 252
    IRP_HOS = 253
    IRP_SEL = 254
    IRP_ERR = 255


class TINY(Enum):
    # Enum for IS_TINY sub-type
    TINY_NONE = 0
    TINY_VER = 1
    TINY_CLOSE = 2
    TINY_PING = 3
    TINY_REPLY = 4
    TINY_VTC = 5
    TINY_SCP = 6
    TINY_SST = 7
    TINY_GTH = 8
    TINY_MPE = 9
    TINY_ISM = 10
    TINY_REN = 11
    TINY_CLR = 12
    TINY_NCN = 13
    TINY_NPL = 14
    TINY_RES = 15
    TINY_NLP = 16
    TINY_MCI = 17
    TINY_REO = 18
    TINY_RST = 19
    TINY_AXI = 20
    TINY_AXC = 21
    TINY_RIP = 22
    TINY_NCI = 23
    TINY_ALC = 24
    TINY_AXM = 25
    TINY_SLC = 26
class SMALL(Enum):   
    # Enum for IS_SMALL sub-type
    SMALL_NONE = 0
    SMALL_SSP = 1
    SMALL_SSG = 2
    SMALL_VTA = 3
    SMALL_TMS = 4
    SMALL_STP = 5
    SMALL_RTP = 6
    SMALL_NLI = 7
    SMALL_ALC = 8
    SMALL_LCS = 9

class TTC(Enum):
    # Fourth byte of IS_TTC
    TTC_NONE = 0
    TTC_SEL = 1
    TTC_SEL_START = 2
    TTC_SEL_STOP = 3

class ISF(Enum):
    # Bit flags for ISI Flags
    ISF_RES_0 = 1
    ISF_RES_1 = 2
    ISF_LOCAL = 4
    ISF_MSO_COLS = 8
    ISF_NLP = 16
    ISF_MCI = 32
    ISF_CON = 64
    ISF_OBH = 128
    ISF_HLV = 256
    ISF_AXM_LOAD = 512
    ISF_AXM_EDIT = 1024
    ISF_REQ_JOIN = 2048

class MSO(Enum):
    # Enum for IS_MSO UserType
    MSO_SYSTEM = 0
    MSO_USER = 1
    MSO_PREFIX = 2
    MSO_O = 3

class SND(Enum):
    # Enum for IS_MSL Sound
    SND_SILENT = 0
    SND_MESSAGE = 1
    SND_SYSMESSAGE = 2
    SND_INVALIDKEY = 3
    SND_ERROR = 4
class VOTE(Enum):
    # Enum for IS_VTN Action
    VOTE_NONE = 0
    VOTE_END = 1
    VOTE_RESTART = 2
    VOTE_QUALIFY = 3
class PITLANE(Enum):
    # Enum for IS_PLA Fact
    PITLANE_EXIT = 0
    PITLANE_ENTER = 1
    PITLANE_NO_PURPOSE = 2
    PITLANE_DT = 3
    PITLANE_SG = 4
class VIEW(Enum):
    # Enum for IS_STA InGameCam
    VIEW_FOLLOW = 0
    VIEW_HELI = 1
    VIEW_CAM = 2
    VIEW_DRIVER = 3
    VIEW_CUSTOM = 4
    VIEW_ANOTHER = 255
class LEAVR(Enum):
    # Enum for IS_CNL Reason
    LEAVR_DISCO = 0
    LEAVR_TIMEOUT = 1
    LEAVR_LOSTCONN = 2
    LEAVR_KICKED = 3
    LEAVR_BANNED = 4
    LEAVR_SECURITY = 5
    LEAVR_CPW = 6
    LEAVR_OOS = 7
    LEAVR_JOOS = 8
    LEAVR_HACK = 9
class PENALTY(Enum):
    # Enum for IS_PEN Penalty
    PENALTY_NONE = 0
    PENALTY_DT = 1
    PENALTY_DT_VALID = 2
    PENALTY_SG = 3
    PENALTY_SG_VALID = 4
    PENALTY_30 = 5
    PENALTY_45 = 6
class PENR(Enum):
    # Enum for IS_PEN Reason
    PENR_UNKNOWN = 1
    PENR_ADMIN = 2
    PENR_WRONG_WAY = 3
    PENR_FALSE_START = 4
    PENR_SPEEDING = 5
    PENR_STOP_SHORT = 6
    PENR_STOP_LATE = 7
class TYRE(Enum):
    # Enum for IS_PIT Tyres
    TYRE_R1 = 0
    TYRE_R2 = 1
    TYRE_R3 = 2
    TYRE_R4 = 3
    TYRE_ROAD_SUPER = 4
    TYRE_ROAD_NORMAL = 5
    TYRE_HYBRID = 6
    TYRE_KNOBBLY = 7
    TYRE_NOT_CHANGED = 255
class ISS(Enum):
    # Bit flags for IS_STA Flags
    ISS_GAME = 1
    ISS_REPLAY = 2
    ISS_PAUSED = 4
    ISS_SHIFTU = 8
    ISS_DIALOG = 16
    ISS_SHIFTU_FOLLOW = 32
    ISS_SHIFTU_NO_OPT = 64
    ISS_SHOW_2D = 128
    ISS_FRONT_END = 256
    ISS_MULTI = 512
    ISS_MPSPEEDUP =    1024
    ISS_WINDOWED = 2048
    ISS_SOUND_MUTE = 4096
    ISS_VIEW_OVERRIDE = 8192
    ISS_VISIBLE = 16384
    ISS_TEXT_ENTRY = 32768
class PSE(Enum):
    # Bit flags for IS_PIT Work
    PSE_NOTHING = 1
    PSE_STOP = 2
    PSE_FR_DAM = 4
    PSE_FR_WHL = 8
    PSE_LE_FR_DAM = 16
    PSE_LE_FR_WHL = 32
    PSE_RI_FR_DAM = 64
    PSE_RI_FR_WHL = 128
    PSE_RE_DAM = 256
    PSE_RE_WHL = 512
    PSE_LE_RE_DAM = 1024
    PSE_LE_RE_WHL = 2048
    PSE_RI_RE_DAM = 4096
    PSE_RI_RE_WHL = 8192
    PSE_BODY_MINOR = 16384
    PSE_BODY_MAJOR = 32768
    PSE_SETUP = 65536
    PSE_REFUEL = 131072
    PSE_NUM = 262144
class PIF(Enum):
    # Bit flags for IS_NPL Flags
    PIF_SWAPSIDE = 1
    PIF_RESERVED_2 = 2
    PIF_RESERVED_4 = 4
    PIF_AUTOGEARS = 8
    PIF_SHIFTER = 16
    PIF_RESERVED_32 = 32
    PIF_HELP_B = 64
    PIF_AXIS_CLUTCH = 128
    PIF_INPITS = 256
    PIF_AUTOCLUTCH = 512
    PIF_MOUSE = 1024
    PIF_KB_NO_HELP = 2048
    PIF_KB_STABILISED = 4096
    PIF_CUSTOM_VIEW = 8192
class CONF(Enum):
    # Bit flags for IS_RES Confirm
    CONF_MENTIONED = 1
    CONF_CONFIRMED = 2
    CONF_PENALTY_DT = 4
    CONF_PENALTY_SG = 8
    CONF_PENALTY_30 = 16
    CONF_PENALTY_45 = 32
    CONF_DID_NOT_PIT = 64
    CONF_DISQ = CONF_PENALTY_DT | CONF_PENALTY_SG | CONF_DID_NOT_PIT
    CONF_TIME = CONF_PENALTY_30 | CONF_PENALTY_45
class HOSTF(Enum):
    # Bit flags for IS_RST Flags
    HOSTF_CAN_VOTE = 1
    HOSTF_CAN_SELECT = 2
    HOSTF_MID_RACE = 32
    HOSTF_MUST_PIT = 64
    HOSTF_CAN_RESET = 128
    HOSTF_FCV = 256
    HOSTF_CRUISE = 512
class CCI(Enum):
    # Bit flags for CompCar Info
    CCI_BLUE = 1
    CCI_YELLOW = 2
    CCI_LAG    = 32
    CCI_FIRST = 64
    CCI_LAST = 128
class BFN(Enum):
    # Enum for IS_BFN SubT
    BFN_DEL_BTN = 0
    BFN_CLEAR = 1
    BFN_USER_CLEAR = 2
    BFN_REQUEST = 3
    INST_ALWAYS_ON = 128
class ISB(Enum):
    # Bit flags for IS_BTN BStyle
    ISB_C1 = 1
    ISB_C2 = 2
    ISB_C4 = 4
    ISB_CLICK = 8
    ISB_LIGHT = 16
    ISB_DARK = 32
    ISB_LEFT = 64
    ISB_RIGHT = 128
    # Bit flags for BTN CFlags
    ISB_LMB = 1
    ISB_RMB = 2
    ISB_CTRL = 4
    ISB_SHIFT = 8
class RIP(Enum):
    # Enum for IS_RIP Error
    RIP_OK = 0
    RIP_ALREADY = 1
    RIP_DEDICATED = 2
    RIP_WRONG_MODE = 3
    RIP_NOT_REPLAY = 4
    RIP_CORRUPTED = 5
    RIP_NOT_FOUND = 6
    RIP_UNLOADABLE = 7
    RIP_DEST_OOB = 8
    RIP_UNKNOWN = 9
    RIP_USER = 10
    RIP_OOS = 11
class RIPOPT(Enum):
    # Enum for IS_RIP Options
    RIPOPT_LOOP = 1
    RIPOPT_SKINS = 2
    RIPOPT_FULL_PHYS = 4
class SSH(Enum):
    # Enum for IS_SSH Error
    SSH_OK = 0
    SSH_DEDICATED = 1
    SSH_CORRUPTED = 2
    SSH_NO_SAVE = 3
class SETF(Enum):
    # Bit flags for IS_NPL SetF
    SETF_SYMM_WHEELS = 1
    SETF_TC_ENABLE = 2
    SETF_ABS_ENABLE = 4
class LANG(Enum):
    # Languages
    LFS_ENGLISH = 0
    LFS_DEUTSCH = 1
    LFS_PORTUGUESE = 2
    LFS_FRENCH = 3
    LFS_SUOMI = 4
    LFS_NORSK = 5
    LFS_NEDERLANDS = 6
    LFS_CATALAN = 7
    LFS_TURKISH = 8
    LFS_CASTELLANO = 9
    LFS_ITALIANO = 10
    LFS_DANSK = 11
    LFS_CZECH = 12
    LFS_RUSSIAN = 13
    LFS_ESTONIAN = 14
    LFS_SERBIAN = 15
    LFS_GREEK = 16
    LFS_POLSKI = 17
    LFS_CROATIAN = 18
    LFS_HUNGARIAN = 19
    LFS_BRAZILIAN = 20
    LFS_SWEDISH = 21
    LFS_SLOVAK = 22
    LFS_GALEGO = 23
    LFS_SLOVENSKI = 24
    LFS_BELARUSSIAN = 25
    LFS_LATVIAN = 26
    LFS_LITHUANIAN = 27
    LFS_TRADITIONAL_CHINESE = 28
    LFS_SIMPLIFIED_CHINESE = 29
    LFS_JAPANESE = 30
    LFS_KOREAN = 31
    LFS_BULGARIAN = 32
    LFS_LATINO = 33
    LFS_UKRAINIAN = 34
    LFS_INDONESIAN = 35
    LFS_ROMANIAN = 36
class AOBJ(Enum):
    # Autocross Objects
    AXO_START_LIGHTS = 149
    MARSH_IS_CP = 252       # insim checkpoint
    MARSH_IS_AREA = 253     # insim circle
    MARSH_MARSHALL = 254    # restricted area
    MARSH_ROUTE	= 255       # route checker
class FLAGS(Enum):
    # SMALL_LCS Flags
    LCS_SET_SIGNALS = 1		# bit 0
    LCS_SET_FLASH = 2		# bit 1
    LCS_SET_HEADLIGHTS = 4	# bit 2
    LCS_SET_HORN = 8		# bit 3
    LCS_SET_SIREN = 0x10	# bit 4

    LCS_Mask_Signals = 0x0300       # bits  8-9   (Switches & 0x0300) - Signal    (0 off / 1 left / 2 right / 3 hazard)
    LCS_Mask_Flash = 0x0400         # bit   10    (Switches & 0x0400) - Flash
    LCS_Mask_Headlights = 0x0800    # bit	11    (Switches & 0x0800) - Headlights
    LCS_Mask_Horn = 0x070000        # bits  16-18 (Switches & 0x070000) - Horn    (0 off / 1 to 5 horn type)
    LCS_Mask_Siren = 0x300000       # bits  20-21 (Switches & 0x300000) - Siren   (0 off / 1 fast / 2 slow)
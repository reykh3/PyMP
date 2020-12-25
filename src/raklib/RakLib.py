"""
 __ _____         ___    ___      _____ ______           ________
|\   __  \       |\  \  /  /|    |\   _ \  _   \        |\   __  \
\ \  \|\  \      \ \  \/  / /    \ \  \\\__\ \  \       \ \  \|\  \
 \ \   ____\      \ \    / /      \ \  \\|__| \  \       \ \   ____\
  \ \  \___|       \/  /  /        \ \  \    \ \  \       \ \  \___|
   \ \__\        __/  / /           \ \__\    \ \__\       \ \__\
    \|__|       |\___/ /             \|__|     \|__|        \|__|
                \|___|/

"""

class RakLib:

    VERSION = '0.9.0'
    PROTOCOL = 6
    MAGIC = "\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"

    PRIORITY_NORMAL = 1
    PRIORITY_IMMENDIATE = 0

    FLAG_NEED_ACK = 0b00001000

    PACKET_ENCAPSULATED = 0x01
    PACKET_OPEN_SESSION = 0x02
    PACKET_CLOSE_SESSION = 0x03
    PACKET_INVALID_SESSION = 0x04
    PACKET_SEND_QUEUE = 0x05
    PACKET_ACK_NOTIFICATION = 0x06
    PACKET_SET_OPTION = 0x07
    PACKET_RAW = 0x08
    PACKET_BLOCK_ADDRESS = 0x09
    PACKET_UNBLOCK_ADDRESS = 0x0a
    PACKET_REPORT_PING = 0x11
    PACKET_SHUTDOWN = 0x7e
    PACKET_EMERGENCY_SHUTDOWN = 0x7f

    SYSTEM_ADDRESS_COUNT = 20

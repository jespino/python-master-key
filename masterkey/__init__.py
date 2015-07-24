import ctypes
from operator import xor

longsize = ctypes.sizeof(ctypes.c_long)

def open_class(klass):
    int_flags = ctypes.c_long.from_address(id(klass) + longsize * 21)
    int_flags.value |= 1 << 9

def close_class(klass):
    int_flags = ctypes.c_long.from_address(id(klass) + longsize * 21)
    int_flags.value = xor(int_flags.value, 1 << 9)

import ctypes

def open_class(klass):
    int_flags = ctypes.c_long.from_address(id(klass) + ctypes.sizeof(ctypes.c_long) * 21)
    int_flags.value |= 1 << 9

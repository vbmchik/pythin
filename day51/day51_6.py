from ctypes import c_uint8 as unsigned_byte

print(unsigned_byte(-42).value)
#  10101010 - 170
#  00101010 - 42
#  11010110 - 214
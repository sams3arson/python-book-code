import struct

# 'data' contains width and height of image in binary; taken from a PNG file
data = b"\x00\x00\x00\x9a" + b"\x00\x00\x00\x8d"
print(data)

width, height = struct.unpack(">LL", data)
print(width, height)
# explanation: first argument of unpack is a string that tells how to interpret
# input byte sequences;
# > означает, что целые числа хранятся в формате big-endian (прямой порядок байтов)
# L означает четырехбайтовое целое число типа unsigned long

# обратно:
bwidth = struct.pack(">L", width)
bheight = struct.pack(">L", height)
print(bwidth, bheight)

struct.unpack(">2L", data) # 2L instead of LL

# for all specificators, look at screenshot or visit
# https://www.bestprog.net/ru/2020/05/08/python-module-struct-packing-unpacking-data-basic-methods-ru
# have a look at following modules: bitstring, construct, kaitai, hachoir, binio


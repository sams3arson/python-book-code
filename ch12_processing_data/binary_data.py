# 2 types of binary data:
# bytes - immutable, like tuple of bytes
# bytearray - mutable, like list of bytes

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

# bytes - immutable, bytearray - mutable
try:
    the_bytes[1] = 127
except TypeError as e:
    print(e)

print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

the_bytes = bytes(list(range(0, 256)) + list(range(0, 256)))
print(the_bytes)


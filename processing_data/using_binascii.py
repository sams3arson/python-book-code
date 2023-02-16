import binascii

# обычно питон для содержимого байтов выводит символы ascii и escape последовательности
# 

valid_png_header = b"\x89PNG\r\n\x1a\n"
hexlified_header = binascii.hexlify(valid_png_header)
print(hexlified_header)

header_back = binascii.unhexlify(hexlified_header)
print(header_back)



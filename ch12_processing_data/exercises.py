# 12.1
mystery = "\U0001f4a9"
print(mystery)
import unicodedata
print(ord(mystery), unicodedata.name(mystery))

# 12.2
pop_bytes = mystery.encode("utf-8")
print(pop_bytes)

# 12.3
pop_string = pop_bytes.decode("utf-8")
print(pop_string, pop_string == mystery)

# 12.4
mammoth = """We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.
Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing oh! Queen of Cheese.
We'rt thou suspended from baloon,
You'd caste a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon."""

# 12.5
import re
print(re.findall(r"\bc\w*", mammoth))

# 12.6
print(re.findall(r"\bc\w{4}\b", mammoth))

# 12.7
print(re.findall(r"[\s^](r\w*)", mammoth))

# 12.8
print(re.findall(r"\w*[euioa]{3}\w*", mammoth))
print(re.findall(r"\b\w*[aeiou]{3}\w*\b", mammoth))

# 12.9
import binascii
bin_string = "47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b"
gif = binascii.unhexlify(bin_string)
print(gif)

# 12.10
if gif[:6] == b"GIF89a":
    print("Correct gif")

# 12.11
import struct
width, height = struct.unpack("<2H", gif[6:10])
print(width, height)


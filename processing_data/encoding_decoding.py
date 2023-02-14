fuck = "🖕"
print(fuck, len(fuck))

fuck_enc = fuck.encode("utf-8")
print(fuck_enc, len(fuck_enc))

try:
    fuck_ascii = fuck.encode("ascii")
except UnicodeEncodeError as e:
    print(e)


# str.encode() can take second arg:
# 'ignore' = ignore any symbols that can't be encoded
# 'replace' = replace those symbols with ?
# 'backslashreplace' = replace those symbols with unicode escape sequences (\u....)
# 'xmlcharrefreplace' = encode to strings that are safe for html

place = "caf\u00e9"
print(place, type(place), len(place))
place_bytes = place.encode("utf-8")
print(place_bytes, type(place_bytes), len(place_bytes))

place_decoded = place_bytes.decode("utf-8")
print(place_decoded)

try:
    place2_dec = place_bytes.decode("ascii") # trying to decode with wrong encoding
except UnicodeDecodeError as e:
    print(e)

# best advice: use utf-8 everywhere possible and make sure that sources of your data
# are using utf-8, or at least get to know their encoding.


# HTML Entities #
# Another way of encoding is html mnemonic symbols (мнемонические символы, символы-мнемоники).
# (Especially if you're working with web apps)

import html

# from html entity to python unicode symbol:
print("unescape by code:", html.unescape("&#233")) # by code
print("unescape by name:", html.unescape("&eacute;")) # by name
print("from dict by name:", html.entities.html5["eacute;"]) # from a dict; only by name

# from python unicode symbol to html entity:
char = "\u00e9"
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])

# or by encode+decode (easier way):
place = "caf\u00e9"
byte_value = place.encode("ascii", "xmlcharrefreplace")
print(byte_value, type(byte_value))
place_redecoded = byte_value.decode()
print(place_redecoded, type(place_redecoded))

# Normalization #
# case: we have two é's - e with acute and default e, with added combining acute
# in comparison, they will be different. we can fix that with function
# unicodedata.normalize("NFC", symbol); "NFC" stands for "normal form, composed"
# (нормальная форма, составной символ)
eacute = "\N{LATIN SMALL LETTER E WITH ACUTE}"
eacute_combined = "e\N{COMBINING ACUTE ACCENT}"
print(eacute, eacute_combined) # look same
print(len(eacute), len(eacute_combined)) # different length
print(eacute == eacute_combined) # not equal

# how to fix:
import unicodedata
eacute_normalized = unicodedata.normalize("NFC", eacute_combined)
print("normalized:", eacute_normalized)
print(len(eacute_normalized)) # 1
print(eacute == eacute_normalized)
print(unicodedata.name(eacute_normalized))


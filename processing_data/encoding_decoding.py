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


import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f"{value=}, {len(value)=}, {name=}, {value2=}")

unicode_test("A")
unicode_test("$")
unicode_test("🖕")
unicode_test("\u20ac")
unicode_test("\N{LATIN SMALL LETTER E WITH ACUTE}")

fuck = "🖕"
print(ord(fuck), chr(ord(fuck)))


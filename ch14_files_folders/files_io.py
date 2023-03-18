poem = """There was a young lady named Bright,
Whose speed was far faster than light;
She set out one day
In a relative way,
And returned on the previous night."""
print("porm length:", len(poem))

fout = open("relativity", "w")
fout.write(poem)
fout.close()

# записываем строку по фрагментам
offset = 0
chunk = 100
size = len(poem)
fout = open("relativity", "w")
while offset < size:
    fout.write(poem[offset:offset + chunk])
    offset += chunk
fout.close()

# x mode will prevent from rewriting already existing file
# will only work if that file doesn't exist
try:
    fout = open("relativity", "x")
except FileExistsError as e:
    print(e)

# reading big files
poem = ""
fin = open("relativity", "r")
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print("read; len:", len(poem))

# reading by line
poem = ""
fin = open("relativity", "r")
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print("read by line; len:", len(poem))

# also reading by line
poem = ""
fin = open("relativity", "r")
for line in fin:
    poem += line
fin.close()
print("read by line (less code); len:", len(poem))

# readlines = list of lines
fin = open("relativity", "r")
lines = fin.readlines()
fin.close()
print(len(lines), "lines read")
for line in lines:
    print(line, end="") # lines already contain "\n" except the last one
print()

# writing bytes
bdata = bytes(range(0, 256))
print(len(bdata))
fout = open("bfile", "wb")
fout.write(bdata)
fout.close()

# reading bytes
fin = open("bfile", "rb")
bdata = fin.read()
print("read bytes:", len(bdata))
fin.close()

# changing position in the file using seek()
fin = open("bfile", "rb")
print("current position:", fin.tell())
fin.seek(255)
bdata = fin.read()
print(bdata, len(bdata))

# seek() syntax: seek(offset, origin)
# origin = 0: move [offset] bytes from the starting of file (default)
# origin = 1: move [offset] bytes from current position in file
# origin = 2: move [offset] bytes from the end of file (add minus to offset value)
fin = open("bfile", "rb")
fin.seek(-1, 2)
print(fin.tell())
bdata = fin.read()
print(bdata, len(bdata))

# WARNING: use seek() in binary mode; when using in text mode, amount of bytes
# on every symbol will vary depending on encoding

# INFO: have a look at mmap - memory-mapped file support
# https://docs.python.org/3.7/library/mmap.html


import os

# if files exists
print("#file-existance")

print(os.path.exists("relativity"))
print(os.path.exists("./relativity"))
print(os.path.exists("waffles"))
print(os.path.exists("."), os.path.exists(".."))

print()
# if the filename refers to a file or a dir
print("#filename-type")
name = "relativity"
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir("."))

# abosulte pathname
print(os.path.isabs(name))
print(os.path.isabs("/big/fake/name"))

# copying and moving files
import shutil
shutil.copy("relativity", "bullshit")
shutil.move("bullshit", "bullshit_moved")

# renaming
os.rename("bullshit_moved", "bullshit")

# links and symlinks
os.link("bullshit", "bullshit_link")
print(os.path.isfile("bullshit_link"))
os.remove("bullshit_link")

os.symlink("bullshit", "bullshit_symlink")
print(os.path.isfile("bullshit"),
      os.path.islink("bullshit"))
os.remove("bullshit_symlink")

# chmod
# as second arg we pass octadecimal number (0o prefix) that represents rights
# as it would when we do 'chmod [number]'
os.chmod("bullshit", 0o755)

# chown
uid = 5 # user ID
gid = 22 # group ID
# syntax:
# os.chown(pathname, uid, gid)

# removing
os.remove("bullshit")
print(os.path.exists("bullshit"))


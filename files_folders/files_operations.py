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


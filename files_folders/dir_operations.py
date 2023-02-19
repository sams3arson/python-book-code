#### deleting poems for the script to work (unempty dir)
import shutil
shutil.rmtree("poems")
####

import os


# creating dirs
os.mkdir("poems")
print(os.path.exists("poems"))

# deleting dirs
os.rmdir("poems")
print(os.path.exists("poems"))

# listing dirs
os.mkdir("poems")
print(os.listdir("poems"))
os.mkdir("poems/mcintyre")
print(os.listdir("poems"))

with open("poems/mcintyre/the_good_man", "w") as fout:
    fout.write("Fuck you.")

print(os.listdir("poems/mcintyre"))

# changing dirs (current dir, cwd)
os.chdir("poems")
print(os.listdir("."))

# finding filenames, matching Unix shell patterns (*, ?, [abc], [!abc], etc.)
import glob
print(glob.glob("m*"))
print(glob.glob("??"))
print(glob.glob("[klm]*e"))


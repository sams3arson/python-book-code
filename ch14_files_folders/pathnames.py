import os

# use \\ or r"" when creating pathnames for windows
win_file = "eek\\urk\\snort.txt"
win_file2 = r"eek\urk\snort.txt"

# abs path
print(os.path.abspath("relativity"))

# real path (use on a symlink to get path to the original file)
print(os.path.realpath("relativity"))

# creating pathname from pieces
win_file = os.path.join("eek", "urk")
win_file = os.path.join(win_file, "snort.txt")


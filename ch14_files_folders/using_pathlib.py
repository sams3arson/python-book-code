from pathlib import Path
import pprint

# working with pathnames on a higher level
# you can
file_path = Path("eek") / "urk" / "snort.txt"
pprint.pprint(file_path)
print(file_path.name, file_path.suffix, file_path.stem)

from pathlib import PureWindowsPath
pprint.pprint(PureWindowsPath(file_path))


import os
import re

dirs = [f.split(".")[0] for f in os.listdir(".") if re.match(".*\.md$", f) != None and f!="index.md"]

for i in range(len(dirs)):
    dirs[i] = "- [{}]({})".format(dirs[i], dirs[i])

_list="\n".join(dirs)

with open("index.md", "w") as f:
    f.write("# IDC409\n## List of topics\n\n")
    f.write(_list)


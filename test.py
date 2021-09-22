# python批量更换后缀名
import os
import sys
import re

# 列出当前目录下所有的文件
files = os.listdir('.')
for filename in files:
	portion = os.path.splitext(filename)
	if portion[1] == ".cpp" or portion[1] == ".c":
		# 重新组合文件名和后缀名
		newname = "test" + ".txt"
		os.rename(filename,newname)

PY_PATTERN = re.compile(

	r"""

     \s*\#(?:[^\r\n])*

     | \s*__(?:[^\r\n]*)

     | "{3}(?:\\.|[^\\])*"{3}

     | '{3}(?:\\.|[^\\])*'{3}

     """,

	re.VERBOSE | re.MULTILINE | re.DOTALL

)

txt = open("test.txt").readlines()

b = re.sub(PY_PATTERN, '', ''.join(txt))

single = re.compile(r"\n\n")

b = re.sub(single, '\n', b)

print(b)

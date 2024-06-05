import re
str="""

"""
p=re.compile(r'"av".{11}')
for i in p.findall(str):
	if i[-1]!='}':
		print(i)
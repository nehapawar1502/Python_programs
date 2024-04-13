import re


pattern = r"[A-Z]+yclone"

text = ''' i am  cyclone able to understand i am busy , dyclone byclone i am not aware of this

'''

matches = re.finditer(pattern,text)

for matchs in matches:
    print(matchs)
 
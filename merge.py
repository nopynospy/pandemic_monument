# In this script, I update the json from my Chrome extension.
# Because I have accumulated news headlines each day, I merge the day's new headlines.

import json

old = json.load(open("jan2020_to_27-10-21.json", encoding="utf8"))
# current = json.load(open("oct_27.json", encoding="utf8"))[0]['items']
current = []
for c in json.load(open("oct_28.json", encoding="utf8")):
    current.append(c)

def DictListUpdate( lis1, lis2):
    lis2 = lis2[0]['items']

    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return lis2

with open('jan2020_to_28-10-21.json', 'w') as f:
    json.dump(DictListUpdate(old, current), f)
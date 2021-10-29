# In this script, I update the json from my Chrome extension.
# Because I have accumulated news headlines each day, I merge the day's new headlines.

import json

old = json.load(open("jan2020_to_28-10-21.json", encoding="utf8"))
# current = json.load(open("oct_27.json", encoding="utf8"))[0]['items']
current = []
for c in json.load(open("bug_fix.json", encoding="utf8")):
    current.append(c)

def DictListUpdate( lis1, lis2):
    lis2 = lis2
    new_list = []
    for ls in lis2:
        new_list.append(ls['items'])
    new_list = list(reversed(new_list))
    new_list = [item for sublist in new_list for item in sublist]
    for aLis1 in lis1:
        if aLis1 not in new_list:
            new_list.append(aLis1)
    return new_list

with open('jan2020_to_28-10-21b.json', 'w') as f:
    json.dump(DictListUpdate(old, current), f)
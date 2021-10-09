import json

old = json.load(open("jan2020_to_7-10-21.json", encoding="utf8"))
current = json.load(open("oct_8.json", encoding="utf8"))[0]['items']

def DictListUpdate( lis1, lis2):
    lis2 = lis2
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return lis2

with open('jan2020_to_8-10-21.json', 'w') as f:
    json.dump(DictListUpdate(old, current), f)
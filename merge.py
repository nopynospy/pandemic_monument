import json

old = json.load(open("fmt_headlines_from_jan2020.json", encoding="utf8"))
current = json.load(open("oct_1.json", encoding="utf8"))

def DictListUpdate( lis1, lis2):
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return lis2

with open('merged.json', 'w') as f:
    json.dump(DictListUpdate(old, current), f)
import json

f = open('sample-data.json')

data = json.load(f)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for i in data['imdata']: 
    l1 = i["l1PhysIf"]
    at = l1["attributes"]
    print(at["dn"], "                            ", at["speed"], " ", at["mtu"])
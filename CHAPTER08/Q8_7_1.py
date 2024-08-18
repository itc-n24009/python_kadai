import json
name = {"tanaka":{"age":20,"bloodtype":"A","gender":"female"}, "satou":{"age":19, "bloodtype":"O", "gender":"female"}, "suzuki":{"age":20, "bloodtype":"AB","gender":"male"}}
with open("name.json", "w") as f1:
    json.dump(name, f1)
with open("name.json", "r") as f2:
    name2 = json.load(f2)
for x, y in name2.items():
    print(x, y)

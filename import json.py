import json
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def get_json_str(p):
        dic = {"__class__" : "point",
        "x" : p.getx(), 
        "y" : p.gety()}
        return json.dumps(dic,indent=1)
point = Point(3,4)
z = Point.get_json_str(point)
print(z) #question A

def read_json_str(s):
    ran = json.loads(s)
    exe = ran["x"]
    why = ran["y"]
    print(f"({exe},{why})")
read_json_str(z)


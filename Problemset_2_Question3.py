class Marsupial:
# the constructor
def __init__(self):
self.pouch=[]
# the required method
def put_in_pouch(self, item):
# adds item to the pouch
self.pouch.append(item)
def pouch_contents(self):
return self.pouch
# the required class
class Kangaroo(Marsupial):
# the constructor
def __init__(self, x,y):
# parents constructor
Marsupial.__init__(self)
self.x=x
self.y=y
# the required method
def jump(self, dx, dy):
# incrmetns the respective instace variables
self.x+=dx
self.x+=dy
def __str__(self):
return "I am a Kanagroo located at coordinates ("+str(self.x)+","+str(self.y)+")"
k = Kangaroo(0,0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)

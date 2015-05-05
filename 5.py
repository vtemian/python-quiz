class Wrapper:
   def __init__(self):
       self.obj = range(10)

   def __getitem__(self, idx):
       if idx > len(self.obj):
           raise IndexError()
       return self.obj[idx]

w = Wrapper()
try:
   for i in w:
       print(i)
except TypeError:
   print("not an iterator")

try:
    print(2 in w)
except TypeError:
   print("not a container")

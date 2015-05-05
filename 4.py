import shutil
from tempfile import mkdtemp


class TemporaryDirectory:
   def __init__(self):
       self.tmp = mkdtemp()

   def __enter__(self):
       return self.tmp

   def __exit__(self, *args):
       shutil.rmtree(self.tmp)
       return True


with TemporaryDirectory() as tmp:
   print(tmp)
   1 / 0

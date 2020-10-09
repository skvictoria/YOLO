from string import ascii_lowercase
from random import choice, randint, random
import os
 
def randomize_files(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        if os.path.isfile(path):
            ext = os.path.splitext(f)[1]
            newname = os.path.join(dir, ''.join([choice(ascii_lowercase) for _ in range(randint(5, 8))]))
            newpath = newname + ext
            os.rename(path, newpath)
            print("rename {} to {}".format(path, newpath))
 
randomize_files('image 폴더명')

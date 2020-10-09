from string import ascii_lowercase
from random import choice, randint, random
import os

def randomize_files(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        if os.path.isfile(path):
            ext = os.path.splitext(f)[1]
            if(ext != '.JPG'):
                continue
            ext1 = os.path.splitext(f)[0]
            print("Must be JPG: ", ext)
            for g in os.listdir(dir):
                if os.path.isfile(os.path.join(dir,g)):
                    if os.path.splitext(g)[1]=='.JPG' or os.path.splitext(g)[0]!=ext1:
                        continue
                    else:
                        ext2 = os.path.splitext(g)[1]
                        print("jpg: ", ext1, ext)
                        print("txt: ", os.path.splitext(g)[0], ext2)

                        newname = os.path.join(dir, ''.join([choice(ascii_lowercase) for _ in range(randint(5, 8))]))
                        newpath_jpg = newname + ext
                        newpath_txt = newname + ext2
                        print("newpath : ", newpath_jpg, newpath_txt)
                        print("-------------")

                        os.rename(os.path.join(dir,f), newpath_jpg)
                        os.rename(os.path.join(dir,g), newpath_txt)

                        print("rename {} to {}".format(os.path.join(dir,f), newpath_jpg))
                        print("rename {} to {}".format(os.path.join(dir,g), newpath_txt))

randomize_files('./train/')

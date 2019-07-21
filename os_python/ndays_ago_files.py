import glob
import os
import time

target = 4*24*60*60   # 4 days in seconds

for path, subdirs, files in os.walk('/etc'):
    for name in files:
        print(os.path.getctime(os.path.join(path, name)))
        if time.time()-os.path.getctime(os.path.join(path, name)) > target:
            print(name, os.path.getctime(os.path.join(path, name)))

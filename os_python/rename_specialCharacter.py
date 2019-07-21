import sys
import os
import re

regex = re.compile('[@!#$%^&*()<>?\|}{~:]')

for path, subdirs, files in os.walk('/tmp'):
    for name in files:
        if(regex.search(name) == None):
            print(os.path.join(path, name))
        else:
            print(os.path.join(path, name), '!!! ------>>>>> special character')
            reFileName = re.sub(
                '[@!#$%^&*()<>?/\|}{~:]', '', os.path.join(path, name))
            print(reFileName)

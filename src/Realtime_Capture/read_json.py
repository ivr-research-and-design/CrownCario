import json

import os
print ('\n ::::::::::: \n')
print( os.getcwd())

f = open('src/Realtime_Capture/example.json')

data = json.load(f)

print (data)
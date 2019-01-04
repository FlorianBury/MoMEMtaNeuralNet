import os

with open('retest.csv','w') as f:
   f.write('Hello') 

print (os.path.abspath('retest.csv'))
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    print (dirpath, dirnames, filenames)


print (os.getcwd())


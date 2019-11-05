import os
import shutil

print(os.getcwd())
print(shutil.copy('./pytest1.txt','./code'))
#print(shutil.move('./pytest2.txt','./code'))
print(shutil.move('./pytest3.txt','./code/pytest4.txt'))
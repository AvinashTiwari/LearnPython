import os

print(os.getcwd())
print(os.chdir("E:\\Learnpython\\1_Python\\Chap1\\Helloworld\\OsModule\\changedir"))
print(os.getcwd())
print(os.chdir("..\\"))
print(os.getcwd())
print(os.listdir("."))

myfile = open("pytest.txt")
print(myfile.read())
myfile.close()

myfile = open("pytest.txt")
myfile.readlines()
myfile.close()

myfile  = open("pytest.txt",'w')
myfile.write('hello world \n')
myfile.close()

myfile  = open("pytest.txt",'a')
myfile.write('hello world 2 \n')
myfile.close()
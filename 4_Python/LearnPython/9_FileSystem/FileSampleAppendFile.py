newfile = open("./newfile.txt","w")
newfile.write("I like pyton \n do you")
newfile.close()

newfile = open("./newfile.txt","a")
newfile.write("This String was appened")
newfile.close()

newfile = open("./newfile.txt","w+")
newfile.write("Write to read")
newfile.seek(0)
print(newfile.read())
newfile.close()


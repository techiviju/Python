f = open("file.txt")

# lines = f.readlines()  # return lst
# print(lines)


# line1 = f.readline()   # str print only one line
# print(line1," ",type(line1))

# line2 = f.readline()   # str print only one line
# print(line2," ",type(line2))

# line3 = f.readline() 
# print(line3)

# line4 = f.readline() 
# print(line4)

# line5 = f.readline() 
# print(line5)

line=f.readline()
while(line != ""):
    print(line)
    line=f.readline()

f.close()

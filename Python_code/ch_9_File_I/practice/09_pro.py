with open("this.txt") as f:
    content1=f.read()

with open("this_copy.txt") as f:
    content2=f.read()

if(content1 == content2):
    print("File's are same content !")

else:
    print("Content is not Identical")

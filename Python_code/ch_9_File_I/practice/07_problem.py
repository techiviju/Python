# 7. Write a program to find out the line number where python is present from ques 6.

with open("log.txt","r") as f:
    lines=f.readlines()

line_no=1
for line in lines:
    if("python" in line):
        print(f"Python is present in line number :-{line_no}")
        break
    line_no+=1

else:
    print("Python is Not present in the file")
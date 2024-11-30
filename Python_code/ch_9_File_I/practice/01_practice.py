# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f =open("poems.txt")

contents = f.read()
if("Twinkle" in contents):
    print("Twinkle is present in the content")
else:
    print("Not present in the Content.")

f.close()

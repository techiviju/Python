# Repeat program 4 for a list of such words to be censored.

str =["donkey","kunal","hemant","radhe"]

with open("donkey.txt","r") as f:
    content=f.read()

for words in str:
    content=content.replace(words,"*"*len(words))

with open("donkey.txt","w") as f:
    f.write(content)

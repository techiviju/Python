

def rem(l,word):
      n=[]
      for item in l:
            if not(item == word):
                  n.append(item.strip(word))
            return n

l = ["vijay","Rohan","mohan","Sohan","the_an","an"]

print(rem(l,"an"))
# pg 26

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("Enter your message :-")
if((p1.lower() in message.lower()) or (p2 in message) or (p3 in message) or (p4 in message)):
      print("This message is a SPAM")
else:
      print("This message is not a spam")
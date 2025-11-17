# A spam comment is defined as a text containing following keywords:
# "make a lot of money","buy money", "subscribe this", "Click this". 
# write a program to detect these spams.
p1="make a lot of money"
p2="buy money"
p3="subscribe this"
p4="Click this"

message=input("enter the comment:- ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is a spam comment. Stay alert")

else:
    print("this is not spam comment")



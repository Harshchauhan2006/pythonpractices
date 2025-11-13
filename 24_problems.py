#create a empty dictionary. Allow 4 friends to enter their favourite language as values and use key as their names. Assume that number are unique.
a={}
name=input("enter friends name:-")
lang=input("enter lang:-")
a.update({name:lang})

name1=input("enter friends name:-")
lang1=input("enter lang:-")
a.update({name1:lang1})

name=input("enter friends name:-")
lang=input("enter lang:-")
a.update({name:lang})

name=input("enter friends name:-")
lang=input("enter lang:-")
a.update({name:lang})


print(a)
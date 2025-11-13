#if the 2 keys is same in the dictionary input then what will be the output?
a={}
name=input("enter friends name:-")
lang=input("enter lang:-")
a.update({name:lang})

name1=input("enter friends name:-")
lang1=input("enter lang:-")
a.update({name1:lang1})
 
print(a)


#result will be the last updated lang

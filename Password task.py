password=input()
s="!#$%&'()+,-./:;<=>?@[\]^_`{|}~"
special_char=set(s)
lower=0
upper=0
special=0
digit=0
if (len(password)<6 or len(password) >16):
   print("Invalid Password")
else:
    for i in password:
    
        if (i.islower()):
            lower+=1            
  
        if (i.isupper()):
            upper+=1            
  
        if (i.isdigit()):
            digit+=1            
        if i in special_char:
            special+=1           
    if (lower>=1 and upper>=1 and special>=1 and digit>=1 ):
        print("Valid Password")
    else:
        print("Invalid Password")
import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
plen=int(input("enter password length"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print("your password is: ")
print(" ".join(random.sample(s,plen)))
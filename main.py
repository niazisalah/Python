
import os

def pgcd(a,b):
#test d'egalité
  if a==b:
    return a
#non egalité 
  else:
    while a!=b:
      if a>b:
        a=a-b
      else:
        b=b-a
    return a

def inverse(number):
  i=0
  while((number*i)%8!=1):
    i=i+1
  return i
def inverse2(number,mod):
  i = 0
  while ((number * i) % mod != 1):
    i = i + 1
  return i
#print(" result",66%26)
#number=input("inserer votre numero ici  ")
#MOD=input("inserer votre mod")
#print(inverse(int(number),int(MOD)))
from functools import reduce
#OUR start
#Convert a text to Ascci -65 in mode 26
def num(text):
  h=list(map(ord,text))
  return list(map(lambda x:x-65,h))
#Convert numbers to a text
def unum(l):
  return list(map(lambda a: chr(a + 65), l))


#inverse in mod 26
def inverse(number):
  i=0
  while((number*i)%26!=1):
    i=i+1
  return i

# encrypt chiffrement affine
def encrypt_affine(text,a,b):
  m=num(m)
  m=list(map(lambda x:x,m))
  m=list(map(lambda x:x*a+b,m))
  m=list(map(lambda x: x%26, m))
  m=unum(m)
  return reduce(lambda x,y:x+y,m)

# decrypteur de chifrement affine
def decrypt_affine(text,a,b):
  vide=''
  m=num(text)
  m=list(map(lambda a:a-b,m))
  m=list(map(lambda x:x*inverse(a),m))
  m=list(map(lambda a:a%26,m))
  m = list(map(lambda a: chr(a+65),m))

  return reduce(lambda x,y:x+y,m)
t="HWDUYTLWFUMNJ"
print(decrypt_affine(t,1,5))

#ENCRYPT PERMUTATION
def permut(text,key):
       #From Alphabetics to Numbers by using num Fucntion
  m=num(text)
  i=0
  permute=list(range(len(key)))
  #permute2=[]

  while i<len(m):

    #Make the permutation by using the Key 
    if len(m[i:])>=len(key): 
      for j in range(len(key)):
        permute[j] = m[key[j] + i - 1]
    #Replace original text with permuted one
      for j in range(len(key)):        
        m[j+i]=permute[j]
     
        #decale i
    i=i+len(key)
  
  #Covert Numbers from ACII Code To characters
  m = list(map(lambda a: chr(a + 65), m))

  return reduce(lambda x,y:x+y,m)
#decrypt permutation with key
def unpermut(text,key):
  m=num(text)
  i=0
  permute=list(range(len(key)))

  while i<len(m):
    if len(m[i:])>=len(key): 
      for j in range(len(key)):
        permute[key[j]-1]=m[j+i]

      for j in range(len(key)):
        m[j+i]=permute[j]
    i=i+len(key)
  m = list(map(lambda a: chr(a + 65), m))
  return reduce(lambda x,y:x+y,m)
#decrypt permutaion
#test
#message="TEST"
#key=[2,1]
#print(permut(message,key))
#print(unpermut(permut(message,key),key))

#encrypt vignere
def vignere(text, key):
  m = num(text)
  k = num(key)
  if len(m) <= len(k):
    fusion = list(zip(m, k[:len(m)]))
    m = unum(list(map(lambda x: x % 26, map(lambda x: x[0] + x[1], fusion))))
    return reduce(lambda x, y: x + y, m)
  else:
    key=key+key
    return vignere(text,key)
#decrypt vignere function
def dec_vignere(text, key):
  m = num(text)
  k = num(key)
  if len(m) <= len(k):
    fusion = list(zip(m, k[:len(m)]))
    m = unum(list(map(lambda x: x % 26, map(lambda x: x[0] - x[1], fusion))))
    return reduce(lambda x, y: x + y, m)
  else:
    key=key+key
    return dec_vignere(text,key)
    
#FUNCTIONS:
#inverse(number,mod) 
# vignere(message,key)
# dec_vignere(message,key)
# permut(message,key) ---> key is a list of numbre from 1 to n
#unpermut(Crypted_message,Key) ---> key is a list of numbre from 1 to n
#encrypt_affine(text,a,b) 
#decrypt_affine(text,a,b)







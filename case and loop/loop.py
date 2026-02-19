stmt="Hello!!! Data Engineer 2026"

vowels=0
cons=0
spa=0
num=0
punc=0
words=len(stmt.split())
print(words)
char_num= len(stmt)
print (char_num)
for ch in stmt.lower():
    if ch in ("aeiou"):
        vowels +=1
    elif ch.isalpha():
        cons +=1
    elif ch.isnumeric():
        num +=1
    elif ch.isspace():
        spa +=1
    else:
        punc +=1

print("Vowels: ", vowels)
print("Consonents: ", cons)
print("Numeric: ", num)
print("Spaces: ", spa)
print("Punctuations: ", punc)
print ("Total Chars:", char_num-spa)

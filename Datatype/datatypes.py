#Learning different datatypes
#String
name="Soubhagya Ramprasath"

print(name)
print(name.split())#Split function


github="https://github.com/Soubhagya-R"

print(github.split("/")[-1]) #Here separator is / and selected last element
###########Case conversion###################

print(name.upper())
print(name.capitalize())

##########Concatination#############################

str1="Welcome"
str2="Home"

print(str1+" "+str2)

#############Length#####################

print(len(name))

#############Strip(Trim)###############

text="                       Uhoooooo               "
print(text)
print(text.strip()) #removes spaces at start and end

##################Replace###############

text="I am a Consultant"
print(text.replace("Consultant","Employee"))

###############Sub string###############

print(text[0:4])
print(text[4:])
print(text[-4:])
print(text[:-4])
print(text[::2])
print(text[::-1])
######################################################


##########INT & FLOAT###############

n1=5
n2=3
print(n1+n2)

n1=22.0
n2=7.0
print(n1+n2)
print(n1-n2)
print(n2-n1)
print(abs(n2-n1))
print(n1*n2)
print(n1/n2)
print(n1%n2)

print(round((n1/n2),2)) #Rounding

#####################################################
#Regular Expression

import re
text="There is a cat sitting on the wall along with a small baby cat"
pattern="cat"
find=re.search(pattern,text)
print(find)

find=re.match(pattern,text)
print(find)

find=re.findall(pattern,text)
print(find)

text = "Contact us at support@email.com"
emails = re.findall(r"\S+@\S+", text)
print(emails)

text = "Date: 2026-02-18"
date = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print(date)


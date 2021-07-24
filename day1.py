# Developer: siddharth kumar singh
# Maintainer: siddharth singh
# startdate: 24 july 2021
# Mail: siddharthsingh2910@gmail.com
#Github: https://www.github.com/agentsid
#Dockerhub:
#######################################################################################################################################
""" #######remove this multi line comment to run below
'''
Always validate main.py with below hello world program
this will also test multi line comment

'''

print("NO ERROR ON MAIN.PY")


################################################# Below area is for testing and learning ################################################
import math
# import sys

# check if math module is impoeted or not
print(math.gcd(3,6))

######################################### data types#####################

a=5 # this is integer data type
b= "siddharth" # this is string data type
c=1.0 # this is float data type


# testing above
print(b)
print(a+c)
print(c+1.0)
#DMAS test################################## operator#####################
print("testing Add SUB MULT DIV")
print(a+c)
print(a-c)
print(a*c)
print(a/c)

#############try below operator
# ** = exponential
# // = floor divison
# % = modulo operator

# validate data type
print(type(a))
print(type(b))
print(type(c))

# try assing a differnt value , it will pick new value not old one
a="this is new value of a previously 5"
b="55"
print(type(b))
print(type(a))
print(a)
b=int(b)
print(type(b))
print(b)

################### type casting ##############
d="55"
print(type(d))
e=int(d)
#print(e+d) throw error because u can add int value with string so convert to int then add check below
d=int(d)
print(e+d)
""" #######remove this multi line comment to run above
"""
################################################# variable rules##################
#### 1. allowed value ( seminmeric, strint, )
     # 2. always start with under score  or 



######################################### SLICING ################################

name="abcdefghijklmnopqrstuvwxyz"
print(name[0]) # print 1st character
#print(name[name2]) # print last character
name1=(len(name))
name2=name1-1
print(name[0:26]) # print all the character
print(name[2:12]) # this will print from 2nd character till lastvalue -1 character
print(name[-1]) # print last value
print(name[-1:]) # also print last value
print(name[:-1]) # exclude last lave and print all the character

####################### removing space with strip function  and finding length of string#############

name3= "              this is siddharth learning strip function                                   "
print(name3)
name4=(name3.strip())
print(name4)
print(len(name3))
print(len(name4))


########################### converting to upper and lower case #############################

name5="siddharth"
name6="SIDDHARTH"

print(name5.upper())
print(name6.lower())

###################### replace function ############
name7="GOOGLE"
name7=name7.lower()
print(name7.replace("o","w"))
print(name7.replace("g","d"))
name8="      siddharth,ushasi,mummy,papa          "
# name9=name8.replace("," , " ")
# name10=name8.replace("," , "")
# print(name9)
# name11=(name10.strip())
# name12=(name11.replace(" ", "\n"))
# print(name12)
name9=name8.strip()
name10=name9.replace(",","\n")
print(name10)
print(type(name10))


############################## template creating ######################################

t1="siddharth"
t2="ushasi"
temp="between {0} and {1} who is good".format(t1,t2)
temp1="between {1} and {0} who is good".format(t1,t2)
temp3="between {1} and {4} who is good".format(t1,t2, "fuddu",2, 1.5 )
temp4= f"between {t1} and {t2} who is good"  ##################################  f string #################
print(temp)
print(temp1)
print(temp3)
print(temp4)
"""
"""
############################### list manupilatio #########################3
l1=[1,2,3,4,5]
l2=["one","two","three","four","five"]

print(type(l2))

l2[2]= "six"
print(l2)

###################### append function #####################
l2.append("severn")
l1.append(6)
print(l2)
print(l1)


################################## insert function ########################

l1.insert(-1,100)
l1.insert(-2,300)
l1.insert(0,400)
l1.insert(9,1000)
l1[1]=200
print(l1)

############################## remove pop and del function ######################

l1.remove(1000)
print(l1)
l2.pop() ### simpley remove last value from list)
del l1[3]
print(l2)
print(l1)
#################################python collections#################################
####################### clear list function ##################### 

l3=[1,2,3,4,5,6,7]
#print(l3.replace(","," ")) ########### not working because of list
print(l3)
l3.clear()
print(l3)

##################################### tuple ####################
# same like list but cant changable
l4=(1,2,3,4,5)
l5=("one", "two", "three")

print(type(l4))
print(type(l5))
#l4.append(6)  ###### this is not allowed#############
print(l4)

################################ set #######################################

s1={1,2,3,3,3,3,3,3,3,3,3,2,8,2,2,2,5,2,2,2,9}
s2={"kanu","kanu","kanu","sid","sid","sid","kanu"}

print(type(s1))
print(type(s2))
print(s1)
print(s2)
#adding method
s1.add(10)
print(s1)
s1.update([3,33,3,3,4,3,3,3,3,3,3,3,35,3535,3553,5355,35355,35])
print(s1)
s1.remove(35355) # this is remove this value from set
s1.discard(152525)  ### idealy it throw error with remove but not with discard 
print(s1)
## use .clear , .pop , del, intersection, union
"""
"""
############################## Dictionary #########################

from os import times


siddict={
     "name": "siddharth",
     "age": 29,
     "sex": "male",
     "mobile": 9663551146,
     "city": "Bangalore",
     "DOB": "29/10/1999"
}
print(siddict)
print(siddict["DOB"])
# date is not correct
siddict["DOB"]= "29/10/1992"
print(siddict)
# remove dictonery element use .del and .clear and for update use .update
siddict.pop("sex")
siddict.update({"sex": "male"})
print(siddict)
siddict.update({"name": "ushasi"})
siddict["name"] ="ushasi"
siddict.update({"name": "siddharth"})
print(siddict)
#################################
"""

################################# taking input from user and using small if and elif statement ###########
# writing a simple program for voting eligibility

age=input("please enter the age to check voting eligibility\n") #### this always take value as string
print(type(age))
age=int(age)
print(type(age))

if(age==18):
     print("1st timer ")

elif(age<18):
     print("not allowed")
else:
     print("welcome sir ")

#####################################################################################################################

####################################################### for and while loops


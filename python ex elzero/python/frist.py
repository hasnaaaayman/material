#print("hello\bworld")
#print(type([1,2,3]))
#print("\x4f")
# a = "frist\
# second\
# third"

# b="a\
#     b\
#     c"
# print(a +"\n"+b)

# name = ''' hasnaa
# ayman \\ "test" \
# mariam
# '''
# print(name)

# msg = "hasnaa"
# lang ="ayman"
# print(msg+" "+lang)

# msg = "hasnaa"
# lang ="ayman"
# print(msg+"\t"+lang)


           #33string
from functools import reduce


myString="I love you mariam php  3g php"
#print(myString[-1])        #index
#print(myString[0:5:2])     #slicing
#print(len(myString))
# print(myString.strip())
# print(myString.rstrip())
# print(myString.lstrip())
# myString="###I love you mariam###"
# print(myString.strip("#"))
#print(myString.title())
# print(myString.capitalize())
# print(myString.upper())
# print(myString.lower())
print(myString.split(" "))
# print(myString.center(30,"#"))
# print(myString.count("php"))
# print(myString.count("php",10,))
# print(myString.swapcase())
# print(myString.startswith("I",0,2))
# print(myString.endswith("p"))
# print(myString.index("p"))
# print(myString.find("p",1,3))
# print(myString.rjust(30,"%"))
# print(myString.ljust(40,"&"))
#print(myString.isalpha())
# print(myString.isalnum())
# print(myString.replace("php","java"))

# list = ["mariam","ayman","akl"]
# print(" ".join(list))
 
# g = "hello\tworld\tmariam"
# print(g.expandtabs(2))

# Line ='''aymam
# hasnaa 
# dgj
#  '''
# print(Line.splitlines())
# myString="I-love-you-mariam-3g"
# print(myString.split("-"))
# print(myString.split("-",2))
# print(myString.rsplit("-",2))
# a,b,c ="1","11","111"
# print(a.zfill(3),b.zfill(2),c.zfill(3))

                           ###formatting####
# name = "hasnaa" 
# age = 24
# range = 20.2
# print("my name is%s andmyage%d andmyrang%f "%(name,age,range))
# print("my name is%.2s andmyage%d andmyrang%.5f "%(name,age,range))
# print("my name is{}".format(name))
# print("my age is{:d}".format(age))
# print("my rang{:.2f}".format(range))
# print(f"my name is{name} andmyage{age} andmyrang{range}")


# money =2531552
# print("my money in bank{:_d}".format(money))

# a,b,c ="one","two","three"
# print("hello{2}{1}{0}".format(a,b,c))
# a,b,c =1,2,3
# print("hello{2:d}{1:.2f}{0:f}".format(a,b,c))

#####333333333333333333333333333333333333333     list    ############################################
#  mylist =["hasnaa","mariam","zena",[1,2]]
# mylist1 =["A","B"]
# mylist3 =[2,5,8,3,1,4]
# mylist[2]="ahmed"
# print(mylist)
# print(mylist[0:2])
# mylist.append("mohamed")
# print(mylist)
# mylist1 = ["a","b"]
# mylist.append(mylist1)
# print(mylist)
# mylist.extend(mylist1)
# print(mylist)
# mylist.remove("hasnaa")
# print(mylist)
# mylist3.sort()
# print(mylist3)
# mylist3.sort(reverse=True)
# print(mylist3)
# mylist3.reverse()
# print(mylist3)
# mylist.clear()
# print(mylist)
# b=mylist1.copy()
# print(b)
# print(mylist.index("hasnaa"))
# mylist.insert(0,"mohamed")
# print(mylist)

##########################################   tuple#################################
# mytuple1 =(1,2,3,4,"mariam","hasnaa")
# mytuple2 =(5,6,7)
# # print(mytuple1[1])
# # print(mytuple1+mytuple2)
# # print(mytuple2.count(5))
# a=("A","B","c")
# x,z,y = a
# print(a)
#######################################   set #######################################
# myset={1,2,3,4}
# myset0 ={1,2,3}
# myset1={1,2,"osama","ahmed"}
# print(myset.difference(myset1))
# print(myset)
# myset.difference_update(myset1)
# print(myset)
# print(myset.intersection(myset1))
# print(myset)
# myset.intersection_update(myset1)
# print(myset)
# print(myset.union(myset1))
# myset.add(5)
# print(myset)
# myset.remove(7) ######### erro
# myset.discard(7)
# print(myset)
# myset.pop()
# print(myset)
# myset.update(myset1)
# print(myset)
# print(myset.issuperset(myset0))
# print(myset.issubset(myset0))
# print(myset.isdisjoint(myset0))
############################################dictionary#################################
# user = {
#     "name":"hasnaa",
#     "age":22,
#     "country":"egypt",
#     "skills":["css","js","html"]
# }
# print(user['skills'])
# print(user.get("country"))
# print(user.keys())
# print(user.values())

# languges={
#     "one":{"name":"html",
#            "progress":"80%"},
#     "two":{"name":"css",
#            "progress":"20%"},
#     "three":{"name":"js",
#              "progress":"50%"}     
# }
# print(languges['one']['name'])
# print(len(languges["three"]))

# one={"name":"html",
#     "progress":"80%"}
# two={"name":"css",
#     "progress":"20%"}
# three={"name":"js",
#     "progress":"50%"}    
# alldick={
#     "one":one,
#     "two":two,
#     "three":three
# }
# print(alldick["one"])
# alldick.clear()
# print(alldick)
# alldick.update({"four":"country"})
# print(alldick)
# b=alldick.copy()
# print(b)
# print(one.setdefault("country","css"))
# print(one)
# user = {
#     "name":"ahmed"
# }
# print(user.setdefault("age","36"))
# print(user)
# print(one.popitem( ))
# allitems=one.items()
# one.update({"country":"egypt"})
# one["conty"]="egypt"
# print(one)
# a =("m","e","g")
# b="x"
# print(dict.fromkeys(a,b))
# name=" "
# print(name.isspace())
#####################################boolean######################
# print(bool(True))
# name="osama"
# age=36
# country="egypt"
# print(name=="osama" or age<36 )
# print(not age>20)
###############################type conversion########################
# a = 10
# print(type(str(10)))
# print(type(a))
# name = "mohamed"
# print(list(name))
# print(tuple(name))
# print(set(name))
########################dict########################
# mylist = [("a",1),("b",2),("c",3)]
# mytuple =(("a",1),("b",2),("c",3))
# print(dict(mylist))
# print(dict(mytuple))
###################################### user input###################
# fName = input("what\'s your frist name").strip().capitalize()
# mName = input("what\'s your middle name").strip().capitalize()
# lName = input("what\'s your last name").strip().capitalize()
# input(f"my name is{fName} andmyage{mName:.1s} andmyrang{lName}")

# theName =input("what\'s your name").strip().capitalize()
# theEmail =input("what\'s your email").strip().capitalize()
# theUserName =theEmail[:theEmail.index("@")]
# theWebSite = theEmail[theEmail.index("@")+1:]
# print(f"Hello{theName} your email is{theEmail}")
# print(f"your username is{theUserName}\n your website is{theWebSite}")
#################################### age ############################
# age = int(input("what\'s your age ?")) 
# months = age*24
# weeks = months*12
# days = age *365
# hours = days*24
# minutes = hours*60
# second = minutes*60
# print(f"your live for :")
# print(f"{months}month")
# print(f"{weeks}weeks")
# print(f"{days}days")
# print(f"{hours}hours")
# print(f"{second:,}second")
# print(f"{minutes:,}minutes"
#############################if#########################################
# uName = "osama"
# uAge = 36
# uCountry ="egypt"
# cName ='"python'
# price=100
# if uCountry =="egypt":
#  print(f"Hello{uName} because you are from{uCountry}") 
#  print(f"the courses{cName}price is :{price-80}")
# else:
#  print(f"Hello{uName} because you are from{uCountry}") 
#  print(f"the courses{cName}price is :{price-20}")
 ########################## Nested if #############################
# uName = "osama"
# uAge = 36
# uCountry ="egypt"
# cName ='"python'
# price=100
# student = "yes"
# if uCountry =="egypt":
#  if student=="yes":
#   print(f"Hello{uName} because you are from{uCountry}") 
#   print(f"the courses{cName}price is :{price-80}")
# else:
#  print(f"Hello{uName} because you are from{uCountry}") 
#  print(f"the courses{cName}price is :{price-20}")
##################################### ternary condition operator ########################
# movieRate = 18
# age = 18
# print("movie is not good 4u"if age<movieRate else "movie is happy")
###############################
# print("#"*80)
# print("you can write the frist letter or full name of the time unite".center(80,"#"))
# age = int(input("what\'s your age ?")) 

# unite = input("please choose time :months,weeks,Day").lower().strip()

# months = age*24
# weeks = months*12
# days = age *365

# if unite=="months" or "m":
#  print(f" you choose month : {months:,}")
# elif unite == "weeks" or "w":
#  price(f"you choose week :{weeks:,}")
# elif unite== "days" or "d":
#  price(f"you choose day :{days}")
################################## membership operator ####################
# name = "osama"
# print("s" in name)
# mylist = ["osama","ahmed","mohamed"]
# print("mohamed"in mylist)
# print("mohamed" not in mylist)

# myCountryone=["egypt","ksa","kwait"]
# myCountryonediscount = 80
# myCountrytwo =["usa","italy"]
# myCountrytwodiscount=20
# myCountry="italy"
# if myCountry in myCountryone :
#  print(f"hello you have discount :{myCountryonediscount}")
# elif myCountry in myCountrytwo :
#  print(f"hello you have discount : {myCountrytwodiscount}")
#################################### partical membership control ###########################
# admins = ["Ahmed","Mohamed","Mayad","Mmar","Mariam","Hasnaa"]
# name = input("please type your name").strip().capitalize()
# if name in admins :
#  print(f"hello {name}welcome back") 
#  option = input("Delet or Update your name").strip().capitalize()
#  if option == "Update" or option == "u":
#   theNewName = input("type thenewName").strip().capitalize()
#   admins[admins.index( name)]=theNewName
#   print("name update")
#   print(admins)
#  elif option == "delet" or option == "d" :
#   admins.remove(name)
#   print("name delet")
#   print(admins)
#  else :
#   print("wrong option choose")
# else :
#  status = input("Not admin , add you y or no ?").strip().capitalize()
#  if status == "yes" or status == "y" :
#   print("you have been added")
#   admins.append(name)
#   print(admins)
#  else :
#   print("you are not added")
  ############################## loop #############################
# a = 0
# while a <15 :
#     print(a)
#     a+=1 

# mylist = ["os","ah","ma","mo","ha","ho","wa","om","ze","na","ay"]
# a = 0
# while a < len(mylist) :
#     print(f"#{str(a+1).zfill(2)}{mylist[a]}")
#     a+=1
# else :
#     print("all frinds print to screen")
# myLIst = []
# maximumWeb = 5
# while maximumWeb > 0 :
#     web = input("Website name without http://")
#     myLIst.append(f"http//{web.strip().lower()}")
#     maximumWeb-=1
#     print(f"website add,{maximumWeb}plece left")
#     print(myLIst)
# else :
#     print("bookmarker is full")

# if len(myLIst) > 0 :
#  myLIst.sort()
#  index = 0
#  while index < len(myLIst) :
#     print(myLIst[index])
#     index+=1
#############################
# tries = 5
# mainPassword = "osama"
# inputpass = input("Writ your password")
# while inputpass != mainPassword :
#     tries-=1
#     print(f"Wrong pass{"last" if tries == 0 else tries}")
#     inputpass = input("Writ your password")
#     if tries == 0 :
#        print("all tries is finish")
#     break
# else   :
#     print("loop is done ")
##################### nested loop#################
# name = "ahmed"
# for letter in name :
#     print(letter)

# frinds = ["osama","mohamed","ahmed","hasnaa"]
# for name in frinds :
#     print(f"{name} ")

# myRang = range(1,100)
# for number in myRang :
#     print(number)

# mySkills = {
#     "Html" : "90%",
#     "css"  : "80%",
#     "js"   : "70%",
#     "python": "60%",
# }
# for skill in mySkills :
#     print(skill)
#     print(f"my progress in lang {skill} Is :{mySkills[skill]}")

# people = ["ahmed","osama","mohamed","hasnaa"]
# skills = ["html","css","js","python"]
# for name in people :
#     print(f"{name}skills is :")
#     for skill in skills :
#      print(f"{skill}")
# people = {
#     "osama" :{
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     },
#     "ahmed" :{
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     },
#     "mariam" :{
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     },

# }
# for name in people :
#     print(f"skills and prodress for {name} is : ")
#     for skill in people[name] :
#         print(f"{skill} => {people[name][skill]}")
######################3 berak countine pass#################
#myNumber = [1,2,3,4,5,6,7,8,9,10]
# for number in myNumber :
#     if number == 3 : 
#       break
#     print(number)
# for number in myNumber :
#  print(number)
#  if number == 3 : 
#       break

# for number in myNumber :
#     if number == 3 : 
#       continue
#     print(number)

# for number in myNumber :
#     if number == 3 : 
#      pass
#     print(number)

# mySkills = {
#     "Html" : "90%",
#     "css"  : "80%",
#     "js"   : "70%",
#     "python": "60%",
# }
# for key , value in mySkills.items() :
#     print(f"{key} => {value}")


# people = {
#     "osama" :{
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     },
#     "ahmed" :{
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     },
#     "mariam" :{
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     },

# } 
# for key, value in people.items() :
#     print(f"{key} is :")
#     for keymain, valuemain in value.items():
#         print(f"{keymain}=>{valuemain}")

###############################3 function #####################################
# def function_name():
#  return "hello python"
# dataformfunction= function_name()
# print(dataformfunction)


# def addition(n1,n2):
#  if type(n1) != int or type(n2) != int :
#   print("onlt integer allowed") 
#  else :
#   print(n1+n2)
# addition(2,3)

# def full_name(frist,middle,last):
#  print (f"hello{frist.strip().capitalize()}{middle:.1s}{last}")
# print(full_name("hasnaa","Ayman","Akle"))

# def say_Hello(*peoples):
#     for name in peoples:
#      print(f"hello{name}")
# say_Hello("Ahmed","Mohamed","Ayman","Ali") 

# def show_Details(name,*skills):
#     print(f"hello {name} is : ")
#     for skill in skills :
#         print(f"{skill}")
# show_Details("hasnaa","html","css","js")


# def say_Hello(name,age,country = "egypt"):
#   return(f"hello {name} your age is {age} your country is :{country}")
# print(say_Hello("hasnaa",24))

# def show_skills(**skills):
#     for skill,value in skills.items() :
#         print(f"{skill}=>{value}")
# show_skills(html="80%",css="70%",js="60%")

#ام ف حاله موجود dicitionary 
# myskills ={
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     }
# def show_skills(**skills):
#     for skill,value in skills.items() :
#         print(f"{skill}=>{value}")
# show_skills(**myskills)


# myTuple =("php","mysql")
# myskills ={
#         "html":"90%",
#         "css" : "80%",
#         "js"  : "70%",
#         "python" : "60%"
#     }

# def show_skills(name,*skills,**skillprogress):
#     print(f"hello{name}\n skills without progress is :")
#     for skill in skills:
#         print(f"-{skill}")
#     print("skills with progress")
#     for skill_key,skill_value in skillprogress.items() :
#          print(f"{skill_key}=>{skill_value}") 
# show_skills("hasnaa",*myTuple,**myskills)

# def clear_word(word):
#  if(len(word)==1):
#   return(word)
#  if(word[0]==word[1]):
#   return clear_word(word[1:])
#  return word[0]+clear_word(word[1:])


# print(clear_word("wwwoooorrrrldd"))

################################file
# myFile = open("E:\odoo_roadmap\python ex ","r")
# print(myFile)
# print(myFile.mode)
# print(myFile.name)
# print(myFile.read(3))
# print(myFile.readline(3))
# print(myFile.readlines(2))
# for line in myFile :
#     print(line)
#     if line.startswith("07"):
#         break
#     myFile.close

# myFile = open("E:\odoo_roadmap\python ex ","w")
# myFile.write("hasna")
# myFile.write("second line")
# myFile.write("mariam"*1000)
# myList =["hasnaa\n","mariam\n","zena\n"]
# myFile=open("E:\odoo_roadmap\python ex ","w")
# myFile.write(myFile)
# myFile = open("E:\odoo_roadmap\python ex ","a")
# myFile.write("hasna\n")
# myFile.write("second line\n")

############################## Built in function ##############################
###################all
# x= [1,1,5,4,45]
# if all(x):
#     print("tes")
# else :
#     print("no")
# #################### any
# if any(x):
#     print("true")
# else:
#     print("false")
#    ##### ##################### bin
# print(bin(100))
# ########################## id
# a=1
# b=2
# print(id(a))
# print(id(b))
# ############################### sum
# mylist=[2,5,6,7,]
# print(sum(mylist))
# print(sum(mylist,2))
# ################################# round
# print(round(100.499))
# print(round(100.501))
# print(round(150.1999987,1))
# ##########################  rang 
# print(list(range(0,10)))
# print(list(range(10)))
# print(list(range(0)))
# ########################### print 
# print("how / old / are / you")
# print("how","old","are","you", sep="/")
# ########################## end
# print("first line",end=" ")
# print("second line")
# print("thrid line")
# ######################### abs
# print(abs(100))
# print(abs(-100))
# ############################## pow
# print(pow(2,5))
# print(pow(2,5,10))
# ############################## min
# mylist=[2,5,9,10,5,3,11,4]
# print(min(mylist))
# ############################# max
# print(max(mylist))
# ################################ slice
# print(mylist[1:3])
# print(mylist[slice(2,5)])
# ############################ map
# # def formatText(text):
# #     return f"-{text}"

# # mytext =["osama","Ahmed","mohamed"]
# # myformateddata = map(formatText,mytext)
# # for name in myformateddata :
# #     print(name)
# # for name in map(formatText,mytext) :
# #     print(name) 
# ################### lambda
# # mytext =["osama","Ahmed","mohamed"]
# # for name in list(map(lambda text : f"-{text}", mytext ))  :
# #     print(name)
# ########################### filter
# def checkNum(num):
#   return num > 10 
# myNum = [1,2,50,0,12,81]
# # for number in filter(checkNum,myNum):
# #   print(number)
# for number in filter(lambda num : num>10,myNum):
#   print(number)
##########################reduce##########################
# def sumAll(num1,num2):
#   return num1+num2
# myNum =[1,21,4,2]
 
# # result = reduce(sumAll,myNum)
# # print(result)
# #########################lambda##################3
# result = reduce(lambda num1,num2:num1+num2,myNum)
# print(result)
########################## enumerate #################
# myNum =[1,2,3,4,5,6]
# mynumcounter=enumerate(myNum,20)
# for counter , number in mynumcounter:
#     print(f"{number} -> {counter}")
################################# help#######################
# print(help(print))
################################reversed################33
# myStr = "hasnaa"
# print(list(reversed(myStr)))
# for n in  reversed(myStr) :
#   print(n)
####################################3module###################3
# import random
# print(f"{random.random()}")
# from random import randint , randrange
# print(f"{randint(100,200)}")
# print(f"{randrange(100,200)}")
# import sys 
# # print(sys.path)
# sys.path.append()#احط بقا المسار الي عوزاه
# import hasnaa
# print(dir(hasnaa))
# import hasnaa as ss
# ss.sayHowold("ahmed")
# from hasnaa import sayHowold
# sayHowold("ahmed")
# import termcolor
# import pyfiglet
# print(pyfiglet.figlet_format("hasnaa"))
# # print(termcolor.colored("hasnaa",color="yellow"))
# print(termcolor.colored(pyfiglet.figlet_format("hasnaa"),color="yellow"))
############################# data and time############################
# import datetime
# print(dir(datetime.datetime))
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.min)
# print(datetime.datetime.max)

# print(datetime.datetime.now().time())
# print(datetime.datetime.now().time().hour)
# print(datetime.datetime.now().time().minute)
# print(datetime.datetime.now().time().second)
# print(datetime.datetime(2000,9,25,10,55,50))
# myBriday = datetime.datetime(2000,9,25)
# datanow= datetime.datetime.now()
# print(f"your age{(datanow-myBriday).days}")
#################################decortor#####################
# def mydecorator(function):
#   def nestedfunc():
#    print("frist")
#    function()
#    print("last")
#   return nestedfunc
# @mydecorator 
# def hello():
#   print("my name")
# hello()
#####################بدل الي فوق ف حاله اعملها call#################
# afterDecoration = mydecorator(hello)
# afterDecoration()

#ف حاله الفانكشن تاخد اتنين parameter
#وتاخد اكتر من dec
# def mydecorator(function):
#   def nestedfunc(num1,num2):
#    if num1>0 or num2>0:
#     print("frist")
#    function(num1,num2)
#    print("last")
#   return nestedfunc
 
# def dec (function):
#   def nestedfunc(nu1,nu2):
#    print("frist")
#    function(nu1,nu2)
#    print("last")
#   return nestedfunc

# @mydecorator 
# @dec
# def sum(n1,n2):
#   print(n1+n2)
# sum(10,-20)
#############################
# def dec (function):
#   def nestedfunc(*numbers):
#    for n in numbers:
#      if n<0:
#       print("frist")
#    function(*numbers)
#    print("last")
#   return nestedfunc

# @dec
# def sum(n1,n2,n3,n4):
#   print(n1+n2+n3+n4)
# sum(10, 20,2,4)

#################################### speedTest #############################
# from time import time
# def speedTest(funct):
#   def wrapper():
#     start = time()
#     funct()
#     end = time()
#     print(f"function runing time{end-start}")
#   return wrapper

# @speedTest
# def bigloop():
#   for number in range(1,20000):
#    print(number)

# bigloop()
############################################### zip #######################
# list1 = [1,2,3,4]
# list2 = ["A","B","C"]
# tuple = ("Man","Woman","Girle","Boy")
# dic = {"name":"osama","age":36,"country":"egypt"}
# for item1,item2,item3,item4 in zip(list1,list2,tuple,dic):
#     print(f"list1 = >{item1}")
#     print(f"list2 = >{item2}")
#     print(f"tuple = >{item3}")
#     print(f"tuple = >{item4}, value=>{dic[item4]}")
######################################## imagr pillow ########################
# from PIL import Image
# myImage = Image.open("E:\odoo_roadmap\python ex")
# myImage.show()
####################### document ########################
# def hellosay(name):
#     '''this is function to say hello from elzero'''
#     print(f"hello{name}")
# hellosay("ahmed")
# print(hellosay.__doc__)
# help(hellosay)
  
############################## pyline ######################
# def sayHello(name):
#   msg = "hello"
#   return f"{msg} {name}"
# print(sayHello("mohamed"))
############################# Expection ############################
# x= 10
# if x > 0 :
#     raise Exception(f"the number {x} is less than zero")
# else :
#     print(f"{x} is good")
# print("mesage")
# myString = "osama"
# if type(myString) != int:
#     raise ValueError("not int")
# print("m")

# try:
#     number = int(input("write your age : "))
# except:
#     print("this is not int")
# else:
#     print("this is int")
# finally :
#     print("successed")


# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Divise error")
# except NameError :
#     print("name error")
# except:
#     print("error")

##################################### exception ex ######################
# the_File = None
# the_tries = 5
# while the_tries > 0 :
#     try:
#      print("Enter the file name")
#      print(f"{the_tries}Tries left")
#      file_name_and_path = input("File name : ").strip()
#      the_File = open(file_name_and_path,"r")
#      print(the_File.read())
#      break
#     except FileNotFoundError:
#         print("the file not found")
#         the_tries -= 1
#     except:
#         print("Error happen")
#     finally :
#         if the_File is not None:
#          the_File.close()
#          print("file closed")
# else :
#     print("All tries is done")
####################################### regular expression #####################
#######################################searh$###################################
# import re
# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)","Hasnaaayman36@gmail.com") 
# if is_email :
#     print("this is a valid email")
# else :
#     print("this is valid")
########################################findAll####################################
# import re
# email_input =input("please write your email :")
# the_search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)",email_input)
# email_list = []
# if the_search != []:
#   email_list.append(email_input)
#   print("email add")
# else :
#     print("Invalid email")
# for email in email_list :
#     print(email)
################################ split #######################################
# import re
# my_str = "I LOve You Python"
# search = re.split(r"\s",my_str)
# print(search)

# import re
# my_str = "I-Love_A_You-Python"
# search = re.split(r"-|_",my_str,1)
# print(search)
# for counter,word in enumerate(search,1):
#     if len(word)==1 :
#         continue
#     print(f"word number : {counter} = > {word}")
######################################### sub############################
# import re
# print(re.sub(r"\s","_","hasn aa a",1))
#################################### group #################################
# import re
# myweb = "hasannayamn36@gmail.com"
# search = re.search("[A-z0-9\.]+@[A-z0-9]+\.(com|net)",myweb)
# print(search.group())
# print(search.groups())
#################################oop###################################
# class member:
#  not_allowed_name =["mariam","menna","mostafa"]
#  users_number = 0
#  @classmethod
#  def show_users_count(cls):
#     print(f"we have{cls.users_number}users in our system")
#  @staticmethod 
#  def say_hello():
#     print("hello from ststic methods") 
#  def __init__(self,frist_name,middle_name,last_name,gender):
#   self.f_name=frist_name
#   self.m_name=middle_name
#   self.l_name=last_name
#   self.gender = gender
#   member.users_number+=1
#  def full_name(self):
#     if self.f_name in member.not_allowed_name:
#        raise ValueError("name not allowed")
#     else:
#        return(f"{self.f_name} {self.m_name} {self.l_name}")

#  def name_with_title(self):
#     if self.gender == "male":
#      return(f"hello mr {self.f_name}")
#     elif self.gender == "female" :
#         return(f"hello miss {self.f_name}")

#  def get_all_info(self):
#     return(f"{self.name_with_title()} your full_name is {self.full_name()}")
#  def delet_user(self):
#     member.users_number-=1
#     return f"users{self.f_name}delet"
#  pass
# print(member.users_number)
# member_one = member("mohamed","ahmed","ali","male")
# member_two = member("ali","hamed","hassan","male")
# member_three = member("mona","hamed","hassan","female")
# member_four = member("mariam","menna","mostafa","male")
# print(member.users_number)
# print(member_one.delet_user())
# print(member.users_number)
# member.show_users_count()
# member.say_hello()
# print(member_one.f_name,member_one.m_name,member_one.l_name)
# print(member_two.f_name,member_two.m_name,member_two.l_name)
# print(member_three.f_name,member_three.m_name,member_three.l_name)
# print(member_one.full_name())
# print(member_one.name_with_title())
# print(member_one.get_all_info())

# myString = "osama"
# print(type(myString))
# print(myString.__class__)
# print(str.upper(myString))
############################### merag########################3

# class skill():
#     def __init__(self):
#      self.skills =["html","css","js"]

#     def __str__(self):
#        return(f"this is my skills:{self.skills}")

#     def _len_(self):
#      return len(self.skills)
#     pass

# profile = skill()
# print(profile)
# # print(len(profile))
# profile.skills.append("php")
# print(profile.skills )
# print(len(profile))

##############################inheritance############################
# class food():
#   def __init__(self,name,price):
#     self.name=name
#     self.price=price
#     print(f"{self.name}food is created from main class{self.price}")
#   def eat(self):
#     print("Eat method from base class")
#     pass

# class apple(food):
#     def __init__(self,name,price,amount):
#        super().__init__(name,price)
#        self.amount=amount
#        print(f"{self.name}appleis created from deriver class{self.price} the amount{self.amount}")
#     def catch(self):
#         print("method deriver")

# food_one=food("pizza",10)
# food_two =apple("pizza",50,2000)
# # food_two.eat()
# food_two.catch()
########################### multiple inheritance###################3
# class Base_one():
#     def __init__(self):
#         print("Base one")
#         pass

# class Base_two():
#   def _init_(self):
#     print("Base two")
#     pass
# class derived(Base_one,Base_two):
    
#        pass
# my_var = derived()
# print(my_var)
################################### polymorphism ######################
# class A():
#     def do_someTink(self):
#         print("class A")
#         raise NotImplemented("dreibver")
#     pass

# class B(A):
#     def do_someTink(self):
#         print("class A")
#         pass
# class c(A):
#     def do_someTink(self):
#         print("class A")
# my_instance=c()
# my_instance.do_someTink( )
###############################encapsulation3##################
#################################3prodected##########
# class member():
#     def __init__(self,name):
#         self._name=name
#         pass
# one =member("Ahmed")
# print(one._name)
####################### privated #####################################
# class member():
#     def __init__(self,name):
#         self.__name=name

#         pass
# one =member("Ahmed")
# print(one._member.__name)
################################### Getting&Setting ##################
# class member:
#  def __init__(self,name):
#     self.__name = name

#  def say_hello(self):
#     return f"hello{self.__name}"
#  def get_name(self):
#     return self.__name
#  def set_name(self,New_name):
#     self.__name = New_name
# pass

# one = member("Ahmed")
# print(one.get_name())
# one.set_name("mohamed")
# print(one.get_name())
############################# Database #####################################
#import SQlite module
# import sqlite3
# #create database and connect
# db=sqlite3.connect("app.db")
# #create the table and fields
# db.execute("CREATE TABLE if not exists skills(name text,progress integer,user_id integer)")
################################## Insert Data into Database ###########################
# import sqlite3
# db = sqlite3.connect("app2.db")
# cr = db.cursor()
# cr.execute("CREATE TABLE if not exists users(user_id integer,name text)")
# cr.execute("CREATE TABLE if not exists skills(name text,progress integer,user_id integer)")

# cr.execute("insert into users(user_id,name) values(1,'Ahmed')")
# cr.execute("insert into users(user_id,name) values(2,'mohamed')")
# cr.execute("insert into users(user_id,name) values(3,'mohmoud')")
# db.commit()

##################################### insert list Ex #######################
# import sqlite3
# db = sqlite3.connect("app2.db")
# cr = db.cursor()
# cr.execute("CREATE TABLE if not exists users(user_id integer,name text)")

# my_list = ["Ahmed","mohamed","mohamoud","menna","mariam","hasnaa","Alaa","hassan"]
# for key, user in enumerate(my_list):
#   cr.execute(f"insert into users(user_id,name) values({key+1},'{user}')")
# db.commit()
######################### retrive & fetch $####################
# import sqlite3
# db = sqlite3.connect("app1.db")
# cr = db.cursor()
# cr.execute("CREATE TABLE if not exists users(user_id integer,name text)")
# cr.execute("insert into users(user_id,name) values(1,'Ahmed')")
# cr.execute("insert into users(user_id,name) values(2,'mohamed')")
# cr.execute("insert into users(user_id,name) values(3,'omar')")
# # cr.execute("select name from users")
# # print(cr.fetchone())

# # cr.execute("select user_id,name from users")
# # print(cr.fetchall())

# # cr.execute("select*from users")
# # print(cr.fetchall())
# cr.execute("select *from users")
# print(cr.fetchmany(2))
# db.commit()
################################# ex ############################
# import sqlite3
# def get_all_data():
#  try:
#   db =sqlite3.connect("app.db")
#   print("connected to Database successfully")
#   cr = db.cursor() 
#   cr.execute("select * from users")
#   result = cr.fetchall()
#   # هعملها ك tuple
#   print(result[0])
#   # print number of row
#   print(f"Database has {len(result)}rows")
#   for row in result:
#     print(f"user_id => {row[0]}" ,end=" ")
#     print(f"user_id => {row[1]}" )

#  except sqlite3.Error as er:

#   print(f"error reading data {er}")
#  finally :
#   if (db):
#     db.close()
#   print("connection to database is closed")

# get_all_data()
############################# update and delete ##################
import sqlite3
db = sqlite3.connect("app5.db")
cr = db.cursor()
# cr.execute("CREATE TABLE if not exists users(user_id integer,name text)")
# cr.execute("CREATE TABLE if not exists users(user_id integer,name text)")
# cr.execute("insert into users(user_id,name) values(1,'Ahmed')")
# cr.execute("insert into users(user_id,name) values(2,'hasnaa')")
# cr.execute("insert into users(user_id,name) values(3,'menna')")
############################## update ###################
# cr.execute("update users set name ='Gamal' where user_id = 1")
# cr.execute("select * from users")
# print(cr.fetchone())
########################## Delete ###########################
# cr.execute("delete from users where user_id = 4 ")
# cr.execute("select * from users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# db.commit()
############################## ex ##############################
# import sqlite3
# db= sqlite3.connect("app6.db")
# cr = db.cursor()
# cr.execute("CREATE TABLE if not exists skills(user_id integer ,name text , progress integer)")
# #commit and close
# def commit_and_close():
#     db.commit()
#     db.close()
#     print("closed")
# uid=2
# input_message = """
# Whate do you want to do ?
# "s" => show all skills
# "a" => add new skills
# "d" => delet a skills
# "u" => update skill progress
# "q" => quit the app
# choose option :
# """
# user_input = input(input_message).strip().lower()
# print(user_input)

###########command list ###########
# commands_list = ["s","a","d","u","q"]
# def show_skills():
#     cr.execute(f"select * from skills where user_id={uid} ")
#     result = cr.fetchall()
#     print(f"you have {len(result)}skills")
#     if len(result) > 0:
#      print("show skills with progress")
#      for row in result:
#         print(f"skills => {row[0]}",end=" ")
#         print(f"progress => {row[1]}%")
#     commit_and_close() 

# def add_skills():
#     sk = input("Write skill name :").strip().capitalize()
#     cr.execute(f"select name from skills where name ='{sk}' and user_id='{uid}'")
#     result = cr.fetchone()
#     if result == None :
#      print("you can add it")
#      prog = input("write skill progress")
#      cr.execute(f"insert into skills(user_id,name,progress) values({uid},'{sk}','{prog}')")
#     else :
#      print("you cannot add it")
#      add_option = input("skills founded")
#      if add_option == "yes":
#        sk = input("Write the new skills name :").strip().capitalize()
#        cr.execute(f"update skills set progress ='{prog}' where name ='{sk}' and user_id ='{uid}'")

#      else :
#         print("you want add")
 
#     commit_and_close()


# def delet_skills():
#     sk = input("Write skill name :").strip().capitalize()
#     cr.execute(f"delete from skills where name = '{sk}' and user_id = {uid}")

#     commit_and_close()

  
# def update_skills():
#     sk = input("Write skills name :").strip().capitalize()
#     prog = input("write the new skills progress")
#     cr.execute(f"update skills set progress ='{prog}' where name ='{sk}' and user_id ='{uid}'")
#     commit_and_close()


# if user_input in commands_list:
#     print(f"commands found{user_input}")

#     if user_input == "s":
#          show_skills()

#     elif user_input == "a":
#         add_skills()

#     elif user_input == "d":
#         delet_skills()

#     elif user_input == "u":
#         update_skills()

#     else:
#         print("app is closed")

# else:
#     print(f"sorry this\"{user_input}\" is not found")
##################################### ############################
x = []
if x :
    print("hello")
erp = 1 and 5
print(erp)
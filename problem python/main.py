#############################1#######################################
# def reversed_word(word):
    # myList = word.split(" ")
    # myList_reversed = myList[::-1]
    # text_reversed = " ".join(myList_reversed)
    # return text_reversed
    ########################## حل اخر 
    # return " ".join(word.split(" ") [::-1])

# print(reversed_word("hasnaa ayman akle"))
######################################2####################################
# def litres(time):
#     return time//2  
#     # return int(time/2) 
# print(litres(12.2))
################################3##########################################
# def path(h,m,s):
#     return 1000 * ((h*3600) + (m*60) + (s))
# print(path(0,1,1))
###############################4####################################33
# mylist=["hasnsaa","omar","mariam","mohamed"]
# def goose_filter(list):
#     filter_word=[]
#     for name in list:
#         if name not in mylist :
#             filter_word.append(name)
#     return(filter_word)
# print(goose_filter(["mohamed","hager","wafaa","mariam"]))

########################## 5 ##############################
# def invert_value(list):
#     inverted_list =[]
#     for num in list:
#      inverted_list.append(-num)
#     return(inverted_list)
# print(invert_value([1,2,5,7,-1,-2]))
###########################6#################################
# def repeat_str(repeat,str):
    #return str*repeat
#     repeated_string = ""
#     for i in range(repeat):
#         repeated_string+=str
#     return repeated_string
# print(repeat_str(5,"hello"))
###########################7###################################
# def add_length(str):
#  result=[]
#  myLIst= str.split(" ")
#  for word in myLIst :
#      result.append (word + ' ' +str(len(word)))
#  return result
# print(add_length("hasnaa ayman"))
############################# 8###########################
# def how_many_light_sabers_do_you_own(name):
#     if name == "zach":
#         return (18)
#     else :
#         return(0)
# print(how_many_light_sabers_do_you_own("zach"))
############################9##########################
# def power_of_two(n):
#  result =[]
#  x=0
#  while x<= n :
#   result.append(pow(2,x))
#   x+=1
#  return result
#  result=[]

#  for i in range(0,n+1):
#   result.append(pow(2,i))
#  return result
# print(power_of_two(5))
########################### 10 ######################
# def grow(arr): 
#  result = 1
#  for i in arr:
#   result*=i
#  return result
# print(grow([1,2,3,4]))
############################ 11################################3
# def shortcut(arr) :
#  vowel = ["a","e","o","u","i"]
#  result = []
#  for char in arr :
#    if char not in vowel :
#      result.append(char)
#  return  "".join(result) 
# print(shortcut("hello"))
# print(shortcut("mariam"))
################################# 12################################3
# def hotpo(n) :
#  count=0
#  if n <= 0 :
#     return False
#  else :
#    while n != 1:
#        if n % 2 == 0 :
#             n= n/2
#             count+=1
#        else :
#             n = (3 * n) + 1
#             count+=1
#  return count
########### حل اخر
#  count =0
#  while n !=1 :
#   n=(n/2) if n % 2 == 0 else  (3*n)+1
#   count+=1
#  return count


# print(hotpo(1))
# print(hotpo(5))
# print(hotpo(6))
# print(hotpo(23 ))
############################# 13###########################
# fruits={
#  1:"apple",
#  2:",,,"
# }
# def substract_sum(number):
#  number=str(number)
#  number=list(number)
#  number = number - sum([int(x) for x in number])
#  while number not in fruits:
#    number = number - sum([int(x) for x in number])
#  return number , fruits[number]
# print(substract_sum(258))
############################14############################
# def quarter_of(month):
#   from math import ceil
#   return ceil(month/3)
# print(quarter_of(1))
# print(quarter_of(2))
# print(quarter_of(3))
# print(quarter_of(4))
# print(quarter_of(5))
# print(quarter_of(6))
# print(quarter_of(7))
# print(quarter_of(8))
# print(quarter_of(9))
# print(quarter_of(10))
#################################15###################
# def summation(num):
#  result =0
#  for i in range(1,num+1):
#    result+=i
#  return result
####################حل اخر #######################3
#   return sum(range(1,num+1))
# print(summation(10))
# ################################16############################
# def squar(n):
#  return(n*n)
#  return(n**2)
#   return pow(n,2)
# print(squar(2))
#########################17###################################
# def remov_c(s):
# #  return s.replace('!',"")
#  return "".join([x for x in s if x !="!"])
# print(remov_c("hello!mohame!"))
########################### 18 ##############################
# def even_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(2))
# print(even_odd(1))
########################## مسايله تاني ف نفس لفيديو ###############3
# def even_sum(num):
#     if num %2 == 0:
#         return num*2
#     else:
#         return num*3
# print(even_sum(2))
# print(even_sum(1))
###########################18#########################
# def pyth(n1,n2,n3):
    # arr =[]
    # arr.append(n1)
    # arr.append(n2)
    # arr.append(n3)
    # arr1=sorted(arr)
    # a = arr1[0]
    # b = arr1[1]
    # c = arr1[2]
    # if (pow(a,2) + pow(b,2)) == pow(c,2):
    #     return True
    # else:
    #     return False

    ########################################33حل اخر
    # arr =[n1,n2,n3]
    # # arr1=sorted(arr)
    # arr1 = sorted()
    # a = arr1[0]
    # b = arr1[1]
    # c = arr1[2]
    # if (pow(a,2) + pow(b,2)) == pow(c,2):
    #     return True
    # else:
    #     return False
    ######################حل اخر#حل اخر
#      arr =[n1,n2,n3]
#      arr1=sorted(arr)
#      return (pow( arr1[0],2) + pow(arr1[1],2)) == pow(arr1[2],2)
    
# print(pyth(5,3,4))
#####################################19
# def max_min(arr):
#  maxList= max(arr)
#  minList = min(arr)
#  return maxList,minList
# print(max_min([5,6,10,8,1,9]))
########################3حل اخر###################3
# from functools import reduce


# def min_num(arr):
#   def m(a,b):
#      return a if a < b else b
#   result= reduce(m,arr)
#   return result
# def max_num(arr):
#   def m(a,b):
#      return a if  a > b else b
#   result= reduce(m,arr)
#   return result
# print(max_num([5,6,10,8,1,9]))
# print(min_num([5,6,10,8,1,9]))
##################حل اخر##########################3
# def max_min(arr):
#  max_num = sorted(arr)[0]
#  min_number = sorted(arr)[-1]
#  return min_number , max_num
# print(max_min([5,6,10,8,1,9]))
###########################20#####################33
# def find_nult(int,limit):
#  result = []
#  for i in range(int,limit+1):
#   if i % 2 == 0 :
#     result.append(i)
#  return result
#########################حل اخر#######################3
#  return list(range(int,limit+1,int))
# print(find_nult(2,10))
################################21###################
# def check(str):
#  if str[0:].lower() == str[::-1].lower():
#   return True
#  else:
#   return False 
###############################3حل اخر بخطوه تاني #############
#  return str.lower() == str[::-1].lower()
# print(check("Madam"))
################################22#########################
# def check(n1,n2):
#  n1 = 0 if n1 =="" else int(n1)
#  n2 = 0 if n2 =="" else int(n2)
#  return str(n1+n2)
# print(check("1","2"))
# print(check("",""))
# print(check(1,2))
#############################23#########################333
# def bmi(weight,hight):
#  result = (weight)/pow(hight,2) 
#  if result <= 18.5 :
#   return "underWeight"
#  elif result <= 20.5 :
#   return "overWight"
#  elif result > 30 :
#   return "obese"
# print(bmi(80,1.72))
# print(bmi(150,1.72))
# print(bmi(500,1.72))
# print(bmi(86,1.80))
######################################24#############################3
# def positive_negitive(arr):
    # count=0
    # sum=0
    # if len(arr)==0:
    #   return []
    # for num in arr:
    #   if num > 0 :
    #    count+=1
    #   elif num<0:
    #    sum+=num
    # return sum , count
    #############################حل اخر########################
#     positive = []
#     negitive= []
#     if len(arr)==0:
#      return []
#     for num in arr :
#        if num > 0 :
#           positive.append(num)
#        elif num < 0 :
#           negitive .append(num)
#     return [len(positive),sum(negitive)]

# print(positive_negitive([1,2,3,4,5,-6,-7,-8,-9]))
# print(positive_negitive([0,0]))
# print(positive_negitive([]))
###########################1######################################
# def reverses_word(str):
#     # my_list = str.split(" ")
#     # my_reverse = my_list[::-1]
#     # my_str= " ".join(my_reverse)
#     # return my_str
#     return " ".join(str.split(" ") [::-1])
  
# print(reverses_word("my name is hasnaa ayman"))

# def literes(time):
#    return round(time/2)
# print(literes(6))

# my_list = ["mariam","hasnaa","wafaa","ayman"]
# def check(list):
#   new_list = []
#   for name in list:
#     if name not in my_list:
#         new_list.append(name)
#   return new_list
# print(check(["mohamed","omar","hasnaa","zena"]))

# def check(arr):
#     my_list =[]
#     for num in arr:
#      my_list.append(-num)
#     return my_list
# print(check([1,2,-3,-4]))
      
# def check(repeart,string):
#     return string*repeart
# print(check(3,"hello"))

# def check(r,s):
#  repeat_str = ""
#  for i in range(r):
#   repeat_str+=s
#  return(repeat_str)
# print(check(5,"hasnaa"))

# def add_length(str):
#  my_list=[]
#  my_list_str =str.split(" ")
#  for item in my_list_str:
#     my_list.append(f"{item} {len(item)}")
#  return my_list
# print(add_length("hasnaa ayman akle"))

# def check(name="zach"):
#     if name =="zach":
#      return 18
#     else:
#         return 0
# print(check("ahmed"))

# def power(n):
#     my_list=[]
#     for n in range(n):
#         my_list.append(2**n)
#     return my_list
# print(power(10))

# def multiplying(arr):
#     mult=1
#     for n in arr:
#         mult*=n
#     return mult
# print(multiplying([1,2,3,4]))

# def check(str):
#  my_list_add =[]
#  my_list = ["o","e","i","u","a"]
#  for char in str:
#   if char not in my_list:
#    my_list_add.append(char)
#  return "".join(my_list_add)
# print(check("hasnaa"))
# print(check("HELLO"))

# def check(n):
#   count= 0
#   while n!=1:
#    if n % 2==0:
#      n=n/2
#      count+=1
#    else :
#     n=(3*n)+1
#     count+=1
#   return count

# print(check(1))
# print(check(5))
# print(check(6))
# print(check(23))

# def sub_sum(num):
#  count =0
#  number =str(num)
#  number = list(number)
#  for n in number:
#     count+=int(n)
#  result = num-count
#  while result not in fruits:
#     result = num-count
#  return result
# print(sub_sum(235))
 
# def check(month):
#  from math import ceil
#  return ceil((month/3))
# print(check(1))
# print(check(2))
# print(check(3))
# print(check(4))
# print(check(5))
# print(check(6))
# print(check(7))
# print(check(8))
# print(check(9))
# print(check(10))
# print(check(11))
# print(check(12))









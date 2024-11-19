'''a="Vaseem"
b=17
c="my name is {1},my no is {0}"
print(c.format(a,b))'''

'''a="Vaseem"
b=17
print("my name is %s,my no is %d"%(a,b))'''

'''a='vaseem'
b='Vassu'
c=17
print(f"my name is {a} and my number is {c} and my cgpa is {b}".format(a,b,c))'''

'''a="aaat"
b="aaaz"
print(min(a))'''

'''a=[1,2,3,4,6]
for i in range (len(a)):
    if (i%2==0):
        print(a[i])'''

'''a=input("Enter the string: ")
str=a.split
print(str)





#set the kth bit input a=5,k=3,0000101,0000101
#a=12,b=17'''

#Anagram

'''s=input("Enter the string: ")
a=input("Enter the String: ")
s=sorted(s)
a=sorted(a)
if s==a:
    print("Anagram")
else:
    print("not anagram")
'''

# pseuducode

'''n=127
i=0,s=0
function Sample(int n)
    while(n>0)
        r=n%10
        p=8^i
        s=s+p*r
        i++
        n=n/10
    end while
    return s'''
    
"""oops vs pop"""

'''class student:
    name="vaseem"
    num=78
    dep="CSD"
    clg="SVCET"
    def read():
        print("I am a good boy")
    def no_talk():
        print("I dont speak")
obj=student()
print(id(obj))
print(obj.name)
obj2=student()
print(id(obj2))
print(obj2.name)'''

"""class person:
    def vaseem(hi,a):
        print(a+5)
        print("hi")
obj=person()
print(obj)
obj.vaseem(7)
print("-------------------")
obj2=person()
print(obj2)
obj.vaseem(17)
print("-------------------")"""

'''class person:
    clg='scvet'
    def __init__(self,num,age,color,height,weight,rating):
        self.num=num
        self.age=age
        self.color=color
        self.height=height
        self.weight=weight
        self.rating=rating
def display(self):
    print(self.num,self.age,self.color,self.height,self.weight,self.rating)
vinay=person(90,22,'white',5.9,89,9.9)
Constructor vs method
vinay.display()
print(vinay.clg)'''

#Constructor
'''class person:
    clg='scvet'
    def __init__(self, num, age, color, height, weight, rating):
        self.num = num
        self.age = age
        self.color = color
        self.height = height
        self.weight = weight
        self.rating = rating

    def display(self):
        print(self.num, self.age, self.color, self.height, self.weight, self.rating)

vinay = person(90, 22, 'white', 5.9, 89, 9.9)
vinay.display()
print(vinay.clg)'''

#Inheritance
#using the already present information and adding new feature to the presented information
#Acquiring properties from parent class to child class

'''class mujeeb_khan:#single heritance
     def profession(self):
        print("I am railway driver")
     def qualities(self):
        print("I like my grandchildren ")
class manzoor_ali(mujeeb_khan): # multiple heritance(2parents class at a time)
    def wives(self):
        print("I have two Wives ")
    def names(self):
        print("Their Names are Shabana,Khuster")
class khuster_jahan(manzoor_ali):
    def childerns(self):
        print("My childrens are Vaseem and Manal")
    def work(self):
        print("i am housewife")
class manal(manzoor_ali): #Hierrachial Interitance
    def relation(self):
        print(" My parents are khuster_jahan and Manzoor ali")
    def brother(self):
        print("My brother name is Vaseem")
class vaseem(khuster_jahan): #multilevel Inheritance
    def loves(self):
        print("I love my mom ")
    def hobbies(self):
        print("I play football and basketball")

class zameer():
    def mama(self):
        print("i am khuster jahan's brother")
    def job(self):
        print("i work as a RPA developer and i have 11 Years of Experience")
mujeeb=mujeeb_khan()
mujeeb.profession()
mujeeb.qualities()
khan=manzoor_ali()
khan.wives()
khan.names()
zeeshan.childrens()
zeeshan.work()
zeeshan.name()
zeeshan.relation()
zeeshan.brother()
zeeshan.love()
zeeshan.hobbies()
zeeshan.mama()
zeeshan.job()'''


#method overloading
'''class exam:
    def add(a,b):
        print(a+b)
    def add(a=12,b=7,c=0):
        print(a+b+c)
    def add(self):
        print('This is one method')
obj=exam()
obj.add()        
'''
'''#exam.add()static method'''

#mehtod overwriting
'''class a:
    def hello(self):
        print("hello")
class b:
    def hello(self):
        #super().hello
        print("hi")
obj=a()
obj.hello()
obj2=b()
obj2.hello()'''


'''class CSK:
    def captain(self):
        print("Gaikwad")
    def moto(self):
        print("Whistle podu")
    def place(self):
        print("chennai")
class RCB(CSK):
    def captain(self):
        super().captain()
        print("Virat")
    def moto(self):
        super().moto()
        print("E saala cup NAMDHE")
    def place(self):
        print("UP")
thala=RCB()
thala.moto()
'''
#abstraction
from abc import ABC, abstractmethod
class display(ABC):
    @abstractmethod
    def disp(self):
        pass
class phone (display):
    def disp(self):
        print("6 inches")
class laptop (display):
    def disp(self):
        print("16 inches")
class smartwatch(display):
    def disp(self):
        print("5 inches")
    def an(self):
        print("hi")
        
sw=smartwatch()
sw.disp()
        
       




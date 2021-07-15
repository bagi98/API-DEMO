
'''
class myclass():
	no=20
	name="bagi"
	sal=27000
obj1=myclass()
print(obj1.no)
print(obj1.name)
print(obj1.sal)
'''
'''
class myclass:
	def __init__(self,no,name,sal):
		self.no=no
		self.name=name
		self.sal=sal
	def show(self):
		print(self.no,self.name,self.sal)
obj1=myclass(100,"sai",27000)
obj1.show()
'''	
'''
class employess():
	def __init__(x,empno,empname,basic_sal,total_all,total_ded):
		empno=input("enter employee number ")
		x.empno=empno
		empname=input("enter employee name")
		x.empname=empname
		x.basic_sal=basic_sal
		x.total_all=total_all
		x.total_ded=total_ded
	def show(x):
		print("employee_name ",x.empname," salary in hand ",x.basic_sal+x.total_all-x.total_ded)
obj1=employess()
obj1.show()
'''	
'''	
class A():
	def __init__(self):
		print("welcome to class A constructor")	
	no=101
	name="bagi"
	def show_A(self):
		print(self.no,self.name)
obj=A()
obj.show_A()
'''

'''
class A():
	def __init__(self):
		print("welcome to class A constructor")	
	def show_A(self):
		print("i am in class A ")
		
class B(A):
	def __init__(self):
		print("welcome to class B constructor")	
	def show_B(self):
		print("i am in class B ")
		
class C(B):
	def __init__(self):
		print("welcome to class C constructor")	
	def show_C(self):
		print("i am in class C ")
		
obj=C()
obj.show_C()
obj.show_B()
obj.show_A()

'''
'''
class animals():
	def __init__(self):
		print("welcome to animals class")
	def show_A(self):
		print("we have more number animals")
		
class Dog(animals):
	def __init__(self,name):
		self.name = name
	def speak(self):
		return self.name + " says BOWW"
		
class Cat(Dog):
	def __init__(self,name):
		self.name = name
	def speak(self):
		return self.name + " says MEOW"
		
my_dog = Dog("dog")
my_cat = Cat("cat")

print(my_dog.speak())
print(my_cat.speak())
		
'''
'''
class animals():
	def __init__(self):
		print("welcome to animals class")
	def show_A(self):
		print("we have more number animals")
'''
'''
class Cat(animals):
        def __init__(self):
            print("welcome to Cat class ")
        def guess_who(self):
            print("I am a cat")
        def meow(self):
            print("I say MEOWW!")
my_cat = Cat()
my_cat.guess_who()
my_cat.meow()
my_cat.show_A()

'''
class BankAccount():
    def _init_(self,accountnumber,name,balance):
        self.acc=accountnumber
        self.name=name
        self.bal=balance-balance*0.0255
    def deposit(self,amt):
        self.bal+=amt
        self.bal-=self.bal*0.0255
        print("Updated balance is",self.bal)
    def withdrawal(self,amt):
        if(amt>self.bal):
            print("Not enough Cash")
        else:
            self.bal-=amt
            print("Updated balance is",self.bal)
    def bankCharges(self):
        print("Bank Charges appied to your account are",self.bal*0.0255)
    def display(self):
        print("Name:",self.name,"\nAccount number:",self.acc,"\nBalance:",self.bal)
udts={}
while True:
    i=int(input("press 1 to create account. press 2 for banking services. Press 3 to exit "))
    if(i==1):
        acc=int(input("Enter account Number "))
        name=input("Enter name ")
        bal=int(input("Enter entry deposit "))
        usr=input("Almost done, Set username ")
        pwd=input("create password ");
        ls=[pwd,acc,name,bal]
        print("Your account has been successfully created")
        udts[usr]=ls
    elif(i==2):
        usr=input("Welcome to our Bank, Please enter your username ")
        if(usr not in udts.keys()):
            print("Sorry, no such user exists")
            continue
        pwd=input("Password ")
        if(udts[usr][0]!=pwd):
            print("Wrong password")
            continue
        obj=BankAccount(udts[usr][1],udts[usr][2],udts[usr][3])
        n=int(input("Login Successful\n Press 1 to deposit, 2 to withdraw, 3 to see applicable bank charges, 4 to see all details."))
        if(n==1):
            csh=int(input("Enter amount to deposit"))
            obj.deposit(csh)
        elif(n==2):
            csh=int(input("Enter amount to withdraw"))
            obj.withdrawal(csh)
        elif(n==3):
            obj.bankCharges()
        elif(n==4):
            obj.display()
    else:
        break;












































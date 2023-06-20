##################################
# 1- Text Type:
##################################
str() #string
"Hello"
'Hello'
print("Hello")
type("Hello") # what's type()?
567234234
##################################
# 2- Numeric Types:
##################################
int() # integer
5
type(5)
"5" # str
type("5")

float() #float
5.1
type(5.1)

5.0 # float not int
type(5.0)
type(5.)

complex()
1+2j
type(1+2j)

##################################
# 3- Boolean Type:
##################################
bool()
True
False
type(True)

##################################
# 4- Setting and Changing the Data Type:
##################################
a = "Hello"
print(a) # what's print()?
type(a)

del a
print(a) # NameError

a = "5"
type(a)
int(a)  # str > int
type(a)
a = int(a) # inplace False
type(a)

a = "5.7"
type(a)
a = int(float(a)) # str > int
type(a)

a = "5.7"
type(a)
a = float(a) # str > float
type(a)

# a= "0"
# type(a)
# a = bool(a) # str > bool
# type(a)

b = 5
type(b)
b=str(b) # int > str
type(b)

b = 5
type(b)
b = float(b) # int > float
type(b)

b = 1
type(b)
b = bool(b) # int > bool
type(b)

c = 5.7
type(c)
c=str(c) # float > str
type(c)

c = 5.7
type(c)
c=int(c) # float > int (not round)
type(c)

c = float(c)

type(round(5.7))

c = 1.0
type(c)
c = bool(c) # float > bool
type(c)

d=True
type(d)
d = str(d) # bool > str
type(d)

d=True
type(d)
d = int(d) # bool > int
type(d)

d=True
type(d)
d = float(d) # bool > float
type(d)

a = "" # str
bool(a)

a = " " # str
bool(a)

a = 0 # int
bool(a)

a = 5 # int
bool(a)

a = 0.0 # float
bool(a)

a = 0.1 # float
bool(a)

a = None # Nonetype
bool(a)

set1={1,2,3,4,"Onur","Lokum","Semanur"}
set1.remove(5)
set1.discard(5)
del set1[0] #sette yok

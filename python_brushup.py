import test_module #User defined module


print("Hello World !!!")

# Data types. No need to mention the data type before variable name as in C++
var_int = 1
var_bool = False
var_float = 2.4
var_string = "Febin"

print(var_bool)
print(str(var_int) + " " + var_string )

# Collection data types
# List - Mutable, Unordered
my_list = [] #Empty list
my_list_new = [1, "Febin", 2.5]
print(my_list_new[1])
my_list.append(1)
print(my_list)

# Dictionary
my_dict = {}
my_dict_new = {"key" : "value", 1 : 2}
print(my_dict_new["key"], my_dict_new[1])
my_dict["First Key"] = "First Value"
print(my_dict["First Key"])

# Tuple, Set - Other data types

# Loops
for item in my_dict_new:
    print(item) # Name of keys printed

for items in range(len(my_list_new)):
    print(my_list_new[items])


count = 0
while True:
    print("Fail again, Fail better")
    count += 1
    if count == 3:
        break

print("Out of while loop")

# Operators
add = 1 + 2
sub = 1 - 2
mul = 1 * 2
div = 1 / 2
exp = 1 ** 2
rem = 1 % 2

print(add, sub, mul, div, exp, rem)

# Functions
def add(num1, num2):
    return num1 + num2

result = add(num1=1, num2=2)
print(result)

# Class
class Animal:
    def __init__(self, name):
        self.name = name
        print("Constructor awakened")
    
    def report(self):
        print("Animal's name: ", self.name)
    
class Dog(Animal):
    #Explicit initialization
    #def __init__(self,name):
        #super().__init__(name)
    def report(self):
        print("Dog's name: ", self.name)

obj1 = Animal("Django")
obj1.report()
obj2 = Dog("Kaiser")
obj2.report()

# Modules
res = test_module.sub(num1=10, num2=5)
print(res)



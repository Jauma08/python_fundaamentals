# Declaración de una variable de tipo cadena
name = "Alice" 
# Declaración de una variable de tipo cadena
age = 30
#
print("Name:", name)
print(age)
# change the value of the variable "name"
name= "Bob"
print(name)
age=45
print(age)
# the function "type()" is used to read the type of an object
print(type(name))

print(type(0.25))
print(type(0.0025))
print(type(10))
print(type(age))

is_running = True

variable_type = type(is_running)
print(variable_type)
is_running=False
print(type(is_running))
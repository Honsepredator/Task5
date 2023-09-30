name = input("Enter your name.")
age = input("Enter your age")
street= input("provide your street")
city=input("Provide city")
country=input("Enter country")
print(f"\"Name :{name}\" ")
print(f"\"Age : {age}\"")
print(f"Adress: {street},{city},{country}")
print(f"Hello {name} Your age is {age} Years Old,Your Address is {street},{city},{country}")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of street:", type(street))
print("Type of city:", type(city))
print("Type of country:", type(country))
print(f"\"Hello {name}, How Are You? \ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")
print(f"\"Hello {name}, How Are You? \ \n \"\"\" Your Age Is \"{age}\"\" + And\n Your Country Is: {country}")
name = 'ITF Gsg Python'
print(f"First letter is \" {name[0]} \"")
print(f"Third letter is \"{name[2]}\"")
print(f"last letter is \"{name[-1]}\"")
print(name[-3:])
print(name[:3])
print(name[0:7:2])
print(name[:7:-1])
name = "$&$&Mohammed$&$&"
print(name.strip("$&"))
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love"))
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6)
#Title makes every first letter of a word in a string capital
#capitalize makes every letter capital
Pen="mercy core"
print(Pen.capitalize())
print(Pen.title())
first_name = input("AbdulRahman")
print("*" * 11 + first_name)
print("*" * 11 + first_name + "*" * 11)
print(first_name + "*" * 11)
name1 = "SaMER"
name2 = "Abed"
print(name1[0].lower() + name1[1:].upper())
print(name2[0].lower() + name2[1:].upper())
print(name1.lower())
print(name2.upper())
if name1.isupper():
    print("name1 contains only uppercase letters.")
else:
    print("name1 does not contain only uppercase letters.")
if name2.islower():
    print("name2 contains only lowercase letters.")
else:
    print("name_2 does not contain only lowercase letters.")
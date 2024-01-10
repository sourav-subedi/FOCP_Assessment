# 1
def validate_input(number):
    if 0<=number<=100:
        return True
    else:
        return False
number=int(input("Enter integer number"))
print(validate_input(number))

# 2
def count_uppercase_and_lowercase_letters(string_word):
    uppercase = sum(1 for letter in string_word if letter.isupper())
    lowercase = sum(1 for letter in string_word if letter.islower())
    return uppercase, lowercase
word=input("Enter a word")
counts=count_uppercase_and_lowercase_letters(word)
print(f"Uppercase letters: {counts[0]}\nLowercase letters: {counts[1]}")

# 3
name = input("Hello,What is your name? ")
if name:
    print(f"Hello, {name.capitalize()}. Good to meet you!")
else:
    print("Hello, Stanger")

# 4

# def remove_last_character(word):
#     if len(word)
#     return new_word
# word=input("Enter a word")
# print(f"The new word is {remove_last_character(word)}")
    
# 5
def centigrade_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32
def fahrenheit_to_centigrade(fahrenheit):
    return (fahrenheit - 32) * 5/9

celcius=float(input("Enter the temperature in celcius: "))
fahrenheit=centigrade_to_fahrenheit(celcius)
print(f"{celcius}°C is equivalent to {fahrenheit}°F")

fahren=float(input("Enter the temperature in fahrenheit: "))
centigrade=fahrenheit_to_centigrade(fahren)
print(f"{fahren}°F is equivalent to {centigrade}°C")

# 7
temperature=[]
for i in range(6):
    temp=float(input(f"Enter the {i+1} temperature: "))
    temperature.append(temp)
maximum_temperature=max(temperature)
minimum_temperature=min(temperature)
avg_temp=sum(temperature)/6
print(f"Maximum Temperature is :{maximum_temperature}\n Minimum Temperature is :{minimum_temperature}\n Average Temperature is :{avg_temp}")

# 8
temperature=[]
number=int(input("Enter the number of data to be processed :"))
if number!=None:
    for i in range(6):
        temp=float(input(f"Enter the {i+1} temperature: "))
        temperature.append(temp)
    maximum_temperature=max(temperature)
    minimum_temperature=min(temperature)
    avg_temp=sum(temperature)/6
    print(f"Maximum Temperature is :{maximum_temperature}\n Minimum Temperature is :{minimum_temperature}\n Average Temperature is :{avg_temp}")




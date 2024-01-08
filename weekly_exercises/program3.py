# 1
name = input("Hello,What is your name? ")
if name:
    print(f"Hello, {name}. Good to meet you!")
else:
    print("Hello, Stanger")

# 2
new_password=input("Enter New Password: ")
confirm_password=input("Confirm New Password: ")
if new_password==confirm_password:
    print("Password Set")
else:
    print("Passwords Do Not Match")

#3
new_password=input("Enter New Password: ")
confirm_password=input("Confirm New Password: ")
if new_password==confirm_password and (8<=new_password<=12):
    print("Password Set")
else:
    print("Passwords Do Not Match")    

# 4
BAD_PASSWORD=['password', 'letmein', 'sesame', 'hello', 'justinbieber']
new_password=input("Enter New Password: ")
confirm_password=input("Confirm New Password: ")
if new_password==confirm_password and (new_password in BAD_PASSWORD):
    print("Password already exists")
elif new_password==confirm_password:
    print("Password Created Successfully")
else:
    print("Passwords Do Not Match")

# 5
while 1:
    new_password=input("Enter New Password: ")
    confirm_password=input("Confirm New Password: ")
    if new_password==confirm_password and (new_password in BAD_PASSWORD):
        print("Password already exists")
    elif new_password==confirm_password:
        print("Password Created Successfully")
        break
    else:
        print("Passwords Do Not Match")

# 6
print("Seven Times Table\n")
for i in range(12):
    print(f"{i} * 7 = {i*7}")

# 7
number_table=float(input("Enter the number of table required (0,12): "))
for i in range(12):
    print(f"{i} * {number_table} = {i*number_table}")

# 8

number_table=float(input("Enter the number of table required (0,12): "))
if number_table>=0:
    for i in range(12):
        print(f"{i} * {number_table} = {i*number_table}")
elif number_table<0:
    for i in range(12,0):
        print(f"{i} * {number_table} = {i*number_table}")
    

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
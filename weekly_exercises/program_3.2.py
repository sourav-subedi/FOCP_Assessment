#3
new_password=input("Enter New Password: ")
confirm_password=input("Confirm New Password: ")
if new_password==confirm_password and (8<=new_password<=12):
    print("Password Set")
else:
    print("Passwords Do Not Match")    

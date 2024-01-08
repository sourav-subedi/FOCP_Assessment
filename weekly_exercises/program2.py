# 1
name = input("Hello,What is your name? ")
print(f"Hello, {name}. Good to meet you!")

# 2
deg_C=float("Enter a temperature in celcius: ")
deg_f=(deg_C*(9/5)+32)
print(f"{deg_C}C is equivalent to {deg_f}F")

# 3
group_number=int(input("How many Students? "))
group_size=int(input("Required group size?"))
groups=group_number//group_size
reminder=group_number%group_size
print(f"There will be {5} groups with {3} students left over")

# 4
sweets=int(input("How many sweets do you have? "))
pupils=int(inputJ("How many pupil attend the class? "))
per_pupil=sweets//pupils
leftovers=sweets%pupils
print(f"Each child will get {per_pupil} sweets and there will be {leftovers} left")
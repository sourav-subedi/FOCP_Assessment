# 1
print("Hello World")

# 2
name = input("What is your name? ")
print(f"Hello, {name}")

# 3
deg_C=38.4
deg_f=(deg_C*(9/5)+32)
print(f"{deg_C}C equals to {deg_f}F")

# 4
batted=1014
not_out=162
runs=48426
completed_innings=batted-not_out
batting_average=runs/completed_innings
print(f"Boycott's batting average: {batting_average}")

# 5
lsit_of_students=[113,175,12]

for students in lsit_of_students:
    full_group=students//24
    remaining_students=students%24

    print(f"For {students} students: ")
    print(f"\tFull group of classes: \t\t{full_group}")
    print(f"\tRemaining students in leftover group: \t{remaining_students}")

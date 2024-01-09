# 1 Write a program that prints a cheery message (such as "Hello World") on the
# screen. Run it, and note that you have taken the first step to becoming a
# programmer!
print("Hello World")

# 2. Make a copy of the previous program, and modify it so that it displays your name.
# So if your name is Herbert the message should become:
# Hello, Herbert!
# Note: Very few programs are written from scratch. It is usually best to start with a
# program that you know works, and ideally does something similar to the new
# program.

name = input("What is your name? ")
print(f"Hello, {name}")

# 3. Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
# converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
# displays both.

deg_C=38.4
deg_f=(deg_C*(9/5)+32)
print(f"{deg_C}C equals to {deg_f}F")

# # 4. In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.
# Note: A batting average is the number of runs scored divided by the number of
# completed innings (i.e. the total times batted minus the times not out).
batted=1014
not_out=162
runs=48426
completed_innings=batted-not_out
batting_average=runs/completed_innings
print(f"Boycott's batting average: {batting_average}")

# 5. The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "leȦ over"
# group
lsit_of_students=[113,175,12]

for students in lsit_of_students:
    full_group=students//24
    remaining_students=students%24

    print(f"For {students} students: ")
    print(f"\tFull group of classes: \t\t{full_group}")
    print(f"\tRemaining students in leftover group: \t{remaining_students}")

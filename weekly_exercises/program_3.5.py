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
    
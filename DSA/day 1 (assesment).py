# Monthly expenses
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compared to January?
print("1. Extra spent in February:", expenses[1] - expenses[0])

# 2. Total expense in the first quarter (January + February + March)
print("2. Total expense in first quarter:", expenses[0] + expenses[1] + expenses[2])

# OR
# print("2. Total expense in first quarter:", sum(expenses[:3]))

# 3. Find out if you spent exactly 2000 dollars in any month
print("3. Did you spend exactly $2000 in any month?", 2000 in expenses)

# 4. Add June expense (1980)
expenses.append(1980)
print("4. Expenses after adding June:", expenses)

# 5. April expense was refunded by $200
expenses[3] = expenses[3] - 200
print("5. Expenses after April refund:", expenses)
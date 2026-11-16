expenses = []

def add_expense(amount):
    expenses.append(amount)

def show_expenses():
    print("Expenses:", expenses)
    print("Total:", sum(expenses))

add_expense(500)
add_expense(200)
add_expense(300)
add_expense(400)

show_expenses()
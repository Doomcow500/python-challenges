value = int(input("How many pounds do you want to convert?"))

print(f"£{value} = €{value * 1.15}")
value = value * 1.15

fiftyNotes = value // 50
twentyNotes = (value % 50) // 20 
tenNotes = ((value % 50) % 20) // 10
fiveNotes = (((value % 50) % 20) % 10) // 5
left = (((value % 50) % 20) % 10) % 5
print(f"This equals: \n{fiftyNotes} £50 Notes\n{twentyNotes} £20 Notes\n{tenNotes} £10 Notes\n {fiveNotes} £5 Notes\nWith £{left} left over.")

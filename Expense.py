def menu():
    print("===== EXPENSE TRACKER =====")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Calculate Total Expenses")
    print("4.Calculate Expenses by Category")
    print("5.Exit")     
l=[]

while True:
 menu()
 choice=int(input("Enter your choice(1 to 5): "))
 if choice==1:
     count=int(input("Enter how many expance do you want to add: "))
     for i in range(count):
       name = input("Enter expense name: ")
       category = input("Enter category: ")
       amount = int(input("Enter amount: "))
       d={}
       d["name"]=name
       d["category"]=category
       d["amount"]=amount
       l.append(d)
     print("your expance added sucesfully")
 elif choice==2:
    print(l)
 elif choice==3:
    sum_of_all=0 
    for expance in l:
        cal=expance.get("amount")
        sum_of_all+=cal
    print(f"Total Expenses: ₹{sum_of_all}") 
 elif choice==4:
    total=0
    to_check=input("Enter category: ").lower()
    for expance in l:
     cal=expance.get("amount")
     catg=expance.get("category")
     if to_check==catg.lower():
        total+=cal
    print(f"Total {to_check.title()} Expenses: ₹{total}") 
 elif choice==5:
    print("Thank You.")
    break
 else:
    print("Enter valid input!")
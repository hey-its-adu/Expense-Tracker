import json
def menu():
    print("===== EXPENSE TRACKER =====")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Calculate Total Expenses")
    print("4.Calculate Expenses by Category")
    print("5.Delete Expance")
    print("6.Exit")     
def store_expense():
   with open("expense.txt","w") as file:
      json.dump(l,file)
def open_expense():
    with open("expense.txt","r") as file:
     return json.load(file)
try:
    l=open_expense()
except FileNotFoundError:
   l=[]

while True:
 menu()
 try:
    choice=int(input("Enter your choice(1 to 6): "))
    if choice==1:
        try:
           count=int(input("Enter how many expance do you want to add: "))
           if(count>0):
             for i in range(count):
              d={}
              name = input("Enter expense name: ").strip()
              d["name"]=name
              category = input("Enter category: ").strip()
              d["category"]=category        
              amount = int(input("Enter amount: ").strip())
              d["amount"]=amount
              if name.isdigit() or category.isdigit() or name == "" or category == "" or amount<=0:
                   print("You enter invald data!")
                   print("Try to add valid data")
              else:
                  l.append(d)
                  store_expense()
                  print("your expance added sucesfully")          
           else:
                 print("Enter positive numbers")  
        except ValueError:
            print("Please enter a valid number for the count or amount.")


    elif choice==2:
         if l:
          print("=======YOUR EXPANCE=======")
          for i in l:
             print(f"name: {i.get('name')} | category: {i.get('category')} | amount: ₹{i.get('amount')}")
         else:
            print("No expenses added yet")

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
       to_del=input("Enter Expense to delete: ").lower()
       for i in l:
           if i.get("name").lower() ==to_del:
             l.remove(i)
             print(f"{i.get('name')} Expense deleted Sucesfully")
             store_expense()
             break
       else:
              print("expensce not found")
       
    elif choice==6:
       print("================= Thank You =========================")
       break
    else:
       print("Enter valid input!")
 except ValueError:
     print("Enter number in (1 to 6)")
     
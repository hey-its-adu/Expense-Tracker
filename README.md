# 💰 Python Expense Tracker

A command-line Expense Tracker built with Python to help users record daily expenses, monitor spending, and understand where their money goes.

The application allows users to add and view expenses, calculate total spending, analyse expenses by category, and delete records. It also uses JSON to preserve expense data between program runs.

**Built as my second Python project to apply programming concepts to a practical, real-world problem.**

##  Project Overview

Keeping track of everyday spending can be difficult without a simple system. This project provides a lightweight solution that allows users to record expenses and calculate spending totals directly from the terminal.

The project focuses on writing clear program logic, validating user input, handling common errors, and saving data for future use.

##  Features

* **Add Expenses:** Record an expense name, category, and amount.
* **View Expenses:** Display saved expenses in a readable format.
* **Calculate Total Spending:** Calculate the combined amount of all recorded expenses.
* **Category-Wise Analysis:** Calculate spending for a selected category, such as Food or Travel.
* **Delete Expenses:** Remove an expense by entering its name.
* **Input Validation:** Reject empty names and categories, names or categories containing only digits, and amounts that are zero or negative.
* **Error Handling:** Use `try/except` to handle invalid numeric input without immediately terminating the application.
* **Persistent Data Storage:** Save expenses to a file and load them when the program starts, so records remain available between sessions.

## 🛠️ Technologies Used

| Technology             | Purpose                                  |
| ---------------------- | ---------------------------------------- |
| Python 3               | Application logic and expense management |
| Lists and Dictionaries | Store and organize expense records       |
| Functions              | Organize reusable operations             |
| JSON                   | Save and load expense data               |
| Exception Handling     | Handle invalid numeric input             |
| Git                    | Track code changes                       |
| GitHub                 | Host and showcase the project            |

**No external Python packages are required.** The project uses Python's built-in `json` module.

##  Project Structure

```text
Expense-Tracker/
├── Expense.py
├── expense.txt
└── README.md
```

* **`Expense.py`** — Contains the application, menu, validation logic, and expense calculations.
* **`expense.txt`** — Stores expense records in JSON format.
* **`README.md`** — Provides project documentation and setup instructions.


##  Available Operations

When the program starts, the following menu is displayed:

```text
===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Calculate Total Expenses
4. Calculate Expenses by Category
5. Delete Expense
6. Exit
```

Select an option by entering its corresponding number.

## 💡 Example

Suppose the following expenses are recorded:

| Expense Name | Category |   Amount |
| ------------ | -------- | -------: |
| Lunch        | Food     |     ₹100 |
| Bus          | Travel   |      ₹40 |
| Dinner       | Food     |     ₹200 |
| **Total**    |          | **₹340** |

### Calculate Total Expenses

```text
Total Expenses: ₹340
```

### Calculate Expenses by Category

When the user selects `Food`:

```text
Total Food Expenses: ₹300
```

This allows the user to see both overall spending and spending within a particular category.

## 💾 How Data Storage Works

The application uses Python's built-in `json` module to store expense records in `expense.txt`.

Each expense is represented as a dictionary containing its name, category, and amount. The dictionaries are stored together in a list.

For example:

```json
[
  {
    "name": "Lunch",
    "category": "Food",
    "amount": 100
  },
  {
    "name": "Bus",
    "category": "Travel",
    "amount": 40
  }
]
```

The application uses:

* **`json.dump()`** to save the expense list to a file.
* **`json.load()`** to load previously saved expenses.
* **File handling** to read and write expense data.

When the program starts, it loads the saved expenses. Adding or deleting an expense updates the stored data, allowing those changes to remain available after the application closes.

**Important:** Keep `expense.txt` in the project folder. If the file contains existing expense records, preserve them when updating or moving the project.

##  Concepts Practised

Building this project helped me practise and combine the following Python concepts:

* Variables and data types
* Lists and dictionaries
* Functions and function calls
* `while` and `for` loops
* Conditional statements (`if`, `elif`, and `else`)
* String methods such as `.strip()`, `.lower()`, and `.isdigit()`
* List operations such as `.append()` and `.remove()`
* Input validation
* Exception handling using `try/except`
* File handling using `open()`
* JSON serialization and deserialization
* Breaking a problem into smaller, manageable operations

##  Possible Future Improvements

Ideas for future versions include:

* **Edit Expenses:** Update an existing expense without deleting and re-adding it.
* **Date Tracking:** Record when each expense occurred.
* **Monthly Reports:** Calculate spending over a selected period.
* **Budget Tracking:** Compare total spending with a user-defined budget.
* **Improved Expense Selection:** Assign each expense a unique ID to make editing and deleting records unambiguous.
* **Automated Tests:** Add tests to check calculations, validation, and data storage.
* **Graphical Interface:** Replace the command-line menu with a desktop or web interface.

These are potential enhancements, not features currently implemented.

##  Author

**Adarsh**

GitHub: [@hey-its-adu](https://github.com/hey-its-adu)

##  Project Status

**Completed — Version 1**

The core expense-management features are implemented, including adding, viewing, calculating, deleting, and saving expenses. Future improvements may extend the application's functionality.

---

*Built with Python as part of my journey toward becoming a software developer.*

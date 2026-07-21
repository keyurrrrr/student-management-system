import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    branch TEXT,
    year INTEGER,
    email TEXT,
    phone TEXT
)
""")
con.commit()

def add_student():
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = int(input("Enter Year: "))
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    cur.execute(
        "INSERT INTO students(name,branch,year,email,phone) VALUES(?,?,?,?,?)",
        (name, branch, year, email, phone)
    )

    con.commit()
    print("\n✅ Student Added Successfully!")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

con.close()

from connect import connect
import csv

# -------- INSERT --------
def insert():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Added!")

# -------- SHOW --------
def show():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()

# -------- SEARCH --------
def search():
    keyword = input("Search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s OR phone ILIKE %s",
        (f"%{keyword}%", f"%{keyword}%")
    )

    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()

# -------- UPDATE --------
def update():
    name = input("Enter name to update: ")
    new_phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Updated!")

# -------- DELETE --------
def delete():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")

# -------- CSV --------
def insert_csv():
    with open("contacts.csv", "r") as f:
        reader = csv.DictReader(f)

        conn = connect()
        cur = conn.cursor()

        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )

        conn.commit()
        cur.close()
        conn.close()

    print("CSV imported!")

# -------- MENU --------
while True:
    print("\n1.Add")
    print("2.Show")
    print("3.Search")
    print("4.Update")
    print("5.Delete")
    print("6.Import CSV")
    print("7.Exit")

    c = input(">> ")

    if c == "1":
        insert()
    elif c == "2":
        show()
    elif c == "3":
        search()
    elif c == "4":
        update()
    elif c == "5":
        delete()
    elif c == "6":
        insert_csv()
    elif c == "7":
        break
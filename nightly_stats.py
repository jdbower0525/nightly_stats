import psycopg2
import datetime
from tabulate import tabulate
import os

conn = psycopg2.connect("dbname=Bower user=Bower host=/tmp/")
cur = conn.cursor()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add_day():
    try:
        new_year = int(input("What year is it (yyyy)? "))
        new_month = int(input("What month is it (mm)? "))
        new_date = int(input("What is the date (dd)? "))
        new_day = input("What day of the week is it? ").capitalize()
        new_sales = int(input("What were the sales for that day? "))
        new_lunch = int(input("What were the lunch sales of that day? "))
        new_closing_manager = input("Who is the closing manager this day? "
                                    ).capitalize()
        new_lbw = float(input("What was your LBW on that day? "))
        new_ta = input("What were the takeaway sales of this day? ")
        new_grill = input("Who was on grill? ").capitalize()
        new_prime = float(input("What was their prime rib accuracy? "))
        new_hw = input("Who was the HW? ").capitalize()
        new_drop = float(input("What was the drop variance? "))
        new_row = """INSERT INTO nightly_stats (target_date, day, sales,
                    closing_manager, lunch_sales, lbw, takeaway,
                    grill, prime_acc, hw, drop)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cur.execute(new_row, (datetime.date(new_year, new_month,
                              new_date), new_day, new_sales,
                              new_closing_manager, new_lunch, new_lbw, new_ta,
                              new_grill, new_prime, new_hw, new_drop))
        conn.commit()
    except:
        print("That is an invalid input.")
        add_day()
    redirect = input("Would you like to add another day"
                     "(a) or return to the main menu (m)? ")
    if redirect == 'a':
        add_day()
    else:
        initial_input()


def search_database():
    clear()
    first_search = input("Would you like to search (s) for a specific"
                         "rows or see a ranking (r)? ")
    if first_search == 'r':
        ranking()
    else:
        search_row()


def ranking():
    clear()
    rank_input = input("""
What would you like a ranking on?
1) Sales
2) Lunch Sales
3) LBW %
4) Takeaway Sales
5) Prime Accuracy
6) Drop variance

>>> """)
    if rank_input == '1':
        search = 'sales'
    elif rank_input == '2':
        search = 'lunch_sales'
    elif rank_input == '3':
        search = 'lbw'
    elif rank_input == '4':
        search = 'takeaway'
    elif rank_input == '5':
        search = 'prime_acc'
    elif rank_input == '6':
        search = 'drop'
    sql = "SELECT * from nightly_stats order by " + search + " desc"
    cur.execute(sql, (search,))
    print(tabulate(cur, tablefmt="fancy_grid",
                   headers=['Date', 'Day', 'Sales', 'Manager', 'Lunch Sales',
                            'LBW %', 'Takeaway Sales', 'Grill',
                            'Prime Accuracy', 'HW', 'Drop +/-']))
    redirect = input("Would you like to see another ranking (r)"
                     "or return to the main menu (m)? ")
    if redirect == 'r':
        ranking()
    else:
        clear()
        initial_input()


def search_row():
    try:
        search_input = input("""
What column would you like to search for?
1) Date
2) Day of the week
3) Closing Manager
4) Grill
5) HW

>>> """)
        if search_input == '1':
            row_search = input("Which date would you"
                               "like to search form (YYYY-MM-DD)? "
                               ).capitalize()
            search = 'target_date'
        elif search_input == '2':
            row_search = input("Which day of the week would"
                               "you like to search for? "
                               ).capitalize()
            search = 'day'
        elif search_input == '3':
            row_search = input("Which of the closing managers"
                               "would you like to search for? "
                               ).capitalize()
            search = 'closing_manager'
        elif search_input == '4':
            row_search = input("What grill worker would"
                               "you like to search for? "
                               ).capitalize()
            search = 'grill'
        elif search_input == '5':
            row_search = input("Which HW would you like"
                               "to search for? "
                               ).capitalize()
            search = 'hw'
        sql = "SELECT * from nightly_stats WHERE " + search + " = %s"
        cur.execute(sql, (row_search,))
    except:
        print("That is an invalid input.")
        search_row()
    clear()
    print(tabulate(cur, tablefmt="fancy_grid",
                   headers=['Date', 'Day', 'Sales', 'Manager', 'Lunch Sales',
                            'LBW %', 'Takeaway Sales', 'Grill',
                            'Prime Accuracy', 'HW', 'Drop +/-']))
    redirect = input("Would you like to search for something else"
                     "(s) or return to the main menu (m)? ")
    if redirect == 's':
        search_row()
    else:
        initial_input()


def view_database():
    clear()
    sql = ("SELECT * FROM nightly_stats")
    cur.execute(sql)
    print(tabulate(cur, tablefmt="fancy_grid",
                   headers=['Date', 'Day', 'Sales', 'Manager', 'Lunch Sales',
                            'LBW %', 'Takeaway Sales', 'Grill',
                            'Prime Accuracy', 'HW', 'Drop +/-']))
    initial_input()


def delete_row():
    clear()
    sql = ("SELECT * FROM nightly_stats")
    cur.execute(sql)
    print(tabulate(cur, tablefmt="fancy_grid",
                   headers=['Date', 'Day', 'Sales', 'Manager', 'Lunch Sales',
                            'LBW %', 'Takeaway Sales', 'Grill',
                            'Prime Accuracy', 'HW', 'Drop +/-']))
    del_input = input("Which row (by ID) would you like to delete? ")
    sql = "DELETE FROM nightly_stats WHERE id = %s"
    cur.execute(sql, (del_input,))
    redirect = input("Would you like to delete another day (d)"
                     "or return to the main menu (m)? ")
    if redirect == 'd':
        clear()
        delete_row()
    else:
        clear()
        initial_input()


def initial_input():
    print("""
Welcome to the Nightly Statistics Database
    """)
    first_input = input("""
What would you like to do?
1) View the Database.
2) Search the Databse.
3) Add to the Database.
4) Delete a day from the Database.
5) Exit

>>> """)
    if first_input == '1':
        view_database()
    elif first_input == '2':
        search_database()
    elif first_input == '3':
        add_day()
    elif first_input == '4':
        delete_row()
    else:
        conn.commit()
        exit()


if __name__ == "__main__":
    clear()
    initial_input()

cur.close()
conn.close()

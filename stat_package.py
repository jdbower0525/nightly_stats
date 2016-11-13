import psycopg2
import datetime

# Connect to an existing database
conn = psycopg2.connect("dbname=Bower user=Bower host=/tmp/")
cur = conn.cursor()


def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS nightly_stats (
    "id"  SERIAL ,
    "target_date" DATE NOT NULL,
    "day" CHAR(10) NOT NULL ,
    "sales" INTEGER NOT NULL ,
    "closing_manager" CHAR(10) NOT NULL,
    "lunch_sales" INTEGER NOT NULL,
    "lbw" FLOAT NOT NULL,
    "takeaway" INTEGER NOT NULL,
    "grill" CHAR(15) NOT NULL,
    "prime_acc" FLOAT NOT NULL,
    "hw" CHAR(15) NOT NULL,
    "drop" FLOAT NOT NULL,
    PRIMARY KEY ("id"));""")


def generate_data():
    dump = """INSERT INTO nightly_stats (target_date, day, sales,
    closing_manager, lunch_sales, lbw, takeaway, grill, prime_acc,
    hw, drop) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(dump, (datetime.date(2016, 11, 1),
                'Tuesday', 8150, 'Nicole', 2000, 12.5, 3000,
                       'Gaspar', 70.5, 'Steph', 3.05))
    cur.execute(dump, (datetime.date(2016, 11, 2),
                'Wednesday', 6000, 'Ryan', 1500, 11.5, 2400,
                       'Jaime', 81.2, 'Sean', -3.2))
    cur.execute(dump, (datetime.date(2016, 11, 3),
                'Thursday', 9000, 'Jenn', 1250, 13, 2550,
                       'Gaspar', 71.8, 'Shae', 5.03))
    cur.execute(dump, (datetime.date(2016, 11, 4),
                'Friday', 18500, 'Jenn', 4000, 12, 4000,
                       'Rojas', 60.2, 'Shae', 4.32))
    cur.execute(dump, (datetime.date(2016, 11, 5),
                'Saturday', 19500, 'Nici', 3000, 10.5, 2300,
                       'Gaspar', 75.3, 'Steph', 2.10))
    cur.execute(dump, (datetime.date(2016, 11, 6),
                'Sunday', 16150, 'Nicole', 3000, 9.4, 3000,
                       'Jaime', 70.5, 'Sean', -4.30))
    cur.execute(dump, (datetime.date(2016, 11, 7),
                'Monday', 7750, 'Anthony', 1500, 12.3, 2333,
                       'Gaspar', 75.76, 'Steph', 3.30))
    cur.execute(dump, (datetime.date(2016, 11, 8),
                'Tuesday', 6750, 'Anthony', 3500, 10.5, 2000,
                       'Rojas', 50.34, 'Sean', -5.34))
    cur.execute(dump, (datetime.date(2016, 11, 9),
                'Wednesday', 9900, 'Jenn', 2200, 9.5, 1750,
                       'Gaspar', 75.45, 'Shae', 2.33))
    cur.execute(dump, (datetime.date(2016, 11, 10),
                'Thursday', 8549, 'Jenn', 3500, 11.4, 2400,
                       'Jaime', 77.2, 'Steph', -3.10))
    cur.execute(dump, (datetime.date(2016, 11, 11),
                'Friday', 18090, 'Ryan', 5000, 12.3, 5000,
                       'Gaspar', 80.45, 'Steph', 1.23))
    cur.execute(dump, (datetime.date(2016, 11, 12),
                'Saturday', 9000, 'Nicole', 2300, 13.4, 3000,
                       'Jaime', 75.65, 'Sean', 3.43))
    cur.execute(dump, (datetime.date(2016, 11, 13),
                'Sunday', 16440, 'Nici', 3444, 9.81, 2334,
                       'Rojas', 61.43, 'Shae', 0.34))
    cur.execute(dump, (datetime.date(2016, 11, 14),
                'Monday', 8882, 'Nici', 2111, 13.4, 2336,
                       'Gaspar', 75.43, 'Sean', -5.40))
    cur.execute(dump, (datetime.date(2016, 11, 15),
                'Tuesday', 2345, 'Anthony', 1400, 12.1, 3000,
                       'Jaime', 73.21, 'Sean', -3.43))
    cur.execute(dump, (datetime.date(2016, 11, 16),
                'Wednesday', 8756, 'Anthony', 4000, 13.43, 2000,
                       'Jose', 34.21, 'Steph', 0.32))
    cur.execute(dump, (datetime.date(2016, 11, 17),
                'Thursday', 8899, 'Nici', 5000, 12.2, 4000,
                       'Gaspar', 75.21, 'Sean', -4.54))
    cur.execute(dump, (datetime.date(2016, 11, 18),
                'Friday', 17699, 'Nici', 2100, 9.54, 1200,
                       'Rojas', 54.21, 'Shae', 50.32))
    cur.execute(dump, (datetime.date(2016, 11, 19),
                'Saturday', 21540, 'Jenn', 3400, 13.4, 2000,
                       'Gaspar', 75.65, 'Steph', 3.23))
    cur.execute(dump, (datetime.date(2016, 11, 20),
                'Sunday', 16504, 'Nicole', 3444, 8.4, 5400,
                       'Jose', 66.23, 'Sean', -15.87))


def main():
    create_table()
    generate_data()
    conn.commit()

if __name__ == "__main__":
    main()

cur.close()
conn.close()

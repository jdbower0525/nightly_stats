## README ##

This database program is meant to be used nightly to organize the closing
information that a restaurant manager has to record every night.  The purpose
of this is to make this information more accessible, easier to read, and
be able to search for certain data easier than a handwritten spreadsheet.

To run this program the first time, run stat_package.py to create the table and
insert an initial set of information into it.  After running stat_package.py,
the main database can be accessed by running nightly_stats.py.

When running nightly_stats.py, you will have the option of viewing the current
database in the order that information was placed into it.  You will also
be able to add rows to the database, where each row is the information for a
given day at the restaurant.  In addition to that, you will be able to search
for who worked on specific days, or be able to arrange the database by the
values contained in each row.  Finally you also have the option to delete a row
out of the database.  After each one of those options, you will be able to
choose to continue manipulating the database in that way, or exit to the main
menu.

The last option is to exit the database.

This assignment was designed to practice SQL and Python integration, and will
likely be built upon once I am able to make it into a more accessible app.

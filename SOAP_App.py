import sqlite3

conn = sqlite3.connect("SOAP.db")
c = conn.cursor()

# insert a record into the tables
gsa_offices_insert_query = "INSERT INTO gsa_offices VALUES('testName', 'theCity', 2000.25);"
agencies_insert_query = "INSERT INTO agencies VALUES('12345', 'testAgency', 'testAddress', 'testCity', 4435551234);"
rental_agreements_insert_query = "INSERT INTO rental_agreements VALUES('67890', 'testName', 1000000, 2024, 8, 7);"
ra_agencies_insert_query = "INSERT INTO ra_agencies VALUES('67890', '12345');"

# select records from the tables
rental_agreements_select_query = 	"SELECT gsa_offices.office_name AS GSA_office_name, \
										agency_name, \
										agencies.city AS Agency_city, \
										phone_number AS Agency_phone \
									FROM rental_agreements, ra_agencies, agencies, gsa_offices \
									WHERE rental_agreements.ra_id == ra_agencies.ra_id \
										AND agencies.agency_id == ra_agencies.agency_id \
										AND rental_agreements.office_name == gsa_offices.office_name;"

# delete a record from the tables
gsa_offices_delete_query = "DELETE from gsa_offices where office_name = 'testName';"

insert_statements = [gsa_offices_insert_query, agencies_insert_query, rental_agreements_insert_query, ra_agencies_insert_query]
print("\nTesting insert statements:")
for stmnt in insert_statements:
	print(stmnt)
	try:
		c.execute(stmnt)
		rows = c.fetchall()
	except sqlite3.Error as e:
		print("An error occurred:", e.args[0])
	for row in rows:
		print(row)

print("Testing select statement:")
print(rental_agreements_select_query)
try:
	c.execute(rental_agreements_select_query)
	rows = c.fetchall()
except sqlite3.Error as e:
	print("An error occurred:", e.args[0])
for row in rows:
	print(row)

print("Testing delete statement:")
print(gsa_offices_delete_query)
try:
	c.execute(gsa_offices_delete_query)
	rows = c.fetchall()
except sqlite3.Error as e:
	print("An error occurred:", e.args[0])
for row in rows:
	print(row)


myStmt = "select * from gsa_offices"
while myStmt != "quit":
	myStmt = input("Enter SQL Statement :")
	if myStmt != "quit":
		try:
			c.execute(myStmt)
			rows = c.fetchall()
		except sqlite3.Error as e:
			print("An error occurred:", e.args[0])
		for row in rows:
			print(row)
		rows = "go"
		myWait = input("Press enter to continue :")
	else:
		conn.commit()
		conn.close()

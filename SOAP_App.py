import sqlite3

def execute_query(cursor, query):
	try:
		print(query)
		cursor.execute(query)
		responses = cursor.fetchall()
	except sqlite3.Error as e:
		print("An error occurred:\n", e.args[0])
	if "SELECT" in query.upper():
		# get the maximum width of each column in the response
		column_widths = [max(len(str(val)) for val in col) for col in zip(*responses)]

		# Print the response headers and rows, with the columns separated by '|'
		print()
		for i, col in enumerate(cursor.description):
			column_widths[i] = max(column_widths[i], len(col[0]))
			print(f"| {col[0]:<{column_widths[i]}} ", end="")
		print(f"|\n-{'-' * (sum(column_widths) + len(column_widths) * 3)}")
		for row in responses:
			for i, val in enumerate(row):
				print(f"| {val:<{column_widths[i]}} ", end="")
			print("|")
		print()

def test_insert(cursor):
	# insert a record into the tables
	insert_statements = []
	insert_statements.append("INSERT INTO gsa_offices VALUES('GSA Baltimore', 'Baltimore', 2000.25);")
	insert_statements.append("INSERT INTO gsa_offices VALUES('testName', 'theCity', 89657.09);")
	insert_statements.append("INSERT INTO agencies VALUES('12345', 'MD Supreme Courts', '100 Sup Court Dr.', 'Baltimore', 4435551234);")
	insert_statements.append("INSERT INTO agencies VALUES('39945', 'MD Marshalls', '100 Sup Court Dr.', 'Baltimore', 4435555678);")
	insert_statements.append("INSERT INTO rental_agreements VALUES('67890', 'GSA Baltimore', 1000000, 2025, 8, 7);")
	insert_statements.append("INSERT INTO ra_agencies VALUES('67890', '12345');")
	insert_statements.append("INSERT INTO ra_agencies VALUES('67890', '39945');")
	print("\nTesting insert statements:")
	for stmnt in insert_statements:
		execute_query(cursor, stmnt)

def test_select(cursor):
	# select records from the tables
	rental_agreements_select_query = 	"SELECT gsa_offices.office_name AS GSA_office_name, \
											agency_name, \
											agencies.city AS Agency_city, \
											phone_number AS Agency_phone \
										FROM rental_agreements, ra_agencies, agencies, gsa_offices \
										WHERE rental_agreements.ra_id == ra_agencies.ra_id \
											AND agencies.agency_id == ra_agencies.agency_id \
											AND rental_agreements.office_name == gsa_offices.office_name;"
	print("Testing select statement:")
	execute_query(cursor, rental_agreements_select_query)

def test_delete(cursor):
	# delete a record from the tables
	gsa_offices_delete_query = "DELETE from gsa_offices WHERE office_name = 'testName';"
	print("Testing delete statement:")
	execute_query(cursor, gsa_offices_delete_query)

try:
	soap_cursor = sqlite3.connect("SOAP.db").cursor()
except sqlite3.Error as e:
	print("An error occurred while connecting to the SOAP database:", e.args[0])

test_insert(soap_cursor)
test_select(soap_cursor)
test_delete(soap_cursor)

print("\n\nEnter 'quit' to finalize the database changes and exit the program.")
user_query = "select * from gsa_offices"
while user_query != "quit":
	user_query = input("Enter SQL Statement: ")
	if user_query != "quit":
		execute_query(soap_cursor, user_query)
	else:
		soap_cursor.connection.commit()
		soap_cursor.connection.close()

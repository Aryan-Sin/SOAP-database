import sqlite3

def execute_query(cursor, query):
	try:
		print(query)
		cursor.execute(query)
		responses = cursor.fetchall()
	except sqlite3.Error as e:
		print("An error occurred:\n", e.args[0])
	if "SELECT" in query.upper():
		# maximum width of each column in the response
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

try:
	soap_cursor = sqlite3.connect("SOAP.db").cursor()
except sqlite3.Error as e:
	print("An error occurred while connecting to the SOAP database:", e.args[0])

print("\n\nEnter 'quit' to finalize the database changes and exit the program.")
user_query = "select * from gsa_offices"
while user_query != "quit":
	user_query = input("Enter SQL Statement: ")
	if user_query != "quit":
		execute_query(soap_cursor, user_query)
	else:
		soap_cursor.connection.commit()
		soap_cursor.connection.close()

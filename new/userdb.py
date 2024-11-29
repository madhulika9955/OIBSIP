import sqlite3

def display_users():
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Query to select all data from the 'users' table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Display the data
    if rows:
        print("ID | Name         | Email                | Password")
        print("---------------------------------------------------")
        for row in rows:
            print(f"{row[0]:<3} | {row[1]:<12} | {row[2]:<20} | {row[3]}")
    else:
        print("No users found in the database.")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    display_users()

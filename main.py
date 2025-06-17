# main.py
from db_connection import connection_to_database
from library import library_book_info, add_library_book, remove_library_book
from issue_return import issued_book_info, returned_books_info, issue_book, return_book

def main():
    conn, cursor = connection_to_database()
    if not conn or not cursor:
        print("Failed to connect to database. Exiting...")
        return

    while True:
        print("\n--- Library Management System ---")
        print("1. View Library Book")
        print("2. View Issued Book")
        print("3. View Returned Book")
        print("4. Add Library Book")
        print("5. Remove Library Book")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        match choice:
            case 1:
                result = library_book_info(cursor)
                print("\nResult:")
                if result:
                    if isinstance(result, list):
                        for record in result:
                            print(record)
                    else:
                        print(result)
                else:
                    print("No records found.")

            case 2:
                result = issued_book_info(cursor)
                print("\nResult:")
                if result:
                    if isinstance(result, list):
                        for record in result:
                            print(record)
                    else:
                        print(result)
                else:
                    print("No records found.")
            case 3:
                result = returned_books_info(cursor)
                print("\nResult:")
                if result:
                    if isinstance(result, list):
                        for record in result:
                            print(record)
                    else:
                        print(result)
                else:
                    print("No records found.")

            case 4:
                add_library_book(cursor, conn)
            case 5:
                remove_library_book(cursor, conn)
            case 6:
                issue_book(cursor, conn)
            case 7:
                return_book(cursor, conn)
            case 8:
                print("Exiting the Library Management System. Goodbye!")
                break

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

# issued.py
from datetime import datetime

def issued_book_info(cursor):
    print("1. View all records")
    print("2. Search by issue id")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        cursor.execute("SELECT * FROM BOOK_ISSUED")
        return cursor.fetchall()
    elif choice == 2:
        issue_id = int(input("Enter the issue id: "))
        cursor.execute("SELECT * FROM BOOK_ISSUED WHERE id = %s", (issue_id,))
        return cursor.fetchone()
    
def returned_books_info(cursor):
    print("1. View all records")
    print("2. Search by issue id")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        cursor.execute("SELECT * FROM RETURNED_BOOKS")
        return cursor.fetchall()
    elif choice == 2:
        issue_id = int(input("Enter the issue id: "))
        cursor.execute("SELECT * FROM RETURNED_BOOKS WHERE id = %s", (issue_id,))
        return cursor.fetchone() 
   
def issue_book(cursor, conn):
    issue_id = int(input("Enter Issue Id: "))
    user_id = int(input("Enter User Id: "))
    book_id = int(input("Enter Book Id: "))
    book_title = input("Enter book title: ")
    number_of_copies_issued = int(input("Enter number of copies issued: "))

    cursor.execute("SELECT * FROM LIBRARY_BOOKS WHERE BOOK_ID = %s", (book_id,))
    result = cursor.fetchone()
    if result is None:
        print("Book not found")
        return
    available = result[3]
    if number_of_copies_issued > available:
        print("Not enough copies available")
        return

    date = input("Enter Date of issuance (YYYY-MM-DD): ")
    issue_date = datetime.strptime(date, "%Y-%m-%d").date()
    sql = "INSERT INTO BOOK_ISSUED (ISSUE_ID, USER_ID, BOOK_ID, BOOK_TITLE, NUMBER_OF_COPIES_ISSUED, ISSUE_DATE) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (issue_id, user_id, book_id, book_title, number_of_copies_issued, issue_date)
    cursor.execute(sql, val)
    # UPDATING THE LIBRARY_BOOKS
    update_sql = "UPDATE LIBRARY_BOOKS SET NUMBER_OF_COPIES_AVAILABLE = NUMBER_OF_COPIES_AVAILABLE - %s WHERE BOOK_ID = %s"
    cursor.execute(update_sql, (number_of_copies_issued, book_id))
    conn.commit()
    print("Book issued and inventory updated successfully.")

def return_book(cursor, conn):
    issue_id = int(input("Enter issue id: "))
    cursor.execute("SELECT * FROM BOOK_ISSUED WHERE ISSUE_ID = %s", (issue_id,))
    result = cursor.fetchone()
    if result is None:
        print("Issue ID not found.")
        return

    user_id, book_id, issue_date = result[1], result[2], result[5]
    number_of_books_returned = int(input("Enter number of books returned: "))
    date = input("Enter Date of return (YYYY-MM-DD): ")
    return_date = datetime.strptime(date, "%Y-%m-%d").date()

    cursor.execute("UPDATE BOOK_ISSUED SET RETURN_DATE = %s WHERE ISSUE_ID = %s", (return_date, issue_id))

    delta = (return_date - issue_date).days
    fine = max(0, (delta - 30) * 1 * number_of_books_returned)
    print("Your fine is:", fine)

    # Updating the available copies from Library_Books
    # QUERY
    update_library_books_available_copies_query = "UPDATE LIBRARY_BOOKS SET NUMBER_OF_COPIES_AVAILABLE = NUMBER_OF_COPIES_AVAILABLE + %s WHERE BOOK_ID = %s"
    # VALUE
    update_library_books_available_copies_value = (number_of_books_returned, book_id)
    cursor.execute(update_library_books_available_copies_query, update_library_books_available_copies_value)

    # Updating the BOOK_ISSUED TABLE
    # QUERY
    update_book_issued_table_query = "UPDATE BOOK_ISSUED SET NUMBER_OF_COPIES_ISSUED = NUMBER_OF_COPIES_ISSUED - %s WHERE ISSUE_ID = %s"
    # VALUE
    update_book_issued_table_value = (number_of_books_returned, issue_id)
    cursor.execute(update_book_issued_table_query, update_book_issued_table_value)

    # Updating the FINE column of BOOK_ISSUED
    # QUERY
    updated_fine_query = """ UPDATE BOOK_ISSUED SET FINE = CASE
    WHEN NUMBER_OF_COPIES_ISSUED>0 AND DATEDIFF(RETURN_DATE, ISSUE_DATE)>30
    THEN DATEDIFF(RETURN_DATE, ISSUE_DATE) * 1 * NUMBER_OF_COPIES_ISSUED
    ELSE 0
    END
    WHERE ISSUE_ID = %s"""
    # VALUE
    updated_fine_value = (issue_id,)
    cursor.execute(updated_fine_query, updated_fine_value)

    # UPDATING THE RETURNED_BOOKS RECORD
    cursor.execute("SELECT ISSUE_ID FROM RETURNED_BOOKS WHERE ISSUE_ID = %s", (issue_id,))
    res = cursor.fetchone()
    if res is None:
        query = "INSERT INTO RETURNED_BOOKS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (issue_id, user_id, book_id, result[3], number_of_books_returned, issue_date, return_date, fine)
        cursor.execute(query, values)
    else:
        query = "UPDATE RETURNED_BOOKS SET RETURN_DATE = %s, NUMBER_OF_COPIES_RETURNED = NUMBER_OF_COPIES_RETURNED + %s, FINE = FINE + %s WHERE ISSUE_ID = %s"
        values = (return_date, number_of_books_returned, fine, issue_id)
        cursor.execute(query, values)

    sql_remove_book = "DELETE FROM BOOK_ISSUED WHERE ISSUE_ID = %s AND NUMBER_OF_COPIES_ISSUED = %s"
    sql_remove_book_value = (issue_id, 0)
    cursor.execute(sql_remove_book, sql_remove_book_value)

    conn.commit()

    print("Books returned and inventory updated successfully.")


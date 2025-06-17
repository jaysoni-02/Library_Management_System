# library.py
def library_book_info(cursor):
    print("1. View all records")
    print("2. Search by book id")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        cursor.execute("SELECT * FROM LIBRARY_BOOKS")
        return cursor.fetchall()
    elif choice == 2:
        book_id = int(input("Enter the book id: "))
        cursor.execute("SELECT * FROM LIBRARY_BOOKS WHERE id = %s", (book_id,))
        return cursor.fetchone()
def add_library_book(cursor, conn):
    book_id = int(input("Book Id: "))
    book_title = input("Book Title: ")
    book_author = input("Book Author: ")
    number_of_copies_available = int(input("Number of Copies Available: "))
    sql = "INSERT INTO LIBRARY_BOOKS (BOOK_ID, BOOK_TITLE, BOOK_AUTHOR, NUMBER_OF_COPIES_AVAILABLE) VALUES (%s, %s, %s, %s)"
    val = (book_id, book_title, book_author, number_of_copies_available)
    cursor.execute(sql, val)
    conn.commit()
    ans = input("Are there any more books to add? (y/n) ")
    if ans.lower() == 'y':
        add_library_book(cursor, conn)
    else:
        print("Books added successfully.")

def remove_library_book(cursor, conn):
    book_id = int(input("Enter the book id of the book you want to remove: "))
    sql = "DELETE FROM LIBRARY_BOOKS WHERE BOOK_ID = %s"
    cursor.execute(sql, (book_id,))
    conn.commit()
    ans = input("Are there any more books to remove? (y/n) ")
    if ans.lower() == 'y':
        remove_library_book(cursor, conn)
    else:
        print("Book removed successfully.")
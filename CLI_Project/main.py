from library_manager import *

def main():
    connect()  # Initialize database

    while True:
        print("\n=== 📚 DIGITAL LIBRARY MENU ===")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Add User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(title, author)
            print("✅ Book added successfully!")

        elif choice == '2':
            books = view_books()
            print("\nID | Title | Author | Available")
            for b in books:
                status = "✅ Yes" if b[3] == 1 else "❌ No"
                print(f"{b[0]} | {b[1]} | {b[2]} | {status}")

        elif choice == '3':
            keyword = input("Enter title or author keyword: ")
            results = search_books(keyword)
            for r in results:
                print(f"{r[1]} by {r[2]} — {'Available' if r[3] else 'Borrowed'}")

        elif choice == '4':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(name, email)
            print("✅ User added!")

        elif choice == '5':
            email = input("Enter your email: ")
            book_id = int(input("Enter book ID to borrow: "))
            borrow_book(email, book_id)

        elif choice == '6':
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)

        elif choice == '7':
            print("👋 Exiting the system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

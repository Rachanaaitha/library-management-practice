books = []

while True:
    print("\n--- Library Management (Level 1) ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter book id: ")
        book_name = input("Enter book name: ")
        books.append([book_id, book_name])
        print("✅ Book added!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nBooks List:")
            for b in books:
                print("ID:", b[0], "| Name:", b[1])

    elif choice == "3":
        print("Bye 👋")
        break

    else:
        print("❌ Invalid choice")

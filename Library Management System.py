from datetime import datetime, timedelta

# Class for Library Items (Books, Magazines, DVDs)
class LibraryItem:
    def __init__(self, title, author, category, item_type):
        self.title = title
        self.author = author
        self.category = category
        self.item_type = item_type
        self.is_checked_out = False
        self.due_date = None
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.due_date = datetime.now() + timedelta(days=14)  # 2 weeks checkout period
            print(f"{self.title} has been checked out. Due date: {self.due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            self.due_date = None
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")
    
    def calculate_fine(self):
        if self.is_checked_out and datetime.now() > self.due_date:
            overdue_days = (datetime.now() - self.due_date).days
            fine = overdue_days * 1  # Assume $1 per overdue day
            return fine
        return 0

    def display_info(self):
        status = "Available" if not self.is_checked_out else f"Checked out (Due: {self.due_date.strftime('%Y-%m-%d')})"
        print(f"Title: {self.title}, Author: {self.author}, Category: {self.category}, Type: {self.item_type}, Status: {status}")

# Library Management System
class Library:
    def __init__(self):
        self.items = []

    def add_item(self, title, author, category, item_type):
        new_item = LibraryItem(title, author, category, item_type)
        self.items.append(new_item)
        print(f"{item_type} '{title}' added to the library.")

    def search_items(self, search_term, search_type="title"):
        results = []
        for item in self.items:
            if search_type == "title" and search_term.lower() in item.title.lower():
                results.append(item)
            elif search_type == "author" and search_term.lower() in item.author.lower():
                results.append(item)
            elif search_type == "category" and search_term.lower() in item.category.lower():
                results.append(item)
        
        if results:
            for item in results:
                item.display_info()
        else:
            print("No items found matching your search.")

    def check_out_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.check_out()
                return
        print(f"Item titled '{title}' not found in the library.")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                fine = item.calculate_fine()
                item.return_item()
                if fine > 0:
                    print(f"Overdue fine: ${fine:.2f}")
                return
        print(f"Item titled '{title}' not found in the library.")

# Main Program
def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add New Item")
        print("2. Search Item")
        print("3. Check Out Item")
        print("4. Return Item")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            category = input("Enter the category: ")
            item_type = input("Enter the type (Book, Magazine, DVD): ")
            library.add_item(title, author, category, item_type)

        elif choice == '2':
            search_term = input("Enter search term: ")
            search_type = input("Search by title, author, or category? ").lower()
            library.search_items(search_term, search_type)

        elif choice == '3':
            title = input("Enter the title of the item to check out: ")
            library.check_out_item(title)

        elif choice == '4':
            title = input("Enter the title of the item to return: ")
            library.return_item(title)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

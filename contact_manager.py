"""Contact Manager

This is my fixed version of buggy_contacts.py. It doesn't crash anymore
when you type something weird or look up someone who isn't saved.
"""

contacts = {}


class DuplicateContactError(Exception):
    """Gets raised when you try to add a name that's already saved."""


def add_contact(name, phone):
    """Adds a new contact to the list.

    If the name is already saved it raises DuplicateContactError
    so the old number doesn't get replaced by accident.
    """
    if name in contacts:
        raise DuplicateContactError(f"{name} is already in your contacts.")
    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Looks up a contact and gives back their number or None if they're not there."""
    try:
        phone = contacts[name]
    except KeyError:
        # the name isn't in the dictionary so we just let the user know
        print("Contact not found.")
        return None
    print(f"{name}: {phone}")
    return phone


def delete_contact(name):
    """Deletes a contact. Gives back True if it worked and False if they weren't saved."""
    try:
        del contacts[name]
    except KeyError:
        # deleting a name that isn't there causes a KeyError so we catch it here
        print("Contact not found.")
        return False
    print(f"Deleted {name}.")
    return True


def get_menu_choice():
    """Keeps asking for a menu option until the user types an actual number."""
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            # int() breaks on stuff like "abc" so we ask again instead of crashing
            print("That's not a number. Try a number from 1 to 4.")


def main():
    """Runs the menu so the user can add or find or delete contacts."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = get_menu_choice()

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            try:
                add_contact(name, phone)
            except DuplicateContactError as error:
                # add_contact raises this and main is where we show the message
                print(f"Oops! {error}")
        elif choice == 2:
            name = input("Enter name to find: ").strip()
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            delete_contact(name)
        elif choice == 4:
            print("Bye!")
            break
        else:
            print("That's not an option. Pick a number from 1 to 4.")


if __name__ == "__main__":
    main()
# Contact Manager

A simple contact list you run in the terminal. The starter code crashed a lot so I fixed it and added tests.

## Files

- buggy_contacts.py is the original code
- contact_manager.py is my fixed version
- test_contact_manager.py has the tests

## What I fixed

- Typing letters in the menu doesn't crash it anymore
- Looking up or deleting someone who isn't saved just says "Contact not found."
- Adding the same name twice shows an error instead of replacing the number

## How to run it

Run the program:

```
python contact_manager.py
```

Run the tests:

```
python -m unittest test_contact_manager.py
```

## Testing

I used unittest and wrote the tests first then fixed the code until they passed. The tests check adding and finding and deleting contacts plus the error cases.

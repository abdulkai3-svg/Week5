"""Tests for contact_manager.py

Every test starts with an empty contact list so they don't mess with
each other. I also turned off the print messages so the test results
are easier to read.
"""

import unittest
from unittest.mock import patch

import contact_manager
from contact_manager import DuplicateContactError


class TestContactManager(unittest.TestCase):
    """Tests for adding and finding and deleting contacts."""

    def setUp(self):
        """Clears the contacts and hides print output before each test."""
        contact_manager.contacts.clear()
        patcher = patch("builtins.print")
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_add_new_contact(self):
        """Adding a contact should actually save it."""
        contact_manager.add_contact("Amina", "612-555-1234")
        self.assertEqual(contact_manager.contacts["Amina"], "612-555-1234")

    def test_find_existing_contact(self):
        """Finding a saved contact should give back their number."""
        contact_manager.add_contact("Amina", "612-555-1234")
        self.assertEqual(contact_manager.find_contact("Amina"), "612-555-1234")

    def test_find_nonexistent_contact(self):
        """Finding someone who isn't saved should give back None and not crash."""
        self.assertIsNone(contact_manager.find_contact("Nobody"))

    def test_delete_existing_contact(self):
        """Deleting a saved contact should remove them."""
        contact_manager.add_contact("Amina", "612-555-1234")
        self.assertTrue(contact_manager.delete_contact("Amina"))
        self.assertNotIn("Amina", contact_manager.contacts)

    def test_delete_nonexistent_contact(self):
        """Deleting someone who isn't saved should give back False and not crash."""
        self.assertFalse(contact_manager.delete_contact("Nobody"))

    def test_add_duplicate_contact(self):
        """Adding the same name twice should raise DuplicateContactError."""
        contact_manager.add_contact("Amina", "612-555-1234")
        with self.assertRaises(DuplicateContactError):
            contact_manager.add_contact("Amina", "651-555-9999")
        # making sure the first number didn't get replaced
        self.assertEqual(contact_manager.contacts["Amina"], "612-555-1234")


if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
from models import *
import os
from models.base_model import Base
from models.engine.db_storage import DBStorage

storage_type = os.environ.get('HBNB_TYPE_STORAGE')

@unittest.skipIf(storage_type != 'db', 'skip if environ is not db')
class TestDBStorageDocs(unittest.TestCase):
    """Class for testing DBStorage docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For DBStorage Class .......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ' Database engine '
        actual = DBStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = DBStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """... documentation for all method"""
        expected = ' returns a dictionary of all objects '
        actual = DBStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """... documentation for new method"""
        expected = ' adds objects to current database session '
        actual = DBStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save method"""
        expected = ' commits all changes of current database session '
        actual = DBStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """... documentation for reload method"""
        expected = ' creates all tables in database & session from engine '
        actual = DBStorage.reload.__doc__
        self.assertEqual(expected, actual)

    def test_doc_delete(self):
        """... documentation for delete method"""
        expected = ' deletes obj from current database session if not None '
        actual = DBStorage.delete.__doc__
        self.assertEqual(expected, actual)

    def test_doc_get(self):
        """... documentation for get method"""
        expected = ' fetches specific object '
        actual = DBStorage.get.__doc__
        self.assertEqual(expected, actual)

    def test_doc_count(self):
        """... documentation for count method"""
        expected = ' count of instances '
        actual = DBStorage.count.__doc__
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

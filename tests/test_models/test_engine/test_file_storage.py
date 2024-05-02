#!/usr/bin/python3
"""
Unit Test for FileStorage Class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import os
import json

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


@unittest.skipIf(storage_type == 'db', 'skip if environment is db')
class TestFileStorageDocs(unittest.TestCase):
    """Class for testing FileStorage documentation"""

    @classmethod
    def setUpClass(cls):
        """Setup for the test"""
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """Test for documentation in the file"""
        expected = ("\nHandles I/O, writing and reading, of JSON for storage "
                    "of all class instances\n")
        actual = FileStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """Test for documentation in the all() method"""
        expected = 'returns private attribute: __objects'
        actual = FileStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """Test for documentation in the new() method"""
        expected = ("sets / updates in __objects the obj with key <obj class "
                    "name>.id")
        actual = FileStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """Test for documentation in the save() method"""
        expected = 'serializes __objects to the JSON file (path: __file_path)'
        actual = FileStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """Test for documentation in the reload() method"""
        expected = ("if file exists, deserializes JSON file to __objects, "
                    "else nothing")
        actual = FileStorage.reload.__doc__
        self.assertEqual(expected, actual)


@unittest.skipIf(storage_type == 'db', 'skip if environment is db')
class TestFileStorageInstances(unittest.TestCase):
    """Class for testing FileStorage class instances"""

    @classmethod
    def setUpClass(cls):
        """Setup for the test"""
        print('\n\n.................................')
        print('...... Testing FileStorage ......')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def setUp(self):
        """Setup for the test"""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Teardown for the test"""
        del self.storage
        del self.base_model

    def test_instance(self):
        """Test whether the object is an instance of FileStorage"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_storage_file_exists(self):
        """Test whether the file.json exists after save()"""
        os.remove(FileStorage._FileStorage__file_path)
        self.base_model.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

    def test_obj_saved_to_file(self):
        """Test whether the object is saved to the file"""
        os.remove(FileStorage._FileStorage__file_path)
        self.base_model.save()
        obj_id = self.base_model.id
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            objs_dict = json.load(f)
        self.assertIn(obj_id, objs_dict.keys())

    def test_to_json(self):
        """Test whether to_json returns serializable dictionary"""
        json_dict = self.base_model.to_json()
        self.assertIsInstance(json_dict, dict)

    def test_reload(self):
        """Test whether reload loads objects from file"""
        os.remove(FileStorage._FileStorage__file_path)
        self.base_model.save()
        obj_id = self.base_model.id
        new_storage = FileStorage()
        new_storage.reload()
        objs_dict = new_storage.all()
        self.assertIn(obj_id, objs_dict.keys())


if __name__ == '__main__':
    unittest.main()

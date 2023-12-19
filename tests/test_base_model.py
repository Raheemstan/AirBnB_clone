import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 100
        expected_str = "[BaseModel] ({}) {'name': 'Test Model', 'my_number': 100, 'id': '{}', 'created_at': '{}', 'updated_at': '{}'}"\
            .format(my_model.id, my_model.id, my_model.created_at, my_model.updated_at)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 100
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], 'Test Model')
        self.assertEqual(obj_dict['my_number'], 100)
        self.assertEqual(obj_dict['id'], my_model.id)
        self.assertEqual(obj_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], my_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

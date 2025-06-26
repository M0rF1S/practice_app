import unittest
from form_matcher import find_matching_template

class TestTemplateMatching(unittest.TestCase):

    def setUp(self):
        self.db_path = "database.json"

    def test_match_user_data_template(self):
        data = {"login": "vasya@example.com", "tel": "+7 123 456 78 90"}
        result = find_matching_template(self.db_path, data)
        self.assertEqual(result, "Данные пользователя")

    def test_match_with_additional_fields(self):
        data = {"login": "vasya@example.com", "tel": "+7 123 456 78 90", "extra": "123"}
        result = find_matching_template(self.db_path, data)
        self.assertEqual(result, "Данные пользователя")

    def test_no_matching_template_found(self):
        data = {"foo": "bar"}
        result = find_matching_template(self.db_path, data)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["foo"], "text")

    def test_partial_field_match(self):
        data = {"login": "vasya@example.com"}
        result = find_matching_template(self.db_path, data)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()

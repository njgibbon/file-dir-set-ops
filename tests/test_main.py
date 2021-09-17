import unittest

import file_dir_set_ops.main


class TestMain(unittest.TestCase):
    def test_print_items_with_newline(self):
        items = ['a', 'b']
        file_dir_set_ops.main.print_items_with_newline(items)

    def test_get_file_set_from_dir_path(self):
        expected_set = {'a.txt', 'file.txt'}
        file_set = file_dir_set_ops.main.get_file_set_from_dir_path("tests/data/a")
        print(file_set)
        self.assertTrue(file_set == expected_set)

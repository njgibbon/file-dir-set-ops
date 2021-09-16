import unittest

import file_dir_set_ops.main


class TestMain(unittest.TestCase):
    def test_print_items_with_newline(self):
        items = ['a', 'b']
        file_dir_set_ops.main.print_items_with_newline(items)

import builtins
import contextlib
import io
import unittest
from unittest.mock import Mock

from patterns.functional.hollywood import string_processor


class TestHollywood(unittest.TestCase):
    def test_uppercase_processor(self) -> None:
        mock = Mock()
        mock.side_effect = print
        builtins.print = mock

        def uppercase_processor(input_string: str) -> str:
            return input_string.upper()

        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            string_processor('hello', uppercase_processor)
        output = str_io.getvalue()
        self.assertTrue(print.called)
        self.assertEqual(output, 'HELLO')

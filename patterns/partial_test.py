import unittest
from patterns.partial import get_customer


class TestPartial(unittest.TestCase):
    def test_get_customer(self) -> None:
        customer = get_customer(1)
        self.assertEqual(customer["id"], 1)

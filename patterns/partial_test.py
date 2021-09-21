import unittest
from patterns.partial import get_customer, get_customer_partial


class TestPartial(unittest.TestCase):
    def test_get_customer(self) -> None:
        customer = get_customer(1)
        self.assertEqual(customer["id"], 1)

    def test_get_customer_partial(self) -> None:
        customer = get_customer_partial(1)
        self.assertEqual(customer["id"], 1)

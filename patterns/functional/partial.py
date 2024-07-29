from functools import partial
from typing import TypedDict, Optional


class Customer(TypedDict):
    id: int
    name: str


def get_connection() -> None:
    return None


def get_customer_from_database(connection: None, customer_id: int) -> Optional[Customer]:
    print(connection)
    if customer_id == 1:
        return {"id": 1, "name": "Jon"}
    else:
        return None


def get_customer(customer_id: int) -> Optional[Customer]:
    return get_customer_from_database(get_connection(), customer_id)


get_customer_partial = partial(get_customer_from_database, get_connection())

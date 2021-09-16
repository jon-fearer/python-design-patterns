from functools import partial
from typing import TypedDict, Optional


class Customer(TypedDict):
    id: int
    name: str


class Connection:
    conn: None


def get_customer_from_database(connection: Connection, customer_id: int) -> Optional[Customer]:
    print(connection)
    if customer_id == 1:
        return {"id": 1, "name": "Jon"}
    else:
        return None


def get_customer(customer_id: int) -> Optional[Customer]:
    return get_customer_from_database(Connection(), customer_id)


get_customer_partial = partial(get_customer_from_database, Connection())

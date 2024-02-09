from unittest.mock import Mock

import pytest

from data import BurgerSample
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def database():
    database = Database()
    return database

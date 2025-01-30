# -*- coding: utf-8 -*-
"""test_crud.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cB1ZwLtHflkfmq0pMClctLk-hdLywYMO
"""

pip install pytest

import pytest
from day_11 import create_table, insert, read, update, delete

@pytest.fixture
def setup_database():
    # This will set up the initial database state
    create_table()
    insert("John", 35)
    yield
    # Clean up
    delete(1)

def test_insert_user(setup_database):
    insert("Jane", 28)
    user = read(2)
    assert user[1] == "Jane"
    assert user[2] == 28

def test_update_user(setup_database):
    update(1, "John Doe", 36)
    user = read(1)
    assert user[1] == "John Doe"
    assert user[2] == 36

def test_delete_user(setup_database):
    delete(1)
    user = read(1)
    assert user is None
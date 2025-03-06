# Fixters - similar to Pre-condition - concept in Python

import pytest

@pytest.fixture()
def is_married():
    return False

def test_need_confirmation(is_married):
    assert  is_married == True
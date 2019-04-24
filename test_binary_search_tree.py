import pytest
from binary_search_tree import binary_search_tree


@pytest.fixture
def empty_bst():
    return binary_search_tree()


def test_create_empty(empty_bst):
    bst = empty_bst
    assert(len(bst) == 0)
    assert(bst.num_nodes() == 0)


def test_add_first_value(empty_bst):
    bst = empty_bst
    bst.add(10)
    assert(bst.num_nodes() == 1)


def test_add_multiple_values(empty_bst):
    bst = empty_bst
    bst.add(10).add(20).add(5)
    assert(bst.num_nodes() == 3)


def test_add_multiple_values_deep(empty_bst):
    bst = empty_bst
    bst.add(10).add(20).add(5).add(80).add(2)
    assert(bst.num_nodes() == 5)


def test_contains(empty_bst):
    bst = empty_bst
    bst.add(10).add(20).add(5).add(80).add(2)
    assert(bst.contains(5))
    assert(bst.contains(50) is False)
    assert(bst.contains(7) is False)

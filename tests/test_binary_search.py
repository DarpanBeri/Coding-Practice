from search_algorithms.binary_search import binary_search, recursive_binary_search


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2  # Basic search on a sorted array
    assert binary_search([], 3) == None  # Edge case search
    assert binary_search(['a', 'b', 'c', 'd', 'e', 'f'], 'b') == 1


def test_recursive_binary_search():
    assert recursive_binary_search([1, 2, 3, 4, 5], 3) == 2  # Basic search on a sorted array
    assert recursive_binary_search([], 3) == None  # Edge case search
    assert recursive_binary_search(['a', 'b', 'c', 'd', 'e', 'f'], 'b') == 1
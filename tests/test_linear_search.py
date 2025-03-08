from search_algorithms.linear_search import linear_search


def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 3) == 2  # Basic search on a sorted array
    assert linear_search(["apple", "banana", "cherry"], "cherry") == 2  # Searching strings
    assert linear_search([], 3) == None  # Edge case search
    assert linear_search([3, 4, 51, 2, 6, 9], 4) == 1  # Unsorted search

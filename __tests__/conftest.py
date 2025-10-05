"""
Pytest configuration and shared fixtures
"""

import pytest
from src.linked_lists import ListNode


@pytest.fixture
def sample_linked_list():
    """Fixture providing a sample linked list for testing"""
    return ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


@pytest.fixture
def empty_linked_list():
    """Fixture providing an empty linked list for testing"""
    return None


@pytest.fixture
def single_node_list():
    """Fixture providing a single-node linked list for testing"""
    return ListNode(42)


@pytest.fixture
def sample_array():
    """Fixture providing a sample array for testing"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def empty_array():
    """Fixture providing an empty array for testing"""
    return []


@pytest.fixture
def single_element_array():
    """Fixture providing a single-element array for testing"""
    return [42]

"""
Tests for remove nth from end algorithm
"""

import pytest
from src.linked_lists import remove_nth_from_end, create_linked_list, linked_list_to_array


class TestRemoveNthFromEnd:
    """Test cases for remove_nth_from_end function"""
    
    def test_remove_last_node(self):
        """Test removing the last node from the list"""
        # Arrange
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 1
        expected = [1, 2, 3, 4]
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_remove_first_node(self):
        """Test removing the first node from the list"""
        # Arrange
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 5
        expected = [2, 3, 4, 5]
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_remove_middle_node(self):
        """Test removing a middle node from the list"""
        # Arrange
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 3
        expected = [1, 2, 4, 5]
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_single_node_list(self):
        """Test removing from a single-node list"""
        # Arrange
        head = create_linked_list([1])
        n = 1
        expected = []
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_empty_list(self):
        """Test removing from an empty list"""
        # Arrange
        head = create_linked_list([])
        n = 1
        expected = []
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_invalid_n_greater_than_length(self):
        """Test with n greater than list length"""
        # Arrange
        head = create_linked_list([1, 2, 3])
        n = 5
        expected = [1, 2, 3]  # No changes
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_invalid_n_less_than_one(self):
        """Test with n less than 1"""
        # Arrange
        head = create_linked_list([1, 2, 3])
        n = 0
        expected = [1, 2, 3]  # No changes
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_two_node_list_remove_first(self):
        """Test removing first node from two-node list"""
        # Arrange
        head = create_linked_list([1, 2])
        n = 2
        expected = [2]
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected
    
    def test_two_node_list_remove_second(self):
        """Test removing second node from two-node list"""
        # Arrange
        head = create_linked_list([1, 2])
        n = 1
        expected = [1]
        
        # Act
        result = remove_nth_from_end(head, n)
        
        # Assert
        assert linked_list_to_array(result) == expected


@pytest.mark.parametrize("values,n,expected", [
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
    ([1, 2, 3, 4, 5], 4, [1, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
    ([1, 2], 2, [2]),
])
def test_remove_nth_from_end_parametrized(values, n, expected):
    """Parametrized test for remove_nth_from_end function"""
    head = create_linked_list(values)
    result = remove_nth_from_end(head, n)
    assert linked_list_to_array(result) == expected

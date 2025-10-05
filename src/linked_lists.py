
from typing import Optional

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"

def create_linked_list(values: list[int]) -> Optional['ListNode']:
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def remove_nth_from_end(head: Optional['ListNode'], n: int) -> Optional['ListNode']:
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    for _ in range(n):
        if not fast.next:
            return head
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    if slow.next:
        slow.next = slow.next.next
    
    return dummy.next

def linked_list_to_array(head: Optional['ListNode']) -> list[int]:
    """Helper function to convert linked list to array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
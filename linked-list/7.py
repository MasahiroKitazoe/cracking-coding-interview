import unittest
from linked_list import ListNode

def find_intersection(head_node1, head_node2):
	refs = {}
	while head_node1:
		refs[id(head_node1)] = True
		head_node1 = head_node1.next
	intersection_node = None
	while head_node2:
		if refs.get(id(head_node2)):
			intersection_node =  head_node2
			break
		head_node2 = head_node2.next
	return intersection_node


class TestQuestion7(unittest.TestCase):
	def test_it(self):
		head_node1 = ListNode(1)
		head_node2 = ListNode(1)
		current_node1 = head_node1
		current_node2 = head_node2
		for i in [5, 2]:
			node = ListNode(i)
			current_node1.next = node
			current_node1 = current_node1.next
		for i in [6, 3, 10, 12]:
			node = ListNode(i)
			current_node1.next = node
			current_node2.next = node
			current_node1 = current_node1.next
			current_node2 = current_node2.next

		intersection_node = find_intersection(head_node1, head_node2)
		assert intersection_node.val == 6

	def test_when_no_intersection_exists(self):
		head_node1 = ListNode(1)
		head_node2 = ListNode(1)
		current_node1 = head_node1
		current_node2 = head_node2
		for i in [5, 2]:
			node = ListNode(i)
			current_node1.next = node
			current_node1 = current_node1.next
		for i in [5, 2]:  # val is equal but ref is not
			node = ListNode(i)
			current_node2.next = node
			current_node2 = current_node2.next
		
		intersection_node = find_intersection(head_node1, head_node2)
		assert intersection_node is None


if __name__ == "__main__":
	unittest.main()


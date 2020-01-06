import unittest

from linked_list import ListNode


def find_beginning_of_circular_nodes(head_node):
	refs = {}
	while True:
		if refs.get(id(head_node)):
			return head_node
		refs[id(head_node)] = True
		head_node = head_node.next


class TestQuestion7(unittest.TestCase):
	def test_it(self):
		head_node = ListNode(1)
		current_node = head_node
		for i in [5, 2, 4]:
			node = ListNode(i)
			current_node.next = node
			current_node = current_node.next
		circular_start = current_node
		for i in [6, 8, 10, 12]:
			node = ListNode(i)
			current_node.next = node
			current_node = current_node.next
		current_node.next = circular_start

		loop_start_node = find_beginning_of_circular_nodes(head_node)
		assert loop_start_node == circular_start


if __name__ == "__main__":
	unittest.main()

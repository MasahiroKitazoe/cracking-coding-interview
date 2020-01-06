from linked_list import ListNode


def main(node):
	def helper(node, val):
		if not node.next:
			return
		if node.next.val == val:
			node.next = node.next.next
		helper(node.next, val)
	while True:
		if not node.next:
			break
		helper(node, node.val)
		node = node.next


if __name__ == "__main__":
	head_node = ListNode(1)
	current_node = head_node
	for i in [5, 2, 7, 1, 6]:
		node = ListNode(i)
		current_node.next = node
		current_node = current_node.next
	main(head_node)

	node = head_node
	while True:
		if not node:
			break
		print(node.val)
		node = node.next


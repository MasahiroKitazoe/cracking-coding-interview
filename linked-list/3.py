from linked_list import ListNode

LIST_VALS = [5, 2, 7, 1, 6]


def main(node):
	if not node or not node.next:
		return

	node.val = node.next.val
	node.next = node.next.next


if __name__ == "__main__":
	head_node = ListNode(1)
	current_node = head_node
	target_node = None
	for i, val in enumerate(LIST_VALS):
		if i - 1  == len(LIST_VALS) // 2:
			target_node = current_node
		node = ListNode(val)
		current_node.next = node
		current_node = current_node.next

	main(target_node)
	while True:
		if not head_node:
			break
		print(head_node.val)
		head_node = head_node.next


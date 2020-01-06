from linked_list import ListNode


def main(k, node):
	head_node = node
	count = 0
	while True:
		count += 1
		if not node.next:
			break
		node = node.next

	i = 1
	node = head_node
	while i < count - k:
		node = node.next
		i += 1

	return node


if __name__ == "__main__":
	head_node = ListNode(1)
	current_node = head_node
	for i in [5, 2, 7, 1, 6]:
		node = ListNode(i)
		current_node.next = node
		current_node = current_node.next

	node = main(3, head_node)
	print(node.val)



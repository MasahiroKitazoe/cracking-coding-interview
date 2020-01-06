from linked_list import ListNode


def main(head_node):
	pass


if __name__ == "__main__":
	head_node = ListNode(1)
	current_node = head_node
	for i in [5, 2, 7, 1, 6]:
		node = ListNode(i)
		current_node.next = node
		current_node = current_node.next
	main(head_node)




from Node import Node

def RemoveDups(head):
    first_node_for_comparison = head

    while first_node_for_comparison != None:
        second_node_for_comparison = first_node_for_comparison.next
        for_removing_second_node = first_node_for_comparison
        while second_node_for_comparison != None:
            if first_node_for_comparison.data == second_node_for_comparison.data:
                for_removing_second_node.next = for_removing_second_node.next.next
            for_removing_second_node = for_removing_second_node.next
            second_node_for_comparison = for_removing_second_node.next

        first_node_for_comparison = first_node_for_comparison.next

    return head

linked_list = Node(Node(Node(Node(),7),7),8)
print(RemoveDups(linked_list))
        
    


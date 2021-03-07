class Node:
    def __init__(self, next=None, data = None):
        self.next = next
        self.data = data

    def __str__(self):
        string = str(self.data)
        linked_list = self
        while (linked_list.next != None):
            string += " -> "
            string += str(linked_list.next.data)
            linked_list = linked_list.next

        return string

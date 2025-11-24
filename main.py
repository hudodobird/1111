class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(15)
node2 = Node(3)
node3 = Node(17)
node4 = Node(90)

node1.next = node3
node3.next = node4
node4.next = node2
# node4.next = node1

def print_linked_list(first):
    current = first
    smallestValue = 9999999999999999999

    while current is not None:
        if current.data < smallestValue:
            smallestValue = current.data
        else:
            pass
        print(current.data)
        current = current.next
    print("Smallest value is:", smallestValue)



def remove_node(first, target):
    current = first

    while current is not None:
        if current.data == target:
            current.data = current.next.data
            current.next = current.next.next
            return f"Node with value {target} found and removed"
            
        else:
            current = current.next
    return f"Node with value {target} not found"
        


#print_linked_list(node1)
#remove_node(node1, 17)
#print_linked_list(node1)
print(remove_node(node1, 90))
print_linked_list(node1)
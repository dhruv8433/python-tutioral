class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Traverse and print the linked list
    def traverse(self):
        if not self.head:
            print("List is empty")
            return

        visited = set()  # To avoid infinite loop if there is a cycle
        temp = self.head
        while temp:
            if temp in visited:
                print(f"{temp.data} -> ... (loop detected)")
                break
            print(temp.data, end=" -> ")
            visited.add(temp)
            temp = temp.next
        else:
            print("None")

    # Floyd’s Cycle Detection Algorithm
    def loop_detection(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                print("Loop detected")
                self.remove_loop(slow_ptr)
                return
        print("No loop detected")

    # Create a loop at a specific position
    def create_loop(self, position):
        if position == 0:
            return  # No loop

        loop_start = self.head

        # Move loop_start to the desired position
        for _ in range(position - 1):
            if loop_start is None:
                return
            loop_start = loop_start.next

        end = self.head
        # Move to the last node
        while end.next:
            end = end.next

        # Create the loop
        end.next = loop_start
        print(f"Loop created at position {position} (Node value: {loop_start.data})")

    # Remove loop once detected using Floyd's cycle meeting point
    def remove_loop(self, meeting_point):
        ptr1 = self.head
        ptr2 = meeting_point

        # Find the start of the loop
        while ptr1.next != ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Break the loop
        ptr2.next = None
        print(f"Loop removed. It was looping at node: {ptr1.next.data if ptr1.next else 'None'}")


# ----------------------------
# Example usage:
ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)

ll.traverse()  # Normal list print

ll.create_loop(3)  # Create loop at position 3 (30)

ll.loop_detection()  # Should detect and remove loop

ll.traverse()  # List should now print normally

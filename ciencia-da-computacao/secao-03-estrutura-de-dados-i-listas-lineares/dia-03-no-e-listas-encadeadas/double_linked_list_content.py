from node import Node


class DoubleLinkedList:
    def __init__(self):
        self.head_value = None
        self.tail_value = None
        self.__length = 0

    def __str__(self):
        return f"""
DoubleLinkedList(len={self.__length}, value={self.head_value})"""

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        first_value.previous = self.tail_value
        self.head_value = first_value
        self.__length += 1


if __name__ == "__main__":
    linked_list = DoubleLinkedList()
    linked_list.insert_first(1)
    linked_list.insert_first(2)
    print(linked_list)

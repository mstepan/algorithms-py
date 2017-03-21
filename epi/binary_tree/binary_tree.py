from enum import Enum


class BinaryTree:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def add_edge(self, parent_val, child_val, direction):
        parent = self.__get_node(parent_val)

        if self.root is None:
            self.root = parent

        child = self.__get_node(child_val)

        if direction is NodeDirection.LEFT:
            parent.left = child

        elif direction is NodeDirection.RIGHT:
            parent.right = child

        else:
            raise ValueError

    def __get_node(self, val):
        if val not in self.nodes:
            node = Node(val)
            self.nodes[val] = node
            return node

        return self.nodes[val]


class NodeDirection(Enum):
    LEFT = 0
    RIGHT = 1


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def main():
    tree = BinaryTree()
    tree.add_edge("A", "B", NodeDirection.LEFT)
    tree.add_edge("A", "C", NodeDirection.RIGHT)


if __name__ == "__main__":
    main()

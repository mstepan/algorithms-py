class BinaryTree(object):
    def __init__(self, root):
        self.root = root

    def mirror(self):
        """
        Implement a function which modifies a binary tree
        so that the output is the tree that is a mirror of an input tree
        """
        return BinaryTree(self.__mirror_rec(self.root))

    def __mirror_rec(self, cur):
        if cur is None:
            return None

        left_changed = self.__mirror_rec(cur.left)
        right_changed = self.__mirror_rec(cur.right)

        cur.left = right_changed
        cur.right = left_changed

        return cur

    def __inorder_rec(self, cur):
        if cur is None:
            return ""

        return self.__inorder_rec(cur.left) + ", " + str(cur.value) + self.__inorder_rec(cur.right)


    def post_order(self):
        return "[" + self.__post_order_rec(self.root) + "]"

    def post_order_iter(self):
        if self.root is None:
            return ""

        prev = None
        stack = list()
        stack.append(self.root)

        res = []

        while len(stack) != 0:
            cur = stack.pop()

            if cur.is_leaf() or (cur.left is not None and prev == cur.left) or (
                    cur.right is not None and prev == cur.right):
                res.append(cur.value)
                prev = cur
            else:
                stack.append(cur)

                if cur.right is not None:
                    stack.append(cur.right)

                if cur.left is not None:
                    stack.append(cur.left)

        return res


    def __post_order_rec(self, cur):
        if cur is None:
            return ""

        if cur.left is None and cur.right is None:
            return "'" + str(cur.value) + "'"

        res = ""

        if cur.left is not None:
            res += self.__post_order_rec(cur.left) + ", "

        if cur.right is not None:
            res += self.__post_order_rec(cur.right) + ", "

        return "%s'%s'" % (res, cur.value)


    def __str__(self):
        """
        Compose tree into string using in-order traversation.
        """
        return self.__inorder_rec(self.root)


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        return self.left is None and self.right is None


if __name__ == "__main__":
    # nodes
    f = Node("F")

    b = Node("B")
    g = Node("G")
    a = Node("A")
    d = Node("D")
    i = Node("I")

    m = Node("M")
    c = Node("C")
    e = Node("E")
    h = Node("H")

    t = Node("T")

    # links
    f.left = b
    f.right = g

    b.left = a
    b.right = d

    g.right = i

    a.right = m
    d.left = c
    d.right = e
    i.left = h

    e.right = t

    tree = BinaryTree(f)

    print("pos-order trav:  %s" % tree.post_order())
    print("post-order iter: %s" % tree.post_order_iter())



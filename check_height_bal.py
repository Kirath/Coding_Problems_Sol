class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.node = None


def check_bal(root):
    if root is None:
        return -1, True
    left_h, left_b = check_bal(root.left)
    right_h, right_b = check_bal(root.right)
    height = 1 + max(left_h, right_h)
    balance = abs(left_h - right_h)
    if balance <= 1 and (left_b and right_b):
        return height, True
    return -1, False


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(6)
root.left.right = Node(8)
root.right.right = Node(6)
root.right.right.right = Node(1)
print(check_bal(root))
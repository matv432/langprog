class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_array(arr):
    if not arr or arr[0] is None:
        return None

    nodes = [None if v is None else Node(v) for v in arr]
    n = len(nodes)

    for i, node in enumerate(nodes):
        if node is None:
            continue

        li, ri = 2*i + 1, 2*i + 2

        if li < n:
            node.left = nodes[li]
        if ri < n:
            node.right = nodes[ri]

    return nodes[0]

def is_height_balanced(root):
    def dfs(node):
        if node is None:
            return True, -1  # пустота: высота -1, у листа будет 0
        lb, lh = dfs(node.left)
        if not lb:
            return False, 0
        rb, rh = dfs(node.right)
        if not rb:
            return False, 0
        balanced_here = abs(lh - rh) <= 1
        return balanced_here, 1 + max(lh, rh)

    ok, _ = dfs(root)
    return ok

# Примеры
if __name__ == "__main__":
    root1 = build_tree_from_array([4, 2, 6, 1, 3, 5, 7])
    print(is_height_balanced(root1))  # True

    root2 = build_tree_from_array([1, None, 2, None, None, None, 3])
    print(is_height_balanced(root2))  # False

    root3 = build_tree_from_array([None])
    print(is_height_balanced(root3))  # True
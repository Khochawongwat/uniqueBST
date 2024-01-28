class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def transverse(node, result):
    if node is None:
        return
    result.append(node.data)
    transverse(node.left, result)
    transverse(node.right, result)

def generateBTS(n: int = 3):
    NONE_LIST = [None]

    def helper(start, end):
        if start > end:
            return NONE_LIST
        results = []
        for i in range(start, end + 1):
            left = helper(start, i - 1)
            right = helper(i + 1, end)

            for l in left:
                for r in right:
                    node = Node(i)
                    node.left = l
                    node.right = r
                    results.append(node)
        return results

    bts = helper(1, n)
    results = [transverse(node, []) for node in bts]
    return results

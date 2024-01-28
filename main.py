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
    def helper(start, end):
        if start > end:
            return [None]
        results = []
        for i in range(start, end + 1):
            left = helper(start, i - 1)
            right = helper(i + 1, end)

            for l in left:
                for r in right:
                    node = Node(i)
                    results.append(node)
                    node.left = l
                    node.right = r
        return results
    
    bts = helper(1, n)
    results = []
    for node in bts:
        result = []
        transverse(node, result)
        results.append(result)
    return results

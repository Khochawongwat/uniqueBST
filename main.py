class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

def transverse(node: Node, result: list) -> None:
    if node is None:
        return
    result.append(node.data)
    transverse(node.left, result)
    transverse(node.right, result)

def generateBTS(n: int):
    def helper(start: int, end: int):
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

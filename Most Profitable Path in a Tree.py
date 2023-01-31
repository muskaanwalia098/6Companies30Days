class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobPath = {}
        def dfs_bobTraverse(node, parent, steps):
            bobPath[node] = steps
            if node == 0:   return True
            for neighbour in graph[node]:
                if neighbour == parent: continue
                if dfs_bobTraverse(neighbour, node, steps+1):   return True
            del bobPath[node]
            return False

        dfs_bobTraverse(bob, -1, 0)

        # BFS function for Alice's Traversal
        queue = deque()
        queue.append((0, -1, 0, 0))
        max_net_income = float("-inf")

        while queue:
            node, parent, current_amount, aliceSteps = queue.popleft()
            current_amount += self.getGateAmount(node, aliceSteps, bobPath, amount)

            if len(graph[node]) == 1 and node != 0:
                max_net_income = max(max_net_income, current_amount)
                continue

            for neighbour in graph[node]:
                if neighbour == parent: continue
                queue.append((neighbour, node, current_amount, aliceSteps+1))

        return max_net_income

    def getGateAmount(self, node, aliceSteps, bobPath, amount):
        if node not in bobPath or bobPath[node] > aliceSteps:   return amount[node]
        if bobPath[node] == aliceSteps: return amount[node]//2
        if bobPath[node] < aliceSteps:  return 0

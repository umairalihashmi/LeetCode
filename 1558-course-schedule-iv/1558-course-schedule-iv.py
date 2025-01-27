class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preqs = [ set() for _ in range(numCourses)]
        
        for preq,course in prerequisites:
            preqs[course].add(preq)
        
        visited = set()
        
        def traverse(node):
            if not preqs[node] or node in visited:
                return preqs[node]
            temp = preqs[node]
            for each in preqs[node]:
                temp = temp | traverse(each)
            preqs[node] = temp
            visited.add(node)
            return temp
        
        for i in range(len(preqs)):
            preqs[i] = traverse(i)
        
        return [ preq in preqs[course] for preq,course in queries ]
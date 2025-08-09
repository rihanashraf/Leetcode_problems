class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #unique prerequisites

        #detect if cycle in graph

        if prerequisites == []:
            return True

        D = defaultdict(list)
        for u, v in prerequisites:
            D[v].append(u)

        yes = [True]

        def cycling(node):
            for andi in D[node]:
                if andi in seen:
                    yes[0] = False
                if andi not in seen:
                    seen.add(andi)
                    cycling(andi)


        seen = set()
        seen.add(prerequisites[0][1])
        cycling(prerequisites[0][1]) 
        return yes[0]
        

        
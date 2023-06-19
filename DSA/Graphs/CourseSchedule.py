def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visitSet = set()

        def DFS(course):
            if course in visitSet:
                return False
            if preMap[course] ==[]:
                return True
            
            visitSet.add(course)
            for pre in preMap[course]:
                if not DFS(pre):
                    return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not DFS(course):
                return False
        return True

numCourses = 2
# prerequisites = [[1,0]]
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))
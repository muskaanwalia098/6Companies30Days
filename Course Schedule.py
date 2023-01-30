class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Creating a dictionary for all the courses
        preMap = {i:[] for i in range(numCourses)}
        # Adding prerequisites for each of the courses
        for pre, crs in prerequisites:
            preMap[crs].append(pre)
        # visitSet -> to keep a track of all the courses that have been visited
        visitSet = set()
        def dfs(crs):
            # If the course has already been visited, this means it may be a loop
            if crs in visitSet:
                return False
            # If the course has an empty list it means that 
            # it does not have any prerequisites
            if preMap[crs] == []:
                return True
            # If none of the above cases work it means that we are 
            # visiting that course and hence add it to the visitSet
            visitSet.add(crs)
            # Will check this for all the prerequisites of 'crs'
            for pre in preMap[crs]:
                if not dfs(pre):    return False
            visitSet.remove(crs)    # No longer visiting this course
            preMap[crs] = []    # if ever we visit then it returns True
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):    return False
        return True

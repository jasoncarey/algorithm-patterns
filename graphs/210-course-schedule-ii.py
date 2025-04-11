"""
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/description/

Medium

TC: O(V+E)  where V is numCourses, E is number of prerequisites
SC: O(V+E)
"""


def find_order(numCourses, prerequisites):

    adj_list = {i: [] for i in range(numCourses)}  # build adjacency list
    for crs, pre in prerequisites:
        adj_list[crs].append(pre)

    visited = set()
    completed = set()
    result = []

    def dfs(crs):
        if crs in visited:  # cycle
            return False

        visited.add(crs)

        for pre in adj_list[crs]:
            if pre not in completed and not dfs(pre):
                return False

        result.append(crs)
        visited.remove(crs)
        completed.add(crs)
        return True

    for crs in range(numCourses):
        if crs not in completed:
            if not dfs(crs):
                return []

    if len(result) == numCourses:
        return result
    else:
        return []

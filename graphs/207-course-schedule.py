"""
207. Course Schedule
https://leetcode.com/problems/course-schedule

Medium

TC: 
SC: 
"""


def can_finish(numCourses, prerequisites):

    adj_list = {i: [] for i in range(numCourses)}  # map each course to empty list
    for crs, pre in prerequisites:
        adj_list[crs].append(pre)

    visited = set()

    def dfs(crs):
        if crs in visited:
            return False  # if we already visited, there's a cycle
        if adj_list[crs] == []:
            return True  # no pre means we can complete it

        visited.add(crs)
        for pre in adj_list[crs]:
            if not dfs(pre):
                return False

        visited.remove(crs)
        adj_list[crs] = []  # optimisation, since we know this course can be completed
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False

    return True


def can_finish_topological(numCourses, prerequisites):

    adj_list = {i: [] for i in range(numCourses)}
    in_degree = {i: 0 for i in range(numCourses)}

    for crs, pre in prerequisites:
        adj_list[pre].append(crs)
        in_degree[crs] += 1

    q = deque()

    # if the course has no prerequisites, q it
    for crs in range(numCourses):
        if in_degree[crs] == 0:
            q.append(crs)

    courses_taken = 0

    while q:
        crs = q.popleft()
        courses_taken += 1

        for nei in adj_list[crs]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)

    return courses_taken == numCourses

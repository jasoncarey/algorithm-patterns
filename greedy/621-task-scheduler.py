"""
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/description/

Medium

Intuition:
- Higher frequency tasks should be prioritised to minimize idle time

TC: O(timer * log(k))
SC: O(n)
"""

from collections import Counter, deque


def least_interval(tasks, n):
    freq = Counter(tasks)  # count the frequency of each task
    heap = []  # tracks all available tasks, highest frequency popped first
    cooldown = deque()  # (remaining executions, next available time)
    timer = 0

    for key, value in freq.items():
        heapq.heappush(heap, -value)  # create max heap with item frequency

    while heap or cooldown:
        if heap:
            task = -heapq.heappop(heap)
            if task > 1:  # if the task can be executed
                cooldown.append((task - 1, timer + n + 1))
        timer += 1

        while cooldown and cooldown[0][1] == timer:
            task_count, _ = cooldown.popleft()
            heapq.heappush(heap, -task_count)

    return timer

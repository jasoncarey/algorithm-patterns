"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

Medium

TC:
SC:
"""


def find_cheapest_price(n, flights, src, dst, k):
    def dijkstra(graph, source):

        heap = [(0, source, k + 1)]
        visited = dict()

        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost

            if stops > 0:
                for neighbour, weight in graph.get(node, []):
                    new_cost = cost + weight
                    key = (neighbour, stops - 1)

                    if key not in visited or new_cost < visited[key]:
                        visited[key] = new_cost
                        heapq.heappush(heap, (cost + weight, neighbour, stops - 1))

        return -1

    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    return dijkstra(graph, src)

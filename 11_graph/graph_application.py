# -*- coding:utf-8 -*-



from collections import deque
from graph import Undigraph

def find_vertex_by_degree(graph, s, degree):
    """
    查找某个顶点的degree度关系
    例如，起始顶点最近的一层顶点也就是起始顶点的一度好友
    """
    if len(graph) <= 1:
        return []
    if degree == 0:
        return [s]
    d_vertices = []
    queue = deque()
    prev = [-1] * len(graph)
    visited = [False] * len(graph)
    visited[s] = True
    queue.append(s)
    while len(queue) > 0:
        sz = len(queue)
        for i in range(sz):
            v = queue.popleft()
            for adj_v in graph[v]:
                if not visited[adj_v]:
                    prev[adj_v] = v
                    visited[adj_v] = True
                    queue.append(adj_v)
        # 每一层的顶点遍历完 全部popleft出去，队列中剩下的是下一层的所有顶点
        degree -= 1
        if degree == 0 and len(queue) != 0:
            return queue 

   
if __name__ == '__main__':
    g = Undigraph(8)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)
    print(g.adj_tbl)
    print(find_vertex_by_degree(g, 0, 4))

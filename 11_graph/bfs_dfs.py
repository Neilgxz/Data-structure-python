"""
    Breadth-first search and depth-first search.

    Author: Wenru Dong
"""

from typing import List, Optional, Generator, IO
from collections import deque

class Graph:
    """Undirected graph."""
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]

    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
        # 可以递归的返回搜索路径，从s开始一直到t结束
        # 例如顺序是0 1 2 5 7
        # bfs函数中如果neighbor == t 会调用 self._generate_path(0, 7, prev)
        # 接下来调用 self._generate_path(0, prev[7], prev) 也就是(0, 5 ,prev)
        # (0, 2 ,prev)
        # (0, 1, prev)
        # (0, 0, prev)
        # 在 (0, 0, prev) 内因为0==0 所以 输出 str(0) 也就是0
        # 之后递归回到 函数 (0, 1, prev) 内执行 str(1) 
        # 之后递归回 str(2),str(5) ,str(7)
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int) -> IO[str]:
        """Print out the path from Vertex s to Vertex t
        using bfs. 借助双端队列，类似于完全二叉树的层次遍历
        """
        if s == t: return
        # visited 表示这个顶点是否被访问过
        visited = [False] * self._num_vertices
        visited[s] = True
        # 队列用来存储已经被访问、但相连的顶点还没有被访问的顶点。
        q = deque()
        q.append(s)
        # prev[i] = j 表示下标为i的顶点是从j这个前驱顶点遍历而来的，用于返回搜索路径
        prev = [None] * self._num_vertices

        while q:
            # 出队头元素 第K层的顶点
            v = q.popleft()
            for neighbour in self._adjacency[v]: # 遍历与v相连的k+1层的顶点。
                if not visited[neighbour]:
                    # 如果他连接的下级顶点没有没访问过则执行
                    # 这个下级顶点被标记为由 v 遍历而来
                    prev[neighbour] = v
                    # 如果在下级结点中找到终点直接结束并打印路径
                    if neighbour == t:
                        print("->".join(self._generate_path(s, t, prev)))
                        return
                    # 下级顶点标记为visited
                    visited[neighbour] = True
                    # 把这个下级顶点从队尾加入，
                    q.append(neighbour)
        # 0
        # 1 3
        #   3 2 4
        #     2 4 
        #       4 5
        #         5 6
        #           6 7
    def dfs(self, s: int, t: int) -> IO[str]:
        """Print out a path from Vertex s to Vertex t
        using dfs. 借助系统的函数调用栈 call stack
        """
        found = False
        visited = [False] * self._num_vertices
        prev = [None] * self._num_vertices

        def _dfs(from_vertex: int) -> None:
            nonlocal found
            if found: return # 找到了就不用继续调用_dfs了，回溯递归
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self._adjacency[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)
        _dfs(s)
        print("->".join(self._generate_path(s, t, prev)))


if __name__ == "__main__":
    
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    graph.bfs(0, 7)
    graph.dfs(0, 7)

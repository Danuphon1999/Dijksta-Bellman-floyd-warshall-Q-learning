#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[float("inf") for _ in range(num_vertices)] for _ in range(num_vertices)]
        

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        

    
    def floyd_warshall(self):
        dist = [[float("inf") for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        visited = [[[] for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.graph[i][j] != float("inf"):
                    visited[i][j].append(i)
                    visited[i][j].append(j)
                    dist[i][j] = self.graph[i][j] #ใส่ค่าน้ำหนักลงไปในจุดตนและปลาย
                   
                    
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if dist[i][j] > dist[i][k] + dist[k][j]: #หากเงื่อนไขเป็นจริง แสดงว่าเส้นทางปัจจุบันระหว่าง (i, j) ยาวกว่าเส้นทางที่ผ่านจุด (k) ซึ่งอาจเป็นเส้นทางที่สั้นที่สุดที่ผ่านจุด (k) ได้ ดังนั้น เราจะอัปเดตค่าระยะทางระหว่าง (i, j) เป็นระยะทางระหว่าง (i, k) บวกกับระยะทางระหว่าง (k, j) เพื่อให้ได้เส้นทางที่สั้นที่สุดใหม่
                        dist[i][j] = dist[i][k] + dist[k][j]
                        visited[i][j] = visited[i][k] + visited[k][j][1:]
        return dist, visited

# Example usage
g = Graph(6)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 1)
g.add_edge(0, 4, 4)
g.add_edge(1, 0, 2)
g.add_edge(1, 4, 5)
g.add_edge(4, 1, 5)
g.add_edge(1, 2, 6)
g.add_edge(1, 5, 2)
g.add_edge(2, 1, 6)
g.add_edge(2, 5, 3)
g.add_edge(3, 4, 8)
g.add_edge(3, 0, 1)
g.add_edge(4, 5, 1)
g.add_edge(4, 3, 8)
g.add_edge(4, 0, 4)
g.add_edge(4, 1, 5)
g.add_edge(5, 1, 2)
g.add_edge(5, 2, 3)
g.add_edge(5, 4, 1)

dist, visited = g.floyd_warshall()

# Print results
for src in range(g.num_vertices):
    for dst in range(g.num_vertices):
        if src == dst:
            print(f"Shortest path from {src} to {dst}\nDistance:{0} ")
            print(f"Visited nodes: {src}")
        elif dist[src][dst] == float("inf"):
            print(f"No path from {src} to {dst}")
        else:
            print(f"Shortest path from {src} to {dst}\nDistance: {dist[src][dst]}")
            print(f"Visited nodes: {visited[src][dst]}")


# In[ ]:





# In[ ]:





# In[ ]:





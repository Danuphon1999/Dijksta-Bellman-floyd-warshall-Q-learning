#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.inf = 999999999
      
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])
 
    def addNode(self,value):
        self.nodes.append(value)
        
        
    def print_solu(self,dist, visited):
        print("Distance=", dist)
        print("Visited nodes=", visited)
        
            
    def bellmanFord(self,src,goal):
        predecessor = dict()
        dist ={i : self.inf for i in self.nodes}
        visited = []
        dist[src] = 0
 
        for _ in range(self.V-1):
            for u, v, w in self.graph:
                if dist[u] !=  self.inf and dist[u] + w < dist[v]: #เป็นเงื่อนไขที่ใช้ตรวจสอบว่าระยะทางปัจจุบันของโหนด u ไม่ใช่ค่าอินฟินิตี้ (ค่าไม่ถูกตั้งค่า) และระยะทางปัจจุบันระหว่างโหนด u บวกกับน้ำหนักของเส้นทาง (u, v) มีค่าน้อยกว่าระยะทางปัจจุบันของโหนด v
                    dist[v] = dist[u] + w #update ค่า v เมื่อเงื่อนไขเป็นจริง
                    predecessor[v] = u
                       
        for u,v,w in self.graph:
             if dist[u] !=  self.inf and dist[u] + w < dist[v]:
                    print('Negative cycle detected')
                    return
             
        node = goal
        while node != src:
            visited.append(node)
            node = predecessor[node]
        visited.append(src)
        visited.reverse()
        
        self.print_solu(dist[goal], visited)
        
g = Graph(6)
g.addNode("0")
g.addNode("1")#A
g.addNode("2")#B
g.addNode("3")#C
g.addNode("4")#D
g.addNode("5")#E
g.addEdge("0", "1", 2)
g.addEdge("0", "3", 1)
g.addEdge("0", "4", 4)
g.addEdge("1", "0", 2)
g.addEdge("1", "4", 5)
g.addEdge("4", "1", 5)
g.addEdge("1", "2", 6)
g.addEdge("1", "5", 2)
g.addEdge("2", "1", 6)
g.addEdge("2", "5", 3)
g.addEdge("3", "4", 8)
g.addEdge("3", "0", 1)
g.addEdge("4", "5", 1)
g.addEdge("4", "3", 8)
g.addEdge("4", "0", 4)
g.addEdge("4", "1", 5)
g.addEdge("5", "1", 2)
g.addEdge("5", "2", 3)
g.addEdge("5", "4", 1)

x = str(input("src="))
y= str(input("dst="))
g.bellmanFord(x, y)


# In[ ]:





# ### 

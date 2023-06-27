Graph = {'0':{'1':2,'3':1,'4':4},'1':{'0':2,'2':6,'4':5,'5':2},'2':{'1':6,'5':3},'3':{'0':1,'4':8},'4':{'1':5,'3':8,'0':4,'5':1},'5':{'2':3,'1':2,'4':1}}
def Dijkstra(Graph,start,end):
    shortest_distance = dict()
    predecessor =dict()
    path = []
    for node in Graph:
        shortest_distance [node] = 99999 #ให้ทุกNodeให้มีค่ามากๆ
    shortest_distance [start] = 0 #ให้Nodeเริ่มเป็น0
    
    while Graph:
        minNode = None
        for node in Graph:
            if minNode is None :#เงื่อนไขที่ใช้ตรวจสอบว่าตัวแปร minNode มีค่าเป็น None หรือไม่ หาก minNode ยังไม่มีค่า จะทำการกำหนดค่า minNode เป็นโหนดแรกใน Graph
                minNode = node
            elif  shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
                
        for childNode, weight in Graph[minNode].items():
            if weight + shortest_distance[minNode]  < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode   
        Graph.pop(minNode)
        
    currentNode = end
    while  currentNode  != start:
        try:
            path.insert(0,currentNode )
            currentNode =  predecessor[currentNode]
        except KeyError:
            print('path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[end] != 99999:
        print( "Distance ="+str(shortest_distance[end]))
        print("Visited nodes="+str(path))
              
x = str(input("src ="))
y = str(input("dst ="))
Dijkstra(Graph,x,y)
    
    
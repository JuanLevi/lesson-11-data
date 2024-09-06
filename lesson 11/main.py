class Graph:
    def __init__(self,inp):
        self.nodes=inp
        self.adj=[ []*inp for i in range(inp)]

                 
    def Edge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)


    def BFS(self,source):
        visited=[False]*self.nodes
        result=[]
        queue=[]
        queue.append(source)
        visited[source]=True
        while len(queue)>0:
            m=queue.pop(0)
            result.append(m)
            for node in self.adj[m]:
                if visited[node]==False:
                    queue.append(node)
                    visited[node]=True
        return result


    
graph1=Graph(4)

graph1.Edge(1,2)
graph1.Edge(1,3)
graph1.Edge(2,4)
graph1.Edge(4,3)

print(graph1.BFS(0))
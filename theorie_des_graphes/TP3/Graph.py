#!/usr/bin/env python3
class Graph:
    """This class is a new type for describing the graphs
    """
    def __init__(self):
        """this allow the graph to be create 
        it is empty at the begin
                self.nodes is a set wich contains all the node
                self.edges is a list of every edge in the graph
                self.adjency_list is a dictionnary wich have nodes as
                key and the node linked as values
        """
        self.nodes = set()
        self.edges = list()
        self.adjency_list = dict()

    def add_a_node(self, node_name):
        """add a new node in the node set and refresh 
                the adjency_list
                node_name is a string which contain the new node 
                comming into the graph
        """
        if node_name in self.nodes:
            print("ce node est deja dans le graphe")
            return False
        self.nodes.add(node_name)
        self.adjency_list[node_name] = list()
    
    def add_an_edge(self, from_node, to_node):
        """add en edge between from_node to the node to_node
        from_node is a string which contain the parent node
        to_node is a string which contain the link's child
        """
        if not(from_node in self.nodes)\
                    or not(to_node in self.nodes):
            raise NameError("node aren't in the graph") 
            return False
        self.edges.append((from_node, to_node))
        self.adjency_list[from_node].append(to_node)
        
    def __str__(self):
        """allow the user to display the graph in a print()
        """
        nodes = ""
        for node in self.nodes:
            nodes += node + ","
        
        edges = ""
        for edge in self.edges:
            edges += edge[0] + "---->" + edge[1] + "\n"
        
        return \
        "*************************\n"\
        "*  Display of the graph *\n"\
        "*************************\n"\
        "Nodes :\n"\
        "------------\n" +\
        nodes[:len(nodes)-1] +"\n"+\
        "Edges :\n"\
        "------------\n"+\
        edges +"\n" +\
        "=========================\n"

    def breadth_first_search(self, departure):
        colors = {}
        for node in self.nodes:
            colors[node] = "white"
            
        parents = {}
        fifo = []
        fifo.append(departure)
        colors[departure] = "grey"
        parents[departure] = None
        
        for node in sorted(self.nodes):

            while fifo != []:
                in_progress = fifo[0]
                fifo.pop(0)
                for neighbour in self.adjency_list[in_progress]:
                    if colors[neighbour] == "white":
                        parents[neighbour] = in_progress
                        colors[neighbour] = "grey"
                        fifo.append(neighbour)
                colors[in_progress] = "black"
                #do here what you want for the node in_progress
                
            
            if colors[node] != "white":
                continue
            colors[node] = "grey"
            parents[node] = None
            fifo.append(node)
            
        return parents
    
    def depth_first_search(self, departure):
        colors = {}

        for node in self.nodes:
            colors[node] = "white"
            
        parents = {}
        lifo = []
        lifo.append(departure)
        colors[departure] = "grey"
        parents[departure] = None
        
        for node in sorted(self.nodes):

            while lifo != []:
                in_progress = lifo[-1]
                lifo.pop()
                for neighbour in self.adjency_list[in_progress]:
                    if colors[neighbour] == "white":
                        parents[neighbour] = in_progress
                        colors[neighbour] = "grey"
                        lifo.append(neighbour)
                colors[in_progress] = "black"
                #do here what you want for the node in_progress
            
            if colors[node] != "white":
                continue
            colors[node] = "grey"
            parents[node] = None
            lifo.append(node)
            
        return parents
        
    def is_bipartite(self):
        parents = self.depth_first_search(sorted(list(self.nodes))[0])
        
        
        colors = {}
        for key in sorted(list(parents)):
            
            if parents[key] == None:
                continue
                
            if  key in colors and \
                parents[key] in colors and\
                colors[key] != colors[parents[key]]:
                return False
                
            if key in colors:
                colors[parents[key]] = - colors[key]
                continue
                
            if parents[key] in colors:
                colors[key] = - colors[parents[key]]
                continue
            
            

            colors[key] = 1
            colors[parents[key]] = -1
        
        
        for edge in self.edges:
            from_node, to_node = edge
            if colors[from_node] == colors[to_node]:
                return False
        return True
    
    
    
if __name__ == "__main__":
    graph = Graph()
    graph2 = Graph()
    graph3 = Graph()
    for i in range(ord("a"), ord("d")):
        graph3.add_a_node(chr(i))
    
    for i in range(ord("a"), ord("i")):
        graph.add_a_node(chr(i))
        graph2.add_a_node(chr(i))
        
    graph.add_an_edge("a", "b")
    graph.add_an_edge("b", "c")
    graph.add_an_edge("c", "d")
    graph.add_an_edge("d", "e")
    graph.add_an_edge("e", "f")
    graph.add_an_edge("f", "g")
    graph.add_an_edge("g", "h")
    
    graph2.add_an_edge("a", "b")
    graph2.add_an_edge("a", "e")
    graph2.add_an_edge("b", "c")
    graph2.add_an_edge("b", "d")
    graph2.add_an_edge("c", "a")
    graph2.add_an_edge("d", "c")
    graph2.add_an_edge("d", "e")
    graph2.add_an_edge("f", "e")
    graph2.add_an_edge("g", "d")
    graph2.add_an_edge("g", "f")
    graph2.add_an_edge("g", "h")
    graph2.add_an_edge("h", "f")
    
    print(graph.is_bipartite())
    print(graph2.is_bipartite())
    
    graph3.add_an_edge("a", "b")
    graph3.add_an_edge("b", "c")
    graph3.add_an_edge("c", "a")
    print(graph3.is_bipartite())

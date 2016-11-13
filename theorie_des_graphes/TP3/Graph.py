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
        "*************************\n\
        *  Display of the graph *\n\
        *************************\n\
        Nodes :\n\
        ------------\n" +\
        nodes[:len(nodes)-1] +"\n"+\
        "Edges :\n\
        ------------\n"+\
        edges +"\n" +\
        "=========================\n"

    def breadth_first_search(self, departure):
        colors = {}
        for node in self.nodes:
            colors[node] = "white"
            
        parents = {}
        fifo = []
        for node in self.node:
            if colors[node] != "white":
                continue
            colors[node] = "grey"
            parents[node] = None
            fifo.append(node)
            
            while fifo != []:
                in_progress = fifo[0]
                fifo.pop(0)
                for neighbour in adjency_list[in_progress]:
                    if colors[neighbour] == "white":
                        parents[neighbour] = in_progress
                        colors[neighbour] = "grey"
                        fifo.append(neighbour)
                colors[in_progress] = "black"
        return parents
    
    def depth_first_search(self, departure):
        colors = {}
        for node in self.nodes:
            colors[node] = "white"
            
        parents = {}
        lifo = []
        for node in self.node:
            if colors[node] != "white":
                continue
            colors[node] = "grey"
            parents[node] = None
            lifo.append(node)
            
            while fifo != []:
                in_progress = fifo[-1]
                lifo.pop()
                for neighbour in adjency_list[in_progress]:
                    if colors[neighbour] == "white":
                        parents[neighbour] = in_progress
                        colors[neighbour] = "grey"
                        lifo.append(neighbour)
                colors[in_progress] = "black"
        return parents
        
        

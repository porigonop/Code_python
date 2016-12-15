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
        """add a new node in the node set and refresh the adjency_list
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
        """
        return a dictionnary that have node as key and node as value 
        the node in value is the parent of the node in the key
        
        use the fifo methode to determine which one is the next to look at.
        
            departure is the first starting point of the course
        """
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
                for neighbour \
                        in sorted(self.adjency_list[in_progress]):
                    if colors[neighbour] == "white":
                        parents[neighbour] = in_progress
                        colors[neighbour] = "grey"
                        fifo.append(neighbour)
                colors[in_progress] = "black"
                
                
            
            if colors[node] != "white":
                continue
            colors[node] = "grey"
            parents[node] = None
            fifo.append(node)
            
        return parents
        
        
        
        
    def recursive(self,\
                colors, \
                lifo = [], \
                departure = None, \
                parents = {}):
                
        """
         useful for depth_first_search to always look at the last
         in and change the focus with every new neighbour found
         
         it allow to go to the next node and keep the current in another 
         iteration
        """
                
        if departure != None:
            lifo = []
            lifo.append(departure)
            parents = {}
            colors[departure] = "grey"
            parents[departure] = None
        departure = None
        
        if lifo != []:
            in_progress = lifo[-1]
            lifo.pop()
            for neighbour \
                    in sorted(self.adjency_list[in_progress]):
                if colors[neighbour] == "white":
                    parents[neighbour] = in_progress
                    colors[neighbour] = "grey"
                    lifo.append(neighbour)
                    colors[in_progress] = "black"
                    parents, colors = self.recursive(lifo = lifo, \
                                            colors = colors, \
                                            departure = None, \
                                            parents = parents)
                
            if lifo == []:
                return parents, colors
    
    def depth_first_search(self, departure):
        """
        return a dictionnary that have node as key and node as value 
        the node in value is the parent of the node in the key

        use the lifo methode to determine which one is the next to look at.

            departure is the starting point of the course
        """
        colors = {}
        parents_list = []
        parents = {}
        for node in self.nodes:
            colors[node] = "white"
        in_queue, colors = self.recursive(colors = colors,\
                                            departure = departure)
        parents_list.append(in_queue)
        for node in sorted(self.nodes):
            if node in parents or colors[node] != "white":
                continue
            in_queue, colors = self.recursive(colors = colors,\
                                                departure = node)
            parents_list.append(in_queue)
            
        for parents_ in parents_list:
            for key in parents_:
                parents[key] = parents_[key]
        return parents
        
    def is_bipartite(self):
        """
this methode attribut a colors at each node in the graph, 
based on the parent/child combinaison given by the
breadth_first_search methode it while give a different color to the
child and the parent, if there is a problem in the attribution then
the graph isn't bipartite, after that, if it succed,
all the node have a color and we just have to test with the list of
edges if they all have a different colors

return True or False
        """
        parents = self.breadth_first_search(sorted(list(self.nodes))[0])
        
        
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
    
    
    def articulation_point(self):
        """
        find every articulation point in a non-oriented graph,
        with the simple algorythm that use the facts that this point
        will have 2 sons or more in a depth course algorythm
        so the method test every point and test if it has more than
        2sons
        
        return a list of node
        """
        articulation_point = []
        for root in self.nodes:
            course = self.depth_first_search(root)
            if len([node for node in course.values() \
                        if node == root]) >= 2:
                articulation_point.append(root)
        return articulation_point
            
            
        
        return articulation_point
    


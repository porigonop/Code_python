#!/usr/bin/env python3
from Graph import Graph
from pprint import pprint
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
    
    print("grahe ligne :")
    pprint(graph.depth_first_search("a"))
    
    print("\n\ngraph cours :")
    pprint(graph2.depth_first_search("a"))
    
    graph3.add_an_edge("a", "b")
    graph3.add_an_edge("b", "c")
    graph3.add_an_edge("c", "a")
    
    graph3.add_an_edge("b", "a")
    graph3.add_an_edge("c", "b")
    graph3.add_an_edge("a", "c")
    
    print("\n\ngraph 3 sommets :")
    pprint(graph3.articulation_point())

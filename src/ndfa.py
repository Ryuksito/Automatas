from src.automaton import Automaton
from src import Node, Link
from typing import List
import json

class NDFA(Automaton):
    def __init__(self, initial_node:Node, nodes:List[Node], terminal_nodes:List[Node]):
        super().__init__(initial_node, nodes, terminal_nodes)
        self.initial_node = initial_node
        self.nodes = nodes
        self.terminal_nodes = terminal_nodes 
    
    def get_next_nodes(self, current_node:Node, etiquette:str):
        next_nodes:List[Node] = []
        link:Link
        for link in current_node.links:
            if link.etiquette == etiquette or link.etiquette == '\0': 
                next_nodes.append(link.to_node)
        return next_nodes

    def accepts(self, string:str):
        paths = [(self.initial_node, 0)]
        while paths:
            node, index = paths.pop()
            
            if index == len(string):
                if node in self.terminal_nodes:
                    return True
                continue
            
            current_char = string[index]
            next_nodes = self.get_next_nodes(node, current_char)
            
            for next_node in next_nodes:
                paths.append((next_node, index + 1))
        
        return False
    
    def __str__(self):
        return json.dumps(self.automaton, indent=4)

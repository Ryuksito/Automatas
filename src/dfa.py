from .link import Link
from .node import Node
from .automaton import Automaton
import json
from typing import List

class DFA(Automaton):
    def __init__(self, initial_node:Node, nodes:List[Node], terminal_node:Node):
        super().__init__(initial_node, nodes, terminal_node)
        self.initial_node = initial_node
        self.nodes = nodes
        self.terminal_node = terminal_node

    def get_next_node(self, current_node:Node, etiquette:str):
        link:Link
        for link in current_node.links:
            if link.etiquette == etiquette:
                return link.to_node
        return None
    
    def accepts(self, string:str):
        node = self.initial_node
        for character in string:
            node = self.get_next_node(node, character)
            if node is None: return False
        return self.terminal_node.equals(node)
    
    def __str__(self):
        return json.dumps(self.automaton, indent=4)
    
    def __add__(self, other):
        return str(self) + other
    
    def __radd__(self, other):
        return other + str(self)

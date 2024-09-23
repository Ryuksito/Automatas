from src.node import Node

class Link:
    def __init__(self, from_node:Node, etiquette:str, to_node:Node):
        self.from_node = from_node
        self.etiquette = etiquette
        self.to_node = to_node
    def __str__(self):
        return "(%s --%s--> %s)" % (self.from_node.val, self.etiquette, self.to_node.val)
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)
    def equals(self, link):
        return (self.from_node == link.from_node) and (self.etiquette == link.etiquette) and (self.to_node == link.to_node)


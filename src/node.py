
class Node:
    def __init__(self, val):
        self.val = val
        self.links = []
    def add_link(self, link):
        self.links.append(link)
    def __str__(self):
        node = "(%s):\n" % self.val
        for link in self.links:
            node += "\t" + link + "\n"
        return node
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)
    def equals(self, node):
        ok = (self.val == node.val)
        if len(self.links) == len(node.links):
            for i in range(len(self.links)):
                ok = ok and (self.links[i] == node.links[i])
            return ok
        else:
            return False
import matplotlib.pyplot as plt
import networkx as nx

class Automaton:
    def __init__(self, initial_node, nodes, terminal_nodes):
        self.initial_node = initial_node
        self.nodes = nodes
        self.terminal_nodes = terminal_nodes
        self.generate_automaton()

    def generate_automaton(self):
        self.automaton = dict()
        for node in self.nodes:
            conecctions = dict()
            for link in node.links:
                conecctions[link.to_node.val] = []
            for link in node.links:
                conecctions[link.to_node.val].append(link.etiquette)
            
            self.automaton[node.val] = conecctions

    def graph(self, save:bool=False, filename="automaton.png"):
        G = nx.DiGraph()

        for node in self.automaton.keys():
            G.add_node(node, shape='circle')
            for subnode, etiquettes in self.automaton[node].items():
                filtered_etiquettes = [etiquette if etiquette != '\0' else 'ε' for etiquette in etiquettes]
                G.add_edge(node, subnode, label=', '.join(filtered_etiquettes), font_size=10)

        pos = nx.spring_layout(G, k=10)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        if save: plt.savefig(filename)
        plt.show()
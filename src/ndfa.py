from src.automaton import Automaton
import json

class NDFA(Automaton):
    def __init__(self, initial_node, nodes, terminal_nodes):
        super().__init__(initial_node, nodes, terminal_nodes)
        self.initial_node = initial_node
        self.nodes = nodes
        self.terminal_nodes = terminal_nodes  # Ahora puede haber múltiples estados finales
    
    def get_next_nodes(self, current_node, etiquette):
        # Aquí retornamos todos los nodos posibles con una transición desde current_node
        next_nodes = []
        for link in current_node.links:
            if link.etiquette == etiquette or link.etiquette == '\0':  # También permite transiciones epsilon
                next_nodes.append(link.to_node)
        return next_nodes

    def accepts(self, string):
        # Usamos una pila (stack) para explorar múltiples caminos simultáneamente
        paths = [(self.initial_node, 0)]  # Guardamos nodos y la posición en el string
        while paths:
            node, index = paths.pop()
            
            # Si hemos recorrido toda la cadena, verificamos si estamos en un nodo final
            if index == len(string):
                if node in self.terminal_nodes:
                    return True
                continue
            
            # Obtenemos los siguientes nodos posibles por la etiqueta actual
            current_char = string[index]
            next_nodes = self.get_next_nodes(node, current_char)
            
            # Agregamos los siguientes nodos a explorar en la pila
            for next_node in next_nodes:
                paths.append((next_node, index + 1))
        
        return False  # Si no llegamos a ningún estado final, la cadena no es aceptada
    
    def __str__(self):
        return json.dumps(self.automaton, indent=4)

from src import NDFA, Link, Node
import json

# Crear nodos
q0 = Node("q0")
q1 = Node("q1")
q2 = Node("q2")

# Crear enlaces
q0_1 = Link(q0, '0', q0)
q0_2 = Link(q0, '0', q1)
q0_3 = Link(q0, '1', q0)

q1_1 = Link(q1, '1', q2)

# Agregar enlaces a los nodos
q0.add_link(q0_1)
q0.add_link(q0_2)
q0.add_link(q0_3)
q1.add_link(q1_1)
q2.add_link(Link(q2, '\0', q2))


# Crear el NDFA
ndfa = NDFA(q0, [q0, q1, q2], [q2])



# Imprimir el autómata
print(ndfa)
ndfa.graph()
print(ndfa.accepts('00100\0\0'))


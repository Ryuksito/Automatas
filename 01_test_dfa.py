from src import DFA, Link, Node

# Crear nodos
q0 = Node("q0")
q1 = Node("q1")
q2 = Node("q2")

# Q0 connecciones
q0_0_q0 = Link(q0, 'b', q0)
q0_1_q1 = Link(q0, 'a', q1)

# Q1 connecciones
q1_1_q0 = Link(q1, 'b', q0)
q1_0_q2 = Link(q1, 'a', q2)


# Q2 connecciones
q2_0_q0 = Link(q2, 'b', q0)
q2_1_q2 = Link(q2, 'a', q2)

# Agregar las conecciones
q0.add_link(q0_0_q0)
q0.add_link(q0_1_q1)
q1.add_link(q1_0_q2)
q1.add_link(q1_1_q0)
q2.add_link(q2_0_q0)
q2.add_link(q2_1_q2)

# Crear el automata
a = DFA(q0, [q0, q1, q2], q1)

# Mostrar el automata y verificar si acepta cadenas
print(a)
a.graph()
print(a.accepts('abba'))
from src import Language

############################### Ejemplo de Reglas #################################
def regla_a_n_b_n(s):
    """
    Regla que define el lenguaje a^n b^n: el número de 'a's debe ser igual al número de 'b's
    y todas las 'a's deben preceder a las 'b's.
    """
    num_a = 0
    num_b = 0
    i = 0
    while i < len(s) and s[i] == 'a':
        num_a += 1
        i += 1
    while i < len(s) and s[i] == 'b':
        num_b += 1
        i += 1
    return i == len(s) and num_a == num_b

def regla_a_star_b_star(s):
    """
    Regla que define el lenguaje regular a^* b^*: 
    Cualquier número de 'a's seguido por cualquier número de 'b's.
    """
    i = 0
    while i < len(s) and s[i] == 'a':
        i += 1
    while i < len(s) and s[i] == 'b':
        i += 1

    return i == len(s)


############################### Ejemplo 1 #################################
# lenguaje a^n b^n: la misma cantidad de a's seguidas de la misma cantidad de b's
# y todas las 'a's deben preceder a las 'b's
lenguaje = Language(alphabet={'a', 'b'}, reglas=[regla_a_n_b_n])

p = 3
s = 'a'*p + 'b'*p
k_range = range(0,5)

if lenguaje.pumping_lemma_check(s, p, k_range):
    print(f"La cadena: <{s}> cumple con el Pumping Lemma.")
else:
    print(f"La cadena: <{s}> NO cumple con el Pumping Lemma (no es regular).")


print()
############################### Ejemplo 2 #################################

# lenguaje a^* b^*: cualquier cantidad de a's seguidas de cualquier cantidad de b's
lenguaje = Language(alphabet={'a', 'b'}, reglas=[regla_a_star_b_star]) 

p = 3
s = 'a'*(2*p) + 'b'*4  # cadena es valida en el lenguaje a^* b^*
s = 'aaaaaaabbbb'
k_range = range(0,5)

if lenguaje.pumping_lemma_check(s, p, k_range):
    print(f"La cadena: <{s}> cumple con el Pumping Lemma.")
else:
    print(f"La cadena: <{s}> NO cumple con el Pumping Lemma (no es regular).")
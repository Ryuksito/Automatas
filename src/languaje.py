class Language:
    def __init__(self, alphabet, reglas):
        """
        Initializes a language with an alphabet and a set of rules.
        
        :param alphabet: Language alphabet (set of allowed characters)
        :param reglas: Function or list of functions that define the rules of the language
        """
        self.alphabet = alphabet
        self.reglas = reglas
    
    def satisfies_rules(self, s):
        """
        Checks whether a string complies with the rules of the language.
        
        :param s: Chain to be verified
        :return: True if it follows the rules, False if it does not
        """
        return all(regla(s) for regla in self.reglas)

    def pumping_lemma_check(self, s, p, k_range:range):
        """
        Checks whether a string 's' satisfies the Pumping Lemma for a given value of 'p'.
        
        :param s: chain to check
        :param p: pumping constant
        :return: True if the Pumping Lemma passes, False if it fails
        """
        if len(s) < p:
            return True 

        for i in range(p+1):
            x = s[:i]
            y = s[i:p+1]
            z = s[p+1:]


            for k in k_range:
                pumped_string = x + y * k + z
                if not self.satisfies_rules(pumped_string):
                            return False
        return True
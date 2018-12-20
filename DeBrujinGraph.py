class DeBrujinGraph:

    def __init__(self, nodes: Iterable[str], k=21):
        pass # initialise la structure de données

    def __contains__(self, N: str) -> bool:
        pass # détermine si le graphe de Brujin contient le noeud N

    def __iter__(self) -> Iterable[str]:
        return self.nodes() # retourne un itérable sur les noeuds du graphe

    def load_factor() -> float:
        pass # calcule le facteur de charge de la table de hachage sous-jacente

    def add(self, N: str):
        pass # ajoute le noeud N au graphe

    def remove(self, N: str):
        pass # enlève le noeud N du graphe

    def nodes(self) -> Iterable[str]:
        pass # retourne un itérable sur les noeuds du graphe

    def predecessors(self, N: str) -> Iterable[str]:
        pass # retourne tous les prédécesseur du noeud N

    def successors(self, N: str) -> Iterable[str]:
        pass # retourne tous les successeurs du noeud N



'''
Implementation de hasMap avec sondage lineaire
(pour favoriser la rechercher lorsque l'on veut trouver les predecesseur et successeur)
TODO changer l'approche de division pour MAD
'''
class HashMapDebrujin:

    '''
    initialise le Hashmap en preparant le tableau
    et en sauvegardant la valeur
    '''
    def __init__(self, cap=100):
        self._data  = [null] * cap #table des valeurs
        self._cap = cap #capacite de la table
        self._n = 0 #nbr d'element dans la table
        # self.p = #TODO pour implementer avec nombre premier

    '''
    Fonction pour obtennir une clefs si rien
    n'est passer a setitem. Specifique au probleme passe en parametre
    '''
    def _getKey(self, value):
        pass

    def _hashFunction(self, value):
        pass

    def __len__(self):
        return self._cap

    def __getitem__:
        pass

    def __setitem__(self, k=null , v):
        if (k == null):
            k = self._getKey(v)

        pass 

    def __delitem__(self, k):
        pass

    def _resize(self):
        pass


    '''
    renvoie les clefs du tableau
    '''
    def __iter__:
        for i in range(len(self._data)):
            if (not(i == null) and not(i == _AVAIL)):
                yield self.data[i]

from random import randrange

# class DeBrujinGraph:

    def __init__(self, nodes: Iterable[str], k=21):
        self._map = self.HashMapDeBrujin(len(nodes))
        for i in range(0, len(nodes), k):
            self._map[nodes[i:k+1]] = nodes[i:k+1]

    def __contains__(self, N: str) -> bool:
        try:
            self._map[N]
            return True
        except KeyError:
            return false

        
    def __iter__(self) -> Iterable[str]:
        return self.nodes() # retourne un itérable sur les noeuds du graphe

    def load_factor() -> float:
        return(self._map._n / self._map._mask)

    def add(self, N: str):
        self._map[N] = N

    def remove(self, N: str):
        del self._map[N]

    def nodes(self) -> Iterable[str]:
        i = 0
        while(i < self._map._mask)
            try:
                yield(self._map[i])
            except KeyError:
                i +=  0

    def predecessors(self, N: str) -> Iterable[str]:
        pred_list = []
        options = {1: A, 2: C, 3: G, 4: T}
        for i in range(1, 5):
            try:
                if options[i] != N[:1]:
                    pred_list += self._map[options[i] + N[1:]]
            except KeyError:

    def successors(self, N: str) -> Iterable[str]:
        succ_list = []
        options = {1: A, 2: C, 3: G, 4: T}
        for i in range(len(options)):
            try:
                if(options[i] != N[-1:]):
                    succ_list += self._map[[N:-1] + options[i]]
            except KeyError:

'''
Implementation de hasMap avec sondage lineaire
(pour favoriser la rechercher lorsque l'on veut trouver les predecesseur et successeur)
TODO changer l'approche de division pour MAD
'''
class HashMapDeBrujin:

    class _Item:
        #enregistrement statique et efficace
        __slots__ = '_key', '_value'
 
        #constructeur avec valeur None de défaut pour valeur
        def __init__( self, k, v = None ):
            self._key = k
            self._value = v
 
        #égalité de clé
        def __eq__( self, other ):
            return self._key == other._key
 
        #non-égalité de clé
        def __ne__( self, other ):
            return not( self == other )
 
        #clé strictement inférieure
        def __lt__( self, other ):
            return self._key < other._key
 
        #clé supérieure ou égale
        def __ge__( self, other ):
            return self._key >= other._key
 
        #prettyprint d'un élément
        def __str__( self ):
            return "<" + str( self._key ) + "," + str( self._value ) + ">"
 
        #accède la clé
        def key( self ):
            return self._key
 
        #accède la valeur
        def value( self ):
            return self._value

    _AVAIL = object() #_AVAIL definie un objet qui a ete effacer

    '''
    initialise le Hashmap en preparant le tableau
    et en sauvegardant la valeur
    '''
    def __init__(self, cap=100, p=109345121):
        self._data  = [None] * cap #table des valeurs
        self._n = 0 #nbr d'element dans la table
        self._prime = p # nombre premier pour la compression
        self._scale = 1 + randrange(p-1) #
        trouver = False
        while not trouver:
            self._scale = 1 + randrange(p-1)
            if not (self._scale % p) == 0:
                trouver = True
        self._shift = randrange(p)
        self._mask = cap
        self._mid_prime = self._get_mid_prime()

    def _get_mid_prime(self):
        result = [True]*(self._mask + 1)
        for i in range(2, len(result)):
            if(result[i]):
                if(i >= self._mask/2):
                    return i
                else:
                    for j in range(i, len(result), i):
                        result[j] = False

    def _gethashkey(self, key):
        k = 0
        options = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        for letter in key:
            k = (k*10) + options[letter]
        return k

    def _hashFunction(self, key):
        k = self._gethashkey(key)
        # Fonction de Hachage MAD
        return(k * self._scale + self._shift) % self._prime % self._mask

    def _secondaryHashFunction(self, key, firstAvail):
        return((firstAvail+1) % self._mask)


    def __len__(self):
        return self._n

    def __getitem__(self, key):
        """Getter qui retourne la valeur de la hashMap a l'index entrer en parametre"""
        i = self._hashFunction(key)
        if self._data[i] is None:
            raise KeyError
        else:
            while self._data[i].key() != key:
                i = self._secondaryHashFunction(key, i)
                if self._data[i] is None:
                    raise KeyError
            return self._data[i]    

    def __setitem__(self, key, item):
        """Setter qui set a un index du tableau la valeur entrer en parametre"""
        i = self._hashFunction(key)
        if self._data[i] is None or self._data[i] is self._AVAIL:
            self._data[i] = self._Item(key, item)
        else:
            i = self._find_slot(i, key)
            self._data[i] = self._Item(key, item)

        self._n +=1
        self._resize()

    def _find_slot(self, spot, key):
        firstAvail = spot
        while True:
            if self._data[firstAvail] is None or self._data[firstAvail] is self._AVAIL:
                return firstAvail
            else:
                #Utilisation de Hachage Double pour trouver firstAvail
                firstAvail = self._secondaryHashFunction(key, firstAvail)
                #print(firstAvail)

    def __delitem__(self, key):
        i = self._hashFunction(key)
        while self._data[i].key() != key:
            i = self._secondaryHashFunction(key, i)
            if self._data[i] is None :
                raise KeyError
        self._data[i] = self._AVAIL
        self._n -=1

    def _resize(self):
        c = self._mask*4
        if (self._n/self._mask) < 0.75:
            return
        else:
            old = self._data[:]
            self._mask = c
            self._data = [None]*c
            for item in old:
                if item is not self._AVAIL and item is not None:
                    self[item.key()] = item.value() 


    def test(self):
        for i in range(self._mask):
            print(i, self._data[i])

    '''
    renvoie les clefs du tableau
    '''
    def __iter__(self):
        for i in range(len(self._data)):
            if (not(i == None) and not(i == self._AVAIL)):
                yield (self._data[i].key(),self._data[i].value())

if __name__ == '__main__':
    for i in range(100):
        hashmap = HashMapDeBrujin(10, 47)
        hashmap['ACGT'] = 'ACGT'
        hashmap['AA'] = '1'
        hashmap['AC'] = '2'
        hashmap['AG'] = '3'
        hashmap['AT'] = '4'
        hashmap['AAA'] = '5'
        hashmap['AAC'] = '6'
        hashmap['AAG'] = '7'
        hashmap['AAT'] = '8'
        hashmap.test()
        print("===========================")
    del hashmap['ACGT']
    hashmap.test()
    # VERIFIER BENCHMARK AVEC RAND SCALE

    #PETIT TABLE SIZE = ERREUR!

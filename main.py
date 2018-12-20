import gzip
from itertools import islice

'''
Fonciton de lecture pour les fichiers FASTA
Formats de fichiers
FASTA
Le fichier FASTA contient des séquences identifiées et annotés brièvement par une description.
>ID DESCRIPTION
SEQUENCE
'''
def read_fasta(path):
    with gzip.open(path, 'rt') as f:
        accession, description, seq = None, None, None
        for line in f:
            if line[0] == '>':
                # yield current record
                if accession is not None:
                    yield accession, description, seq

                # start a new record
                accession, description = line[1:].rstrip().split(maxsplit=1)
                seq = ''
            else:
                seq += line.rstrip()

'''
FASTQ

Le format FASTQ contient des fragments annotés
avec une qualité pour chaque symboles lus par le système de séquençage.
@SEQID DESCRIPTION
SEQUENCE
+
QUALITY
'''
def read_fastq(path):
    with gzip.open(path, 'rt') as f:
        seqid, description = f.readline()[1:].rstrip().split(maxsplit=1)
        sequence = f.readline().rstrip()
        _ = f.readline()
        quality = f.readline().rstrip()
        yield seqid, description, sequence, quality

'''
Fonction de lecture des fichiers BED
Le format BED est un format tabulaire de 3 à 12 colonnes
qui contient des annotations de sous-séquences.

"reference    start    end    name"
Dans ce TP, nous utiliserons seulement les 4 premières colonnes pour identifier
la référence, une paire de coordonnées `(début, fin)` et l'identifiant du
contig assemblé depuis notre graphe de Brujin.
'''
def read_bed(path):
    with open(path) as f:
        ref, start, end, name = f.readline().rstrip().split('\t')
        yield ref, int(start) - 1, int(end), name

seq = next(read_fasta('GCF_000002985.6_WBcel235_rna.fna.gz'))[2]
l = len(seq)

'''
Fonction de generation des kmer pour une sequence donner,
selon une grandeur k specifie
'''
def generate_kmers(k, seq):
    yield seq[0:k]
    for i in range(1,len(seq)-k+1):
        yield seq[i:i+k]
'''
Debut des tests
'''

a = read_fastq("reads.fastq.gz")
for i in a:
    print(i[0],i[1],"\n",i[2],"\n",i[3])
    b = [i for i in generate_kmers(4, i[2])]

for i in b:
    print(i)

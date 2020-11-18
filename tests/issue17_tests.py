'''Unit tests for issue17.py'''

from htsinfer.issue17 import extend_motifs
import pytest

sequences_DNA = [
    "CGTACTTGGTTCGATCAACCAGGCCGTAAAGTACGACGTCATCAAAAACGTTTAAACAAA",
    "GCTCAACGTGTTGCTCCTCGACCAGCCAAAGGTTCATTACGGCCAGTTGTTCGTGGTACC",
    "GCTGCTGGTCTTCATCCAACCTATGCTCGAACCATCGGTATTTCAGTTGATCATCGACGA",
    "ACACGTCGTTATAACATGAAAGTACGTTCTGGACGCGGTTTTTCTTTGGATGAAATTCGT"
    ]

sequences_RNA = [
    "CGUACUUGGUUCGAUCAACCAGGCCGUAAAGUACGACGUCAUCAAAAACGUUUAAACAAA",
    "GCUCAACGUGUUGCUCCUCGACCAGCCAAAGGUUCAUUACGGCCAGUUGUUCGUGGUACC",
    "GCUGCUGGUCUUCAUCCAACCUAUGCUCGAACCAUCGGUAUUUCAGUUGAUCAUCGACGA",
    "ACACGUCGUUAUAACAUGAAAGUACGUUCUGGACGCGGUUUUUCUUUGGAUGAAAUUCGU"
    ]

core_motifs_DNA = ["GCT", "TAT", "ACA", "CGC", "TGT", "GAG", "AAA", "GGG", "CCC", "TTT"]

core_motifs_RNA = ["GCU", "UAU", "ACA", "CGC", "UGU", "GUG", "AAA", "GGG", "CCC", "UUU"]

#Class TestInfer:
    '''Test extend_motifs function'''
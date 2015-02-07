# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 22:34:23 2015

@author: Tiago
"""

from Bio import Entrez
Entrez.email = "tiago_alves26@hotmail.com"     
#pesquisa = Entrez.esearch(db="Taxonomy", term="Neisseria gonorrhoeae", id="242231", retmode="text")
#record = Entrez.read(pesquisa)
#print record


handle = Entrez.efetch(db="Taxonomy", id="242231", retmode="xml")
record = Entrez.read(handle)

print "Linhagem:",str(record[0]["Lineage"])
print "Codigo genetico:\n"
print "\tTabela de traducao:",str(record[0]["GeneticCode"]["GCId"])
print "\tNome do codigo genetico:",str(record[0]["GeneticCode"]["GCName"])
print "Nome cientifico:",str(record[0]["ScientificName"])

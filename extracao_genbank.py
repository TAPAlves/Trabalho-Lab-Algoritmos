# -*- coding: utf-8 -*-

#Importação
from Bio import Entrez
from Bio import SeqIO

# Abrir a nossa sequencia acedendo ao NCBI
Entrez.email = "patriciamoreira_@live.com.pt"
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="59800473", seq_start="727401", seq_stop="942520" )

#Escrever no ficheiro
SeqIO.write((SeqIO.read(handle, "gb")), 'sequence.gb', "genbank")

handle.close() 

#Imprimir na consola os dados obtidos
record = SeqIO.read("sequence.gb", "genbank")
print record


#  Para a realização deste script utilizamos como referência, os
#    slides fornecidos pelo professor no decorrer das aulas.

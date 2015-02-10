# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 17:44:27 2015

@author: Tiago
"""
#importacao de dados

from Bio.Blast import NCBIXML
from Bio import SeqIO

record = SeqIO.read("sequence.gb", "genbank")



#organizacao dos ficheiros em diferentes listas

featcds = [ ]
featgene=[]
outrasfeat=[]
for feat in range(len(record.features)):
    if record.features[feat].type == "CDS":
        featcds.append(record.features[feat])
    elif record.features[feat].type=="gene":
        featgene.append(record.features[feat])
    else:
        outrasfeat.append(record.features[feat])




tamanhos=[]#tamanhos das sequencias da query
for i in range(len(featcds)):
    result_handle = open("Blast/ficheiro_blast_proteinas"+str(i)+".xml","r")
    tamanhos.append(len(featcds[i].qualifiers["translation"][0]))
    E_VALUE_THRESH = 1
    blast_record = NCBIXML.read(result_handle)
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print "****Alinhamento****"
                    print "####Proteina %s- locus_tag: %s####"%(i,featcds[i].qualifiers["locus_tag"][0])
                    print 'Sequencia:', alignment.title
                    print 'Score:', hsp.bits
                    print 'e-value:', hsp.expect
                    print "Tamanho do alinhamento:",hsp.align_length
                    print "Cobertura da query:",float(hsp.align_length)/tamanhos[i]
                 
        

result_handle.close()
    
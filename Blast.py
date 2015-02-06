# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 17:22:28 2015

@author: Tiago
"""


#importacao de dados
from Bio.Blast import NCBIWWW
from Bio import SeqIO
import os
import time
    
#abrir ficheiro com as sequencias pretendidas e organizacao das mesmas em listas

record = SeqIO.read("sequence.gb", "genbank")
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
        
#busca da sequencia proteica presente no ficheiro genbank relativa às proteinas das features do tipo CDS.
proteinas=[]        
for feature in range(len(featcds)):
    proteinas.append(str((featcds[feature].qualifiers["translation"][0])))



#criar uma pasta designada de "Blast" para colocar os ficheiros de Blast
pasta=os.mkdir("Blast")  

#Blast

protein=0
for protein in range(76,len(proteinas)):
    save_file = open(("Blast/ficheiro_blast_proteinas%s.xml"%(protein)), "w")
    result_handle = NCBIWWW.qblast("blastp", "swissprot", proteinas[protein].format("fasta"))
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()
    protein+=1
    time.sleep(1)    
    print "A iniciar a iteracao seguinte:",protein#Para ir verificando em que posicao se encontra o Blast (processo moroso) 

#Confirmacao de Blast efetuado com sucesso
if len(protein)==len(proteinas)-1:
    print "Blast concluido com sucesso para todas as proteínas da regiao de interesse!"
            

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 17:45:25 2015

@author: Tiago
"""

#importacao de dados
from Bio import SeqIO
from Bio.SeqIO import UniprotIO
from Bio import SwissProt
import urllib
import os
'''
record = SeqIO.read("sequence.gb", "genbank")

#organizacao dos ficheiros em diferentes listas (igual ao ficheiro festures_analise.py)

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



#Obtencao dos ID da Uniprot - ADAPTADO DE GRUPO 1
proteinas=[]

for k in featcds:
   proteinas.append(k.qualifiers["protein_id"][0]) 


#print proteinas#para verificar se o conteudo esta correto

IDs=[]
erros=0    
for prot in range(len(proteinas)):
    data = urllib.urlopen("http://www.uniprot.org/uniprot/?query="+proteinas[prot]+"&sort=score").read()
    
    if len(data.split())>=3298:
        valor=(data.split()[3312])#OU 3319
        tratado=valor.strip("id=")#eliminar o id:
        tratado2=tratado[1:-1]#eliminar as aspas
        IDs.append(tratado2)
    else:
        IDs.append(proteinas[prot])
        erros+=1
print IDs
print "Erros encontrados:",erros

'''

#analise das proteinas recorrendo a uniprot
IDs=['Q5F8N9', 'Q5F8N8', 'Q5F8N7', 'Q5F8N6', 'Q5F8N5', 'Q5F8N4', 'Q5F8N3', 'Q5F8N2', 'Q5F8N1', 'Q5F8N0', 'Q5F8M9', 'Q5F8M8', 'Q5F8M7', 'Q5F8M6', 'Q5F8M5', 'Q5F8M4', 'Q5F8M3', 'Q5F8M2', 'Q5F8M1', 'Q5F8M0', 'Q5F8L9', 'Q5F8L8', 'YP_207882.2', 'Q5F8L6', 'Q5F8L5', 'Q5F8L4', 'Q5F8L3', 'Q5F8L2', 'Q5F8L1', 'Q5F8L0', 'Q5F8K9', 'Q5F8K8', 'Q5F8K7', 'Q5F8K6', 'Q5F8K5', 'Q5F8K4', 'Q5F8K3', 'Q5F8K2', 'Q5F8K1', 'Q5F8K0', 'Q5F8J9', 'Q5F8J8', 'Q5F8J6', 'Q5F8J5', 'Q5F8J4', 'Q5F8J3', 'Q5F8J2', 'Q5F8J1', 'Q5F8J0', 'Q5F8I9', 'Q5F8I8', 'Q5F8I7', 'Q5F8I6', 'Q5F8I5', 'Q5F8I4', 'Q5F8I2', 'Q5F8I1', 'Q5F8I0', 'Q5F8H9', 'Q5F8H8', 'Q5F8H6', 'Q5F8H5', 'Q5F8H4', 'Q5F8H3', 'Q5F8H2', 'Q5F8H1', 'Q5F8H0', 'Q5F8G9', 'Q5F8G8', 'Q5F8G7', 'Q5F8G6', 'Q5F8G5', 'Q5F8G3', 'Q5F8G2', 'Q5F8G1', 'Q5F8G0', 'Q5F8F9', 'Q5F8F8', 'Q5F8F7', 'Q5F8F6', 'Q5F8F5', 'Q5F8F4', 'Q5F8F3', 'Q5F8F2', 'Q5F8F1', 'Q5F8F0', 'Q5F8E9', 'Q5F8E8', 'Q5F8E7', 'Q5F8E6', 'Q5F8E5', 'Q5F8E4', 'Q5F8E3', 'Q5F8E2', 'Q5F8E1', 'Q5F8E0', 'Q5F8D8', 'Q5F8D7', 'Q5F8D6', 'Q5F8D5', 'Q5F8D4', 'Q5F8D3', 'Q5F8D2', 'Q5F8D1', 'Q5F8D0', 'Q5F8C9', 'Q5F8C8', 'Q5F8C7', 'Q5F8C6', 'Q5F8C4', 'Q5F8C3', 'Q5F8C2', 'Q5F8C1', 'Q5F8C0', 'Q5F8B9', 'Q5F8B8', 'Q5F8B7', 'Q5F8B6', 'Q5F8B4', 'Q5F8B3', 'Q5F8B2', 'Q5F8B1', 'Q5F8B0', 'Q5F8A8', 'Q5F8A7', 'Q5F880', 'Q5F8A5', 'Q5F8A4', 'Q5F8A3', 'Q5F8A2', 'Q5F8A1', 'YP_207999.2', 'Q5F898', 'Q5F897', 'Q5F896', 'Q5F895', 'Q5F894', 'Q5F893', 'Q5F892', 'Q5F891', 'Q5F890', 'Q5F889', 'Q5F888', 'Q5F887', 'Q5F886', 'Q5F885', 'Q5F884', 'Q5F883', 'Q5F882', 'Q5F881', 'Q5F880', 'Q5F879', 'Q5F878', 'Q5F877', 'Q5F876', 'Q5F875', 'Q5F874', 'Q5F873', 'Q5F872', 'Q5F871', 'Q5F870', 'Q5F869', 'Q5F868', 'Q5F867', 'Q5F866', 'Q5F865', 'Q5F864', 'Q5F863', 'Q5F862', 'Q5F861', 'Q5F860', 'Q5F859', 'Q5F858', 'Q5F857', 'Q5F856', 'Q5F855', 'Q5F854', 'Q5F853', 'Q5F852', 'Q5F851', 'Q5F850', 'YP_008914850.1', 'Q5F849', 'Q5F848', 'Q5F847', 'Q5F846', 'YP_008914851.1', 'Q5F845', 'Q5F844', 'Q5F843', 'Q5F842', 'Q5F841', 'Q5F840', 'Q5F839', 'Q5F838', 'Q5F837', 'Q5F836', 'Q5F835', 'Q5F833', 'Q5F832', 'Q5F831']
'''
pasta=os.mkdir("UniProt_proteinas")

#guardar os ficheiros em xml
for protein in range(len(IDs)):
    data = urllib.urlopen("http://www.uniprot.org/uniprot/" + IDs[protein] + ".xml")
        
    ficheiro=open("UniProt_proteinas/"+IDs[protein]+".xml","w")
    
    ficheiro.write(data.read())
    ficheiro.close()



#guardar os ficheiros em txt

for protein in range(len(IDs)):
    data_txt = urllib.urlopen("http://www.uniprot.org/uniprot/" + IDs[protein] + ".txt")
        
    ficheiro_txt=open("UniProt_proteinas/"+IDs[protein]+".txt","w")
    
    ficheiro_txt.write(data_txt.read())
    ficheiro_txt.close()
''' 
   
#Abrir todos os ficheiros para extracao de informacao - ADAPTADO DE GRUPO 1

names=[]
refs=[]
descricao=[]
aminoacidos=[]
gene=[]
comentarios=[]
proteina_seq=[]
  
    

for i in range (len(IDs)):
    if IDs[i][0]=="Q":
        handle=open("UniProt_proteinas/"+IDs[i]+".xml")
        handle_txt=open("UniProt_proteinas/"+IDs[i]+".txt")
        records=UniprotIO.UniprotIterator(handle,return_raw_comments=True)    
        for rec in records:
            
            try:
                if rec.id==IDs[i]:
                    try:
                        names.append(IDs[i])
                        names.append(rec.id)#id da proteina
                    except:
                        names.pop()                 
                        pass
                    try:
                        refs.append(IDs[i])
                        refs.append(rec.dbxrefs)#referencias a outras bases de dados
                    except:
                        refs.pop()                 
                        pass
                    try:
                        descricao.append(IDs[i])
                        descricao.append(rec.description)#descricao da prroteina
                    except:
                        descricao.pop()
                        pass
                    try:
                        aminoacidos.append(IDs[i])
                        aminoacidos.append(len(rec.seq))#tamanho da sequencia em aminoacidos
                    except:
                        aminoacidos.pop()
                        pass
                    try:
                        gene.append(IDs[i])
                        gene.append(rec.gene_name)#Nome dos genes
                    except:
                        gene.pop()                
                        pass
                   
                    try:
                        proteina_seq.append(">"+str(IDs[i])+"\n")
                        proteina_seq.append(str(rec.seq)+"\n\n")
                    except:
                        proteina_seq.pop()
                        pass
            except:
                pass
        
        
        while True:
            try:
                parser_file = SwissProt.read(handle_txt)
                for ref in parser_file.references:
                    comentarios.append(IDs[i])
                    comentarios.append(parser_file.comments)
                break    
            except:
                break
        handle.close()
    else:
        pass


#Impressao de propriedades das proteinas
print "\nId da proteina:\n"
print names

print "\nDescricao da prroteina:\n"
print descricao  

print "\nNome dos genes:\n"
print gene


print "\nTamanho da sequencia em aminoacidos:\n"
print aminoacidos


print "\nComentarios:\n"
print comentarios

print "\nReferencias a outras bases de dados:\n"
print refs




#Extrair a sequencia para posterior analise


guardar=open("UniProt_proteinas/proteinas_sequencia_uniprot"+".txt","w")
for i in range (len(proteina_seq)):
    guardar.write(proteina_seq[i])
guardar.close()

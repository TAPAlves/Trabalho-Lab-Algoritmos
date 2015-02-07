# -*- coding: utf-8 -*-
"""
Created on Sun Feb 01 15:32:59 2015

@author: Tiago
"""


#importacao de dados
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
        
    

#CDS

#1 tabela
print "\nTabela de localizacoes no genoma/Nome da proteina \n"
for k in featcds:
    print k.qualifiers["locus_tag"][0] , k.location , k.qualifiers["product"][0]
    
#2 tabela
print "\nTabela de Ids da proteina associada/Referencias \n"
for k in featcds:
    print k.qualifiers["locus_tag"][0], k.qualifiers["protein_id"][0], k.qualifiers["db_xref"][0]
    #print k.extract(record.seq)#verificar se ficamos com isto ou se colocamos noutro lado

#3 tabela - ADAPTADO DO GRUPO 1
print "\nTabela de EC Numbers \n"
for k in featcds:
    if "EC_number" in k.qualifiers:
        print k.qualifiers["locus_tag"][0],k.qualifiers["EC_number"][0]
    else:
        print k.qualifiers["locus_tag"][0],"Nao contem EC_number!"
        
#4tabela
print "\nTabela de nomes dos genes \n"
for k in featcds:
    if "gene" in k.qualifiers:
        print k.qualifiers["locus_tag"][0],k.qualifiers["gene"][0]
    else:
        print k.qualifiers["locus_tag"][0],"Nome de gene nao encontrado!"    
    
#5tabela
print "\nTabela de notas \n"
for k in featcds:
    if "note" in k.qualifiers:
        print k.qualifiers["locus_tag"][0],k.qualifiers["note"][0]
    else:
        print k.qualifiers["locus_tag"][0], "Nao estao registadas notas!"   


#6tabela - ids de proteinas hipoteticas - ADAPTADO GRUPO 1
print "Lista de proteinas hipoteticas (ID):"
hypo=[]
locus=[]
unreviewed=[]
for k in featcds:
    if k.qualifiers["product"]==["hypothetical protein"]:
        hypo.append(k.qualifiers["protein_id"][0])
        locus.append(k.qualifiers["locus_tag"][0])
        unreviewed.append(">"+str(k.qualifiers["locus_tag"][0])+"\n")
        unreviewed.append(str(k.qualifiers["translation"][0])+"\n\n")
for i in range (len(hypo)):
    print locus[i],hypo[i]




#impressao da sequencia para posterior analise da localizacao
guardar=open("proteinas_unreviewed"+".txt","w")
for i in range (len(unreviewed)):
    guardar.write(str(unreviewed[i]))
guardar.close()




#Gene

print "Tabela de informacoes acerca de features do tipo 'gene' \n"
locus=[]
for k in featgene:
    #print k #para poder perceber aquilo que usar
    print "Locus:" + str(k.qualifiers["locus_tag"][0]),  "localizacao:" , k.location, k.qualifiers["db_xref"][0] 


#Verificacao da existencia de pseudogenes:
pseudogene=[]    
for k in featgene:
    if "pseudogene" in k.qualifiers:
        pseudogene.append(k.qualifiers["locus_tag"][0])
if len(pseudogene)!=0:
    print pseudogene
else:
    print "Nao existem pseudogenes a analisar"
    
    
    
    
#outras fetures

print "\nInformacoes de outras features presentes na regiao do genoma em estudo\n"
for k in outrasfeat:
    print k





#VALIDACAO DE RESULTADOS

#carregar tabela 

ficheiro = open("ProteinTable_editada_729_970.txt", "r")
tabela=[]
for line in ficheiro.readlines():
    tabela.append(line.split("\t"))#ao carregar separamos a string por tabs. caso contrario obteria-se uma lista com os caracteres |t
ficheiro.close()





#validacao das features em comparacao com a tabela de proteinas em http://www.ncbi.nlm.nih.gov/genome/proteins/864?genome_assembly_id=169534&gi=59800473

sucesso=[]
insucesso=[]

for i in range(1,len(tabela)):
    #Locus_tag
    if str("["+"'"+tabela[i][7]+"'"+"]")== str(featcds[i-1].qualifiers["locus_tag"]):
        #GeneID        
        if str(tabela[i][5])== str(featcds[i-1].qualifiers["db_xref"][1]).strip("GeneID:"):
            #Protein Product
            if str("["+"'"+tabela[i][8]+"'"+"]")== str(featcds[i-1].qualifiers["protein_id"]):
                sucesso.append(i)                
            else:
                insucesso.append(i)
        else:
            insucesso.append(i)
    else: 
        insucesso.append(i)
        
if len(sucesso)==(len(tabela)-1):
    print "Verificacao efetuada COM sucesso!"
else:
    print "Ocorreu um erro na verificacao na/s posicao/oes:", insucesso,"."
    for i in insucesso:
        print "\nDETALHES DAS FEATURES COM ERROS NA VERIFICACAO:\n"
        print "\nTabela de dados:\n"+str(tabela[i])
        print "\nCDS:\n"+str(featcds[i-1])


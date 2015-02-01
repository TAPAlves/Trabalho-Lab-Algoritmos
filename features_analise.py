
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
print "Tabela de localizacoes no genoma/Nome da proteina \n"
for k in featcds:
    print k.qualifiers["locus_tag"] , k.location , k.qualifiers["product"]

#2 tabela
print "Tabela de Ids da proteina associada/Referencias \n"
for k in featcds:
    print k.qualifiers["locus_tag"], k.qualifiers["protein_id"], k.qualifiers["db_xref"]
    #print k.extract(record.seq)#verificar se ficamos com isto ou se colocamos noutro lado




#Gene

print "Tabela de informacoes acerca de features do tipo 'gene' \n"
for k in featgene:
    #print k #para poder perceber aquilo que usar
    print "Locus" + str(k.qualifiers["locus_tag"]),  k.location, k.qualifiers["db_xref"] 



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

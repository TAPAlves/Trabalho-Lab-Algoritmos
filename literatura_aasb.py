# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 13:41:07 2015

@author: Tiago
"""


#pesquisa no PubMed para verificar os artigos referentes a especie em estudo

from Bio import Entrez
Entrez.email = "tiago_alves26@hotmail.com"
#handle= Entrez.einfo() # permite visualizar todas as bases de dados onde posso efetuar a pesquisa
pesquisa = Entrez.esearch(db="pubmed", term="Neisseria gonorrhoeae")
record=Entrez.read(pesquisa)


print "Numero de artigos encontrados:",str(record["Count"])

#Ids que surgem no nosso record
print "Lista de Ids:",str(record["IdList"])+"\n"

for num in record["IdList"]:
    handle=Entrez.efetch(db="pubmed",id=str(num) , retmode="xml")
    dados=Entrez.read(handle)
    
    #impressao de dados acerca dos artigos    
    print "\nTitulo do artigo:\n"
    print "\t"+repr(dados[0]["MedlineCitation"]["Article"]["ArticleTitle"])
    
    print "\nLista de autores:\n"
    for aut in range(len(dados[0]["MedlineCitation"]["Article"]["AuthorList"])):
        print "\tPrimeiro nome:"        
        try:
            print repr(dados[0]["MedlineCitation"]["Article"]["AuthorList"][aut]["ForeName"])
        except KeyError:
            print "Primeiro nome nao registado"
        print "\tUltimo nome:"
        try:
            print repr(dados[0]["MedlineCitation"]["Article"]["AuthorList"][aut]["LastName"])
        except:
             print "Ultimo nome nao registado"
        print "\tAfiliacao:"
        try:
            print repr(dados[0]["MedlineCitation"]["Article"]["AuthorList"][aut]["AffiliationInfo"][0]["Affiliation"])
        except IndexError:
            print "Afiliacao nao registada"
        
    print "\nTipo de publicacao:\n"
    print str(dados[0]["MedlineCitation"]["Article"]["PublicationTypeList"][0])
        
    print "\nInformacao da publicacao:\n"
    print "\tISSN:"        
    try:
        print str(dados[0]["MedlineCitation"]["Article"]["Journal"]["ISSN"])
    except:
        print"ISSN nao registado"
    print "\tAbreviatura do Jornal:"
    print str(dados[0]["MedlineCitation"]["Article"]["Journal"]["ISOAbbreviation"])
    print "\tVolume:"
    try:
        print str(dados[0]["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["Volume"])
    except:
        print "Volume inexistente"
    print "\tAno da publicacao:"
    print str(dados[0]["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]["Year"])
    print "\tIdentificacao do local da publicacao:"        
    try:
        print str(dados[0]["MedlineCitation"]["Article"]["ELocationID"][0])
    except:
        print"Local nao reconhecido"
    print "\tAbstract do artigo:"
    print str(dados[0]["MedlineCitation"]["Article"]["Abstract"]["AbstractText"])
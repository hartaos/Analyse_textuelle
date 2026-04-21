#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:45:58 2025

@author: jerem
"""

#En se basant sur le COURS 2

import os
import pandas as pd
import treetaggerwrapper
import xlsxwriter
import treetaggerwrapper
import os
import nltk
import matplotlib.pyplot as plt


# Spécifie le chemin du dossier TreeTagger
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGDIR="/Users/jerem/Desktop/2024/M2/Texto/Fachosphère/TreeTagger")  # Remplace par ton chemin exact

#Import Rapptor Dissident 
os.chdir("/Users/jerem/Desktop/2024/M2/Texto/Fachosphère")
chemin = "leraptor.txt"           # nom du fichier contenant nos textes        
f=open(chemin,"r")   
textebrut1 = f.read() 


tags=tagger.tag_text(textebrut1)
print (tags)

####export Vers Excel#### A
LH = xlsxwriter.Workbook('/Users/jerem/Desktop/2024/M2/Texto/Fachosphère/LemRaptor.xlsx')
export= LH.add_worksheet()

row=1
col=0
export.write(0,0,'Graphies')
export.write(0,1,'POS')
export.write(0,2,'Lemmes')

for element in tags:
    extrait=element.split('\t')[0]
    export.write(row,col,extrait)
    extrait=element.split('\t')[1]
    export.write(row,col+1,extrait)
    extrait=element.split('\t')[2]
    export.write(row,col+2,extrait)
    row += 1
    col=0    

LH.close()

#BARBARE CIVILISE
#Import BARBARE CIVILISE
os.chdir("/Users/jerem/Desktop/2024/M2/Texto/Fachosphère")
chemin1 = "Barbare_civilisé.txt" # nom du fichier contenant nos textes        
f1=open(chemin1,"r")   
textebrut2 = f1.read() 

tags1=tagger.tag_text(textebrut2)
print (tags1)

####export Vers Excel#### A
import xlsxwriter
LH1 = xlsxwriter.Workbook('/Users/jerem/Desktop/2024/M2/Texto/Fachosphère/LemBarbare.xlsx')
export= LH1.add_worksheet()

row=1
col=0
export.write(0,0,'Graphies')
export.write(0,1,'POS')
export.write(0,2,'Lemmes')

for element in tags1:
    extrait=element.split('\t')[0]
    export.write(row,col,extrait)
    extrait=element.split('\t')[1]
    export.write(row,col+1,extrait)
    extrait=element.split('\t')[2]
    export.write(row,col+2,extrait)
    row += 1
    col=0    

LH1.close()


#############################################
#############################################
####### Analyse
#############################################
#############################################

barbare = r"/Users/jerem/Desktop/2024/M2/Texto/Fachosphère/LemBarbare.xlsx"
raptor = r"/Users/jerem/Desktop/2024/M2/Texto/Fachosphère/LemRaptor.xlsx"

# Chargement des fichiers
barbare_df = pd.read_excel(barbare)
raptor_df = pd.read_excel(raptor)

# Vérification de la structure des colonnes
print("Aperçu des données Barbare :")
print(barbare_df.head())
print("\nAperçu des données Raptor :")
print(raptor_df.head())


#Ici on prend tout les lemmes 
# Comptage des occurrences pour chaque catégorie grammaticale
barbare_pos_counts = barbare_df['POS'].value_counts()
raptor_pos_counts = raptor_df['POS'].value_counts()

# Fusionner les deux séries pour comparer
pos_comparison = pd.DataFrame({
    'Barbare': barbare_pos_counts,
    'Raptor': raptor_pos_counts
}).fillna(0)  # Remplacer les NaN par 0

# Création des histogrammes comparatif

# ici on choisi les lemmes à conserver
graph1 = ['NOM', 'ADJ','ADV']
barbare_filtered = barbare_df[barbare_df['POS'].isin(graph1)]
raptor_filtered = raptor_df[raptor_df['POS'].isin(graph1)]

# Comptage des occurrences pour chaque catégorie grammaticale
barbare_pos_counts = barbare_filtered['POS'].value_counts()
raptor_pos_counts = raptor_filtered['POS'].value_counts()

# Fusionner les deux séries pour comparer
pos_comparison = pd.DataFrame({
    'Barbare': barbare_pos_counts,
    'Raptor': raptor_pos_counts
}).fillna(0)

# Création de l'histogramme comparatif
plt.figure(figsize=(12, 6))
pos_comparison.plot(kind='bar', color=['skyblue', 'salmon'], edgecolor='black')
plt.title('Comparaison des catégories grammaticales (NOM et ADJ)')
plt.xlabel('Catégorie grammaticale')
plt.ylabel('Nombre d’occurrences')
plt.xticks(rotation=45)
plt.legend(["Barbare", "Raptor"])
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()

#############################################
####### Comparaison des pronoms #############
#############################################

graph2  = ['PRO:IND','PRO:PER','PRO:DEM','PRO:REL']

barbare_filtered = barbare_df[barbare_df['POS'].isin(graph2)]
raptor_filtered = raptor_df[raptor_df['POS'].isin(graph2)]

# Comptage des occurrences pour chaque catégorie grammaticale
barbare_pos_counts = barbare_filtered['POS'].value_counts()
raptor_pos_counts = raptor_filtered['POS'].value_counts()

# Fusionner les deux séries pour comparer
pos_comparison = pd.DataFrame({
    'Barbare': barbare_pos_counts,
    'Raptor': raptor_pos_counts
}).fillna(0)

# Création de l'histogramme comparatif
plt.figure(figsize=(12, 6))
pos_comparison.plot(kind='bar', color=['skyblue', 'salmon'], edgecolor='black')
plt.title('Comparaison des pronoms gramaticaux')
plt.xlabel('pronom grammaticale')
plt.ylabel('Nombre d’occurrences')
plt.xticks(rotation=45)
plt.legend(["Barbare", "Raptor"])
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()

#############################################
###### Comparaison des verbes
#############################################

graph3 = [ 'VER:pper','VER:pres','VER:futu','VER:infi','VER:simp','VER:impf','VER:subp','VER:cond','VER:impe','VER:ppre','VER:subi']

barbare_filtered = barbare_df[barbare_df['POS'].isin(graph3)]
raptor_filtered = raptor_df[raptor_df['POS'].isin(graph3)]

# Comptage des occurrences pour chaque catégorie grammaticale
barbare_pos_counts = barbare_filtered['POS'].value_counts()
raptor_pos_counts = raptor_filtered['POS'].value_counts()

# Fusionner les deux séries pour comparer
pos_comparison = pd.DataFrame({
    'Barbare': barbare_pos_counts,
    'Raptor': raptor_pos_counts
}).fillna(0)

# Création de l'histogramme comparatif
plt.figure(figsize=(12, 6))
pos_comparison.plot(kind='bar', color=['skyblue', 'salmon'], edgecolor='black')
plt.title('Comparaison des temps verbaux')
plt.xlabel('Temps de conjugaison')
plt.ylabel('Nombre d’occurrences')
plt.xticks(rotation=45)
plt.legend(["Barbare", "Raptor"])
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()

###############################
######## comptage  ###########
##############################

print("Colonnes disponibles dans barbare_df :")
print(barbare_df.columns)
print("\nColonnes disponibles dans raptor_df :")
print(raptor_df.columns)

# Filtrer les catégories pour les noms et verbes
noms_pos = ['NOM']
adv_pos = ['ADV']
verbes_pres = ['VER:pres']
verbes_pper = ['VER:pper']
verbes_infi = ['VER:infi']


# Compter les occurrences des noms
barbare_noms_count = barbare_df[barbare_df['POS'].isin(noms_pos)]['Lemmes'].value_counts()
raptor_noms_count = raptor_df[raptor_df['POS'].isin(noms_pos)]['Lemmes'].value_counts()

# Compter les occurrences des ADV
barbare_adv_count = barbare_df[barbare_df['POS'].isin(adv_pos)]['Lemmes'].value_counts()
raptor_adv_count = raptor_df[raptor_df['POS'].isin(adv_pos)]['Lemmes'].value_counts()

# Compter les occurrences des verbes au présent
barbare_verbes_count = barbare_df[barbare_df['POS'].isin(verbes_pres)]['Lemmes'].value_counts()
raptor_verbes_count = raptor_df[raptor_df['POS'].isin(verbes_pres)]['Lemmes'].value_counts()

# Compter les occurrences des verbes au infinitif
barbare_verbes_count1 = barbare_df[barbare_df['POS'].isin(verbes_infi)]['Lemmes'].value_counts()
raptor_verbes_count1 = raptor_df[raptor_df['POS'].isin(verbes_infi)]['Lemmes'].value_counts()

# Compter les occurrences des verbes pper
barbare_verbes_count2 = barbare_df[barbare_df['POS'].isin(verbes_pper)]['Lemmes'].value_counts()
raptor_verbes_count2 = raptor_df[raptor_df['POS'].isin(verbes_pper)]['Lemmes'].value_counts()

# Affichage des résultats
print("Top 10 des noms (Barbare) :\n", barbare_noms_count.head(10))
print("\nTop 10 des noms (Raptor) :\n", raptor_noms_count.head(10))
print("Top 10 des ADV (Barbare) :\n", barbare_adv_count.head(10))
print("\nTop 10 des ADV (Raptor) :\n", raptor_adv_count.head(10))
print("\nTop 10 des verbes au présent(Barbare) :\n", barbare_verbes_count.head(10))
print("\nTop 10 des verbes au présent (Raptor) :\n", raptor_verbes_count.head(10))
print("\nTop 10 des verbes à l'infinitif (Barbare) :\n", barbare_verbes_count1.head(10))
print("\nTop 10 des verbes au l'infinitif (Raptor) :\n", raptor_verbes_count1.head(10))
print("\nTop 10 des verbes pper (Barbare) :\n", barbare_verbes_count2.head(10))
print("\nTop 10 des verbes pper présent (Raptor) :\n", raptor_verbes_count2.head(10))




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:49:36 2025

@author: jerem
"""

#Importation des outils nécéssaire à l'analyse"
import os
import csv
import re
from collections import defaultdict
from nltk.corpus import stopwords
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Charger les stopwords français
stopwords_fr = set(stopwords.words('french'))
# Fonction pour nettoyer un texte
def nettoyer_texte(texte):
    texte = re.sub(r"[^\w\s]", " ", texte)  # Supprimer ponctuation
    texte = re.sub(r"\d+", " ", texte)      # Supprimer chiffres
    texte = texte.lower()                   # Mettre en minuscules
    mots = texte.split()                    # Découper en mots
    return " ".join([mot for mot in mots if mot not in stopwords_fr])  # Supprimer stopwords

# Charger le corpus
os.chdir("/Users/jerem/Desktop/2024/M2/Texto/Fachosphère")
chemin = "corpus.txt"
f=open(chemin,"r") 
texte_brut = f.read() 

# Diviser le corpus en documents avec le séparateur ****
documents = texte_brut.split("****")[1:]  # Ignorer tout ce qui précède le premier document

# Regrouper contenus par ID
contenus_par_id = defaultdict(str)
for doc in documents:
    match = re.search(r"\*chaine_[^\s]+", doc)
    if match:
        id_extrait = match.group(0)
        contenu = re.sub(r"\*chaine_[^\s]+", "", doc).strip()
        contenus_par_id[id_extrait] += " " + contenu

# Nettoyer les textes et organiser les données
idtex = list(contenus_par_id.keys())
textes_nettoyes = [nettoyer_texte(contenu) for contenu in contenus_par_id.values()]

# Fusion globale des textes
d = ' '.join(textes_nettoyes)
e = d.split()

# Compter les mots dans tout le corpus
motot = defaultdict(int)
for mot in e:
    motot[mot] += 1

# Compter les mots par document
motex = {mot: [0] * len(idtex) for mot in motot}
for i, texte in enumerate(textes_nettoyes):
    for mot in texte.split():
        if mot in motex:
            motex[mot][i] += 1

# Exportation des données lexicales en CSV
chemin_export = "/Users/jerem/Desktop/2024/M2/Texto/Fachosphère/tablexfile.csv"
with open(chemin_export, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    
    # Écrire la première ligne avec les titres des colonnes
    writer.writerow(["Titres"] + idtex)
    
    # Écrire les mots et leurs occurrences
    for mot, effectifs in motex.items():
        if motot[mot] >= 2:  # Garder uniquement les mots présents au moins 2 fois
            writer.writerow([mot] + effectifs)

print("Export du tableau lexical entier effectué avec succès !")

###################################################
########Comparaison entre les youtubeur############
###################################################

df = pd.read_csv("/Users/jerem/Desktop/2024/M2/Texto/Fachosphère/tablexfile.csv", sep=";")
# Vérification des données chargées
print(df.head())

# Exclure la ligne 'id_doc'
df = df[df['Titres'] != 'id_doc']

# Conversion explicite en types numériques pour les colonnes de données
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    
    
df = df[df['Titres'].str.len() >= 4]

for chaine in df.columns[1:]:
    # Trier par occurrences pour cette chaîne
    top20_mots = df[['Titres', chaine]].sort_values(by=chaine, ascending=False).head(20)

    # Création du graphique
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top20_mots, x=chaine, y='Titres', palette='viridis')
    plt.title(f'20 mots les plus utilisés pour {chaine}')
    plt.xlabel('Nombre d’occurrences')
    plt.ylabel('Mots')
    plt.grid(axis='x', linestyle='--', linewidth=0.5)
    plt.show()

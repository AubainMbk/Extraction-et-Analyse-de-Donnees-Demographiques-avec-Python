# PopScraper: Extraction et Analyse de Données Démographiques avec Python

## Description

PopScraper est un projet Python alliant web scraping et analyse de données pour extraire des informations sur la population mondiale depuis le site Worldometers. Ce projet inclut une analyse approfondie des tendances démographiques, ainsi que la prédiction des populations futures en utilisant des techniques de machine learning.

L'objectif est de scraper les données démographiques en temps réel, de les analyser pour en tirer des insights et de prédire les populations futures pour les années à venir.
Objectifs du Projet

    Récupérer des données de population mondiale à partir de Worldometers via le scraping web.
    
    Nettoyer et transformer les données pour une analyse approfondie.
    
    Analyser les tendances démographiques passées à l'aide de techniques de visualisation.
    
    Prédire les populations futures en utilisant des modèles de régression linéaire et des modèles non linéaires.
    
    Comparer les prédictions avec les données réelles pour évaluer la précision du modèle.

## 🚀Fonctionnalités

    Web Scraping avec BeautifulSoup :
    
        Extraction des données de population par pays en temps réel depuis la page Worldometers.
        
        Sauvegarde des données dans des fichiers CSV ou JSON pour les analyses ultérieures.

    Analyse et Visualisation des Données :
    
        Exploration et nettoyage des données avec Pandas.
        Visualisation des tendances démographiques avec Matplotlib et Seaborn.

    Prédiction de la Population Future :
        Modélisation de la population future avec régression linéaire et Random Forest pour affiner les prédictions.

    Comparaison et Validation des Prédictions :
        Comparaison des prédictions de population future avec les tendances réelles pour évaluer la précision.

## 📊 Exemple de Visualisation

Voici des exemples des graphiques générés dans ce projet pour analyser et prédire la population par pays.

    Graphique de la Population Mondiale Historique vs Prédite :
    
    ![Capture d'écran 2024-11-29 223126](https://github.com/user-attachments/assets/230ce580-5bda-489d-adee-9f0225e8dcfd)


    Corrélation entre l'Année et la Population :

    ![Capture d'écran 2024-11-29 223335](https://github.com/user-attachments/assets/6b95d369-90fb-4381-a58a-cbf8e01f1afb)


Ces graphiques aident à visualiser l'évolution de la population à travers le temps, ainsi que les écarts entre les prédictions du modèle et les valeurs réelles.

## 🧑‍💻 Méthodologie
## 1. Web Scraping

Utilisation de BeautifulSoup pour analyser la structure HTML de la page Worldometers et extraire les informations sur la population de chaque pays.

    Request envoi des requêtes HTTP pour récupérer le contenu.
    
    BeautifulSoup parse le HTML et extrait les tables de données pertinentes.

## 2. Analyse des Données

Après l'extraction, les données sont nettoyées et analysées à l'aide de Pandas. Les tendances démographiques sont visualisées avec Matplotlib.

## 3. Modélisation Prédictive

Le modèle de Random Forest est utilisé pour prédire les populations futures sur la base des données historiques. 

La performance des modèles est évaluée à l'aide des métriques suivantes :

    Erreur quadratique moyenne (MSE).
    
    Score R² pour mesurer la qualité de la prédiction.

## 💬 Résultats Exemple

Les résultats incluent les prédictions des populations mondiales et par pays pour les années à venir (5-10 ans) et leur comparaison avec les données réelles.

    Précision des modèles :
        Erreur quadratique moyenne (MSE) : 1521407560806947.2
        Score R² : 0.9912037870149346
    Prédictions visuelles :
        Graphiques illustrant les populations prévues et réelles pour les pays sélectionnés.
        
        ![Capture d'écran 2024-11-29 223928](https://github.com/user-attachments/assets/9cac3ff3-7711-403a-8352-ef432423f325)


## 🤝 Contributions

Les contributions sont les bienvenues ! Si vous identifiez un problème, souhaitez ajouter une fonctionnalité ou améliorer la documentation, n'hésitez pas à ouvrir une pull request ou à soumettre une issue.

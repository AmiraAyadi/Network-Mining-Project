1.Ouvrir un shell
2. Executer le fichier "Cleaning.py" de la manière suivante:>> python 3 Cleaning.py

information: 
-Le fichier Merge.py permet de fusionner les fichiers test_info_sid.csv et test_set_sid.csv, celui-ci a aussi été utilisé pour fusionner le fichier training_set et training_info en changeant le nom des fichiers.
- Cleaning est la fonction principale, elle permet de prédire les destinataires en utilisant la mehode SVM
Pour cela, nous avons utilisé plusieurs fonctions et classe externe :
-Email: permet de céer une classe afin d'avoir plus rapidement toutes les informations concernant un email.
-TextUtils: permet après un nettoyage du texte (utilisation de la liste stopword) de créer un vecteur puis une matrice de vecteur des mots.
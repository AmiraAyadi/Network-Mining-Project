1.Ouvrir un shell
2. Executer le fichier "Cleaning.py" de la mani�re suivante:>> python 3 Cleaning.py

information: 
-Le fichier Merge.py permet de fusionner les fichiers test_info_sid.csv et test_set_sid.csv, celui-ci a aussi �t� utilis� pour fusionner le fichier training_set et training_info en changeant le nom des fichiers.
- Cleaning est la fonction principale, elle permet de pr�dire les destinataires en utilisant la mehode SVM
Pour cela, nous avons utilis� plusieurs fonctions et classe externe :
-Email: permet de c�er une classe afin d'avoir plus rapidement toutes les informations concernant un email.
-TextUtils: permet apr�s un nettoyage du texte (utilisation de la liste stopword) de cr�er un vecteur puis une matrice de vecteur des mots.
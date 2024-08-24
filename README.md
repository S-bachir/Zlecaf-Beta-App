**Zlecaf E-commerce in Africa**
*SABO bachir* 

Avant de lancer l'application, la mise en place d'une base de données et de certains packages est requise.

1. Installation de packages : Les packages dont dépend notre application se trouvent dans le fichier requirements.txt, ainsi que la version compatible de Python (3.6). Pour les installer, il faudra exécuter la commande "pip install -r requirements.txt" dans le terminal.

2. Pour la mise en place de la base de données, plusieurs fichiers se trouvent dans le répertoire "bdd". Parmi ces fichiers, il y en a 2 au format SQL à copier/coller et à exécuter dans un éditeur de requêtes SQL, ainsi qu'un autre au format Python à lancer dans votre IDE. La classe permettant la connexion entre l'application et la base de données se trouve dans "dao/pool_connection.py", où vous trouverez toutes les informations nécessaires à ce sujet. (Les articles permettant de remplir la base de données ont été scrapés à partir de plusieurs sites e-commerce entre juillet et septembre 2021).

Après avoir mis en place tout cela, vous pouvez lancer l'application dans votre IDE en passant par le fichier "main.py" se trouvant à la racine du projet, ou en exécutant la commande "python3 main.py" dans le terminal, ou "python.exe main.py" selon votre système d'exploitation.

Le fichier PDF "Rapport_Zlecaf_Beta_App" permet de mieux comprendre les enjeux de la Zlecaf en termes d'exploitation des sites de e-commerce. Il permet également de comprendre les étapes de mise en place de cette application. (Rappelons que cette application n'est qu'une maquette qui servira de plan pour une architecture plus globale).

Merci de votre attention !
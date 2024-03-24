
Ce script Python permet de générer automatiquement une lettre de motivation personnalisée pour différentes positions dans le domaine de l'informatique, en utilisant GPT-4 d'OpenAI pour générer le contenu de la lettre. Il est conçu pour des candidats à des alternances pour un BTS SIO option solutions logicielles et applications métiers.

## Fonctionnalités

- Sélection d'un poste parmi une liste prédéfinie.
- Personnalisation du nom de l'entreprise.
- Génération du contenu de la lettre de motivation à l'aide de GPT-4.
- Création d'un fichier PDF contenant la lettre de motivation personnalisée.

## Prérequis

Pour exécuter ce script, vous aurez besoin de Python 3.6 ou supérieur et de quelques dépendances listées dans le fichier `requirements.txt`.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en exécutant la commande suivante dans votre terminal :

pip install -r requirements.txt

3. Assurez-vous d'avoir une clé API valide pour OpenAI et de la configurer dans le script.

## Utilisation

Pour lancer le script, naviguez jusqu'au dossier contenant le script et exécutez :

python generate_motivation_letter.py


Suivez ensuite les instructions à l'écran pour sélectionner un poste et entrer le nom de l'entreprise. Le script générera un fichier PDF `custom_letter.pdf` contenant votre lettre de motivation personnalisée.



## Licence

Ce projet est distribué sous la Licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

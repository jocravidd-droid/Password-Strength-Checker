# Password Strength Checker
Petit outil en Python qui évalue la robustesse d'un mot de passe 
selon plusieurs critères de sécurité (longueur, majuscules, 
chiffres, caractères spéciaux).

Projet réalisé dans le cadre de mon apprentissage autodidacte 
en Python, en lien avec mon projet d'orientation vers la 
cybersécurité et les réseaux (Bac Pro CIEL).

# Fonctionnement !!
Cette outils d'analyse verifie si c'est condition sont remplie :

- Fonction check_length(password) → renvoie True si le mot de passe fait 8 caractères ou plus.
- Fonction check_uppercase(password) → renvoie True s'il contient au moins une majuscule.
- Fonction check_digit(password) → renvoie True s'il contient au moins un chiffre.
- Fonction check_special_char(password) → renvoie True s'il contient au moins un caractère spécial (!@#$%^&* par exemple).
- Fonction evaluate_password(password) → utilise les 4 fonctions ci-dessus, compte combien de critères sont validés, et renvoie un score : "Faible", "Moyen", "Fort".
- Boucle principale → demande un mot de passe à l'utilisateur (input()), affiche le résultat, et redemande tant qu'il tape pas "quitter".

## Objectif du projet

Ce projet a pour unique but de démontrer mes compétences techniques. Il ne poursuit aucun objectif lucratif ni éducatif. Sa réalisation dictée par le défi technique est également un pur plaisir personnel.

## Remerciements et soutien

* **@Brascq** : Testeur
* **@K2h** : Analyse
* **@lgm** : Co-pilote (un soutien précieux pour débloquer les situations complexes et orienter la réflexion, évitant ainsi le recours aux IA afin de préserver tout le plaisir du développement)

Si vous voulez le mode premium : bacprociel Okai5@

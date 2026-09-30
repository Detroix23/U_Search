# U_Search
A travers une API, permet d'accéder à des pages Web
## Fonctionnement
1) Pour éviter de potentiels sécurités, on chiffre le lien demandé par l'utilisateur
2) Le lien, envoyé via l'API, est déchiffré
3) On utilise le module "requests" pour obtenir la page Web
4) La page est renvoyée à l'utilisateur
## Déployement (sur un serveur FastAPI Cloud)
1) S'assurer de posséder un compte FastAPI Cloud
2) Installer FastAPI[standard] si non présent sur le PC
3) Entrer "fastapi deploy" dans une console au niveau du répertoire de main.py (le nom doit être conservé comme tel) et de requirement.txt
4) Suivre les instructions de la console 
## Notes
L'API est utilisable par n'importe qui possédant le lien, il est nécessaire de le garder confidentiel
FastAPI Cloud est en capacité de voir les requêtes faites et donc, les pages demandées
Les liens doivent passés par le client pour pouvoir être utilisable
Il n'y a pas de modifications de la page initiale, il est donc normal que certaines ressources (Images, CSS, JS) ne s'affichent pas
Je décline toutes responsabilités quand à l'utilisation de cet outil et ses risques

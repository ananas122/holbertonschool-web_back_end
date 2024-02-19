# Projet XYZ

Ce projet vise à fournir des solutions pour la gestion sécurisée des données sensibles, l'authentification des utilisateurs et l'accès à une base de données. Il comprend des fonctionnalités telles que l'obfuscation des informations personnellement identifiables (PII), le cryptage des mots de passe et l'authentification à la base de données à l'aide de variables d'environnement.

---

## Table des matières

- [Projet XYZ](#projet-xyz)
  - [Table des matières](#table-des-matières)
  - [Fonctionnalités](#fonctionnalités)
    - [Cryptage des mots de passe](#cryptage-des-mots-de-passe)
    - [Authentification à la base de données](#authentification-à-la-base-de-données)
  - [Licence](#licence)

---

## Fonctionnalités

- **Obfuscation des PII dans les journaux**: Cette fonctionnalité permet de masquer les informations personnellement identifiables dans les journaux d'application pour des raisons de sécurité et de confidentialité.
- **Cryptage des mots de passe**: Le projet propose des fonctions pour crypter les mots de passe des utilisateurs afin de protéger leurs informations d'identification.
- **Authentification à la base de données**: L'application permet de s'authentifier à une base de données en utilisant des variables d'environnement pour garantir la sécurité des informations d'accès.

1. `.` (point) : Correspond à n'importe quel caractère sauf un retour à la ligne.
2. `^` : Correspond au début d'une ligne.
3. `$` : Correspond à la fin d'une ligne.
4. `*` : Correspond à zéro ou plusieurs occurrences du caractère précédent.
5. `+` : Correspond à une ou plusieurs occurrences du caractère précédent.
6. `?` : Rend l'élément précédent facultatif (zéro ou une occurrence).
7. `{n}` : Correspond exactement à n occurrences du caractère précédent.
8. `{n,}` : Correspond à au moins n occurrences du caractère précédent.
9. `{n,m}` : Correspond à entre n et m occurrences du caractère précédent.
10. `[]` : Correspond à un seul caractère parmi ceux spécifiés entre crochets.
11. `[^]` : Correspond à un seul caractère qui n'est pas parmi ceux spécifiés entre crochets.
12. `\` : Permet d'échapper les caractères spéciaux pour les considérer littéralement (par exemple, `\.` correspond à un point).
13. `\d` : Correspond à un chiffre (0-9).
14. `\D` : Correspond à tout caractère qui n'est pas un chiffre.
15. `\w` : Correspond à un caractère alphanumérique (a-z, A-Z, 0-9, _).
16. `\W` : Correspond à tout caractère qui n'est pas alphanumérique.
17. `\s` : Correspond à un caractère d'espace (espace, tabulation, retour à la ligne).
18. `\S` : Correspond à tout caractère qui n'est pas un espace.
19. `(...)` : Utilisé pour grouper des expressions régulières.
20. `|` : Opérateur "OU" permettant de spécifier des alternatives.

---



### Cryptage des mots de passe

Utilisez les fonctions `encrypt_password` et `verify_password` du module `password_utils.py` pour crypter et vérifier les mots de passe respectivement.

### Authentification à la base de données

Assurez-vous que les variables d'environnement suivantes sont définies avec les valeurs appropriées :
- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

Ensuite, exécutez le script `database_auth.py` pour vous authentifier et accéder à la base de données.

---



---

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.


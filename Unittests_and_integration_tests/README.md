# Tests Unitaires en JavaScript avec Jest

Ce projet vous guide sur la manière d'écrire et d'exécuter des tests unitaires en JavaScript en utilisant le framework Jest. Les tests unitaires sont essentiels pour assurer la qualité du code et détecter les erreurs dès le début du processus de développement.

## Installation

Avant de commencer, assurez-vous d'avoir Node.js installé sur votre machine. Ensuite, suivez ces étapes pour installer Jest :

```bash
# 1. Clonez ce dépôt sur votre machine :
git clone https://github.com/votre-utilisateur/votre-projet.git

# 2. Accédez au répertoire de votre projet :
cd votre-projet

# 3. Installez Jest à l'aide de npm (Node Package Manager) :
npm install --save-dev jest

# 4. Écrire des Tests :
    Créez des fichiers de test pour chaque module que vous souhaitez tester. Ces fichiers de test doivent avoir l'extension .test.js. Par exemple, si vous avez un fichier myFunction.js, le fichier de test correspondant pourrait s'appeler myFunction.test.js.

```javascript
// myFunction.js
function add(a, b) {
  return a + b;
}

module.exports = add;


// myFunction.test.js
const add = require('./myFunction');

test('adds 1 + 2 to equal 3', () => {
  expect(add(1, 2)).toBe(3);
});

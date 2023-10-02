/**
 * Handles the signup process for a user profile by signing up the user and uploading a photo.
 * @param {string} firstName - The first name of the user.
 * @param {string} lastName - The last name of the user.
 * @param {string} fileName - The name of the photo file to upload.
 * @returns {Promise} A promise that resolves to an [objet] representing the status and value.
 */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  // Appels des 2 fonctions et attente de leur résolution ou rejet
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ])
    // map: result converti en 1 objet qui a 2 proprietes: stauts et value
    .then((results) => results.map((value) => ({ status: 'fulfilled', value })))
    .catch((errors) => {
    // Vérifie si les erreurs st sous forme de tableau
      if (Array.isArray(errors)) {
        return errors.map((value) => ({ status: 'rejected', value }));
      }
      // Si ce n'est pas un tableau, retournez une structure d'erreur
      return [{ status: 'rejected', value: errors }];
    });
}

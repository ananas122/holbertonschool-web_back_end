/**
 * Handles the signup process for a user's profile.
 * Calls the signUpUser and uploadPhoto functions concurrently using Promise.allSettled.
 * Returns an array of objects containing the status and value of each promise result.
 *
 * @param {string} firstName - The first name of the user.
 * @param {string} lastName - The last name of the user.
 * @param {string} fileName - The name of the file to upload.
 * @returns {Promise<Array>} - A promise that resolves to [objet] of with status, value properties.
 *                            If the promise is fulfilled, the value will be the resolved value.
 *                            If the promise is rejected, the value will be an error message.
 */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ])
    .then((results) => results.map((result) => {
      if (result.status === 'fulfilled') {
        return { status: result.status, value: result.value };
      }
      return { status: result.status, value: `${result.reason.name}: ${result.reason.message}` };
    }));
}

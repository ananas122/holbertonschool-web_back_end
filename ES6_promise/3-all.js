/**
 * Handles the signup process for a user profile by uploading a photo and creating a user.
 * @returns {Promise} A promise that resolves when the signup process is successful.
 * @example
 * handleProfileSignup()
 *   .then(() => console.log('Signup successful'))
 *   .catch(() => console.log('Signup system offline'));
 */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup () {
  return Promise.all([uploadPhoto(), createUser()])
    .then((result) => {
      console.log(`${result[0].body} ${result[1].firstName} ${result[1].lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}

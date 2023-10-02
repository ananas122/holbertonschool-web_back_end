/* Handles the signup process for a user profile by uploading a photo and creating a user */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    // destructuration qui extrait les results des promesses ds le tableau
    .then(([uploadPhotoResult, createUserResult]) => {
      console.log(`${uploadPhotoResult.body} ${createUserResult.firstName} ${createUserResult.lastName}`);
    })
    .catch((error) => {
      console.error('Signup system offline', error);
    });
}

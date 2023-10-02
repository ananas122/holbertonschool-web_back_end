/**
 * Uploads a photo with the provided file name.
 * @param {string} fileName - The name of the photo file to upload.
 * @returns {Promise} A promise that rejects with an error
 */
export default function uploadPhoto(fileName) {
  // new error: créer une instance de l objet Error
  return Promise.reject(new Error(`${fileName} cannot be processed`));
}

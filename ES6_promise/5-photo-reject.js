/* eslint-disable prefer-promise-reject-errors */
/**
 * Uploads a photo with the provided file name.
 * @param {string} fileName - The name of the photo file to upload.
 * @returns {Promise} A promise that rejects with an error
 */
export default function uploadPhoto(fileName) {
  return Promise.reject(`${fileName} cannot be processed`);
}

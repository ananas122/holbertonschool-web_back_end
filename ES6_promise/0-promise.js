/* Return a Promise */
export default function getResponseFromAPI () {
  return new Promise((resolve, reject) => {
    const condition = true;

    if (condition) {
      resolve('true');
    } else {
      reject(new Error('Operation failed.')); // La promesse est rejetée avec une erreur
    }
  });
}

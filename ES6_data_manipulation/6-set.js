/**
* Creates a Set from an array.
* More detailed explanation:
* - Takes an array and creates a new Set using it.
* - The Set contains unique values from the array.
* @param {Array} array The input array.
* @returns {Set} A new Set created from the array.
*/

export default function setFromArray(array) {
  return new Set(array);
}

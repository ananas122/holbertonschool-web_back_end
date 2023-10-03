/**
* Checks if a set contains all values from an array.
* Validates array input and returns a boolean indicating if the set contains all array values.
* @param {Set} set - The set to check
* @param {Array} array - The array of values to check for
* @returns {boolean} True if set contains all array values, false otherwise.
*/
export default function hasValuesFromArray(set, array) {
  if (!Array.isArray(array)) { return false; }
  // check if set contains each value
  return array.every(val => set.has(val));
}

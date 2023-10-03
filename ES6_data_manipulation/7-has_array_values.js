/**
 * Checks if a set contains all array values.
 *
 * @param {Set} set
 * @param {Array} array
 * @returns {boolean}
*/

export default function hasValuesFromArray(set, array) {
  if (!Array.isArray(array))
  return false
  // Verify if  set contains each value
  return array.every(val => set.has(val));
}

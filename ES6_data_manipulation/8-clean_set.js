/**
* Filters a set by prefix and joins values with dashes.
* Takes a set and string prefix, filters set to values starting with prefix,
* slices prefix from values, and joins with dashes.
* @param {Set} set The input set to filter and join.
* @param {string} startString The prefix to filter values by.
* @returns {string} The filtered set values joined by dashes.
*/
function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }

  return [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}

export default cleanSet;

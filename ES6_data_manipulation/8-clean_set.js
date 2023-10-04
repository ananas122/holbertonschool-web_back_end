/**
* Filters a set by prefix and joins values with dashes.
* Takes a set and string prefix, filters set to values starting with prefix,
* slices prefix from values, and joins with dashes.
* @param {Set} set The input set to filter and join.
* @param {string} prefix The prefix to filter values by.
* @returns {string} The filtered set values joined by dashes.
*/
export default function cleanSet(set, prefix) {
  if (!prefix) {
    return '';
  }

  return Array.from(set)
    .filter((value) => value.startsWith(prefix))
    .map((value) => value.slice(prefix.length))
    .join('-');
}

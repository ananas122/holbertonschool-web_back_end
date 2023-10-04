/**
* Filters a set by a start string and joins values with dashes.
* Takes a set and string startString, filters set to values starting with
* startString, removes startString from those values, and joins the filtered
* values into a string separated by dashes.
* @param {Set} set - The input set to filter
* @param {string} startString - The string to filter the set by
* @returns {string} The filtered set values joined by dashes
*/
export default function cleanSet(set, startString) {
  const string = [];

  if (
    typeof set !== 'object'
   || typeof startString !== 'string'
   || startString.length === 0
  ) {
    return '';
  }

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      string.push(item.slice(startString.length));
    }
  }
  return string.join('-');
}

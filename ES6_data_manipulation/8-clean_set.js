export default function cleanSet (set, startString) {
  const array = Array.from(set);
  if (
    typeof set !== 'object' ||
 typeof startString !== 'string' ||
 startString.length === 0
  ) {
    return '';
  }
  return array
    .filter(item => item.startsWith(startString))
    .map(item => item.slice(startString.length))
    .join('-');
}

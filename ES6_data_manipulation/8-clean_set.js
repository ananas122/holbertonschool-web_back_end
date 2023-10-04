export default function cleanset(set, startString) {
  if (!startString || !set || typeof set !== 'object') { return ''; }

  return Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}

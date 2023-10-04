/**
 * Update quantity to 100 for items with initial quantity at 1.
 * @param {Map} map - The map to update.
 * @throws {Error} If map is not a valid Map.
 */
export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [item, quantity] of map) {
    if (quantity === 1) {
      map.set(item, 100);
    }
  }
}

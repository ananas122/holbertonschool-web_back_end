/**
* Creates a groceries list as a Map.
* More detailed explanation:
* - Creates a new Map representing a groceries list.
* - The Map contains grocery items as keys and quantities as values.
* @returns {Map} The groceries list Map.
*/
export default function groceriesList() {
  return new Map([
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5]
  ]);
}

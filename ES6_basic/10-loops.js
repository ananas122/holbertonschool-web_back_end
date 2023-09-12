export default function appendToEachArrayValue(array, appendString) {
  // On crée un nouveau tableau vide pour stocker les éléments modifiés.
  const newArray = [];

  // On prc à travers les éléments du tableau d'origine
  for (const value of array) {
    // Pour chaque élément, on ajoute appendString dvt sa valeur, on le stocke ds le newArray
    newArray.push(appendString + value);
  }
  return newArray;
}

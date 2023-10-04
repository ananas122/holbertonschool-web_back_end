/**
 * Creates a DataView with Int8 value at position.
 * @param {number} length
 * @param {number} position
 * @param {number} value
 * @returns {DataView}
 * @throws {Error} If position outside range
 */
export default function createInt8TypedArray(length, position, value) {
  try {
    const buffer = new ArrayBuffer(length);
    // permet de lire et écrire dans le tampon.
    const int8 = new DataView(buffer);
    int8.setInt8(position, value);
    return int8;
  } catch (err) {
    throw Error('Position outside range');
  }
}

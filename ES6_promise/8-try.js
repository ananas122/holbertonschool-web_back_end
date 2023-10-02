/**
 * Implements a function to divide two numbers.
 *
 * @param {number} numerator - The numerator of the division.
 * @param {number} denominator - The denominator of the division.
 * @returns {number} - The result of the division.
 */
export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  }
  return (numerator / denominator);
}

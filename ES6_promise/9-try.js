/**
 * Executes a math function and adds the result or error message to a queue.
 * @param {Function} mathFunction - The math function to execute.
 * @returns {Array} - An []containing the result or error message and a processing message.
 */
export default function guardrail(mathFunction) {
  // Initialize an empty array to store the results or error messages
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(err.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}

/**
 * Returns the sum of student IDs.
 * @param {Array} students - An array of student objects.
 * @returns {number} - The sum of student IDs.
 */

export default function getStudentIdsSum (students) {
  return students.reduce((acc, val) => acc + val.id, 0);
}

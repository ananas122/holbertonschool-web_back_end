/**
 * @param {Array} students - An array of student objects.
 * @returns {Array} - An array of student IDs.
 */

export default function getListStudentIds(students) {
  // arg est un []?
  if (!Array.isArray(students)) {
    return [];
  }
  // map: convertis un [objet] en [id]
  return students.map((student) => student.id);
}

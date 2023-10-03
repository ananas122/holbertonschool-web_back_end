/**
 * Returns an array of students from a specific location.
 * @param {Array} students - An array of student objects.
 * @param {string} city - The city to filter the students by.
 * @returns {Array} - An array of student objects from the specified location.
 */

export default function getStudentsByLocation(students, city) {
  return students.filter((student) => student.location === city);
}

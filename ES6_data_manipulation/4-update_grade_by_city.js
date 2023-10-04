/**
 * Retrieves students from a specific city and updates their grades.
 * @param {Array} students - An array of student objects.
 * @param {string} city - The target city to filter students by.
 * @param {Array} grades - An array of grade objects.
 * @returns {Array} - An array of updated student objects from the specified city.
 */
export default function getStudentsByLocation(students, city, grades) {
  // Map each student, updating their grade based on the grades array
  // If no matching grade is found, default to 'N/A'
  return students
    .map((student) => ({
      ...student,
      grade: (grades.find((grade) => grade.studentId === student.id) || {}).grade || 'N/A',
    }))
    .filter((student) => student.location === city);
}

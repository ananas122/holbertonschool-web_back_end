// Crée un objet rapport sur la liste d'employés
export default function createReportObject(employeesList) {
  return {
    // Propriété "allEmployees" qui contient la liste complète d'employés par département.
    allEmployees: employeesList,

    // pour obtenir le nbr de départements.
    getNumberOfDepartments(employeesList) {
      // Object.keys() : pour obtenir les noms de départements.
      // return la lenght du tableau du nbr de départements.
      return Object.keys(employeesList).length;
    },
  };
}

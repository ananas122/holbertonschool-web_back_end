/**
 * The function `taskBlock` returns an array containing two boolean values, `task` and `task2`, based
 * on the value of the `trueOrFalse` parameter.
 * @param trueOrFalse - A boolean value that determines whether the task variables should be set to
 * true or false.
 * @returns an array containing the values of the variables `task` and `task2`.
 */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}
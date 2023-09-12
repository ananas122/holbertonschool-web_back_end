/**
 * The function `taskBlock` returns an array containing two boolean values, `task` and `task2`, based
 * on the input `trueOrFalse`.
 * @param trueOrFalse - A boolean value that determines whether to execute the if statement or not.
 * @returns an array containing the values of `task` and `task2`.
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

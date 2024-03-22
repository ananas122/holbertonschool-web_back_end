/* The code is written in JavaScript and it is a simple program that prompts the user to enter their
name and then displays it back to them. */
process.stdout.write('Welcome to Holberton School, what is your name?\n');
// écoute les entrées utlisateur
process.stdin.on('readable', () => {
  // lit l'entrée
  const input = process.stdin.read();
  if (input !== null) process.stdout.write(`Your name is: ${input}`);
});
// Event declenché end
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

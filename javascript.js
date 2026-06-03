//## Javascript
// What does this function do?
//
// Notes for Tim: Make sure I check if the ternary operator needs explaining (x?y:z)


// Inputs: Takes a function (fn) and an integer (n)

function mysteryFunction(fn, n) {
  return fn().catch((err) => n > 1 ? mysteryFunction(fn, n - 1) : Promise.reject(err));
}

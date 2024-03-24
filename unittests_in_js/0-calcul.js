function calculateNumber(a, b) {
    // Check if a and b are not numbers
    if (!isNumber(a) || !isNumber(b)) {
        throw new TypeError('Parameters must be numbers');
    }

    // Round the numbers and return their sum
    return Math.round(a) + Math.round(b);
}
module.exports = calculateNumber;
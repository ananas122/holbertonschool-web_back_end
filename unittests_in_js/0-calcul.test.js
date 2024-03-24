// 0-calcul.test.js

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
    it('should return the correct sum for integer numbers', function () {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should round and return the correct sum for non-integer numbers', function () {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should throw TypeError if parameters are not numbers', function () {
        assert.throws(() => {
            calculateNumber('a', 3);
        }, TypeError);

        assert.throws(() => {
            calculateNumber(1, 'b');
        }, TypeError);

        assert.throws(() => {
            calculateNumber('1', '2');
        }, TypeError);
    });
});

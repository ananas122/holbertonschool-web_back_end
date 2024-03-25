// 5-payment.test.js

const assert = require('assert');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi', function () {
    let consoleSpy;

    beforeEach(function () {
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(function () {
        consoleSpy.restore();
    });

    it('should log correct message with totalAmount 100 and totalShipping 20', function () {
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 120');
    });

    it('should log correct message with totalAmount 10 and totalShipping 10', function () {
        sendPaymentRequestToApi(10, 10);
        sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 20');
    });
});

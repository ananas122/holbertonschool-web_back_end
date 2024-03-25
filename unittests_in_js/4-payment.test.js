// 4-payment.test.js

const assert = require('assert');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function () {
    it('should call Utils.calculateNumber', function () {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        
        // Spy to verify console.log
        const consoleSpy = sinon.spy(console, 'log'); 
        // test
        const totalAmount = 100;
        const totalShipping = 20;
        // Calling the function
        sendPaymentRequestToApi(totalAmount, totalShipping);

        // Verifying Utils.calculateNumber call
        sinon.assert.calledOnceWithExactly(stub, 'SUM', totalAmount, totalShipping);

        // Verifying console.log message
        sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 10');

        // Restoring the stub and spy
        stub.restore();
        consoleSpy.restore();
    });
});

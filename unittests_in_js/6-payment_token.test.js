// 6-payment_token.test.js
const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI(true)', function () {
    it('should return a resolved promise with the object {data: "Successful response from the API"}', function (done) {
        getPaymentTokenFromAPI(true)
            .then(response => {
                assert.deepStrictEqual(response, { data: 'Successful response from the API' });
                done(); // Appel de done pour indiquer que le test est terminé
            })
            .catch(error => {
                done(error); // Appel de done avec une erreur en cas d'échec de la promesse
            });
    });
});

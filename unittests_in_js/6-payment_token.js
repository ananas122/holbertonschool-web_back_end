function getPaymentTokenFromAPI(success) {
    if (typeof success !== 'boolean') {
        throw new TypeError('success must be a boolean');
    }

    return new Promise((resolve, reject) => {
        if (success) {
            resolve({ data: 'Successful response from the API' });
        } else {
            reject(new Error('Unsuccessful response from the API'));
        }
    });
}

module.exports = getPaymentTokenFromAPI;

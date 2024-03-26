const request = require('supertest');
const app = require('./api');
const { expect } = require('chai');

describe('Integration testing for new endpoints', () => {
    it('GET /available_payments - should return available payment methods', async () => {
        const response = await request(app).get('/available_payments');
        expect(response.status).to.equal(200);
        expect(response.body).to.deep.equal({
            payment_methods: {
                credit_cards: true,
                paypal: false
            }
        });
    });

    it('POST /login - should return welcome message with username', async () => {
        const username = 'Alice';
        const response = await request(app)
            .post('/login')
            .send({ userName: username });
        expect(response.status).to.equal(200);
        expect(response.text).to.equal(`Welcome ${username}`);
    });
});

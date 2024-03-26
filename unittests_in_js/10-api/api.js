const express = require('express');

const port = 7865;
const app = express();

app.use(express.json());

// Endpoint GET /available_payments
app.get('/available_payments', (req, res) => {
    res.status(200).json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

// Endpoint POST /login
app.post('/login', (req, res) => {
    const { userName } = req.body;
    res.status(200).send(`Welcome ${userName}`);
});

// Endpoint GET /
app.get('/', (request, response) => {
    response.send('Welcome to the payment system');
});

// Endpoint GET /cart/:id
app.get('/cart/:id(\\d+)', (request, response) => {
    const { id } = request.params;
    response.send(`Payment methods for cart ${id}`);
});

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});

module.exports = app;

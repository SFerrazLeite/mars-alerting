'use strict';

import express from 'express';
import axios from 'axios';

const app = express();
app.use(express.json());
app.set('view engine', 'pug');
const port = process.env.PORT || 4000;

app.get('/html-example', async (req, res) => {
    try {
        res.render('index', { title: 'Hey', message: 'Hello there!'});
    } catch (e) {
        console.error(e);
    }
});

app.get('/call-example', async (req, res) => {
    try {
        const marsApiResponse = await axios.get('https://mars-storm.herokuapp.com/data');
        res.json(marsApiResponse.data);
    } catch (e) {
        console.error(e);
    }
});

app.listen(port, () => {
    console.log(`Listening on Port ${port}`);
});
  
module.exports = app;

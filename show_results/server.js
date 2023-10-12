const express = require('express');
const mongoose = require('mongoose');
const path = require('path');

const app = express();

mongoose.connect('mongodb://mongo_db:27017/resultsDB', { useNewUrlParser: true, useUnifiedTopology: true });

const DataSchema = new mongoose.Schema({
    content: String
});

const Data = mongoose.model('Data', DataSchema);

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'results.html'));
});

app.get('/results', (req, res) => {
    Data.find().exec((err, results) => {
        if (err) {
            return res.status(500).json({ message: "Internal Server Error" });
        }
        res.json(results);
    });
});

app.listen(8002, () => {
    console.log('Show Results service listening on port 8002');
});

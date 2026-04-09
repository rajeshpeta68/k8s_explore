// app.js
const express = require('express');
const app = express();

app.get('/health', (req, res) => res.send("OK"));

app.get('/api', (req, res) => res.json({ message: "Hello from backend" }));

app.listen(8080);
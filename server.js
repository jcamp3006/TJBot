const express = require('express');
const app = express();
const path = require('path');

app.use(express.static(path.join(__dirname , '/html')));

app.get('/secret', (req, res) => { res.send('Shh...')});

app.listen(5000, () => {
  console.log("Listening on port : 5000");
  console.log(path.join(__dirname , '/html'));
});
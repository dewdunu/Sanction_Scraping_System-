const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

let port = process.env.PORT || 3000;

const app = express();
app.set('trust proxy', true);
// parse requests of content-type: application/json
app.use(bodyParser.json());
// parse requests of content-type: application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors("*"));

// simple route
app.get("/", (req, res) => {
  res.json({ message: "Welcome to sanctions server." });
});

require("./app/routes/sanctions.routes.js")(app);

// set port, listen for requests
app.listen(port, () => {
  console.log(`Server is running on port ${port}.`);
});
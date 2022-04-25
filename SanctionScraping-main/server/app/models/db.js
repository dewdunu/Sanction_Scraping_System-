const { MongoClient, ServerApiVersion } = require('mongodb');
const dbConfig = require("../config/db.config.js");

// Create a connection to the database

const client = new MongoClient(dbConfig.URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverApi: ServerApiVersion.v1
});

module.exports = client;
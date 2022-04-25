const Sanction = require("../models/sanctions.model.js");

// Retrieve all Customers from the database.
exports.findAll = (req, res) => {
    Sanction.getAll((err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving users."
        });
      else res.send(data);
    });
};
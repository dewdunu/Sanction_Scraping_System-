module.exports = app => {
    const sanctions = require("../controllers/sanctions.controller.js");
    app.get("/sanctions", sanctions.findAll);
};
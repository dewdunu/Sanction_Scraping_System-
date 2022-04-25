const client = require("./db.js");

// constructor
const Sanction = function(user) {
  this.Name = user.Name;
  this.Address = user.Address;
  this.Sanction = user.Sanction;
  this.Other_Name_Logo = user.Other_Name_Logo;
  this.Nationality = user.Nationality;
  this.Effect_Date_Lapse_Date = user.Effect_Date_Lapse_Date;
  this.Grounds = user.Grounds;
};

Sanction.getAll = result => {
  client.connect(async err => {
    const collection = client.db("sanctions_db").collection("sanctions");
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }
    result(null, await collection.find().toArray())
    await client.close();
  });
};

module.exports = Sanction;
## Server 

### Framework
- Node.js

### REST API
    http://localhost:3000/sanctions
    Method : GET
    Output Format : JSON
    
    Example : 
        [
            {
                "Source" : "",
                "Name" : "",
                "Address" : "",
                "Sanction Type" : "",
                "Other Name" : "",
                "Country" : "",
                "Eligibility Period" : "",
                "Grounds" : ""
            },
            ...
        ]

### Setup and Run
#### Setup MySQL Database Credentials
- file path : app/config/db.config.js 
    ##### replace following credentials
      HOST: "localhost",
      USER: "root",
      PASSWORD : "Test123#"
#### install required libraries 
    npm install
#### start server
    npm start
        

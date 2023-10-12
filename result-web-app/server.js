const express = require('express');
var expressLayouts = require('express-ejs-layouts');
const app = express();

const PORT = 8090;
const MongoClient = require('mongodb').MongoClient;

// const url = "mongodb://localhost:27017/mydb";
const DB_HOST = 'results_db'
const DB_PORT = 27017
const DB_NAME = 'grades_app'
const url = `mongodb://${DB_HOST}:${DB_PORT}/${DB_NAME}`;  


// MongoClient.connect(url, function(err, db) {
//     if (err) throw err;
//     console.log("Connected");
//     db.close();
//   });

app.get('/', function(req, res) {
//     res.json({"hello": "world"});
//     var locals = {
//         title: 'Page Title',
//         description: 'Page Description',
//         header: 'Page Header'
//       };

//     res.render("list", locals);
// });

  MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("temp_app");
    var query = {};

dbo.collection("results").find(query).limit(1).sort({$natural:-1}).toArray(function(err, result) {
  if (err) throw err;
  console.log(result);
  db.close();

dbo.collection("course_stats").find(query).toArray(function(err, courses) {
  if (err) throw err;
  console.log(courses);
  db.close();

  var locals = {
    body: info=courses,
    update: result,
    body_length: info.length,
    update_length: result[0].courses.length
  };
  res.render("layout2", locals);

  });


});
});  

});

app.listen(PORT, function(){
    console.log('Your node js server is running on PORT:',PORT);
});
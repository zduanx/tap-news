var bodyParser = require('body-parser');
var express = require('express');
var path = require('path');
var cors = require('cors');
var passport = require('passport');

// Routers
var auth = require('./routes/auth');
var index = require('./routes/index');
var news = require('./routes/news');

var app = express();

var config = require('./config/config.json');
require('./models/main.js').connect(config.mongoDbUri);

app.use(bodyParser.json());

// view engine setup
app.set('views', path.join(__dirname, '../client/build/'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use('/static', express.static(path.join(__dirname, '../client/build/static/')));


// TODO: remove this after development is done
// app.all('*', function(req, res, next){
//   res.header("Access-Control-Allow-Origin", "*");
//   res.header("Access-Control-Allow-Headers", "X-Requested-With");
//   next();
// });

app.use(cors()); // for development xross region

// load passport strategies
app.use(passport.initialize());
var localSignUpStrategy = require('./passport/signup_passport');
var localLoginStrategy = require('./passport/login_passport');
passport.use('local-signup', localSignUpStrategy);
passport.use('local-login', localLoginStrategy);

const authChecker = require('./middleware/auth_checker');

app.use('/', index);
app.use('/auth', auth);
// if not visiting index, start check
app.use('/news', authChecker);
app.use('/news', news);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});

// // error handler
// app.use(function(err, req, res, next) {
//   // set locals, only providing error in development
//   res.locals.message = err.message;
//   res.locals.error = req.app.get('env') === 'development' ? err : {};

//   // render the error page
//   res.status(err.status || 500);
//   res.render('error');
// });

module.exports = app;

const User = require('mongoose').model('User');
const PassportLocalStrategy = require('passport-local').Strategy;

module.exports = new PassportLocalStrategy({
  usernameField: 'email',
  passwordField: 'password',
  passReqToCallback: true
}, (req, email, password, done) => {
  const userData = {
    email: email.trim(),
    password: password
  };

  const newUser = new User(userData);
  newUser.save(err => {
    console.log('Save new user!');
    if(err){
      return done(err);
    }

    return done(null);
  });
  // following codes came from signup for compare reference
  // // find a user by email address
  // return User.findOne({ email: userData.email}, (err, user)=>{
  //   if(err){return done(err);}
  //
  //   if(!user){
  //     const error = new Error('Incorrect email or password');
  //     error.name = 'IncorrectCredentialsError';
  //
  //     return done(error);
  //   }
  //
  //   // check if a hashed user's password is equal to a value saved in the database
  //   return user.comparePassword(userData.password, (passwordErr, isMatch) => {
  //     if(err) { return done(err); }
  //
  //     if(!isMatch) {
  //       const error = new Error('Incorrect email or password');
  //       error.name = 'IncorrectCredentialsError';
  //
  //       return done(error);
  //     }
  //
  //     const payload = {
  //       sub: user._id
  //     }
  //
  //     // create a token string
  //     const token = jwt.sign(payload, config.jwtSecret);
  //     const data = {
  //       name: user.email
  //     };
  //
  //     return done(null, token, data);
  //   });
  // });
});

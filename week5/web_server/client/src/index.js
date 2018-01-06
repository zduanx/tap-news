import React from 'react';
import ReactDom from 'react-dom';
import App from './App/App';
import LoginPage from './Login/LoginPage';
import SignUpPage from './SignUp/SignUpPage';

ReactDom.render(
    <App />,
    // <LoginPage />,
    // <SignUpPage />,
    document.getElementById('root')
);
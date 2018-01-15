import React from 'react';
import ReactDom from 'react-dom';
// import App from './App/App';

import {browserHistory, Router} from 'react-router';
import routes from './routes';


ReactDom.render(
    // <App />,
    <Router history={browserHistory} routes={routes} />,
    document.getElementById('root')
);

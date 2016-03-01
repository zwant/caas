// Do this once before any other code in your app
import 'babel-polyfill';
import React from 'react';
import { render } from 'react-dom';
import Relay from 'react-relay';
import App from './containers/App';
import Reducer from './reducers/reducer';
import MainRoute from './routes/main';
import Name from './components/name';

let rootElement = document.getElementById('root');
render(
  <Relay.RootContainer
    Component={Name}
    route={new MainRoute()}
  />,
  rootElement
);
// render(<App />, rootElement)


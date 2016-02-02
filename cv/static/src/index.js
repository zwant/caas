// Do this once before any other code in your app
import 'babel-polyfill'
import React from 'react';
import { render } from 'react-dom'
import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk'
import createLogger from 'redux-logger'
import { Provider } from 'react-redux';

import App from './containers/App';
import Reducer from './reducers/reducer';

const loggerMiddleware = createLogger()
const createStoreWithMiddleware = applyMiddleware(
  thunkMiddleware, // lets us dispatch() functions
  loggerMiddleware // neat middleware that logs actions
)(createStore)

const store = createStoreWithMiddleware(Reducer)
let rootElement = document.getElementById('root')

render(
  <Provider store={store}>
    <App />
  </Provider>,
  rootElement
)

import React, { Component, PropTypes } from 'react';
import Relay from 'react-relay';
import styles from './name.css';
export default class Name extends Component {
    render() {
        return(<div>This is a Name component</div>)
    }
}

export default Relay.createContainer(Name, {
  fragments: {
    allCvs: () => Relay.QL`
        fragment on Name {
          name
        }
    `
  }
});

import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as Actions from '../actions/Actions';
import Sample from '../components/Sample';
import styles from './app.css';

export default class App extends Component {
    componentDidMount() {
    }

    render() {
        const { dispatch } = this.props;
        const actions = bindActionCreators(Actions, dispatch);
        return (
            <div className={styles.app}>
                <Sample />
            </div>
        );
    }
}

export default connect(
    state => ({})
)(App)

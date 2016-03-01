import React, { Component } from 'react';
import Name from '../components/name';
import styles from './app.css';
export default class App extends Component {
    render() {
        return (
            <div className={styles.app}>
                <Name />
            </div>
        );
    }
}

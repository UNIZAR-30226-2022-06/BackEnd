    // src/App.js

    import React, { Component } from 'react';

    class App extends Component {


        state = {
            usuarios: []
          }

        componentDidMount() {
            fetch('https://db-itreader-unizar.herokuapp.com/itreaderApp/Usuarios')
            .then(res => res.json())
            .then((data) => {
              this.setState({ usuarios: data })
            })
            .catch(console.log)
          }
    }

    export default App;
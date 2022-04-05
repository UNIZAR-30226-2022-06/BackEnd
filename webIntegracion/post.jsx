    // src/App.js

    import React, { Component } from 'react';

    class App extends Component {


        state = {
            usuarios: []
          }

        componentDidMount() {
            fetch('https://db-itreader-unizar.herokuapp.com/itreaderApp/createUsuario', {
                method: 'POST',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "nombre": "tere4",
                    "nomUsuario": "tere5",
                    "password": "tere4",
                    "correo": "tere4",
                    "esAdmin": false
                })
            })
            .then(res => res.json())
            .then((data) => {
              this.setState({ usuarios: data })
            })
            .catch(console.log)
          }
    }

    export default App;
import React, { Component } from "react"
import axios from 'axios';

class App extends Component {
  state = {
    persons: [],
    status: false
  }

  componentDidMount() {
    /* Ejemplo añadir usuario */
    //const persona = { nombre: 'Laura', nomUsuario: 'Laura', password: 'Laura', correo: 'Laura', esAdmin: false};
    //axios.post('https://db-itreader-unizar.herokuapp.com/itreaderApp/createUsuario/', persona)
        //.then(response => this.setState({ status: true }));
    /* Ejemplo obtener todos los usuarios */
    axios.get('https://db-itreader-unizar.herokuapp.com/itreaderApp/Usuarios/')
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  render() {
    return (
      <ul>
        { this.state.persons.map(person => <li>{person.nombre}</li>)}
      </ul>
    )
  }
}

export default App;

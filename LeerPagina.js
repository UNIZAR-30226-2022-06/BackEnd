import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import { Component, useState } from 'react';

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
    axios.get('http://localhost:8000/itreaderApp/leerLibro/libro.epub')
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  render() {
    return (
      <ul>
        { this.state.persons.libro }
        { this.state.persons.pagina }
        { this.state.persons.contenido }
      </ul>
    )
  }
}

export default App;

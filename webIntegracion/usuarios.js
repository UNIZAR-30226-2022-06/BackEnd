import React from 'react'

    const Usuarios = ({ usuarios }) => {
      return (
        <div>
          <center><h1>Usuario List</h1></center>
          {usuarios.map((usuario) => (
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{usuario.nomUsuario}</h5>
                <p class="card-text">{usuario.nombre}</p>
                <p class="card-text">{usuario.password}</p>
                <p class="card-text">{usuario.correo}</p>
                <p class="card-text">{usuario.nombre}</p>
                <p class="card-text">{usuario.esAdmin}</p>
              </div>
            </div>
          ))}
        </div>
      )
    };

    export default Usuarios
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import { Component, useState } from 'react';

function App() {

  const [ title, setTitle ] = useState("");
  const [ cover, setCever ] = useState();

  const newBook = () => {
    const uploadData = new FormData();
    uploadData.append('title', title);
    uploadData.append('formato', 'epub');
    uploadData.append('cover', cover, cover.name);
    
    fetch('http://localhost:8000/itreaderApp/subirLibro/', {
      method: 'POST',
      body: uploadData
    })
    .then( res => console.log(res))
    .catch(error => console.log(error))
  }

  return (
    <div className="App">
      <h3>Upload images with React</h3>
      <label>
        Title
        <input type="text" value={title} onChange={(evt) => setTitle(evt.target.value)}/>
      </label>
      <br/>
      <label>
        Cover
        <input type="file" onChange={(evt) => setCever(evt.target.files[0])}/>
      </label>
      <br/>
      <button onClick={() => newBook()}>New Book</button>
    </div>
  );
}

export default App;

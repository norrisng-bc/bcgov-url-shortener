import { useState } from 'react';
// import logo from './logo.svg';
import './App.css';
import Header from './components/header/Header.jsx'
import UrlUploader from './components/url-uploader/UrlUploader';

const App = () => {

  return (
    <div className="App">
      <Header></Header>
      <div className="app-container">
        <UrlUploader></UrlUploader>
      </div>
      
    </div>
  );
};

export default App;

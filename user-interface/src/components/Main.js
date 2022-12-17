import { useState } from 'react';
import axios from 'axios';
import '../css/Main.css';

function Main() {
  let [genre, setGenre] = useState('undefined');

  const getGenre = () => {
    console.log('Execute getGenre');
    axios.get('http://localhost:8080/get-genre')
      .then((response) => {
        console.log(response)
      });
  }

  const youtubeButton = () => {
    window.open('https://www.youtube.com/', '_blank');
  };

  return (
    <div className='main'>
      <div className='box-content'>
        <h1>Genre Surf</h1>
        <label className='file-button' htmlFor='input-file'>
          Upload Audio File
        </label>
        <input type='file' id='input-file' />
        <br />
        <button className='search-button' onClick={getGenre}>What is the genre?</button>
        <h3>
          Your audio file's genre is:&nbsp;
          <u>&nbsp;&nbsp;</u>
          <u>{genre}</u>
          <u>&nbsp;&nbsp;</u>
        </h3>
        <button className='ytb-button' onClick={youtubeButton}>
          Surf In Youtube
        </button>
      </div>
    </div>
  );
}

export default Main;

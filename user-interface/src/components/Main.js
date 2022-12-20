import { useState } from 'react';
import axios from 'axios';
import '../css/Main.css';
// import { upload } from '@testing-library/user-event/dist/upload';

function Main() {
  let [genre, setGenre] = useState(
    '\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0',
  );

  const apiClient = axios.create({
    baseURL: 'http://localhost:8080',
  });

  const uploadFile = async (file) => {
    console.log('upload file and get genre.');
    try {
      const { data } = await apiClient.post('/get-genre', file).then((response) => {
        setGenre(response.data);
        console.log(response);
      });
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const upload = async (event) => {
    console.log('file: ', event.target.file);
    event.preventDefault();
    console.log('files[0]: ', event.target.file.files[0]);
    const formData = new FormData();
    formData.append('file', event.target.file.files[0]);
    await uploadFile(formData);
  };

  const youtubeButton = () => {
    window.open('https://www.youtube.com/', '_blank');
  };

  return (
    <div className='main'>
      <div className='box-content'>
        <h1>Genre Surf</h1>
        <form encType='multipart/form-data' onSubmit={upload}>
          <input type='file' name='file' id='input-file' />
          <button type='submit' className='file-button'>
            Get genre !
          </button>
        </form>
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

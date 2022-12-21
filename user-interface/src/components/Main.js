import { useState } from 'react';
import axios from 'axios';
import '../css/Main.css';
// import { upload } from '@testing-library/user-event/dist/upload';

function Main() {
  let [genre, setGenre] = useState('');
  let [audioFileName, setAudioFileName] = useState('');
  let [wait, setWait] = useState(false);

  const apiClient = axios.create({
    baseURL: 'http://localhost:8080',
  });

  const uploadFile = async (file) => {
    console.log('upload file and get genre.');
    try {
      const { data } = await apiClient.post('/get-genre', file).then((response) => {
        setWait(false);
        setGenre(response.data);
        console.log(response);
      });
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const upload = async (event) => {
    setWait(true);
    setGenre('Loading...');
    event.preventDefault();
    setAudioFileName(event.target.file.files[0].name);
    console.log('files[0]: ', event.target.file.files[0]);
    const formData = new FormData();
    formData.append('file', event.target.file.files[0]);
    await uploadFile(formData);
  };

  const changeFile = async (event) => {
    setGenre('');
    setAudioFileName(event.target.files[0].name);
  };

  const youtubeButton = () => {
    console.log(`Search ${genre} on Youtube`);
    apiClient.get('/surf-youtube', { params: { genre: genre } }).then((response) => {
      console.log(response.data);
    });
  };

  return (
    <div>
      <div className='main'>
        <div className='box-content'>
          <h1 className={`${wait ? 'loading' : ''}`}>Genre Surf</h1>
          <form encType='multipart/form-data' onSubmit={upload}>
            <label className={`file-button ${wait ? 'loading' : ''}`} htmlFor='input-file'>
              <h3>Upload Audio File</h3>
            </label>
            <input type='file' name='file' id='input-file' onChange={changeFile} />
            {audioFileName ? (
              <div>
                <h3 className='genre'>
                  <span className={`${wait ? 'loading' : ''}`}>
                    {audioFileName}'s genre is:&nbsp;
                  </span>
                  {genre ? (
                    <u>&nbsp;&nbsp;{genre}&nbsp;&nbsp;</u>
                  ) : (
                    <button type='submit' className='get-genre-button'>
                      <h3>Get Genre !</h3>
                    </button>
                  )}
                </h3>
              </div>
            ) : (
              <div>
                <br />
                <br />
              </div>
            )}
          </form>
          <button className={`ytb-button ${wait ? 'loading' : ''}`} onClick={youtubeButton}>
            <h3>Surf In Youtube</h3>
          </button>
        </div>
      </div>
    </div>
  );
}

export default Main;

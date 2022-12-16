import '../css/Main.css';

function Main() {
  const youtubeButton = () => {
    window.open('https://www.youtube.com/', '_blank');
  };

  return (
    <div class='main'>
      <h1>Genre Surf</h1>
      <label class='file-button' htmlFor='input-file'>
        Upload Audio File
      </label>
      <input type='file' id='input-file' />
      <h3>Your audio file's genre is: </h3>
      <label class='ytb-button' htmlFor='ytb-button'>
        Surf In Youtube
      </label>
      <button id='ytb-button' onClick={youtubeButton}>
        <h3>Surf In Youtube</h3>
      </button>
    </div>
  );
}

export default Main;

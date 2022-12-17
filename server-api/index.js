const express = require('express');
const app = express();
const pd = require('node-pandas-js');

app.get('/', (request, response) => {
  response.send('Executed genre-surf server');
});

app.get('/get-genre', (request, response) => {
  console.log('Client called /get-genre...\n');

  const spawn = require('child_process').spawn;
  // const inputFile = 'python-files/Data/genres_original/pop/pop.00015.wav'
  // 테스트용으로 wav파일 하나 입력
  // TODO: 사용자 파일 입력으로 수정할 것
  const inputFile = 'FreeFall.wav';

  const extractAudioFeatures = spawn('python3', ['python-files/audioFeat.py', inputFile]);
  console.log('- - - - - Called audioFeat.py - - - - -\n');
  extractAudioFeatures.stdout.on('data', (audioFeatResult) => {
    const audioFeatures = audioFeatResult.toString();
    console.log('Audio features: \n', audioFeatures);
    console.log('- - - - - Executed audioFeat.py successfully - - - - -\n');

    const predictGenre = spawn('python3', ['python-files/predictGenre.py', audioFeatures]);
    console.log('- - - - - Called predictGenre.py - - - - -\n');
    predictGenre.stdout.on('data', (genreResult) => {
      genre = genreResult.toString();
      console.log('Genre: ', genre);
      console.log('- - - - - Executed predictGenre.py successfully - - - - -\n');

      response.send(genre);
    });
    // response.send('Executed audioFeat.py successfully')
  });
});

app.listen(8080, () => {
  console.log('Server live on port 8080');
});

const express = require('express');
const app = express();
const pd = require('node-pandas-js');
const cors = require('cors');
const multer = require('multer');

app.use(cors());

const storage = multer.diskStorage({
  destination: (req, file, callback) => {
    callback(null, 'uploads/');
  },
  filename: (req, file, callback) => {
    callback(null, file.originalname);
  },
});
const upload = multer({ storage: storage });

app.get('/', (request, response) => {
  response.send('Executed genre-surf server');
});

app.post('/get-genre', upload.single('file'), (request, response) => {
  console.log('Client called /get-genre...\n');

  const fileInput = request.file.path;
  console.log('File name from client: ', fileInput);

  const spawn = require('child_process').spawn;
  console.log('Extracting genre...\n');
  const extractAudioFeatures = spawn('python3', ['python-files/audioFeat.py', fileInput]);
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
  });
});

app.listen(8080, () => {
  console.log('Server live on port 8080');
});

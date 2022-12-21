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
  console.log('\nExtracting genre...\n');
  const extractAudioFeatures = spawn('python3', ['python-files/audioFeat.py', fileInput]);
  console.log('- - - - - Called audioFeat.py - - - - -');
  extractAudioFeatures.stdout.on('data', (audioFeatResult) => {
    const audioFeatures = audioFeatResult.toString();
    console.log('Audio features: \n', audioFeatures);
    console.log('- - - - - Executed audioFeat.py successfully - - - - -\n');

    const predictGenre = spawn('python3', ['python-files/predictGenre.py', audioFeatures]);
    console.log('- - - - - Called predictGenre.py - - - - -');
    predictGenre.stdout.on('data', (genreResult) => {
      const genre = genreResult.toString();
      console.log('Genre: ', genre);
      console.log('- - - - - Executed predictGenre.py successfully - - - - -\n');

      response.send(genre);
    });
  });
});

app.get('/surf-youtube', (request, response) => {
  const genre = request.query.genre;
  const spawn = require('child_process').spawn;
  console.log('\nClient called /surf-youtube...\n');
  console.log(`Search ${genre} genre song Youtube\n`);
  const webCrawler = spawn('python3', ['python-files/youtubeCrawler.py', genre]);
  console.log('- - - - - Called youtubeCrawler.py - - - - -');
  webCrawler.stdout.on('data', (resultMessage) => {
    console.log(resultMessage.toString());
    response.send(resultMessage.toString());
  });
});

app.listen(8080, () => {
  console.log('Server live on port 8080');
});

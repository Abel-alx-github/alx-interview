#!/usr/bin/node

const request = require('request');

const id = isNaN(parseFloat(process.argv[2])) ? null : parseInt(process.argv[2]);


const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
function fetchData (url) {
  if (process.argv.length > 2) {
    request(url, (err, _, body) => {
      if (err) {
        console.log(err);
      }
      const charactersURL = JSON.parse(body).characters;
      const charactersName = charactersURL.map(
        url => new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        }));

      Promise.all(charactersName)
        .then(names => console.log(names.join('\n')))
        .catch(allErr => console.log(allErr));
    });
  }
}

!id ? console.log('Usage: node 0-starwars_characters.js <id:number>') : fetchData(url);

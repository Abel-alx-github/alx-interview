#!/usr/bin/node/

const request = require('request');

const id = isNaN(parseFloat(process.argv[2])) ? null : parseInt(process.argv[2]);
if (!id) {
  console.log('Enter the correct number');
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
try {
  request(url, async (err, res, body) => {
    if (err) {
      console.log('Error occured: ', err);
      return;
    }
    const links = await JSON.parse(body).characters;
    try {
      Promise.all(links.map(link => {
        return request(link, async (er, re, body) => {
          if (er) {
            console.log('error occured while handling link', er);
            return;
          }
          const characterName = await JSON.parse(body).name;
          console.log(characterName);
        });
      }));
    } catch (er) {
      console.log('error catched inside');
    }
  });
} catch (error) {
  console.log('error catched');
}

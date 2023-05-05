#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, _, body) => {
    if (err) console.log(err);
    const cName = JSON.parse(body).characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (pErr, __, pBody) => {
          if (pErr) reject(pErr);

          resolve(JSON.parse(pBody).name);
        });
      }));

    Promise.all(cName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

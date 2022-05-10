# Python 401d1818

## Lab 16: Capital Finder

Use `requests` library to interact with `REST Countries API`
Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
The serverless function should handle a `GET` http request with a given country name that responds with a string with the form `The capital of X is Y`
E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.
The serverless function should handle a GET http request with a given capital that responds with a string with the form `The capital of X is Y`
E.g.`/capital-finder?capital=Santiago` should generate an http response of `Santiago is the capital of Chile.`

### Author: 

Emily Landers


## Tests

- https://capital-finder-otb9veomt-emily-landers.vercel.app/api/capital?capital=bogota 
- https://capital-finder-otb9veomt-emily-landers.vercel.app/api/capital?capital=Taipei 
- https://capital-finder-otb9veomt-emily-landers.vercel.app/api/capital?country=Taiwan
- https://capital-finder-otb9veomt-emily-landers.vercel.app/api/capital?country=egypt 


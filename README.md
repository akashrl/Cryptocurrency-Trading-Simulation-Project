Fortune
======
The Cryptocurrency Trading Simulation Game
======

This is an online web application developed for my course CS307 at Purdue University with a team of 6 in Agile development of a Stock-market based Cryptocurrency online simulation that allows users to practice trading stocks in a risk-free sandbox type environment. The project uses a client-server model. A number of clients connect to the server requesting data such as game/user information. The server then sends a request to the database, which responds with the information. A separate worker component in the server continuously works to keep pricing information of the stocks accurate.

Client:
- Frontend of the project
- Serves as the interface for the game
- Requests information from the server
- Receives information back from the server and modifies the game screen

Server:
- Backend of the project
- Does most of the processing work for the client and API
- Updates database with cryptocurrency market information continuously

Database:
- Stores user and game information received by server
- Sends requested information to the server to handle
- Data is stored securely with user authentication features implemented.

Stock API:
- Third party API that provides information on pricing for various stocks and historical data - Polled by the server at a regular interval to keep prices up-to-date.

Architecture:
- Frontend is developed with ReactJS and the server in Python with Flask - User and stock data is stored in PostgreSQL database, using Docker.

- Web application is deployed through Amazon Web Services.
Our project features real-time data of stock pricing which is done by polling the API for information that is used real-time. We also use historical data as a feature.


To run the frontend, read client-react/README.md
If `npm run` in the client-react directory fails, try `npm install` in the client-react directory.
If npm doesn't work in general, you may not have Node installed.
    You’ll need to have Node 8.16.0 or Node 10.16.0 or later version on your local development machine


Docker
======
If you wanna use docker for an oh-so-clean, system-dependency-free, and
effortless testing setup, run `docker-compose -f dev-docker-compose.yml up` to
spin up a local db, api, and client.  Whenever you add a dependency to
package.json or requirements.txt, you should rebuild: `docker-compose -f
dev-docker-compose.yml build`.

You can run client tests with `docker-compose -f testing-docker-compose.yml run
client`

And api tests with `docker-compose -f testing-docker-compose.yml run api`

Debugging with docker
---------------------
You can debug JS on the browser. If you wanna debug Python, `docker attach
<container id>`. When you hit a `breakpoint()` it'll drop you into pdb.

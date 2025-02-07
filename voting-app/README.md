Application Architecture
The application consists of the following components, as shown in the architecture diagram:

Voting App: A Python-based frontend for voting.
Redis: An in-memory database for temporary vote storage.
Worker: A background processor that transfers votes from Redis to the database.
Postgres: A relational database for persistent storage.
Result App: A Node.js-based frontend for displaying voting results.

https://github.com/awesome-release/release-example-voting-app.git
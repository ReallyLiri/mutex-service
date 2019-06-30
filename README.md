# Mutex API Service

Web server to provide a simple mutex api of a global `lock` and `unlock`.

## Build

`docker build -t mutex .`

## Usage

The mutex is configured with a timeout to avoid infinite locked state.

By default the timeout is 10 minutes, you can configure it via the `LOCK_TIMEOUT` env (measured in seconds).

To run the image:

`docker run -d --name mutex --restart unless-stopped -p 8080:80 mutex`

And with a custom timeout:

`docker run -d --name mutex --restart unless-stopped -p 8080:80 -e LOCK_TIMEOUT=120 mutex`

Once deployed, contact it on `localhost:8080` (or whatever port you choose):

`curl -X PUT http://localhost:8080/lock`
`PUT http://localhost:8080/lock`
* Code 202 on lock successful
* Code 409 on lock unavailable

`curl -X PUT http://localhost:8080/unlock`
* Code 202 on unlock successful

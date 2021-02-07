# wishlist.vote

The source code for the http://wishlist.vote webapp. 

## Running
 
All development is currently being done in docker-compose. Use the command below to bring up a new instance:

```bash
docker-compose up
```

Environment variables are used to configure a large portion of the app. Locally I have a `.env` file that contains all the secrets and confiration. I have a sample of this file included in the repo [here](./sample.env).

## Testing

We are currently testing everything seperately between frontend and backend. This is because everything is in a mono-repo. Was this a good choice? I'm not sure, but I felt it would be easier to package this app as a snap/flatpak when it was finished, so for now it stays that way.

### Backend

Tests are invoked using the command below:

```bash
docker-compose up backend -m pytest
```

The test invokation above may look a litle weird. This is because `python3` is the entrypoint into the [Dockerfile](./backend/Dockerfile) I wrote for the backend. Therefore, everything after `docker-compose up backend` can logically be replaced with `python3` and should run the same. I may change this down the line, but for now it works.
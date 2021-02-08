# list.vote

The source code for the http://list.vote webapp (previously codenamed wishlist.vote). 

## Running
 
All development is currently being done in docker-compose. Use the command below to bring up a new instance:

```bash
docker-compose up
```

Environment variables are used to configure a large portion of the app. Locally I have a `.env` file that contains all the secrets and configuration. I have a sample of this file included in the repo [here](./sample.env).

## Testing

We are currently testing everything separately between frontend and backend. This is because everything is in a mono-repo. Was this a good choice? I'm not sure, but I felt it would be easier to package this app as a snap/flatpak when it was finished, so for now it stays that way.

### Backend

Tests are invoked using the command below:

```bash
docker-compose up backend -m pytest
```

The test invocation above may look a little weird. This is because `python3` is the entry-point into the [Dockerfile](./backend/Dockerfile) I wrote for the backend. Therefore, everything after `docker-compose up backend` can logically be replaced with `python3` and should run the same. I may change this down the line, but for now it works.

## Docs / Articles Used

As with any development, a lot of my time was spent in a [search engine](http://ddg.gg/) finding solutions or looking for guidance. For the time being there is no particular order, just a place to throw links until I have time time to organize it. 

* https://dev.to/lucasmiguelmac/pytest-with-django-rest-framework-from-zero-to-hero-8c4
* https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta
* https://www.django-rest-framework.org/
* https://stackoverflow.com/questions/35518273/how-to-set-current-user-to-user-field-in-django-rest-framework
* https://docs.djangoproject.com/
* https://bezkoder.com/django-react-axios-rest-framework/
* https://www.valentinog.com/blog/drf/
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-scalable-and-secure-django-application-with-kubernetes
 
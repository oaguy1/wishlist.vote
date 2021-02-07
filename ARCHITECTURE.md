# App Architecture

After reading [this Hacker News](https://matklad.github.io//2021/02/06/ARCHITECTURE.md.html) post, I wanted to add a bit about how this app is structured. This is particularly important because this is, for now, mainly a single person effort in my spare time and we have both the frontend code and backend code in a single mono-repo (for now).

## Backend

The backend of the app is a Django app using the Django Rest Framework (DRF). This is logically located in the `backend` directory. The current Django app name is "wishlist" and comprises of two apps, "wishlist" and "api." The API django app contains all the meat and potatoes of the backend. 
Manhunt #9
15
Auth. You're on your own for this :)

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format

This is part of a series, more challenges will be unlocked once you solve this one. While most challenges will be OSINT, some of them may not be.

============================

Walkthrough:

this is the nineth part of the Manhunt series. Auth means authentification. We probably want to gain access to the wordpress.

Because it is a OSINT chanllenge, we probably able to find the source code on the web. Let try to `GitHub`:
```
https://github.com/search?q=dorfmeister&type=users
```

We found the user `JohnnyDorfmeister`. On his repository named `authentication-requests`, we found the following auth page:
```
https://github.com/JohnnyDorfmeister/authentication-requests/blob/master/auth.php
```

The prod auth page has been found here (link on the home page):
```
http://www.howitshould.be/authentication/auth.php
```

The username is pretty easy to get. The password too because Johnny has uploaded the password on github and removed on next commit. 

We are able to retrieve the password using the Github history.

```
Username: johnny
password: letmein
```

Once the authentification is completed, we got the flag.

The flag is:
```
g1ttern00b
```

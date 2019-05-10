# CS445 Internet Security

This project is the semester project for CS445 Internet Security at the
University of Nevada, Reno.

##Current Status

This project is presently not fully complete.  It works on Mac OS to retrieve
the Twitter `auth_token` cookie from Firefox.  It will also retrieve the
encrypted cookie from Chrome, but it is not able to decrypt it at this time.  A
decryption implementation is included in `decrypt.py` but requires system
authentication on Mac OS.

Using that cookie it can make a connection to Twitter, but does not follow the
redirection link.  This is an issue I was unable to resolve.

## Future Work

This project was intended to be extended to all major browsers (Edge and
Safari), and all major plaforms (Linux and Windows), but time did not permit.

This project was also intended to make a sample twitter post, once
authenticated, but due to the unresolved issue outlined above, this did not get
completed.

## Author
Evan Grill
Class of 2019
Manhunt #7 (10 pts)

Can you tell me where he lives? Then I can drop some kind words in his mailbox!

Format: brixelCTF{STREET_NUMBER_POSTALCODE_CITY} e.g brixelCTF{examplestreet_15_8500_kortrijk}

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format

This is part of a series, more challenges will be unlocked once you solve this one. While most challenges will be OSINT, some of them may not be.


============================

Walkthrough:

this is the seventh part of the Manhunt series. Our first attempts to achieve this one is pivoting around the domain by using a whois tool or something but it didn't work. We tried to submit an email through the website, maybe it will send a template with his address.

After using the form, the following message appears:

```
Thanks for contacting me, an e-mail is on the way with more details.

It might happen that the mail server is broken again, if so, please send a letter with the job description to:

Johnny Dorfmeister
Melkvoetstraat 48
3500 Hasselt


Seriously, don't send anything to these people, I don't know them, it's only for the CTF!
```

The flag is:
```
Melkvoetstraat_48_3500_Hasselt
```

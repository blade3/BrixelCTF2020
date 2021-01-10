 Lottery ticket (10 pts)
 
Someone is trying to sell this lottery ticket online, it has the winning numbers but I suspect foul play

Can you tell me which the new numbers are that are photoshopped?

Add them all up, the resulting number is the flag

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format



=======================

Walkthrough:

First, we used exiftool on the jpg to gatther information but nothing useful.


Using binwalk, we verify if any files is embedded into the image.

After extracting the files, we verify if the thumbnail and the full image is the same, yes it is.

Because it talks about the photoshop and modifications, We can try to find a tool to detect different compression on an image.

we used the following to get the response:
(https://29a.ch/photo-forensics/)[29a.ch]

four number has been modified:
```
42, 88, 25, 48
```
The flag is:
```
203
```

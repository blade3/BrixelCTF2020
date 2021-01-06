 Manhunt #1 (5 pts)

My dad is pissed off! He was told by my mother NOT to buy ice cream but he did anyway when she wasn't looking.

Someone posted this picture on the internet and my mother saw it, man, he is in so much trouble!

I want to know WHO posted this picture, let's hunt this guy down!

<img src="https://github.com/blade3/BrixelCTF2020/blob/master/OSINT/Manhunt%20%231/icecream.jpg" width="300">


This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format, replace spaces with underscores ('_')

This is part of a series, more challenges will be unlocked once you solve this one. While most challenges will be OSINT, some of them may not be.

============================
Walkthrough:

this is the first part of the Manhunt series. 

Using `exiftool`, we are able to find the owner:

```
$ exiftool icecream.jpg 
ExifTool Version Number         : 12.12
File Name                       : icecream.jpg
Directory                       : .
File Size                       : 322 KiB
File Modification Date/Time     : 2020:12:29 09:49:59-05:00
File Access Date/Time           : 2020:12:29 09:50:01-05:00
File Inode Change Date/Time     : 2020:12:29 09:50:20-05:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
Flashpix Version                : 0100
Owner Name                      : Johnny Dorfmeister
Image Width                     : 1536
Image Height                    : 2048
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 1536x2048
Megapixels                      : 3.1

```
The flag is:
```
Johnny_Dorfmeister
```

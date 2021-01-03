 Doc-ception (10 pts)

Need to hide something? why not a word document?

You need to dig deeper

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format



===================================================

Walkthrough:

Firstly, since its a stegano, we'll use exiftool:

$ exiftool loremipsum.docx 
ExifTool Version Number         : 12.12
File Name                       : loremipsum.docx
Directory                       : .
File Size                       : 21 KiB
File Modification Date/Time     : 2020:12:30 14:48:43-05:00
File Access Date/Time           : 2020:12:30 14:51:07-05:00
File Inode Change Date/Time     : 2020:12:30 14:51:07-05:00
File Permissions                : rw-r--r--
File Type                       : DOCX
File Type Extension             : docx
MIME Type                       : application/vnd.openxmlformats-officedocument.wordprocessingml.document
Zip Required Version            : 20
Zip Bit Flag                    : 0
Zip Compression                 : Deflated
Zip Modify Date                 : 1980:01:01 00:00:00
Zip CRC                         : 0xb71a911e
Zip Compressed Size             : 234
Zip Uncompressed Size           : 590
Zip File Name                   : _rels/.rels
Template                        : Normal.dotm
Total Edit Time                 : 0
Pages                           : 1
Words                           : 327
Characters                      : 1799
Application                     : Microsoft Office Word
Doc Security                    : None
Lines                           : 14
Paragraphs                      : 4
Scale Crop                      : No
Heading Pairs                   : Titel, 1
Titles Of Parts                 : 
Company                         : 
Links Up To Date                : No
Characters With Spaces          : 2122
Shared Doc                      : No
Hyperlinks Changed              : No
App Version                     : 16.0000
Title                           : 
Subject                         : 
Creator                         : Erna Kevin
Keywords                        : 
Description                     : 
Last Modified By                : Erna Kevin
Revision Number                 : 1
Create Date                     : 2019:04:24 07:47:00Z
Modify Date                     : 2019:04:24 07:47:00Z

nothing interesting.
Trying using binwalk instead:

```
$ binwalk loremipsum.docx 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 234, uncompressed size: 590, name: _rels/.rels
275           0x113           Zip archive data, at least v2.0 to extract, compressed size: 471, uncompressed size: 991, name: docProps/app.xml
792           0x318           Zip archive data, at least v2.0 to extract, compressed size: 359, uncompressed size: 747, name: docProps/core.xml
*1198          0x4AE           Zip archive data, at least v2.0 to extract, compressed size: 10335, uncompressed size: 11262, name: loremipsum.docx
11578         0x2D3A          Zip archive data, at least v2.0 to extract, compressed size: 237, uncompressed size: 817, name: word/_rels/document.xml.rels
11873         0x2E61          Zip archive data, at least v2.0 to extract, compressed size: 1807, uncompressed size: 7336, name: word/document.xml
13727         0x359F          Zip archive data, at least v2.0 to extract, compressed size: 445, uncompressed size: 1419, name: word/fontTable.xml
14220         0x378C          Zip archive data, at least v2.0 to extract, compressed size: 969, uncompressed size: 2649, name: word/settings.xml
15236         0x3B84          Zip archive data, at least v2.0 to extract, compressed size: 2899, uncompressed size: 29156, name: word/styles.xml
18180         0x4704          Zip archive data, at least v2.0 to extract, compressed size: 1725, uncompressed size: 8393, name: word/theme/theme1.xml
19956         0x4DF4          Zip archive data, at least v2.0 to extract, compressed size: 278, uncompressed size: 642, name: word/webSettings.xml
20284         0x4F3C          Zip archive data, at least v2.0 to extract, compressed size: 357, uncompressed size: 1381, name: [Content_Types].xml
21456         0x53D0          End of Zip archive, footer length: 22
```

We can find that is a archive with an another `loremipsum.docx` document inside.

once unzipped, we use binwalk on the other docx:

```
$ binwalk loremipsum.docx 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 234, uncompressed size: 590, name: _rels/.rels
275           0x113           Zip archive data, at least v2.0 to extract, compressed size: 471, uncompressed size: 991, name: docProps/app.xml
792           0x318           Zip archive data, at least v2.0 to extract, compressed size: 359, uncompressed size: 747, name: docProps/core.xml
*1198          0x4AE           Zip archive data, at least v2.0 to extract, compressed size: 14, uncompressed size: 14, name: flag.txt
1250          0x4E2           Zip archive data, at least v2.0 to extract, compressed size: 237, uncompressed size: 817, name: word/_rels/document.xml.rels
1545          0x609           Zip archive data, at least v2.0 to extract, compressed size: 1916, uncompressed size: 9208, name: word/document.xml
3508          0xDB4           Zip archive data, at least v2.0 to extract, compressed size: 445, uncompressed size: 1419, name: word/fontTable.xml
4001          0xFA1           Zip archive data, at least v2.0 to extract, compressed size: 983, uncompressed size: 2680, name: word/settings.xml
5031          0x13A7          Zip archive data, at least v2.0 to extract, compressed size: 2899, uncompressed size: 29156, name: word/styles.xml
7975          0x1F27          Zip archive data, at least v2.0 to extract, compressed size: 1725, uncompressed size: 8393, name: word/theme/theme1.xml
9751          0x2617          Zip archive data, at least v2.0 to extract, compressed size: 278, uncompressed size: 642, name: word/webSettings.xml
10079         0x275F          Zip archive data, at least v2.0 to extract, compressed size: 353, uncompressed size: 1367, name: [Content_Types].xml
11240         0x2BE8          End of Zip archive, footer length: 22
```

Bingo, a file named flag.txt.

$ cat flag.txt 
flag = openxml

The flag is:
openxml

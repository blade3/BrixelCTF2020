 Rufus the vampire cat (15 pts)

This is a picture of Rufus the vampire cat

Despite being cute, Rufus hides a secret, up to you to find it

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format


===================================================

Walkthrough:

We use the stegoveritas tool to discover hidden data on the picture:

```
$ stegoveritas rufus.jpg 
Running Module: SVImage
+------------------+------+
|   Image Format   | Mode |
+------------------+------+
| JPEG (ISO 10918) | RGB  |
+------------------+------+
Found something with StegHide: [redacted]/Rufus the vampire cat/results/steghide_02f1708d1d48659b1f0411e9ed8764f9.bin
+---------+------------------+------------------------------------------------------------------------------------------------------+-----------+
| Offset  | Carved/Extracted | Description                                                                                          | File Name |
+---------+------------------+------------------------------------------------------------------------------------------------------+-----------+
| 0x2192d | Carved           | LZMA compressed data, properties: 0x90, dictionary size: 0 bytes, uncompressed size: 36 bytes        | 2192D.7z  |
| 0x2192d | Extracted        | LZMA compressed data, properties: 0x90, dictionary size: 0 bytes, uncompressed size: 36 bytes        | 2192D     |
| 0x4223d | Carved           | LZMA compressed data, properties: 0x92, dictionary size: 16777216 bytes, uncompressed size: 32 bytes | 4223D.7z  |
| 0x4223d | Extracted        | LZMA compressed data, properties: 0x92, dictionary size: 16777216 bytes, uncompressed size: 32 bytes | 4223D     |
| 0x46f9e | Carved           | LZMA compressed data, properties: 0x92, dictionary size: 0 bytes, uncompressed size: 32 bytes        | 46F9E.7z  |
| 0x46f9e | Extracted        | LZMA compressed data, properties: 0x92, dictionary size: 0 bytes, uncompressed size: 32 bytes        | 46F9E     |
+---------+------------------+------------------------------------------------------------------------------------------------------+-----------+
Running Module: MultiHandler

Found something worth keeping!
JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 1078x950, components 3
Exif
====
+---------------------+-------------------------------------------------------------------------------+
| key                 | value                                                                         |
+---------------------+-------------------------------------------------------------------------------+
| SourceFile          | [redacted]/Rufus the vampire cat/rufus.jpg |
| ExifToolVersion     | 12.13                                                                         |
| FileName            | rufus.jpg                                                                     |
| Directory           | [redacted]/Rufus the vampire cat           |
| FileSize            | 143 KiB                                                                       |
| FileModifyDate      | 2020:12:30 16:27:05-05:00                                                     |
| FileAccessDate      | 2020:12:30 16:30:22-05:00                                                     |
| FileInodeChangeDate | 2020:12:30 16:28:51-05:00                                                     |
| FilePermissions     | rw-r--r--                                                                     |
| FileType            | JPEG                                                                          |
| FileTypeExtension   | jpg                                                                           |
| MIMEType            | image/jpeg                                                                    |
| JFIFVersion         | 1.01                                                                          |
| ResolutionUnit      | inches                                                                        |
| XResolution         | 72                                                                            |
| YResolution         | 72                                                                            |
| ImageWidth          | 1078                                                                          |
| ImageHeight         | 950                                                                           |
| EncodingProcess     | Baseline DCT, Huffman coding                                                  |
| BitsPerSample       | 8                                                                             |
| ColorComponents     | 3                                                                             |
| YCbCrSubSampling    | YCbCr4:2:0 (2 2)                                                              |
| ImageSize           | 1078x950                                                                      |
| Megapixels          | 1.0                                                                           |
+---------------------+-------------------------------------------------------------------------------+
```

We discover a steghide_02f1708d1d48659b1f0411e9ed8764f9.bin file.

$ cat results/steghide_02f1708d1d48659b1f0411e9ed8764f9.bin 
You thought this was a cute cat picture? NOPE! Chuck Testa! (the flag is: chucktesta)


The flag is:
chucktesta
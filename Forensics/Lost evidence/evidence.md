 Lost evidence (30 pts)

A buddy of mine is in serious trouble. He works for the feds and accidentally deleted a pendrive containing crucial evidence

Can you get it back and tell us what the evidence is?

We need to know what the suspect bought


The flag is in this format: brixelCTF{name_of_product_bought}


===========

Walkthrough:

First, we got a raw disk img, we need to detect which img we got:
```
$ file evidence.img 
evidence.img: DOS/MBR boot sector, code offset 0x52+2, OEM-ID "NTFS    ", sectors/cluster 8, Media descriptor 0xf8, sectors/track 63, heads 255, hidden sectors 8211, dos < 4.0 BootSector (0x0), FAT (1Y bit by descriptor); NTFS, sectors/track 63, physical drive 0x80, sectors 1880044, $MFT start cluster 78335, $MFTMirror start cluster 2, bytes/RecordSegment 2^(-1*246), clusters/index block 1, serial number 0a6822852822828ef; contains bootstrap BOOTMGR

```

using fdisk now:

```
$ fdisk -l evidence.img 
Disk evidence.img: 917.99 MiB, 962583040 bytes, 1880045 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x73736572

Device        Boot      Start        End    Sectors   Size Id Type
evidence.img1      1920221984 3736432267 1816210284   866G 72 unknown
evidence.img2      1936028192 3889681299 1953653108 931.6G 6c unknown
evidence.img3               0          0          0     0B  0 Empty
evidence.img4        27722122   27722568        447 223.5K  0 Empty

Partition table entries are not in disk order.
```

Using `foremost`, we retrieve two wav with the same hash:
```
$ foremost evidence.img 
```

Here is the output:
```
.
├── evidence.img
└── output
    ├── audit.txt
    └── wav
        ├── 00011328.wav
        └── 00028304.wav
```
The wav contains a phone communication with a bank. we need to convert the digital phone number into the number. Using the `DTMF decoder` script, on audacity, on the interesting part, we got the following string:

```
8 44 99 0 333 666 777 0 8 44 33 0 222 666 2222 444 66 33 0 22 777 88 44
```

Once converted (manually), the msg is:
```
THX FOR THE COCAINE BRUH
```

The flag is:
 brixelCTF{cocaine}

Scan me (10 pts)

Can you solve this scan puzzle?

It could be handy to hide messages



===================================================

Walkthrough:

Once scanned, we retrieve the following string:
brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF brixelCTF


We'll try to find an hidden image into the QR code. a part of the QR code, its able to discover (using a QR Scanner website: https://online-barcode-reader.inliteresearch.com/) the follwoing website:
http://www.timesink.be/qrcode/flag.html

using the same website, we got the first code:
code-128-easy

The second stage (http://www.timesink.be/qrcode/flag2.php) appears an another code bar, here is the code:
5449000133335

The third stage (http://www.timesink.be/qrcode/flag3.php) appears an another code bar, here is the code:
congratulations_this_is_the_last_barcode

Finaly, after reaching the last page (http://www.timesink.be/qrcode/flag4.php), we got the following string:
That is correct!
Congratulations: the flag is brixelCTF{m4st3r_0f_sc4n5}


The flag is:
brixelCTF{m4st3r_0f_sc4n5}
# random-tools

Random tools I made for random things! Please create an issue for any problems.

## Requirements

All of these subprojects use Python >3.11. Any specific pip dependencies (if applicable) are listed in the `requirements.txt` file in each folder. Other dependencies or requirements are listed in the descriptions below.

---

### email-spam

Sends a number of 8KB text emails to a specified email address. The GNU `mailx` utility and a setup SMTP server are also required.

Sample usage:

```console
user@computer:~$ python email.py "John Doe" john.doe user@example.com 10000
user@computer:~$
```

---

### nested-zip

Zip a file, then zip that zip, then zip that zip, then zip that zip... some number of times.

Sample usage:

```console
user@computer:~$ python zip.py 10 output.zip input1.txt input2.txt input3.txt
Levels: 10
Output file: output.zip
Input files: ['input1.txt', 'input2.txt', 'input3.txt']
Zipping level 1...
Zipping level 2...
Zipping level 3...
Zipping level 4...
Zipping level 5...
Zipping level 6...
Zipping level 7...
Zipping level 8...
Zipping level 9...
Zipping level 10...
Zipped!
user@computer:~$
```

---

### pdf-expand

Expands a PDF to any size by adding a comment to the trailer of the PDF, all according to the ![specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf).

Sample usage:

```console
user@computer:~$ python pdf_expand.py sample.pdf sample_expanded.pdf 10000000
PdfData(
        data:   b'%PDF-1.3\n%\xc4\xe5\xf2\xe5\xeb\xa7'...
        header: b'%PDF-1.3'
        size:   18,810
)
info: PDF version 1.3 supported
info: trailer found at 18662; data is at 18672:18785 (<<...>>)
info: trailer data: b' /Size 26 /Root 13 0 R /Info 1 0 R /ID [ <4e949515aaf132498f650e7bde6cdc2f>\n<4e949515aaf132498f650e7bde6cdc2f> ] '
info: inserting 9981190 bytes into trailer...
info: successfully inserted; new size of PDF is 10000000
info: successfully wrote to PDF
user@computer:~$
```

---

### server-ping

Pings a bunch of SSH servers through a proxy to see who is currently logged into the computers. Tuned to the Clemson University School of Computing's lab computers. The Paramiko pip package is a dependency, as listed in `requirements.txt`. Be sure to create an ED25519 key and specify the location of the key file in the program.

Sample usage:

```console
user@computer:~$ python ping.py
access1.computing.clemson.edu           <users>
access2.computing.clemson.edu           <users>
newton.computing.clemson.edu            <users>
joey1.computing.clemson.edu             <users>
joey2.computing.clemson.edu             <users>
joey3.computing.clemson.edu             <users>
...
ada8.computing.clemson.edu              ERROR: ssh: connect to host ada8.computing.clemson.edu port 22: Connection timed out
...
cirrus8.computing.clemson.edu           <users>
cirrus9.computing.clemson.edu           <users>
titan1.computing.clemson.edu            <users>
titan2.computing.clemson.edu            <users>
titan3.computing.clemson.edu            <users>
titan4.computing.clemson.edu            <users>
titan5.computing.clemson.edu            <users>
user@computer:~$
```

---

### sms-spam

Similar to `email-spam`; uses common phone providers' SMS gateways to send SMS messages to a phone number. Again, the GNU `mailx` utility and a setup SMTP server are also required.

Sample usage:

```console
user@computer:~$ python sms.py 1234567890 verizon "hello there" 100
user@computer:~$
```

---

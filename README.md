# Requirements:
On a linux host install docker and clamav
# How to run:

`python scanner.py -i "ubuntu:latest"`

example output:
```
----------- SCAN SUMMARY -----------
Known viruses: 6549101
Engine version: 0.99.4
Scanned directories: 2635
Scanned files: 15880
Infected files: 0
Data scanned: 135.11 MB
Data read: 89.79 MB (ratio 1.50:1)
Time: 36.902 sec (0 m 36 s)

```

# How it works:
It takes advantage of docker root account as well as volume mount to copy all files from docker container to host system.
Then it uses clamav to scan all the files and show results.

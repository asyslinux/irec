# JPG Recovery Tool

- Usage
```
python3 irec.py /path/to/
python3 irec.py /path/to/rawfile /path/to/recovery/folder
python3 irec.py /path/to/diskimage /path/to/recovery/folder
python3 irec.py /path/to/device /path/to/recovery/folder
```

- Example usage with MooseFS chunk files

Scan all chunks:
```
find /mnt/hdd-1/mfschunks -type f | xargs -I {} python3 irec.py {} /home/recovery/
```

Scan chunks with size greater than 128KB:
```
find /mnt/hdd-1/mfschunks -type f -size +131072c | xargs -I {} python3 irec.py {} /home/recovery/
```

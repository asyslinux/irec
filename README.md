# JPG Recovery Tool
- Install
```
apt -y install recoverjpeg
```

- Usage
```
recoverjpeg --help

recoverjpeg /path/to/device -o /path/to/recovery
recoverjpeg /path/to/rawfile -o /path/to/recovery
recoverjpeg /path/to/imgfile -o /path/to/recovery
```

- Example usage with MooseFS chunk files

1. Download `restore.sh` script from this repo 

```
git clone https://github.com/asyslinux/irec && cd irec && chmod a+x restore.sh
mkdir -p /path/to/prepare && mkdir -p /path/to/recovery
```

2. Restore JPG Images from MooseFS chunk files

Scan all chunks:
```
find /mnt/hdd-1/mfschunks -type f | xargs -i bash -c 'recoverjpeg {} -o /path/to/prepare/ && ./restore.sh /path/to/prepare /path/to/recovery'
```

Scan chunks with size greater than 256KB:
```
find /mnt/hdd-1/mfschunks -type f | xargs -i bash -c 'recoverjpeg {} -s 262144 -o /path/to/prepare/ && ./restore.sh /path/to/prepare/ /path/to/recovery'
```

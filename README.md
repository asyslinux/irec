# JPG Recovery Tool

- Install
```
apt -y install recoverjpeg
```

- Usage
```
recoverjpeg --help

recoverjpeg /path/to/device -m 256m -o /path/to/recovery
recoverjpeg /path/to/rawfile -m 256m -o /path/to/recovery
recoverjpeg /path/to/imgfile -m 256m -o /path/to/recovery
```

Notice: recoverjpeg utility by default has max size 6MB (-m option), if not set more, then `recoverjpeg` would recovery only <6MB size of jpg file images

- Example usage with MooseFS chunk files

Via this simple tool, from MooseFS chunk files can be restored jpg files only with size <64MB

1. Download `restore.sh` script from this repo 

```
git clone https://github.com/asyslinux/irec && cd irec && chmod a+x restore.sh
mkdir -p /path/to/prepare && mkdir -p /path/to/recovery
```

2. Restore jpg images from MooseFS chunk files

Restore all jpg images with size smaller than 64MB:
```
find /mnt/hdd-1/mfschunks -type f | xargs -i bash -c 'recoverjpeg {} -m 64m -o /path/to/prepare/ && ./restore.sh /path/to/prepare /path/to/recovery'
```

Restore all jpg images with size greater than 256KB and smaller than 64MB:
```
find /mnt/hdd-1/mfschunks -type f | xargs -i bash -c 'recoverjpeg {} -s 256k -m 64m -o /path/to/prepare/ && ./restore.sh /path/to/prepare/ /path/to/recovery'
```

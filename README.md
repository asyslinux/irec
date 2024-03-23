# Multi Purpose Recovery Tool

- Install
```
apt -y install testdisk
```

- Usage

Manual: https://www.cgsecurity.org/testdisk_doc/scripted_run.html#automating-recovery-using-photorec

Formats: https://www.cgsecurity.org/wiki/File_Formats_Recovered_By_PhotoRec

```
photorec /d /path/to/recovery /path/to/device
photorec /d /path/to/recovery /path/to/rawfile
photorec /d /path/to/recovery /path/to/imgfile
```

- Example usage with MooseFS chunk files

Via this tool, from MooseFS chunk files can be restored all files only with size <64MB

1. Download `restore.sh` script from this repo 

```
git clone https://github.com/asyslinux/irec && cd irec && chmod a+x restore.sh
mkdir -p /path/to/prepare && mkdir -p /path/to/recovery
```

2. Restore files from MooseFS chunk files

Restore all files with size smaller than 64MB:

```
find /mnt/hdd-1/mfschunks/ -type f | xargs -i bash -c 'photorec /d /path/to/prepare/ /cmd {} partition_none,fileopt,everything,enable,search 1>/dev/null && ./restore.sh /path/to/prepare /path/to/recovery'
```

Restore all jpg images with size smaller than 64MB:

```
find /mnt/hdd-1/mfschunks/ -type f | xargs -i bash -c 'photorec /d /path/to/prepare/ /cmd {} partition_none,fileopt,everything,disable,jpg,enable,search 1>/dev/null && ./restore.sh /path/to/prepare /path/to/recovery'
```

Restore all jpg images with size greater than 256KB and smaller than 64MB:

```
find /mnt/hdd-1/mfschunks/ -type f -size +262144c | xargs -i bash -c 'photorec /d /path/to/prepare/ /cmd {} partition_none,fileopt,everything,disable,jpg,enable,search 1>/dev/null && ./restore.sh /path/to/prepare /path/to/recovery'
```

-----------------------------------------------------------------------------------------------------------------------

# Additional Simple JPG Recovery Tool

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

2. Restore files from MooseFS chunk files

Restore all jpg images with size smaller than 64MB:
```
find /mnt/hdd-1/mfschunks -type f | xargs -i bash -c 'recoverjpeg {} -m 64m -o /path/to/prepare/ && ./restore.sh /path/to/prepare /path/to/recovery'
```

Restore all jpg images with size greater than 256KB and smaller than 64MB:
```
find /mnt/hdd-1/mfschunks -type f | xargs -i bash -c 'recoverjpeg {} -s 256k -m 64m -o /path/to/prepare/ && ./restore.sh /path/to/prepare/ /path/to/recovery'
```

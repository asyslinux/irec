# Multi Purpose Recovery Tool (Recommended)

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

# Supported file types:

# JPG

# Imports

import sys
import os
import math
import uuid
import shutil
import pathlib

# Global variables

# List of file types and their signatures hex values to locate the files
fileSignatureHexValues = {'JPG': 'ffd8ff'}

# List of file types and their trailers hex values to locate the end of the files
endOfFileHexValues = {'JPG': 'ffd9000000'}

# Keeps track of recovered files from raw file or disk image
currentRecoveredFileCount = 0

# Open a raw file or disk image and turn the values into a list of hex values
def openTargetImage(userDiskImage):
    try:
        with open(userDiskImage, 'rb') as diskImage:
            diskHexValues = diskImage.read().hex()
    except FileNotFoundError:
        print(f'Error: File not found - {userDiskImage}')
        return None
    else:
        return diskHexValues

# Locate the number of files in the disk image
def locateFiles(diskContents):
    for hexValue in fileSignatureHexValues:
        findAndRecoverFiles(diskContents, hexValue)

# Search raw file contents for matching hex values and calls the specific recovery function
def findAndRecoverFiles(diskContents, hexValue):
    #print('========================================')
    #print(f'Finding and recovering {hexValue} files')
    #print('========================================')

    hexIdentifier = diskContents.find(fileSignatureHexValues[hexValue])

    recovery_functions = {
        'JPG': recoverJPGFiles,
    }

    while hexIdentifier != -1 and hexValue in recovery_functions:
        recovery_functions[hexValue](diskContents, hexIdentifier)
        hexIdentifier = diskContents.find(fileSignatureHexValues.get(hexValue), hexIdentifier + 1)

def hash2path(_hash):
    return "%s/%s/%s" % (_hash[0:2], _hash[3:5], _hash)

# Write recovered files
def recoverFile(args, fileName, startingOffsetBytes, fileSize):
    # command to recover the files to the system
    if len(sys.argv) == 3:

        extensionFile = pathlib.Path(fileName).suffix

        tmpFileRecoveryPath = os.path.normpath(sys.argv[2] + '/' + fileName)
        recoveryOperation = f'dd if={sys.argv[1]} of={tmpFileRecoveryPath} bs=1 skip={startingOffsetBytes} count={fileSize} >/dev/null 2>&1'

        os.system(recoveryOperation)

        generateFileHash = f'sha256sum -z {tmpFileRecoveryPath} | cut -d " " -f1 | head -c -1'

        recoveryEndPath = hash2path(os.popen(generateFileHash).read())
        recoveryEndDir = os.path.dirname(os.path.normpath(sys.argv[2] + '/' + recoveryEndPath))

        sys.stdout.flush()

        os.system(f'mkdir -p {recoveryEndDir}')
        hashFileName = os.path.normpath(sys.argv[2] + '/' + recoveryEndPath + extensionFile)
    else:
        print('' )
        print('Error: no given raw file or disk image or/and recovery folder path' )
        print('' )
        print('Usage: ./irec.py /path/to/rawfile /path/to/recovery/folder' )
        print('Usage: ./irec.py /path/to/diskimage /path/to/recovery/folder' )
        print('Usage: ./irec.py /path/to/device /path/to/recovery/folder' )
        print('' )
        exit(1)

    shutil.move(tmpFileRecoveryPath, hashFileName)
    print('Recovered file: ' + hashFileName)

# Recover JPG files
def recoverJPGFiles(diskContents, hexIdentifier):
    # Check for files starting at the beginning of a sector
    if (hexIdentifier % 512) == 0:
        global currentRecoveredFileCount
        currentRecoveredFileCount += 1

        # Search for the first end of the trailer type
        fileEndBytes = diskContents.find(endOfFileHexValues['JPG'], hexIdentifier)

        # Add 3 bytes so that we are at the index of the last byte in the file's trailer
        fileEndBytes = fileEndBytes + 3

        uuidStr = str(uuid.uuid4())

        # Calculate file info and print it
        fileName = f'{uuidStr}-{currentRecoveredFileCount}.jpg'

        # Calculate the file's offset in bytes, must divide by 2 for correct offset because 1 byte = 2 hex characters
        startingOffsetBytes = int(hexIdentifier / 2)
        endingOffsetBytes = int(math.ceil(fileEndBytes / 2))
        fileSize = endingOffsetBytes - startingOffsetBytes

        # Print file information: file name, start offset, and end offset
        #printFileInfo(fileName, startingOffsetBytes, endingOffsetBytes)

        # Recover file using the file info we calculated and get SHA-256 hash
        recoverFile(sys.argv[1], fileName, startingOffsetBytes, fileSize)

# Main
def main():
    print('========================================')
    print('JPG Image Recovery Tool!')
    print('========================================')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('' )
        print('Error: no given raw file or disk image or/and recovery folder path' )
        print('' )
        print('Usage: ./irec.py /path/to/rawfile /path/to/recovery/folder' )
        print('Usage: ./irec.py /path/to/diskimage /path/to/recovery/folder' )
        print('Usage: ./irec.py /path/to/device /path/to/recovery/folder' )
        print('' )
        exit(1)
    else:
        userDiskImage = sys.argv[1]
        diskContents = openTargetImage(userDiskImage)
        locateFiles(diskContents)

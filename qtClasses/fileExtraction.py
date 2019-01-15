import argparse
import tarfile
import zipfile

parser=argparse.ArgumentParser()
parser.add_argument('--f', '--sourcefilePath', required=True, dest='filePath', type=str, help="file path to be extracted ")
parser.add_argument("dest",type=str)
args=parser.parse_args()
filePath=args.filePath
destpath=args.dest


if (filePath.endswith("tar.gz")):
    tar = tarfile.open(filePath, "r:gz")
    tar.extractall(destpath)
    tar.close()
elif (filePath.endswith("tar")):
    tar = tarfile.open(filePath, "r:")
    tar.extractall(destpath)
    tar.close()
else:
    zip = zipfile.ZipFile(filePath)
    zip.extractall(destpath)
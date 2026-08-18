import hashlib

md5 = hashlib.md5()

with open("myfile.txt", "rb") as f:
    while chunk := f.read(4096):
        md5.update(chunk)

print(md5.hexdigest())
import hashlib
hashs = hashlib.new("md5","this is md5".encode("utf-8")).hexdigest()
print(hashs)
hashs = hashlib.new("sha256","this is sha256".encode("utf-8")).hexdigest()
print(hashs)
##############

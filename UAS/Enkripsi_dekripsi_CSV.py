# import modul
from cryptography.fernet import Fernet


# key generation
key = Fernet.generate_key()
 
# read string kunci
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)


# pakai kunci
fernet = Fernet(key)
 
# buka file csv
with open('C:/UAS P.SKD/RSA/file_csv.csv', 'rb') as file:
    original = file.read()
     
# enkripsi csv
encrypted = fernet.encrypt(original)
 
# simpan file enkripsi
with open('C:/UAS P.SKD/RSA/file_csv.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


#DEKRIPSI
    
# pakai kunci yang tadi
fernet = Fernet(key)

# buka file hasil enkrpisi
with open('C:/UAS P.SKD/RSA/file_csv.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# langsung di dekripsi 
decrypted = fernet.decrypt(encrypted)

# cek hasil dekripsi cocok apa tidak ??
with open('C:/UAS P.SKD/RSA/file_csv.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
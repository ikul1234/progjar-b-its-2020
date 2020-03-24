import shelve
import uuid
import socket
import os
import base64

class Dire:
    def __init__(self):
      #  self.data = shelve.open('mydata.dat')
        if not os.path.exists("diri"):
            os.makedirs("dir")
    def upload_data(self,nama=None,file=None):
       #====check nama direktori=======
        #print("masuk sini "+file)
        makan = file
        print("halo")
        print(base64.decodestring(makan))
        f = open("dir/"+nama,"wb")
        f.write(base64.decodestring(makan))
        return True
    def download_data(self,nama=None):
        # ======Membaca file download =====
        are = []
        f = open("dir/" + nama, "rb")
        l =f.read()
        f.close()
        print(l)
        # ======Mendownload file =====
        hasil = base64.encodestring(l)
        print(hasil)
        are.append(hasil.decode())
        print(are)
        return are

    def list_data(self):
        file_list = os.listdir("dir")
        f = []
        for filename in file_list:
            f.append(filename)
        return f

if __name__=='__main__':
    dire = Dire()
    input = "pesan.txt"
    print(dire.list_data())
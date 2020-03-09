import logging
import requests
import threading
import datetime
import os

threads = []

def download_gambar(url=None,nama=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'
    
    currentDT = datetime.datetime.now()
    currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = nama
        ekstensi = tipe[content_type]
        logging.warning(f"\n Download {namafile}.{ekstensi},\n Date = {currentDT} ")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__=='__main__':

    x = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/AaItk5N9tIU_oFAfrf_kCyFL8YE=/0x0:0x0/750x500/data/photo/2020/03/09/5e65b4908df04.jpg','Foto_Ke-1',))
    threads.append(x)
    x = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/3v1kOS1k0kFjbzPDSIqTLtXEPbc=/18x0:734x477/750x500/data/photo/2020/03/09/5e65613d60411.jpg','Foto_Ke-2',))
    threads.append(x)
    x = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/l-zUYoLCXYyKqMaAVNz9SexPXsg=/0x0:864x576/750x500/data/photo/2018/11/16/2037804675.jpg','Foto_Ke-3',))
    threads.append(x)
    
    for i in threads:
        i.start()
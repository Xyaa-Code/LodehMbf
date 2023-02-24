import os, time, requests
from rich.console import Console
console = Console()

class Facebook:
    
    def __init__(self):
        self.clear = os.system("clear")
        self.ses = requests.Session()
        self.H2 = "[green1]"
        self.P2 = "[white]"
        self.M2 = "[red1]"
        self.wa = "https://wa.me/+16143244921"
        self.text = "assalamualaikum+bang"
        self.menu()

    def menu(self):
        try:self.clear
        except:pass
        console.print(f" {self.P2}[{self.M2}!{self.P2}] Error {self.M2}404{self.P2} Not Found")
        console.print(f" {self.P2}[{self.M2}!{self.P2}] Script ini sudah di tutup oleh admin")
        xcTeam = console.input(f" {self.P2}[{self.H2}+{self.P2}] Ingin menghubungi admin? (Y/t) : ")
        if xcTeam in ["y","Y"]:
          self.WhatsApp()
        else:
          exit()
     
    def WhatsApp(self):
         console.print(f" {self.P2}[{self.H2}✓{self.P2}] Anda akan di arahkan ke WhatsApp")
         with requests.Session() as ses:
              try:
                  os.system("xdg-open {}?text={}".format(self.wa, self.text))
                  self.clear
                  self.menu()
              except requests.exceptions.ConnectionError:
                  console.print(f" {self.P2}[{self.M2}!{self.P2}] tidak ada koneksi internet")
                  time.sleep(3);console.input(f" {self.P2}[{self.H2}+{self.P2}] Tekan Enter ");self.menu()
              

if __name__ == '__main__':
   try:os.system("git pull")
   except:pass
   Facebook()

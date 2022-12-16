#->> Module
import os, random, requests as r
from requests.exceptions import ConnectionError
from rich.console import Console

url = 'https://wallpaperaccess.com'
ses = r.Session()
con = Console()

succes = 0

def getCount():
    try:
        api = ses.get('https://api.countapi.xyz/hit/ipan/spammer').json()
        count = api['value']
        return count
    except ConnectionError:
        con.print('[bright_red]╭[blue_violet][[green3]•[blue_violet]][bright_white] Connection Error')
        con.print('[bright_red]╰[blue_violet][[green3]•[blue_violet]][bright_white] Koneksi Internet Bermasalah')
        sys.exit()

def getIp():
    try:
        api = ses.get('http://ipwho.is/').json()
        ip = api['ip']
        return ip
    except ConnectionError:
        con.print('[bright_red]╭[blue_violet][[green3]•[blue_violet]][bright_white] Connection Error')
        con.print('[bright_red]╰[blue_violet][[green3]•[blue_violet]][bright_white] Koneksi Internet Bermasalah')
        sys.exit()


def genxtt5():
    global succes, failed, log
    #->> Checking Files
    try:
        log = open('record.txt', 'r').read()
    except FileNotFoundError:
        with open('record.txt', 'w') as gx1:
            gx1.write('')
    #->> maim
    try:
        jumlah = int(con.input("[bright_red]╰[blue_violet][[green3]•[blue_violet]][bright_white] Mau Berapa Gambar [blue_violet]: "))
        con.print('\n[bright_red]╭[blue_violet][[green3]•[blue_violet]][bright_white] Result Random Image Downloader')
        while(succes < jumlah):
            number = random.randrange(0, 9999999)
            #->> request to api
            image = ses.get(f'{url}/full/{number}.jpg', headers={'User-Agent':'Mozilla/5.0 (Linux; U; Android 7.0; es-es; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.4.10'})
            if f'number' in log:
                pass
            else:
                if '<!DOCTYPE html>' in image.text:
                    pass
                else:
                    #->> write image
                    with open(f'/sdcard/download/{number}.jpg', 'wb') as write:
                        write.write(image.content)
                    #->> write log record 
                    with open('record.txt', 'a') as logwrite:
                        logwrite.write(f'{number}, ')
                    con.print(f"[bright_red]├[blue_violet][[green3]•[blue_violet]][bright_white] {number}.jpg [green1]Succes Downloaded")
                    succes += 1
        if succes == jumlah:
            con.print(f"[bright_red]│\n╰[blue_violet][[green3]•[blue_violet]][bright_white] Join Group [bright_yellow]https://fb.com/groups/912488126397893/")
            os.system('xdg-open https://facebook.com/groups/912488126397893/')
    except ValueError:
        con.print('\n[bright_red]╭[blue_violet][[green3]•[blue_violet]][bright_white] ValueError')
        con.print('[bright_red]╰[blue_violet][[green3]•[blue_violet]][bright_white] Masukan Angka Bukan Huruf')

def main():
    os.system('clear')
    con.print(f"""
[blue_violet]╦[bright_white]┌┬┐┌─┐┌─┐┌─┐[blue_violet]╦═╗[bright_white]┌─┐┌┐┌┌┬┐[bright_red] ╭[bright_yellow][[green1]•[bright_yellow]][bright_white] Coded By [blue_violet]:[bright_white] C3ph1r1T
[blue_violet]║[bright_white]│││├─┤│ ┬├┤ [blue_violet]╠╦╝[bright_white]├─┤│││ ││[bright_red] ├[bright_yellow][[green1]•[bright_yellow]][bright_white] Fb [blue_violet]:[bright_white] Novia Lzid
[blue_violet]╩[bright_white]┴ ┴┴ ┴└─┘└─┘[blue_violet]╩╚═[bright_white]┴ ┴┘└┘─┴┘[bright_red] ╰[bright_yellow][[green1]•[bright_yellow]][bright_white] Github [blue_violet]:[bright_white] /hekelpro
---------------------------------------------------
[bright_red]╭[blue_violet][[green3]•[blue_violet]][bright_white] Ip Loockup [blue_violet]:[bright_cyan] {getIp()}
[bright_red]├[blue_violet][[green3]•[blue_violet]][bright_white] Count [blue_violet]:[bright_white] {getCount()}
[bright_red]├[blue_violet][[green3]•[blue_violet]][bright_white] Save In [blue_violet]:[green1] /sdcard/download
[bright_red]│""")
    genxtt5()
    
    
main()

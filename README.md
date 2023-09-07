# PowerJoker
<img src="https://img.shields.io/maintenance/yes/2023"> <img src="https://img.shields.io/badge/Developed%20on-kali%20linux-blueviolet"> <img src="https://img.shields.io/badge/Windws_11-Tested-tested"><br>
Note: if you have issues or have suggestions for improvement, please don't hesitate to reach out
__________________________________________________
'PowerJoker' is a A PowerShell script which obfuscate a SimplePowerShell payload in each execution.
in every execution of the script, after user enter LHOST/LPORT, the script generates a SimplePowerShell code, but in an {0/B/F/u/$/c/a/t/3} way which (for now), can evade the Windows Defender/RealTimeProtection. Instead of try changing it manually, the script check for 'known' words, and replace them with a random onces. When done, executing the .ps file results in a shell on the attacker machine, without victim notice it (process runs background). note: Read Bottom Lines about the .ps1 file.

# Usage
1. Turn on defender on victim machine.
2. git clone
3. pip3 install -r requirements.txt 
4. python3 PowerJoker.py -l [ LOCAL MACHINE ] -p [ PORT ]
5. run the powershell code on the victim machine
NOTE: you can make a .ps file and send it to the victim, which must have admin permissions on the station. when the .ps script launch, it will execute as administrator permissions and could give high permissions. for now, these lines of code are just comments, but you can modifiy them as you wish. just uncoment the 'privilege' inside the source, and play with it the way want [ Read Update please ]
6. Make sure victim runs it.

# ForNow

![1](https://user-images.githubusercontent.com/90532971/207036661-561f7146-46f7-4e55-bd2f-33e2b39a30ed.png)

Windows keeps looking as we all know for such methods of bypassing AV's. for now, it seems the payload works. Please, if from some reason the script got chought by Defender, i would like to know.

https://github.com/Adkali/PowerJoker/assets/90532971/525e7aaa-68c6-4b12-9669-60f95d1c947a

When the process finish, victim must run the genereted PowerShell code. when he does, wait to recieve a shell. Now Soon i will add more options of bypassing Defender because i know that there are more options/method of bypassing, but again - it can change in everyday. what works today, might not work tomorrow.

# Updates
Made the code results in giving the base64 as the payload and also generate a 'Privilege.ps1' file which can have inside it the base64 payload. just replace it inside the section where['BASE64_ENCODED_COMMAND_HERE'] with the base64 payload, and you can use the .ps1 instead using only the payload.<br>
### <b>07/04</b> 
- PowerJoker can now randomly pick variables and strings.
- With this method, it is easier to evade real-time protection. I'm currently working on some new obfuscation techniques.<br>
### <b>28/04 Update:</b>
- Add the ability to show the replaced words in each execution.
- PowerJoker uses the random ability to pick-up from a list.
- Add more functionality to the code for user interaction.
- Using -r flag will show the results in raw mode.
### <b>30/08 Update:</b>
- Auto listener with nc.
- Fix output when commands are entered.<br>
Now Using another layer of obfuscating could be even strong when combine PJ inside a the generated ps1 file.
### <b>5/9 Update:</b>
#### Enhanced Session Management:
- Users can now maintain distinct sessions when interacting with PJ.
- On initiating a session, users have the option of selecting a specific session by entering its ID.
- Once inside the session, pressing "CTRL+C" allows users to pause the current session and switch between sessions.
- Commands like "exit" or "quit" will terminate the current session. If you wish to close all, simply select "0" from the menu. Note while inside a session, and getting a new connection makes it look like it got hanging, press 'CTRL + C' should make it ok.go back and select the SessionID you want.
#### Advanced Payload Obfuscation:
- More layers of obfuscation.
- Note: For users seeking an extra layer, final payload can be a awesome start.
#### Improved User Interface:
- Colors/INFO/OUTPUT has been improved to be much more nicely.
-Note: do not forget to install the requirements.txt. if you face into errors, share me with the information.

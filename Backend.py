from zipfile import ZipFile
from tkinter.filedialog import askopenfilename,askdirectory

def PassCrack(encrpyted,word,result):
    result.set("[+] Beginning bruteforce ")
#Load the zip folder as variable zf    
    with ZipFile(encrpyted) as zf:
#Iterating through the file 'rockyou.txt' and brute force every string into the encrypted zip folder to find if there is any match.
        with open(word, 'r') as passw:
            for line in passw:
                tryword=line.strip()
#Removing the paragraph spaces after every string in 'rockyou.txt'
                try:
                    zf.extractall(pwd=tryword.encode('utf-8'))
#Encode the strings into 'UTF-8' to make it work with the zip folder and print the password if any match is found.
                    result.set("\nPassword is "+tryword+"\n[+] Bruteforce success")
                    save_file=askdirectory(title="Save the File")
                    if save_file:
                        zf.extractall(pwd=tryword.encode('utf-8'),path=save_file)
                    return True
                except:
                    continue
        result.set("\nNo string matched as the password!\n[-] Bruteforce Failed")
        return False

def getZip(zip_file):
    zipath=askopenfilename(title="Select the Zip file",filetypes=[("zip files",".zip")])
    zip_file.set(zipath)

def getWord(word_file):
    wordpath=askopenfilename(title="Select the TXT file",filetypes=[("txt files",".txt")])
    word_file.set(wordpath)

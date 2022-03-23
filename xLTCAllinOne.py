from lxml import html
import requests
import random
from colorama import Fore, Style
from hdwallet import HDWallet
from hdwallet.symbols import LTC as SYMBOL

z = 1
t = 4
while True:
    c1 = str(random.choice('0123456789abcdefABCDEF'))
    c2 = str(random.choice('0123456789abcdefABCDEF'))
    c3 = str(random.choice('0123456789abcdefABCDEF'))
    c4 = str(random.choice('0123456789abcdefABCDEF'))
    c5 = str(random.choice('0123456789abcdefABCDEF'))
    c6 = str(random.choice('0123456789abcdefABCDEF'))
    c7 = str(random.choice('0123456789abcdefABCDEF'))
    c8 = str(random.choice('0123456789abcdefABCDEF'))
    c9 = str(random.choice('0123456789abcdefABCDEF'))
    c10 = str(random.choice('0123456789abcdefABCDEF'))
    c11 = str(random.choice('0123456789abcdefABCDEF'))
    c12 = str(random.choice('0123456789abcdefABCDEF'))
    c13 = str(random.choice('0123456789abcdefABCDEF'))
    c14 = str(random.choice('0123456789abcdefABCDEF'))
    c15 = str(random.choice('0123456789abcdefABCDEF'))
    c16 = str(random.choice('0123456789abcdefABCDEF'))
    c17 = str(random.choice('0123456789abcdefABCDEF'))
    c18 = str(random.choice('0123456789abcdefABCDEF'))
    c19 = str(random.choice('0123456789abcdefABCDEF'))
    c20 = str(random.choice('0123456789abcdefABCDEF'))
    c21 = str(random.choice('0123456789abcdefABCDEF'))
    c22 = str(random.choice('0123456789abcdefABCDEF'))
    c23 = str(random.choice('0123456789abcdefABCDEF'))
    c24 = str(random.choice('0123456789abcdefABCDEF'))
    c25 = str(random.choice('0123456789abcdefABCDEF'))
    c26 = str(random.choice('0123456789abcdefABCDEF'))
    c27 = str(random.choice('0123456789abcdefABCDEF'))
    c28 = str(random.choice('0123456789abcdefABCDEF'))
    c29 = str(random.choice('0123456789abcdefABCDEF'))
    c30 = str(random.choice('0123456789abcdefABCDEF'))
    c31 = str(random.choice('0123456789abcdefABCDEF'))
    c32 = str(random.choice('0123456789abcdefABCDEF'))
    c33 = str(random.choice('0123456789abcdefABCDEF'))
    c34 = str(random.choice('0123456789abcdefABCDEF'))
    c35 = str(random.choice('0123456789abcdefABCDEF'))
    c36 = str(random.choice('0123456789abcdefABCDEF'))
    c37 = str(random.choice('0123456789abcdefABCDEF'))
    c38 = str(random.choice('0123456789abcdefABCDEF'))
    c39 = str(random.choice('0123456789abcdefABCDEF'))
    c40 = str(random.choice('0123456789abcdefABCDEF'))
    c41 = str(random.choice('0123456789abcdefABCDEF'))
    c42 = str(random.choice('0123456789abcdefABCDEF'))
    c43 = str(random.choice('0123456789abcdefABCDEF'))
    c44 = str(random.choice('0123456789abcdefABCDEF'))
    c45 = str(random.choice('0123456789abcdefABCDEF'))
    c46 = str(random.choice('0123456789abcdefABCDEF'))
    c47 = str(random.choice('0123456789abcdefABCDEF'))
    c48 = str(random.choice('0123456789abcdefABCDEF'))
    c49 = str(random.choice('0123456789abcdefABCDEF'))
    c50 = str(random.choice('0123456789abcdefABCDEF'))
    c51 = str(random.choice('0123456789abcdefABCDEF'))
    c52 = str(random.choice('0123456789abcdefABCDEF'))
    c53 = str(random.choice('0123456789abcdefABCDEF'))
    c54 = str(random.choice('0123456789abcdefABCDEF'))
    c55 = str(random.choice('0123456789abcdefABCDEF'))
    c56 = str(random.choice('0123456789abcdefABCDEF'))
    c57 = str(random.choice('0123456789abcdefABCDEF'))
    c58 = str(random.choice('0123456789abcdefABCDEF'))
    c59 = str(random.choice('0123456789abcdefABCDEF'))
    c60 = str(random.choice('0123456789abcdefABCDEF'))
    c61 = str(random.choice('0123456789abcdefABCDEF'))
    c62 = str(random.choice('0123456789abcdefABCDEF'))
    c63 = str(random.choice('0123456789abcdefABCDEF'))
    c64 = str(random.choice('0123456789abcdefABCDEF'))
    magic = (
                c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 + c20 + c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30 + c31 + c32 + c33 + c34 + c35 + c36 + c37 + c38 + c39 + c40 + c41 + c42 + c43 + c44 + c45 + c46 + c47 + c48 + c49 + c50 + c51 + c52 + c53 + c54 + c55 + c56 + c57 + c58 + c59 + c60 + c61 + c62 + c63 + c64)
    PRIVATE_KEY = str(magic)
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    privatekey = hdwallet.private_key()
    addr = hdwallet.p2wsh_address()
    addr1 = hdwallet.p2pkh_address()
    addr2 = hdwallet.p2wpkh_in_p2sh_address()
    addr3 = hdwallet.p2wpkh_address()

    urlblock = "https://litecoin.atomicwallet.io/address/" + addr
    urlblock1 = "https://litecoin.atomicwallet.io/address/" + addr1
    urlblock2 = "https://litecoin.atomicwallet.io/address/" + addr2
    urlblock3 = "https://litecoin.atomicwallet.io/address/" + addr3
    respone_block = requests.get(urlblock)
    respone_block1 = requests.get(urlblock1)
    respone_block2 = requests.get(urlblock2)
    respone_block3 = requests.get(urlblock3)
    byte_string = respone_block.content
    byte_string1 = respone_block1.content
    byte_string2 = respone_block2.content
    byte_string3 = respone_block3.content
    source_code = html.fromstring(byte_string)
    source_code1 = html.fromstring(byte_string1)
    source_code2 = html.fromstring(byte_string2)
    source_code3 = html.fromstring(byte_string3)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    treetxid1 = source_code1.xpath(xpatch_txid)
    treetxid2 = source_code2.xpath(xpatch_txid)
    treetxid3 = source_code3.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    xVol1 = str(treetxid1[0].text_content())
    xVol2 = str(treetxid2[0].text_content())
    xVol3 = str(treetxid3[0].text_content())
    print(Fore.YELLOW + 'LTC P2WSH        : ' + Fore.RED + str(xVol) + ' ' + Fore.GREEN + addr + '\n'
          + Fore.YELLOW + 'LTC P2PKH        : ' + Fore.RED + str(xVol1) + ' ' + Fore.GREEN + addr1 + '\n'
          + Fore.YELLOW + 'LTC  P2SH        : ' + Fore.RED + str(xVol2) + ' ' + Fore.GREEN + addr2 + '\n'
          + Fore.YELLOW + 'LTC P2WPK        : ' + Fore.RED + str(xVol3) + ' ' + Fore.GREEN + addr3 + '\n'
          + Fore.RED + 'LTC PRIVATEKEY   : ' + Fore.WHITE + str(privatekey) + '\n'
          + Fore.YELLOW + 'Scan : ' + Fore.MAGENTA + str(z) + '  ' + Fore.YELLOW + 'Total Scan : ' + Fore.MAGENTA + str(t)
          + Fore.BLUE + '\n=============================[MMDRZA.CoM]==============================' + Style.RESET_ALL)
    z += 1
    t += 4
    if int(xVol) or int(xVol1) or int(xVol2) or int(xVol3) > 0:
        f = open("LTCWINERRRRRRRRRRRRRRRRRRRRRR.txt","a")
        f.write('\n' + addr)
        f.write('\n' + privatekey)
        f.write('\n' + xVol)
        f.write('\n==================[MMDRZA.COM]===================\n')
        f.close()
        print('Details Wallet Saved Text File ....\n-----------MMDRZA.CoM---------------\n')
        continue

from colorama import Fore, Style, init

def bytexor_menu():
    try:
        bytexor = input(f"{Fore.RED}[ByteXor] > ")

        if bytexor == "bytexorencode":
            string = input(f"{Fore.BLUE}[+] String [+] > ")
            key = input(f"{Fore.BLUE}[+] Key [+] > ")
            i = 0
            final = []

            for x in string:
              final.append(chr(ord(x)^ord(key[i])))
              i += 1
              if (i == len(key)):
                i = 0

            finaloutput = str(final).replace('[', "'").replace(']', '').replace("'", '').replace(',', '').replace(' ', '')
            print(f"{Fore.YELLOW}" + finaloutput)
            bytexor_menu()

        elif bytexor == "help":
            a = f"""{Fore.BLUE}
            [+] Usage [+]
    
        [Xor Bytes] > bytexorencode 
        [Exit]      > exit
                         """
            print(a)
            bytexor_menu()

        elif bytexor == "exit":
            print(f"{Fore.YELLOW}[+] Exit [+]")

        else:
            bytexor_menu()
    except SyntaxError:
        print("[+] Error [+]")
    except ValueError:
        print("[+] Error [+]")
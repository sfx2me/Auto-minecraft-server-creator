import os, requests
def get_version(version):
    if version == "1.18":
        download(18)
    elif version == "1.19":
        download(19)
    else:
        print("Only type 1.19 or 1.18")
        exit()

def download(wanted_version):
    if wanted_version == 18:
        os.system("cls")
        print("go to https://papermc.io/downloads#Paper-1.18")
        print("and get the newest version id and paste below")
        id = input(">>>")
        response = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/386/downloads/paper-1.18.2-{id}.jar")
        open("server.jar", "wb").write(response.content)
    elif wanted_version == 19:
        os.system("cls")
        print("go to https://papermc.io/downloads#Paper-1.19")
        print("and get the newest version id and paste below")
        id = input(">>>")
        response = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/1.19/builds/36/downloads/paper-1.19-{id}.jar")
        open("server.jar", "wb").write(response.content)
        
def setup_server(ram):
    ram = int(ram)
    print("Seting up everything for you...")
    start_server(ram)
    print("Agreeing eula for you")
    os.remove("eula.txt")
    with open('eula.txt', 'w') as f:
        f.write('eula=true')
        f.close()
    write_start_file(ram)
    start_server(ram)

def start_server(ram):
    os.system(f"java -Xmx{ram}G -Xms{ram}G -jar server.jar nogui PAUSE")

def write_start_file(ram):
    with open('START_SERVER.bat', 'w') as f:
        f.write(f'java -Xmx{ram}G -Xms{ram}G -jar server.jar nogui PAUSE')
        f.close()

def main():
    os.system("cls")
    print("\nIn what version should your minecraft server be?")
    print("""
##############
#    1.18    #
#    1.19    #  
##############  
""")
    version = input(">>>")
    get_version(version)
    os.system("cls")
    print("How much ram should the server have? (4 is recommended)")
    print("""
#############
#  1 GB RAM #
#  2 GB RAM #
#  4 GB RAM #
#  8 GB RAM #
#############
""")
    ram = input(">>>")
    setup_server(ram)
main()

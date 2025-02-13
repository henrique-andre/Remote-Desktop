import os
import json

def verificar_ou_criar_json(json_path):
    if not os.path.exists(json_path):
        exemplo_grupos = {
            "USUARIO": "redeboticario\\tr004947",
            "GRUPOS": {
                "MESA1": {
                    "ESTEIRA_1": ["10.197.66.130", "10.197.66.132","10.197.66.133"],
                    "ESTEIRA_2_PRIME": ["10.197.66.134", "10.197.66.135","10.197.66.136","10.197.66.137","10.197.66.138","10.197.66.139"],
                    "ESTEIRA_3": ["10.197.66.140", "10.197.66.141","10.197.66.142","10.197.66.143","10.197.66.146","10.197.66.147","10.197.66.148"],
                    "PDVS_ADICIONAIS":["10.197.66.144","10.197.66.145"],
                    "AUTOMACAO": ["10.197.66.206",""],
                    "ESTEIRA_QDB": ["10.197.66.146", "10.197.66.147","10.197.66.148"],
                },
                "MESA2":{
                    "INFRA VAREJO":["10.197.67.99","10.197.67.99"],
                    "BLZ": ["10.197.67.111 ","10.197.67.112"] ,
                    "DEV MOB GB": ["10.197.67.40"],
                    "OMNICHANNEL": ["10.197.67.99","10.197.67.100","10.197.67.101","10.197.67.102","10.197.67.103"],
                    "MOTOR_PROMOCAO": ["10.197.67.93","10.197.67.90","10.197.67.105","10.197.67.106","10.197.67.107"],
                    "AUTOMACAO": ["10.197.67.94", "10.197.67.95", "10.197.67.96","10.197.67.97"],
                    "VMS_HOSTS": ["10.197.67.116","10.197.67.115","10.197.67.118","10.197.67.117","10.197.67.118"],
                },
                "MESA3":{
                    "ESTEIRA_PDVGB": ["10.197.67.60", "10.197.67.61","10.197.67.62","10.197.67.63","10.197.67.64","10.197.67.65","10.197.67.66","10.197.67.67","10.197.67.68","10.197.67.69","10.197.67.70","10.197.67.71","10.197.67.72","10.197.67.73","10.197.67.74","10.197.67.75"],
                }
            }
        }
        os.makedirs("config", exist_ok=True)
        with open(json_path, "w") as f:
            json.dump(exemplo_grupos, f, indent=4)

def carregar_dados(json_path):
    with open(json_path, "r") as f:
        return json.load(f)

def escolher_opcao(opcoes, mensagem):
    print(f"\n=== {mensagem} ===")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    escolha = int(input("\nEscolha uma opção pelo número: ")) - 1
    return list(opcoes)[escolha]

def criar_arquivo_rdp(ip, usuario):
    os.makedirs("config", exist_ok=True)
    arquivo_rdp = "config/conexao.rdp"
    
    # Se o IP não tiver porta, adiciona 
    if ':' not in ip:
        ip += ':7000'

    conteudo_rdp = f"""
    full address:s:{ip}
    username:s:{usuario}
    screen mode id:i:2
    session bpp:i:32
    compression:i:1
    allow font smoothing:i:1
    disable wallpaper:i:0
    disable full window drag:i:0
    disable menu anims:i:0
    disable themes:i:0
    disable cursor setting:i:0
    bitmapcachepersistenable:i:1
    audiomode:i:0
    redirectclipboard:i:1
    """
    with open(arquivo_rdp, "w") as file:
        file.write(conteudo_rdp)
    return arquivo_rdp

def conectar_rdp(arquivo_rdp, ip, usuario):
    print(f"\nConectando a {ip} como {usuario}...")
    os.system(f'mstsc {arquivo_rdp}')

def main():
    json_path = "config/grupos.json"
    verificar_ou_criar_json(json_path)
    dados = carregar_dados(json_path)
    usuario = dados["USUARIO"]
    grupos = dados["GRUPOS"]
    
    while True:
        grupo_escolhido = escolher_opcao(grupos.keys(), "GRUPOS DISPONÍVEIS")
        esteira_escolhida = escolher_opcao(grupos[grupo_escolhido].keys(), f"Esteiras do grupo {grupo_escolhido}")

        # Agora pegamos a lista de IPs dessa esteira
        lista_ips = grupos[grupo_escolhido][esteira_escolhida]
    
        # Se houver apenas um IP, conectamos diretamente, senão o usuário escolhe um
        if len(lista_ips) == 1:
            ip_selecionado = lista_ips[0]
        else:
            ip_selecionado = escolher_opcao(lista_ips, f"IPs da esteira {esteira_escolhida}")

        arquivo_rdp = criar_arquivo_rdp(ip_selecionado, usuario)
        conectar_rdp(arquivo_rdp, ip_selecionado, usuario)

        continuar = input("\nDeseja conectar a outro IP? (s/n): ").strip().lower()
        if continuar != 's':
            break


if __name__ == "__main__":
    main()
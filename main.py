#Sistema especialista humano Py
#Aluno Paulo Henrique F. dos Santos

base_conhecimento = {
    "lentidão": {
        "sinais": ["computador lento", "carregamento demorado"],
        "causas": ["muitos programas abertos", "malware", "falta de espaço em disco"],
        "solucoes": ["fechar programas desnecessários", "realizar uma verificação de malware", "liberar espaço em disco"]
    },
    "falha_no_sistema": {
        "sinais": ["tela azul", "reinicialização inesperada"],
        "causas": ["conflito de drivers", "hardware com falha"],
        "solucoes": ["atualizar drivers", "testar hardware"]
    },
    "problema_de_hardware": {
        "sinais": ["ruídos estranhos", "não liga"],
        "causas": ["fonte de energia defeituosa", "HD danificado"],
        "solucoes": ["trocar a fonte", "substituir HD"]
    },
    "problemas_de_conectividade": {
        "sinais": ["sem internet", "conexão instável"],
        "causas": ["roteador fora do ar", "cabo danificado"],
        "solucoes": ["reiniciar o roteador", "verificar cabos"]
    },
    "vírus_detectado": {
        "sinais": ["pop-ups constantes", "programas desconhecidos"],
        "causas": ["malware instalado"],
        "solucoes": ["usar antivírus", "restaurar sistema"]
    },
    "erro_de_impressão": {
        "sinais": ["impressora não responde", "impressão falha"],
        "causas": ["drivers da impressora desatualizados", "papel preso"],
        "solucoes": ["atualizar drivers", "remover papel preso"]
    },
    "problemas_de_audio": {
        "sinais": ["sem som", "som distorcido"],
        "causas": ["drivers de áudio desatualizados", "cabo de áudio solto"],
        "solucoes": ["atualizar drivers de áudio", "conectar corretamente os cabos"]
    },
    "atualizações_falhadas": {
        "sinais": ["computador não atualiza", "erros de instalação"],
        "causas": ["falta de espaço", "conflitos com software"],
        "solucoes": ["liberar espaço", "desinstalar software conflitante"]
    },
    "problemas_de_bateria": {
        "sinais": ["bateria não carrega", "duração curta"],
        "causas": ["bateria desgastada", "carregador defeituoso"],
        "solucoes": ["substituir bateria", "testar carregador"]
    },
    "problemas_de_fonte": {
        "sinais": ["computador não liga", "fumaça"],
        "causas": ["fonte de energia queimada"],
        "solucoes": ["substituir a fonte"]
    },
    "sistema_lento_após_atualização": {
        "sinais": ["lento após atualização", "congelamentos"],
        "causas": ["incompatibilidade de software", "drivers desatualizados"],
        "solucoes": ["reverter a atualização", "atualizar drivers"]
    },
    "problemas_de_ventilação": {
        "sinais": ["aquecimento excessivo", "desligamentos repentinos"],
        "causas": ["ventiladores obstruídos", "pasta térmica seca"],
        "solucoes": ["limpar ventiladores", "aplicar nova pasta térmica"]
    },
    "erro_no_navegador": {
        "sinais": ["navegador trava", "páginas não carregam"],
        "causas": ["extensões conflitantes", "cache corrompido"],
        "solucoes": ["desativar extensões", "limpar cache"]
    },
    "problemas_de_login": {
        "sinais": ["não consegue acessar contas", "senha incorreta"],
        "causas": ["senha esquecida", "conta bloqueada"],
        "solucoes": ["recuperar senha", "entrar em contato com suporte"]
    },
    "problemas_de_display": {
        "sinais": ["tela preta", "imagem distorcida"],
        "causas": ["cabo solto", "placa de vídeo com problemas"],
        "solucoes": ["verificar conexões", "substituir a placa de vídeo"]
    },
    "disco_cheio": {
        "sinais": ["mensagens de espaço insuficiente"],
        "causas": ["arquivos grandes", "muitos arquivos temporários"],
        "solucoes": ["limpar arquivos temporários", "mover arquivos para armazenamento externo"]
    },
    "conexão_wifi_intermitente": {
        "sinais": ["desconexões frequentes"],
        "causas": ["interferência de sinal", "distância do roteador"],
        "solucoes": ["reposicionar o roteador", "verificar outros dispositivos"]
    },
    "erros_de_disco": {
        "sinais": ["erro de leitura", "computador não reconhece o disco"],
        "causas": ["disco rígido danificado", "cabo solto"],
        "solucoes": ["substituir disco rígido", "verificar conexões"]
    },
    "problemas_de_sistema_operacional": {
        "sinais": ["sistema não inicia", "loop de inicialização"],
        "causas": ["arquivos de sistema corrompidos"],
        "solucoes": ["usar recuperação de sistema", "reinstalar o SO"]
    },
    "perda_de_dados": {
        "sinais": ["arquivos desaparecidos", "erro de recuperação"],
        "causas": ["exclusão acidental", "formatação"],
        "solucoes": ["usar software de recuperação", "restaurar de backup"]
    },
    "conflito_de_programas": {
        "sinais": ["programas não abrem", "erros de execução"],
        "causas": ["softwares incompatíveis"],
        "solucoes": ["desinstalar programas conflitantes"]
    },
    "atraso_na_resposta": {
        "sinais": ["respostas lentas de aplicativos", "travas frequentes"],
        "causas": ["uso elevado de CPU", "falta de RAM"],
        "solucoes": ["fechar aplicativos pesados", "aumentar memória RAM"]
    },
    "falta_de_driver": {
        "sinais": ["periféricos não reconhecidos"],
        "causas": ["drivers não instalados"],
        "solucoes": ["instalar drivers necessários"]
    },
    "problemas_de_software": {
        "sinais": ["crashes frequentes", "não inicia"],
        "causas": ["software corrompido", "instalação incompleta"],
        "solucoes": ["reinstalar software", "verificar integridade"]
    },
    "problemas_de_atualização_do_windows": {
        "sinais": ["atualização não completa", "erros de instalação"],
        "causas": ["falta de espaço", "conflitos com antivírus"],
        "solucoes": ["liberar espaço", "desativar antivírus temporariamente"]
    },
    "erro_de_aplicativo": {
        "sinais": ["aplicativo fecha inesperadamente"],
        "causas": ["conflito com outro aplicativo", "falta de memória"],
        "solucoes": ["reiniciar o aplicativo", "aumentar memória RAM"]
    },
    "configuração_de_rede_incorreta": {
        "sinais": ["não consegue acessar a rede"],
        "causas": ["configurações de IP erradas"],
        "solucoes": ["verificar configurações de rede", "resetar o roteador"]
    },
    "problemas_de_telefones_e_dispositivos_portáteis": {
        "sinais": ["não conecta ao computador"],
        "causas": ["drivers ausentes", "cabo danificado"],
        "solucoes": ["instalar drivers", "trocar cabo"]
    },
    "atualização_do_bios": {
        "sinais": ["computador não inicia após atualização"],
        "causas": ["atualização incorreta", "compatibilidade"],
        "solucoes": ["reverter atualização", "atualizar BIOS corretamente"]
    },
    "sistema_operacional_corrompido": {
        "sinais": ["erros constantes", "não inicia"],
        "causas": ["arquivos de sistema corrompidos"],
        "solucoes": ["reinstalar o sistema", "usar ferramenta de reparo"]
    },
}


memoria_trabalho = {}

def coletar_informacoes():
    print("""Descreva o problema que você está enfrentando:""")
    problema = input().lower().replace(" ", "_")
    memoria_trabalho['problema'] = problema


def diagnosticar():
    problema = memoria_trabalho.get('problema', '')
    for chave, info in base_conhecimento.items():
        if chave in problema:
            return chave, info
    return None, None

def apresentar_solucao(chave, info):
    print(f"Problema identificado: {chave.capitalize()}")
    print("Possíveis causas:")
    for causa in info["causas"]:
        print(f"- {causa}")
    print("Soluções sugeridas:")
    for solucao in info["solucoes"]:
        print(f"- {solucao}")

def reiniciar():
    global memoria_trabalho
    memoria_trabalho = {}
    print("\nVamos tentar novamente...\n")
while True:
    coletar_informacoes()

    try:
        problema_chave, info_do_problema = diagnosticar()
        if info_do_problema:
            apresentar_solucao(problema_chave, info_do_problema)
            break
        else:
            raise ValueError("Problema não identificado.")

    except ValueError:
        print("Desculpe, não consegui identificar o problema. Tente descrever de outra forma.")
        reiniciar()
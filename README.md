
```markdown
# Conexão RDP QA

Este projeto permite acesso rápido a máquinas do ambiente QA utilizando o protocolo RDP.

## Estrutura do Projeto

```
build/
	conectar_rdp/
		Analysis-00.toc
		conectar_rdp.pkg
		

EXE-00.toc


		localpycs/
		

PKG-00.toc


		PYZ-00.pyz
		PYZ-00.toc
		warn-conectar_rdp.txt
		

xref-conectar_rdp.html




conectar_rdp.py




conectar_rdp.spec


Config/
	conexao.rdp
	grupos.json
image/


README.md




test.py




versionfile.py




versionfile.txt


```

## Instalação

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Para criar um arquivo RDP, execute o script 

test.py

:
```sh
python test.py
```

## Estrutura dos Arquivos

- 

conectar_rdp.py

: Script principal para conexão RDP.
- 

conectar_rdp.spec

: Arquivo de especificação para PyInstaller.
- 

Config

: Contém arquivos de configuração como `conexao.rdp` e `grupos.json`.
- 

versionfile.py

: Script para criar o arquivo de versão.
- 

test.py

: Script de teste para criar arquivos RDP.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
```

Certifique-se de ajustar `<URL_DO_REPOSITORIO>` e `<NOME_DO_REPOSITORIO>` conforme necessário.
Certifique-se de ajustar `<URL_DO_REPOSITORIO>` e `<NOME_DO_REPOSITORIO>` conforme necessário.

Código semelhante encontrado com 1 tipo de licença
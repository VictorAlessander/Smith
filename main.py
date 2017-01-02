# coding: UTF-8


import sites


"""
Program still working only in Kabum website, for now.

"""

print(
"""
 __           _ _   _     
/ _\_ __ ___ (_) |_| |__  
\ \| '_ ` _ \| | __| '_ \ 
_\ \ | | | | | | |_| | | |
\__/_| |_| |_|_|\__|_| |_|
                          

Sites Disponíveis:

+-------------------+
|[S]art / Sair = 0 |
+-------------------+

Digite help para mais informações.

""")

while(True):

	opcao = str.lower(input('>> '))

	if opcao == 'help' or opcao == 'h':
		print(
"""
Ao selecionar uma das opções, o programa irá abrir um arquivo de texto com os links referentes ao site escolhido
e fará a extração dos dados contidos nos links de acordo com os parâmetros de extração (nome do produto, preço).
Esses dados serão jogados em uma planilha que o programa irá criar caso não exista.
"""
)

	elif opcao == 's':
		print("Insira o nome da planilha (Não esqueça de colocar a extensão .xlsx)")
		nome = str(input())
		sites.extrair(nome)

	elif opcao == '0':
		exit(0)

#!/usr/bin/python
# coding: UTF-8
# NowSearch Spotify

''' Bibliotecas utilizadas '''
import json                        #                         Utilizada para pegar os dados do tipo de arquivo utilizado.
from patricia import trie, _NonTerminal #                                                     Arvore patricia utilizada.
import pickle
import heapq                            #                                          Utilizada para organização dos dados.

''' Aguarda tecla para voltar ao Menu Principal '''
def voltaMenu():
	raw_input("Pressione <Enter> para voltar ao Menu Principal")
	menuPrincipal()

########################################################################################################################
''' Limpa a tela '''
def limpaTela():
	print ('\n' * 100)
########################################################################################################################

########################################################################################################################
''' Heapsort utilizado para organizar os dados '''
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

contadorArtistas = 1                                                        #                      Contador de artistas.
contadorMusicas = 0                                                         #                       Contador de musicas.
contadorIndex = 0

arvoreMusica = trie()                                                       #               Árvore com nome das músicas.
arvoreArtistas = trie()                                                     #              Árvore com nome dos artistas.
auxArtista = trie()                                                         #     Árvore Auxiliar com nome dos artistas.
auxMusica = trie()                                                          #      Árvore Auxiliar com nome das músicas.
Index = list()
########################################################################################################################

########################################################################################################################
''' Lendo o arquivo Json '''
arquivo_dados = raw_input("Insira o nome do arquivo de dados (sem o .json): ")
arquivo_dados = arquivo_dados + ".json"
with open(arquivo_dados) as f:
    data = f.read();
    jsondata = json.loads(data)

    for row in jsondata['items']:

        contadorMusicas = contadorMusicas + 1
        contadorIndex = contadorIndex + 1

        #Lendo a musica
        musica = row['track']['name']
        musica = musica.encode('utf-8')
        musica = musica.lower()

		#Lendo o album
        album = row['track']['album']['name']
        album = album.encode('utf-8')

        #Lendo o artista
        artista = row['track']['artists'][0]['name']
        artista = artista.encode('utf-8')
        artista = artista.lower()

        #Lendo a popularidade
        popularidade = row['track']['popularity']

        if arvoreArtistas.isPrefix(artista):
            idArtista = arvoreArtistas[artista]
            arvoreArtistas[artista] = str(idArtista)
            auxArtista[str(idArtista)] = artista
            auxMusica[str(contadorMusicas)] = musica
            arvoreMusica[musica] = str(contadorMusicas)
        else:
            contadorArtistas = contadorArtistas + 1
            arvoreArtistas[artista] = str(contadorArtistas)
            auxArtista[str(contadorArtistas)] = artista
            arvoreMusica[musica] = str(contadorMusicas)
            auxMusica[str(contadorMusicas)] = musica

        Index.insert(contadorIndex, [(arvoreArtistas[artista]), (popularidade), (album)])
########################################################################################################################

########################################################################################################################
''' Função que cria os arquivos binários. utilizados como índices '''
def criaArquivo(ordem, Dados, nomeArquivo):
    if open(nomeArquivo, 'wb'):
        outFile = open(nomeArquivo, 'wb')
        if ordem == 0:
            pickle.dump(sorted(Dados, reverse=False), outFile)
            outFile.close()
        else:
            pickle.dump(sorted(Dados, reverse=True), outFile)
            outFile.close()
    else:
        print('Impossivel criar arquivo')
########################################################################################################################

########################################################################################################################
''' Função que abre o arquivo para leitura '''
def abreArquivo(nomeArquivo):
    if open(nomeArquivo, 'rb'):
        inFile = open(nomeArquivo, 'rb')
        newList = pickle.load(inFile)
        return newList
    else:
        return ('Não foi possível abrir o arquivo')
########################################################################################################################

########################################################################################################################
''' Listagem de musicas '''
def imprimeListagemMusicas(ordem):
    ordenamento = ""
    NomesFiltrados = sorted(arvoreMusica)
    NomesOrdenados = list()
    for NomesFiltrados in NomesFiltrados:
        idMusica = int(arvoreMusica[NomesFiltrados])
        idArtista = str(Index[idMusica - 1][0])
        NomesOrdenados.append( ((auxMusica[arvoreMusica[NomesFiltrados]]), (auxArtista[idArtista]), (Index[idMusica - 1][1]), (Index[idMusica - 1][2])) )

    criaArquivo(ordem, NomesOrdenados, "ListagemMusicas.bin")
    newList = abreArquivo("ListagemMusicas.bin")

    if ordem == 0:
        ordenamento = "crescente"
    else:
        ordenamento = "decrescente"
    print('\n\nListagem de musicas - Ordem {0}: \n'.format(ordenamento))

    for i, v in enumerate(newList):
        print('- Musica: {0}'.format(v[0]))
        print('  Artista: {0}'.format(v[1]))
        print('  Album: {0}'.format(v[3]))
        print('  Popularidade: {0}'.format(v[2]))
        print('------------------------------------------')
########################################################################################################################

########################################################################################################################
''' Ordenar por duração da música '''
def ordenarPorPopularidade(ordem):
	ordenaPopularidade = list()
	listaPopularidade = list()

	for indice, valor in enumerate(Index):
			listaPopularidade.append(Index[indice][1])
	listaPopularidade = heapsort(listaPopularidade)
	if ordem==0:
		ordemPop = "Musicas menos populares"
	else:
		ordemPop = "Musicas mais populares"

	for i in listaPopularidade:
		for indice, valor in enumerate(Index):
			if Index[indice][1] == i:
				ordenaPopularidade.append(((Index[indice][1]), (auxArtista[Index[indice][0]]),(auxMusica[str(indice+1)]), (Index[indice][2])))

	criaArquivo(ordem, ordenaPopularidade, "ListagemPopularidade.bin")
	newList = abreArquivo("ListagemPopularidade.bin")

	print('\n{0}:\n'.format(ordemPop))
	print('------------------------------------------')
	for i, v in enumerate(newList):
		print('- Popularidade: {0}'.format(v[0]))
		print('- Musica: {0}'.format(v[1]))
		print('- Artista: {0}'.format(v[2]))
		print('- Album: {0}'.format(v[3]))
		print('------------------------------------------')
########################################################################################################################

########################################################################################################################
''' Pesquisa por Nome de música '''
def BuscaPorMusica():
    pesquisaNome = str(raw_input('Digite nome da musica a ser pesquisada: '))
    if arvoreMusica.isPrefix(pesquisaNome):
        NomesFiltrados = sorted(arvoreMusica.iter(pesquisaNome))
	print('\n\nResultado da busca por musica:\n')
        for NomesFiltrados in NomesFiltrados:
            idMusica = int(arvoreMusica[NomesFiltrados])

            idartista = str(Index[idMusica - 1][0])
            print('- Musica: ' + auxMusica[arvoreMusica[NomesFiltrados]])
            print('- Artista: ' + auxArtista[idartista])
            print('- Popularidade: ' + str(Index[idMusica - 1][1]))
            print('------------------------------------------')
    else:
        print('Nenhum registro encontrado!')
########################################################################################################################

########################################################################################################################
''' Busca por Artista '''
def BuscaPorArtista():
	pesquisa = str( raw_input('Digite o nome do artista:') )
	if arvoreArtistas.isPrefix(pesquisa):
		NomesFiltrados = sorted(arvoreArtistas.iter(pesquisa))

		print('\n\nResultado da busca por artista:\n')

		for NomesFiltrados in NomesFiltrados:
			print('Artista: {0}'.format(auxArtista[arvoreArtistas[NomesFiltrados]]))
			for indice, valor in enumerate(Index):
				if Index[indice][0] == arvoreArtistas[NomesFiltrados]:
					indiceMusicas = str((indice)+1)
					print(' - Musica(s): {0}.'.format(auxMusica[indiceMusicas]))
			print('------------------------------------------')
	else:
		print('Nenhum registro encontrado!')
########################################################################################################################

########################################################################################################################
''' Menu '''
def menuPrincipal():
	limpaTela()
	opcao=True
	while opcao:
		print("""
		|**|**************************************************|**|
        |**|                  NOWSEARCH                       |**|
		|**|**************************************************|**|
		|**|        Organize-se por um melhor som!            |**|
		|**|                                                  |**|
		|**| O que voce deseja?                               |**|
		|**| (1) Listagem de musicas (ordem crescente)        |**|
		|**| (2) Listagem de musicas (ordem decrescente)      |**|
		|**| (3) Pesquisar por musica (prefixo)               |**|
        |**| (4) Pesquisar por artista (prefixo)              |**|
        |**| (5) Musicas mais bombadas                        |**|
        |**| (6) Musicas menos bombadas                       |**|
        |**| (7) Sair                                         |**|
        |**|**************************************************|**|
		""")
		opcao=str(raw_input("O que voce deseja? "))
		if (opcao=="1"):
			imprimeListagemMusicas(0)
			voltaMenu()
		elif (opcao=="2"):
			imprimeListagemMusicas(1)
			voltaMenu()
		elif (opcao=="3"):
			BuscaPorMusica()
			voltaMenu()
		elif (opcao=="4"):
			BuscaPorArtista()
			voltaMenu()
		elif (opcao=="5"):
			ordenarPorPopularidade(1)
			voltaMenu()
		elif (opcao=="6"):
			ordenarPorPopularidade(0)
			voltaMenu()
			menuPrincipal()
		elif (opcao=="7"):
			print(">>>   Fim do programa   <<<")
			exit()
		else:
			print("\n Opcao invalida")
########################################################################################################################

limpaTela()
menuPrincipal()

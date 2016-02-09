# NowSearch
Programa organizador de playlists do Spotify.

## Descrição do programa
 O  programa tem como objetivo ler os dados de uma
playlist do aplicativo Spotify (https://www.spotify.com/). São
lidas todas as músicas da playlist e para cada música são
salvas também as seguintes informações: artista, álbum e
popularidade.

  As informações são lidas e armazenadas em uma árvore
do tipo Trie, e também são utilizados arrays auxiliares para
armazenar informações, como álbum e popularidade das
músicas.

## Funcionalidades do NowSearch
- Listagem de músicas, por ordem crescente e
descrescente (trazendo junto os dados do artista,
álbum e popularidade referente a cada música.
- Pesquisa por artista/banda e por música. Busca pode
ser feita apenas com o prefixo das palavras.
- Listagem das músicas por ordem das menos
populares e das mais populares.

## Funções para gravação e leitura de arquivos
  Como a gravação e leitura de arquivos é algo executado
mais de uma vez no programa, foram criadas duas funções
para isto.

  Na função de gravação de dados é solicitado um
parâmetro indicando a ordem dos dados a serem gravados
( “0” para ordem crescente e “1” para ordem desrescente) e os
dados a serem armazenados. A gravação é feita usando a
biblioteca Pickle para serialização e indexação de dados, o
arquivo é gravado em forma binária. Para a leitura do arquivo
de dados só é pedido o nome do mesmo, sem a extensão.

## Listagem das músicas
  Foi criada uma função para listagem de música que
permite mostrar todas as músicas lidas da playlist, em ordem
crescente ou decrescente conforme parâmetro passado para a
função.

  Esta função percorre a árvore das músicas e monta um
array com as informações de cada música (título,
artista/banda, álbum e popularidade). Este array de
informações é salvo num arquivo binário e depois lido para
exibir as informações para o usuário.

## Ordenação por popularidade
  Cada música possui uma popularidade perante as demais
músicas da playlist. No momento da leitura das informaçẽos
da playlist é lido também a popularidade da música e salvo
num array auxiliar que possui vínculo com a música. Desta
forma é possível listar as músicas por ordem de popularidade,
que pode ser ordem crescente ou decrescente.

  As músicas são ordenadas pela popularidade, usando o
algoritmo de seleção heapsort, utilizando a biblioteca
HEAPQ do próprio Python, depois essas são salvas em um
arquivo binário, que é lido para exibir as informações na tela
para o usuário.

## Consulta de músicas e de artistas/bandas
  Foi implementado a consulta de músicas e a consulta de
artistas/bandas. Nesta função é solicitado o nome da música
ou artista/banda que se deseja pesquisar e então é feita a busca
na árvore Trie.

  Por utilizarmos essa árvore é possível realizar a busca
por prefixo das palavras. Logo, na busca, não é preciso
pesquisar por todo o nome da música ou do artista/banda,
apenas pelas iniciais da palavra, facilitando a busca dos dados
no programa.

## Extração dos dados utilizados
  Para obter as informações das playlist, utilizamos a API
fornecida pelo Spotify, que nos retorna um arquivo do tipo
Json(http://www.json.org/), o qual o programa lê e processa os
dados. A API para extração dos dados encontra-se em
https://developer.spotify.com/web-api/console/get-playlisttracks/#
complete.

Token utilizado:
BQACteuBVnJ6bHnxcE2EzpUR3tPDWshvXBJCflwW_qhVkc
AgDLd3TS5YUsMEzLbe5DAwUJ7OYzcfUSUNLiG5zZUpjZn
XzO5CkzIQc9nG9ogpFpOYFTO1uQO2STTIFC8rGmEuYHH
TqDlOzKgFbfA0klcsRpbl_eznY1cYNN5QsL6VU0Lw5KTxRn
Ms_GeVHXYrA

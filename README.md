﻿# IA_SeaKids
Detecção de Animais Marinhos em Imagens
Este script usa classificadores Haarcascade para detectar diferentes tipos de animais marinhos em uma imagem fornecida pelo usuário. Se um animal for detectado, o script imprime informações detalhadas sobre o animal.

Funções
detectar_objetos(imagem, classificador, scaleFactor=1.02, minNeighbors=4, minSize=(30, 30))
Esta função detecta objetos em uma imagem usando um classificador Haarcascade.

Parâmetros:

imagem: A imagem na qual os objetos serão detectados (em formato BGR).
classificador: O classificador Haarcascade usado para detectar objetos.
scaleFactor (opcional): Especifica o quanto o tamanho da imagem é reduzido em cada escala de imagem. O valor padrão é 1.02.
minNeighbors (opcional): Especifica quantos vizinhos cada retângulo candidato deve ter para ser retido. O valor padrão é 4.
minSize (opcional): Tamanho mínimo dos objetos detectados. O valor padrão é (30, 30).
Retorno:

bool: Retorna True se pelo menos um objeto for detectado, caso contrário, retorna False.
imprimir_informacoes(animal)
Esta função imprime informações detalhadas sobre um animal específico.

Parâmetros:

animal: Uma string que identifica o animal (pode ser "tubarao", "arraia", "cavalo_marinho", "tartaruga_marinha" ou "baiacu").
Retorno:

Nenhum. A função imprime diretamente as informações na tela.
Uso
Carregamento dos Classificadores Haarcascade: O script tenta carregar classificadores Haarcascade específicos para diferentes tipos de animais marinhos. Se ocorrer um erro durante o carregamento, o script é encerrado.

Carregamento da Imagem do Usuário: O usuário é solicitado a fornecer o caminho para a imagem. Se a imagem for carregada com sucesso, o script tenta detectar cada tipo de animal marinho usando os classificadores carregados.

Detecção e Impressão de Informações: Se um animal for detectado na imagem, as informações detalhadas sobre o animal são impressas. Se nenhum animal for detectado, uma mensagem é impressa informando que nenhum objeto foi reconhecido.


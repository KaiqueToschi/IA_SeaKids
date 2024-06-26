import cv2

def detectar_objetos(imagem, classificador, scaleFactor=1.02, minNeighbors=4, minSize=(30, 30)):
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    objetos_detectados = classificador.detectMultiScale(cinza, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
    return len(objetos_detectados) > 0

def imprimir_informacoes(animal):
    informacoes = {
        "tubarao": """
        Nome: Tubarão Martelo
        Nome científico: Sphyrna
        Classe: Peixes Cartilagíneos
        Reino: Animal
        Estado de ameaça: Criticamente Ameaçadas

        A característica mais marcante do tubarão-martelo é sua cabeça achatada e larga em forma de martelo. Essa forma peculiar oferece diversas vantagens, como melhor visão, maior capacidade de detectar presas e maior agilidade na hora de caçar.
        """,
        "arraia": """
        Nome popular: Arraia-jamanta, Manta-gigante
        Nome científico: Manta birostris
        Classe: Elasmobranchii (Peixes cartilaginosos)
        Família: Myliobatidae
        Estado de ameaça: Vulnerável na Lista Vermelha da IUCN

        As principais ameaças à espécie incluem a pesca predatória, a perda de habitat e a poluição.

        Curiosidades:
        - As arraias-jamanta são conhecidas por seus saltos acrobáticos fora da água. Acredita-se que elas fazem isso para se livrar de parasitas, comunicar-se com outras arraias ou simplesmente por brincadeira.
        - A arraia-jamanta é considerada um dos peixes mais inteligentes do mundo. Elas são capazes de aprender tarefas complexas e resolver problemas.
        - A arraia-jamanta desempenha um papel importante na cadeia alimentar marinha, controlando as populações de plâncton. Elas também ajudam a manter os recifes de coral saudáveis, pois seus excrementos fornecem nutrientes para as algas que crescem nos recifes.
        """,
        "cavalo_marinho": """
        Nome popular: Cavalo-marinho
        Nome científico: Hippocampus (diversas espécies)
        Classe: Osteichthyes (Peixes ósseos)
        Ordem: Syngnathiformes
        Família: Syngnathidae
        Gênero: Hippocampus (diversas espécies)
        Estado de ameaça: O estado de ameaça varia entre as espécies de cavalo-marinho. Algumas espécies, como o cavalo-marinho-anão (Hippocampus zosterae), estão Criticamente Ameaçadas de acordo com a Lista Vermelha da IUCN, enquanto outras, como o cavalo-marinho-de-cabeça-alta (Hippocampus erectus), estão Ameaçadas de Extinção.

        Curiosidades:
        - O cavalo-marinho é um dos melhores exemplos de mimetismo no reino animal. Ele pode mudar de cor e textura para se parecer com algas, corais e até mesmo outros animais. Isso o ajuda a se esconder de predadores e a capturar presas.
        """,
        "tartaruga_marinha": """
        Nome popular: Tartaruga-verde
        Nome científico: Chelonia mydas
        Classe: Reptilia (Répteis)
        Ordem: Testudines (Quelônios)
        Família: Cheloniidae (Quelonídeos)
        Gênero: Chelonia
        Espécie: Chelonia mydas
        Estado de ameaça: Em Perigo na Lista Vermelha da IUCN

        As principais ameaças à espécie incluem a pesca predatória, a perda de habitat e a poluição.

        Curiosidades:
        - As tartarugas-verdes podem viver por muito tempo. Algumas tartarugas-verdes podem viver até 100 anos ou mais.
        """,
        "baiacu": """
        Nome popular: Baiacu espinho, Peixe-fugu
        Nome científico: Takifugu rubripes, Torastes spongiosus, Tetraodon nigroviridis
        Estado de ameaça: Varia entre as espécies, algumas Ameaçadas de Extinção

        Características:
        - Tamanho variável
        - Aparência peculiar
        - Capacidade de se inflar em um balão espinhoso
        - Defesa contra predadores
        - Toxina mortal no fígado e ovários

        Curiosidades:
        - Inteligência
        - Boa visão
        - Hábitos noturnos
        - Importância no ecossistema

        Ameaças:
        - Pesca predatória
        - Perda de habitat
        """
    }
    print(informacoes[animal])

# Carregar os classificadores Haarcascade
try:
    haarcascade_tubarao = cv2.CascadeClassifier('haarcascade_tubarao.xml')
    haarcascade_arraia = cv2.CascadeClassifier('haarcascade_arraia.xml')
    haarcascade_cavalo_marinho = cv2.CascadeClassifier('haarcascade_cavalo_marinho.xml')
    haarcascade_tartaruga_marinha = cv2.CascadeClassifier('haarcascade_tartaruga_marinha.xml')
    haarcascade_baiacu = cv2.CascadeClassifier('haarcascade_baiacu.xml')
except Exception as e:
    print("Erro ao carregar os classificadores Haar:", e)
    exit()

# Carregar a imagem do usuario
caminho_imagem = input("Digite o caminho da imagem: ")
imagem = cv2.imread(caminho_imagem)

# Verificar se a imagem contem algum animal detectado
if imagem is not None:
    if detectar_objetos(imagem, haarcascade_tubarao):
        imprimir_informacoes("tubarao")
    elif detectar_objetos(imagem, haarcascade_arraia):
        imprimir_informacoes("arraia")
    elif detectar_objetos(imagem, haarcascade_cavalo_marinho):
        imprimir_informacoes("cavalo_marinho")
    elif detectar_objetos(imagem, haarcascade_tartaruga_marinha):
        imprimir_informacoes("tartaruga_marinha")
    elif detectar_objetos(imagem, haarcascade_baiacu):
        imprimir_informacoes("baiacu")
    else:
        print("Nenhum objeto reconhecido.")
else:
    print("Erro ao carregar a imagem.")

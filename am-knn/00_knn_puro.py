"""
Implementação de Classificador KNN em Python Puro (Sem numpy)
"""
import math

def distancia_euclidiana(p1, p2):
    """Calcula a distancia euclidiana (linha reta) entre dois pontos"""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    # sqrt raiz quadrada
    return math.sqrt(dx**2 + dy**2)


def distancia_manhattan(p1, p2):
    """Calcula a distancia Manhattan (caminho em grade) entre dois pontos"""
    #abs = numero absoluto (retira negativos)
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx + dy

def knn_classificar(dados_treino, novo_ponto, k=3, metrica="euclidiana"):
    """Classifica um ponto usando KNN e retorna os detalhes da votação"""
    if metrica == "euclidiana":
        funcao_dist = distancia_euclidiana
    elif metrica == "manhattan":
        funcao_dist = distancia_manhattan
    else:
        raise ValueError("Metrica invalida. Use 'euclidiana' ou 'manhattan'.")

    # 1. Calcula a distancia para todas as amostras
    distancias = []
    for amostra in dados_treino:
        ponto_treino = [amostra[0], amostra[1]]
        classe = amostra[2]
        dist = funcao_dist(novo_ponto, ponto_treino)
        distancias.append((dist,classe,ponto_treino))

    # 2. Ordena as distancias da menor para a maior
    distancias.sort(key=lambda x:x[0])

    # 3. Filtra os K vizinhos mais proximos
    vizinhos = distancias[:k]

    # 4. Conta os votos por maioria (moda)
    votos_0 = sum(1 for v in vizinhos if v[1] == 0)
    votos_1 = sum(1 for v in vizinhos if v[1] == 1)

    # 5. Retorna a classe majoritaria e os detalhes dos vizinhos
    classe_predita = 1 if votos_1 > votos_0 else 0
    return classe_predita, vizinhos, votos_0, votos_1

if __name__ == "__main__":
    # Dados historicos de treino : [tempo_indisponibilidade, usuarios_impactados, prioridade]
    dados_treino = [
        [1.0, 1.0, 0],
        [2.0, 2.0, 0],
        [3.0, 2.0, 0],
        [4.0, 3.0, 0],
        [6.0, 5.0, 1],
        [7.0, 6.0, 1],
        [8.0, 7.0, 1],
        [9.0, 7.0, 1],
    ]

    # Novo chamado a ser classificado
    novo_chamado = [7.0, 6.0]
    k_vizinhos = 3

    print("=" * 60)
    print("        TRIAGEM DE CHAMADOS DE SUPORTE (KNN PURO)      ")
    print("=" * 60)
    print(f"Novo Chamado sob Analise: {novo_chamado}")

    for metrica in ["euclidiana", "manhattan"]:
        predicao, vizinhos, v0, v1 = knn_classificar(
            dados_treino, novo_chamado, k=k_vizinhos, metrica=metrica
        )

        rotulo_predicao = (
            "Prioridade Alta (Classe 1)"
            if predicao == 1
            else "Prioridade Normal (Classe 0)"
        )
        unidade = "unidades" if metrica == "euclidiana" else "quarteiroes"

        print(f"--- Metrica: Distancia {metrica.capitalize()} (k={k_vizinhos}) ---")
        for i, (dist, classe, ponto) in enumerate(vizinhos, start=1):
            tipo = "Alta (1)" if classe == 1 else "Normal (0)"
            print(
                f"Vizinho {i}: Ponto={ponto} | classe={tipo} | Distancia={dist:.4f} {unidade}"
            )

        print(f"  Apuração dos Votos: {v1} voto(s) para Alta vs {v0} voto(s) para Normal")
        print(f"  Resultado Final:    {rotulo_predicao}\n")

    print("=" * 60)
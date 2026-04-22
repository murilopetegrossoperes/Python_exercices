#Ela recebe dois vetores (v1 e v2), cada um com 5 elementos inteiros, e deve retornar um terceiro vetor (v3) contendo os elementos de ambos de forma alternada.

def intercalar(v1, v2):
    v3 = [0] * 10
    for i in range(10):
        if i % 2 == 0:
            v3[i] = v1[i//2]
        else:
            v3[i] = v2[i//2]
    # Sua lógica aqui
    return v3
#função que verifica se o valor recebido é inteiro ou não
def verif_int(valor):
    try:
        valor_valido=int(valor)
    except ValueError:
        return -1
    return valor_valido  

#função que procura os indice de determinada string
def procura_indice_string(string, sub_string):
    indice = 0
    if sub_string in string:
        c=sub_string[0]
        for sub_string in string:
            if sub_string==c:
                if string[indice:indice+len(sub_string)]==sub_string:
                    return indice

            indice = indice+1

    return -1

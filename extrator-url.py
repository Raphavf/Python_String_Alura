#url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
url = ""
if url == "":
    raise ValueError("A url está vazia")
#Separa base e os parâmetro
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)
url_param = url[indice_interrogacao+1:]

#Busca o valor de um parâmetro
print(url_param)
parametro_busca = 'quantidade'
indice_parametro = url_param.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_param.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_param[indice_valor:]
else:
    valor = url_param[indice_valor:indice_e_comercial]
print(valor)
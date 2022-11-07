url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)


url_param = url[indice_interrogacao+1:]
print(url_param)
parametro_busca = 'moedaDestino'
indice_parametro = url_param.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_param[indice_valor:]
print(valor)
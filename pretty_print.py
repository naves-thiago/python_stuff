# coding=utf-8
import sys
write = sys.stdout.write

def pretty_print(val, sortDict=True, indent="    "):
	''' Print nested containers in a hierarchical form.
	    Params: val - value to print
	            sortDict - Print dicts sorted by key. Defaults to True
	            indent - String to reresenting each indentation step. Defaults to "    "
	'''
	_pretty_print(val, sortDict, indent, 0, "", False)

def _pretty_print(val, sortDict, indent, indentLevel, indentOffset, indentBrackets):
	indentStr = indent * indentLevel + indentOffset

	if type(val) not in (list, dict, tuple):
		print(indentStr + str(val))
		return

	if type(val) in (tuple, list):
		_prefix = ""
		_sufix  = ""
		if type(val) == tuple:
			_prefix = '('
			_sufix  = ')'
		else:
			_prefix = '['
			_sufix  = ']'

		has_container = False
		for i in val:
			if type(i) in (dict, tuple, list):
				has_container = True
				break

		if indentBrackets:
			line = indentStr + _prefix
		else:
			line = _prefix

		if has_container:
			print(line)
		else:
			write(line)

		if has_container:
			# One value per line
			for i in val:
				_pretty_print(i, sortDict, indent, indentLevel, indentOffset + indent, True)
			
			print(indentStr + _sufix)
		else:
			# All values in the same line
			for i in range(len(val)-1):
				write(str(val[i]) + ', ')
			if len(val) > 0:
				write(str(val[len(val)-1]))

			print(_sufix)

		return

	# Dicts
	if len(val) == 0:
		if indentBrackets:
			print(indentStr + '{}')
		else:
			print('{}')
		return

	keys = [str(x) for x in val.keys()]
	if sortDict:
		keys.sort()

	keys_str = match_lengths(keys)

	if indentBrackets:
		print(indentStr + '{')
	else:
		print('{')

	value_offset = indentOffset + indent
	if len(keys_str) > 0:
		value_offset += (len(keys_str[0]) + 2) * " "

	for i in range(len(keys)):
		write(indentStr + indent + keys_str[i] + ": ")

		if type(val[keys[i]]) in (dict, tuple, list):
			_pretty_print(val[keys[i]], sortDict, indent, indentLevel, value_offset, False)
		else:
			print(val[keys[i]])

	print(indentStr + '}')

def match_lengths(v):
	'''Returns a list containing the string representation of v's values with right space padding to make all strings the same length'''
	max_len = 0
	for i in v:
		max_len = max(max_len, len(str(i)))

	ret = []
	for i in v:
		ret.append(str(i).ljust(max_len))

	return ret

#pretty_print({1:2, 3:{}, 4:[], 5:[{}], 6:{7:[]}})
#pretty_print([1,2,[]])
#pretty_print({"aaaaaaaaaaa":1,"bbbbbb":{"ccccccccccc":3,"d":[1,[2,3,[4,5]]]}})
#pretty_print({"asd":[1,2,3,[4]], 1:2, "bbbbbbbb":{1:2, 2:[3]}})
#pretty_print([1,2,[3,4,[5]]])
#pretty_print({"á" : 1, "b" : "c", "c" : [ 1,2,3,[4,5,[6]], {"aaa":"bbb", 1:3}]})
#print({"á" : 1, "b" : "c", "c" : [ 1,2,3,[4,5,[6]], {"aaa":"bbb", 1:3}]})
#pretty_print({'Especificações de memória': {'Tipos de memória': 'DDR3 1333', 'Largura de banda máxima da memória': '21 GB/s', 'Nº máximo de canais de memória': '2', 'Compatibilidade com memória ECC': 'Yes', 'Tamanho máximo de memória (de acordo com o tipo de memória)': '32 GB'}, 'Intel® Data Protection Technology': {'Chave Segura': 'No', 'Novas instruções Intel® AES': 'No'}, 'Especificações gráficas': {'Máxima frequência dinâmica da placa gráfica': '1.05 GHz', 'Intel® Insider™': 'No', 'Nº de telas suportadas': '3', 'Tecnologia de alta definição Intel® Clear Video': 'No', 'Intel® Quick Sync Video': 'No', 'Intel® Wireless Display': 'No', 'Frequência da base gráfica': '650 MHz', 'Gráficos do processador': 'Intel® HD Graphics', 'Tecnologia Intel® InTru™ 3D': 'No'}, 'Essenciais': {'Status': 'Launched', 'Data de introdução': "Q1'13", 'Opções integradas disponíveis': 'No', 'Litografia': '22 nm', 'Escalabilidade': '1S Only', 'Extensões do conjunto de instruções': 'SSE4.1/4.2', 'DMI': '5 GT/s', 'Livre de conflitos': 'Yes', 'Cache inteligente Intel®': '2 MB', 'Número do processador': 'G1610', 'Preço recomendado para o cliente': 'TRAY: $42.00<br />BOX : $42.00', 'Especificação de solução térmica': '2011C', 'Conjunto de instruções': '64-bit', 'Ficha técnica': '<a href="https://www-ssl.intel.com/content/www/us/en/processors/core/CoreTechnicalResources.html">Link</a>'}, 'Tecnologia de Proteção de Plataforma Intel®': {'Tecnologia anti-roubo': 'No', 'Bit de desativação de execução': 'Yes', 'Trusted Execution Technology': 'No'}, 'Opções de expansão': {'Configurações PCI Express': 'up to 1x16, 2x8, 1x8 & 2x4', 'Revisão de PCI Express': '2.0'}, 'Desempenho': {'Número de núcleos': '2', 'Nº de threads': '2', 'TDP': '55 W', 'Frequência baseada em processador': '2.6 GHz'}, 'Tecnologias avançadas': {'Tecnologia de virtualização Intel® (VT-x)': 'Yes', 'Intel® 64': 'Yes', 'Tecnologia de virtualização Intel® para E/S direcionada (VT-d)': 'No', 'Tecnologias de monitoramento térmico': 'Yes', 'Intel® VT-x com Tabelas de página estendida (EPT)': 'Yes', 'Tecnologia Intel® My WiFi': 'No', 'Tecnologia Hyper-Threading Intel®': 'No', 'Tecnologia Intel® vPro': 'No', 'Tecnologia Intel® Turbo Boost': 'No', 'Estados ociosos': 'Yes', 'Tecnologia Enhanced Intel SpeedStep®': 'Yes'}, 'Especificações de pacote': {'Tamanho do pacote': '37.5mm x 37.5mm', 'Configuração máxima da CPU': '1', 'Soquetes suportados': 'FCLGA1155', 'Opções de Halógena Baixa Disponíveis': 'Consulte MDDS'}})

# coding=utf-8
import sys
write = sys.stdout.write

def pretty_print(val, sortDict=True, indent="|    ", encoding="utf-8"):
	_pretty_print(val, sortDict, indent, 0, "", False, encoding)

def _pretty_print(val, sortDict, indent, indentLevel, indentOffset, indentBrackets, encoding):
	indentStr = _indent_str(indent, indentLevel) + indentOffset


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

		line = ""
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
				_pretty_print(i, sortDict, indent, indentLevel, indentOffset + indent, True, encoding)
			
			print(indentStr + _sufix)
		else:
			# All values in the same line
			for i in range(len(val)-1):
				write(str(val[i]) + ', ')
			write(str(val[len(val)-1]))

			print(_sufix)

		return

	# Dicts
	keys = val.keys()
	if sortDict:
		keys.sort()

	keys_str = match_lengths(keys, encoding)

	if indentBrackets:
		print(indentStr + '{')
	else:
		print('{')

	value_offset = (len(keys_str[0]) + 2) * " "
	for i in range(len(keys)):
		write(indentStr + indent + keys_str[i] + ": ")

		if type(val[keys[i]]) in (dict, tuple, list):
			_pretty_print(val[keys[i]], sortDict, indent, indentLevel + 1, value_offset, False, encoding)
		else:
			print(val[keys[i]])

	print(indentStr + '}')

def _indent_str(indent, level):
	tmp = ""
	for i in range(level):
		tmp += indent

	return tmp


def match_lengths(v, encoding="utf-8"):
	'''Returns a list containing the string representation of v's values with right space padding to make all strings the same length'''
	max_len = 0
	for i in v:
		max_len = max(max_len, len(str(i).decode(encoding)))

	ret = []
	for i in v:
		ret.append(str(i).decode(encoding).ljust(max_len))
	
	return ret

#pretty_print({"asd":[1,2,3,[4]], 1:2, "bbbbbbbb":{1:2, 2:[3]}})
pretty_print([1,2,[3,4,[5]]])
#pretty_print({"á" : 1, "b" : "c", "c" : [ 1,2,3,[4,5,[6]], {"aaa":"bbb", 1:3}]})
#print({"á" : 1, "b" : "c", "c" : [ 1,2,3,[4,5,[6]], {"aaa":"bbb", 1:3}]})
#pretty_print({'Especifica\xc3\xa7\xc3\xb5es de mem\xc3\xb3ria': {'Tipos de mem\xc3\xb3ria': 'DDR3 1333', 'Largura de banda m\xc3\xa1xima da mem\xc3\xb3ria': '21 GB/s', 'N\xc2\xba m\xc3\xa1ximo de canais de mem\xc3\xb3ria': '2', 'Compatibilidade com mem\xc3\xb3ria ECC': 'Yes', 'Tamanho m\xc3\xa1ximo de mem\xc3\xb3ria (de acordo com o tipo de mem\xc3\xb3ria)': '32 GB'}, 'Intel\xc2\xae Data Protection Technology': {'Chave Segura': 'No', 'Novas instru\xc3\xa7\xc3\xb5es Intel\xc2\xae AES': 'No'}, 'Especifica\xc3\xa7\xc3\xb5es gr\xc3\xa1ficas': {'M\xc3\xa1xima frequ\xc3\xaancia din\xc3\xa2mica da placa gr\xc3\xa1fica': '1.05 GHz', 'Intel\xc2\xae Insider\xe2\x84\xa2': 'No', 'N\xc2\xba de telas suportadas': '3', 'Tecnologia de alta defini\xc3\xa7\xc3\xa3o Intel\xc2\xae Clear Video': 'No', 'Intel\xc2\xae Quick Sync Video': 'No', 'Intel\xc2\xae Wireless Display': 'No', 'Frequ\xc3\xaancia da base gr\xc3\xa1fica': '650 MHz', 'Gr\xc3\xa1ficos do processador': 'Intel\xc2\xae HD Graphics', 'Tecnologia Intel\xc2\xae InTru\xe2\x84\xa2 3D': 'No'}, 'Essenciais': {'Status': 'Launched', 'Data de introdu\xc3\xa7\xc3\xa3o': "Q1'13", 'Op\xc3\xa7\xc3\xb5es integradas dispon\xc3\xadveis': 'No', 'Litografia': '22 nm', 'Escalabilidade': '1S Only', 'Extens\xc3\xb5es do conjunto de instru\xc3\xa7\xc3\xb5es': 'SSE4.1/4.2', 'DMI': '5 GT/s', 'Livre de conflitos': 'Yes', 'Cache inteligente Intel\xc2\xae': '2 MB', 'N\xc3\xbamero do processador': 'G1610', 'Pre\xc3\xa7o recomendado para o cliente': 'TRAY: $42.00<br />BOX : $42.00', 'Especifica\xc3\xa7\xc3\xa3o de solu\xc3\xa7\xc3\xa3o t\xc3\xa9rmica': '2011C', 'Conjunto de instru\xc3\xa7\xc3\xb5es': '64-bit', 'Ficha t\xc3\xa9cnica': '<a href="https://www-ssl.intel.com/content/www/us/en/processors/core/CoreTechnicalResources.html">Link</a>'}, 'Tecnologia de Prote\xc3\xa7\xc3\xa3o de Plataforma Intel\xc2\xae': {'Tecnologia anti-roubo': 'No', 'Bit de desativa\xc3\xa7\xc3\xa3o de execu\xc3\xa7\xc3\xa3o': 'Yes', 'Trusted Execution Technology': 'No'}, 'Op\xc3\xa7\xc3\xb5es de expans\xc3\xa3o': {'Configura\xc3\xa7\xc3\xb5es PCI Express': 'up to 1x16, 2x8, 1x8 & 2x4', 'Revis\xc3\xa3o de PCI Express': '2.0'}, 'Desempenho': {'N\xc3\xbamero de n\xc3\xbacleos': '2', 'N\xc2\xba de threads': '2', 'TDP': '55 W', 'Frequ\xc3\xaancia baseada em processador': '2.6 GHz'}, 'Tecnologias avan\xc3\xa7adas': {'Tecnologia de virtualiza\xc3\xa7\xc3\xa3o Intel\xc2\xae (VT-x)': 'Yes', 'Intel\xc2\xae 64': 'Yes', 'Tecnologia de virtualiza\xc3\xa7\xc3\xa3o Intel\xc2\xae para E/S direcionada (VT-d)': 'No', 'Tecnologias de monitoramento t\xc3\xa9rmico': 'Yes', 'Intel\xc2\xae VT-x com Tabelas de p\xc3\xa1gina estendida (EPT)': 'Yes', 'Tecnologia Intel\xc2\xae My WiFi': 'No', 'Tecnologia Hyper-Threading Intel\xc2\xae': 'No', 'Tecnologia Intel\xc2\xae vPro': 'No', 'Tecnologia Intel\xc2\xae Turbo Boost': 'No', 'Estados ociosos': 'Yes', 'Tecnologia Enhanced Intel SpeedStep\xc2\xae': 'Yes'}, 'Especifica\xc3\xa7\xc3\xb5es de pacote': {'Tamanho do pacote': '37.5mm x 37.5mm', 'Configura\xc3\xa7\xc3\xa3o m\xc3\xa1xima da CPU': '1', 'Soquetes suportados': 'FCLGA1155', 'Op\xc3\xa7\xc3\xb5es de Hal\xc3\xb3gena Baixa Dispon\xc3\xadveis': 'Consulte MDDS'}})

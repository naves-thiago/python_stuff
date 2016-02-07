# coding=utf-8
import sys
write = sys.stdout.write

def pretty_print(val, sortDict=True, indent="    ", encoding="utf-8"):
	_pretty_print(val, sortDict, indent, 0, False, encoding)

def _pretty_print(val, sortDict=True, indent="|  ", indentLevel=0, indentBrackets=False, encoding="utf-8"):
	indentStr = _indent_str(indent, indentLevel)

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
				_pretty_print(i, sortDict, indent, indentLevel + 1, True)
			
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

	for i in range(len(keys)):
		write(indentStr + indent + keys_str[i] + ": ")

		if type(val[keys[i]]) in (dict, tuple, list):
			_pretty_print(val[keys[i]], sortDict, indent, indentLevel + 1, False)
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

#pretty_print({"á" : 1, "b" : "c", "c" : [ 1,2,3,[4,5,[6]], {"aaa":"bbb", 1:3}]})
#print({"á" : 1, "b" : "c", "c" : [ 1,2,3,[4,5,[6]], {"aaa":"bbb", 1:3}]})

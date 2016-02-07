import sys
write = sys.stdout.write

def print_table(data, schema, titles = None):
	'''Prints a list of dictionaries as a table
	params: data: The list / tuple of dictionaries / lists / tuples (of dictionaries / lists / tuples ...)
	        schema: A list or an set that describes how to iterate in d
	        titles: Column titles to use instead of the keys

	Schema format:
	[key1, key2, [key3, key3-1], [key3, key3-2], [key3, key3-3, key3-3-1]]

	This prints (here d is the short for data):
	|-------------|--------------|----------------------|----------------------|--------------------------------|
	| key1        |  key2        |  key3-1              |  key3-2              |  key3-3-1                      |
	|-------------|--------------|----------------------|----------------------|--------------------------------|
	| d[0][key1]  |  d[0][key2]  |  d[0][key3][key3-1]  |  d[0][key3][key3-2]  |  d[0][key3][key3-3][key3-3-1]  |
	| d[1][key1]  |  d[1][key2]  |  d[1][key3][key3-1]  |  d[1][key3][key3-2]  |  d[1][key3][key3-3][key3-3-1]  |
	| d[2][key1]  |  d[2][key2]  |  d[2][key3][key3-1]  |  d[2][key3][key3-2]  |  d[2][key3][key3-3][key3-3-1]  |
	| ....                                                                                                      |
	|-------------|--------------|----------------------|----------------------|--------------------------------|

	if titles is provided, it's values will be used as column titles instead of the keys.
	'''

	# Verify param types
	if type(data) not in (list, tuple):
		raise TypeError("data must be a list or a tuple")

	if type(schema) not in (list, tuple):
		raise TypeError("schema must be a list or a tuple")

	if type(titles) not in (list, tuple, None):
		raise TypeError("titles must be a list or a tuple or None")

	# Use keys as titles if needed
	if titles == None:
		titles = _create_titles(schema)
	
	lens = _find_lengths(data, schema, titles)

	# Print top border
	for l in lens:
		write(('|{:-<%d}' % (l+4)).format(""))
	write("|\n")

	# Print column names
	for c in xrange(len(lens)):
		write(('|  {:<%d}  ' % lens[c]).format(titles[c]))
	write("|\n")

	# Print middle border
	for l in lens:
		write(('|{:-<%d}' % (l+4)).format(""))
	write("|\n")

	# Print data
	for line in data:
		for c in xrange(len(lens)):
			write(('|  {:<%d}  ' % lens[c]).format(_col_value(line, schema, c)))
		write("|\n")

	# Print lower border
	for l in lens:
		write(('|{:-<%d}' % (l+4)).format(""))
	write("|\n")

def _create_titles(schema):
	'''Returns a list of column names filled with the keys from schema'''
	ret = []
	for k in schema:
		if type(k) == str:
			ret.append(k)
		else:
			if type(k) in (list, tuple):
				ret.append(k[-1])
			else:
				raise TypeError("Invalid type in schema: Expected list or tuple, got %s." % str(type(k)))

	return ret

def _find_lengths(data, schema, titles):
	'''Returns a list of the lengths of the longest string in each column (including the title '''
	ret = []
	for k in titles:
		ret.append(len(k))

	for line in data:
		for col in xrange(len(schema)):
			l = len(_col_value(line, schema, col))
			if l > ret[col]:
				ret[col] = l

	return ret

def _col_value(line, schema, col):
	'''Returns the value of col-th column of line according to the schema'''
	if type(schema[col]) in (str, int, bool, tuple, float):
		return str(line[schema[col]])
	else:
		val = line
		for k in schema[col]:
			val = val[k]

		return str(val)

	return ""

# test code:
#a = [[1,2,3], [4,5,6], [7,8,9]]
#s = [0,1,2]
#t = ["a", "b", "c"]
#
#print_table(a,s,t)
#
#print("")
#
#a = [["teste 1", ["sub 1-1", "sub 1-2"], "aaaa", {"asd":321, "bbb":"bla bla", "c":[1,2,3]}]]
#s = [0, [1,0], [1,1], 2, [3, "asd"], [3,"bbb"], [3,"c",1]]
#t = ["A", "Very long title :)", "3", "TTTT", "5555", "6666", "7777"]
#
#print_table(a,s,t)

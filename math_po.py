def create_list_countby(x,n):
	""" Return a list, starting from x, n times, with jumps of x*n """
	return list(range(x, x * n + 1, x))

def create_list_countby_from(x,n,y):
	""" Return a list, starting from x, n times, with jumps of x*n, starting from y """
	return list(range(y, x * n + 1+y, x))

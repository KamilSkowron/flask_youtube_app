value1 = '123456789'
value2 = '123456789000111'
value3 = '12345678900099944'

def rep_views(views):
	views = views[::-1]
	subList = [views[n:n+3] for n in range(0,len(views), 3)][::-1]
	Z = [i[::-1] for i in subList]
	views_with_dots = ".".join(Z)
	return views_with_dots
	
print(rep_views(value3))
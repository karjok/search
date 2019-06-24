import os,sys,re,json


# berawal dari keterbatasan otak untuk mengingat, munculah ide untuk membuat sebuah alat dimana bisa mempermudah dalam mencari sebuah file baik nama maupun isinya (kusus file readwrite).
# karjok pangesty
# senin 24 juni 2019
# 2:36pm



# search content
def schCont(q):
	n =[]
	for i in os.walk(dir):
		for f in os.listdir(i[0]):
			ful = os.path.join(i[0],f)
			if os.path.isfile(ful):
				if f.split('.')[-1] == fformat:
					try:
						cek = open(ful,'r').read()
						if q in cek:
							size = os.path.getsize(ful)/1024
							ful = ful.replace(f,'\033[92m'+f+'\033[0m')
							n.append(ful)
							s.append(size)
					except:
						pass
	
	return n
# Search directory
def schDir(q,zero):
	n,s=[],[]
	for r in os.walk(dir):
		for f in os.listdir(r[0]):
			if q in str(f):
				fi = os.path.join(r[0],f)
				sz = os.path.getsize(fi)
				if zero == True:
					if os.path.isfile(fi):
						if sz == 0:
							n.append(fi.replace(f,'\033[92m'+f+'\033[0m'))  
							s.append(sz/1024)      
				else:
					n.append(fi.replace(f,'\033[92m'+f+'\033[0m'))
					s.append(sz/1024)
	lst = [i for i in zip(s,n)]
	if sortmode == 'descending':
		lst.sort(key=lambda s: s[0],reverse=True)
	else:
		lst.sort(key=lambda s: s[0])
	return lst
	
def go(q):
	'''Default Configurations'''
	global dir,fformat,sortmode
	
	conf ={
	'search_mode':'dir',
	'file_format':'py',
	'dir':'/sdcard',
	# dir search only
	'zero_mode':False,
	'sort_mode':'descending'}
	
	dir = conf['dir']
	fformat = conf['file_format']
	sortmode = conf['sort_mode']
	
	if conf['search_mode'] == 'content':
		for i in schCont(q):
			print(i)
	else:
		zero = conf['zero_mode']
		for s,n in schDir(q,zero):
			if s > 1024:
				s = round(s/1024,1)
				m = 'mb'
			else:
				s = round(s,1)
				m = 'kb'
			print(f'[{s}{m}] {n}')	


def main():
	if len(sys.argv) == 1 or len(sys.argv) > 2:
		print("""
File Content Search Engine v1.0

Usage:
* if you have one word in query : search query
* for more than one query       : search 'two query' (use the quotes)
* type 'search -conf' to change the configurations""")
	elif sys.argv[1] == '-conf':
		config()
	else:
		go(sys.argv[1])
		
		
		

if __name__=='__main__':
	main()




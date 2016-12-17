import psutil
import time

def cpu_utilizations():
	results = []
	i = 0
	for x in range(10):
		print (psutil.cpu_percent(interval=1))
		x = psutil.cpu_percent(interval=1)
		results.insert(i,x)
		++i
		#time.sleep(2)
	#print(results)
	return results
cpu_utilizations()
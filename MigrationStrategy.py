############################# CLOUDERA #########################################
########  This script executes the workload prediction and trigger    ##########
########              strategy using the psutil library               ##########
########                  python MigrationStrategy.py                 ##########
################################################################################
 
import psutil
import time


C_his_pattern_list = []

def cpu_utilizations():
	results = []
	i = 0
	for x in range(5):
		#print (psutil.cpu_percent(interval=1))
		x = psutil.cpu_percent(interval=1)
		results.insert(i,x)
		++i
		#time.sleep(2)
	#print(results)
	return results

#pattern matching algorithm performs 2 steps: Preprocess and Match. It returns the predicated list after performing the match
'''
KMP implementation

    # a is bigger
    # b is smaller
'''
def KMP(str_a, str_b):
    return _KMP(str_a,str_b,0)

def _KMP(str_a, str_b, offset_a):
    """
    :type offset_a: int # returns the starting index of matching text(smaller) in pattern(bigger)
    """
    if (len(str_a) - offset_a < len(str_b)):
        return -1
    for i in range(offset_a, offset_a + len(str_b), 1):
        if (str_b[i - offset_a] != str_a[i]):
            return _KMP(str_a, str_b, i+1)
    return offset_a

'''
Calculating euclidean distance of a character from a string character
'''
def euclidean_distance(str, ch):
    sum=0
    n = len(str)
    for index in range(0, len(str)):
        difference = ord(str[index])-ord(ch)
        sum += difference ** 2
    sum = sum ** (0.5)
    return sum

def pattern_matching(cpu_workload):
    '''
    :param cpu_workload: list
    :return: string
     Two steps:
        1. Preprocessing
        2. Match

    '''
    # In this algorithm we get take string x, Observed CPU Workload Time series and after calculations get String z.
    # cpu_workload = [3, 15, 16, 18, 19, 15, 20, 15, 15, 12, 14, 16, 19, 14, 14, 22, 16, 16, 13, 15]

    #cpu_workload = [3, 15, 18]
    cpu_workload_time_diff = []
    i = 0
    for index in range(len(cpu_workload) - 1):
        y = cpu_workload[index + 1] - cpu_workload[index]
        cpu_workload_time_diff.insert(i, y)
        i += 1
    s = []
    #print(cpu_workload_time_diff)
    l = 0
    # building s
    for index in range(len(cpu_workload_time_diff)):
        value = int(cpu_workload_time_diff[index])
        if (value == 0):
            s.insert(l, 'i')
        elif (value == 1):
            s.insert(l, 'k')
        elif (value == 2 or value == 3):
            s.insert(l, 'l')
        elif (value == 4 or value == 5):
            s.insert(l, 'm')
        elif (value > 5):
            s.insert(l, 'n')
        elif (value == -1 or value == -2):
            s.insert(l, 'g')
        elif (value == -3 or value == -4):
            s.insert(l, 'f')
        elif (value <= -5):
            s.insert(l, 'e')
        l += 1

    #print ("I am printing s")
    #print(s)

    # s[1..l] is the output of pre-processing step
    # End of preprocessing step
    # s and C_his_pattern_string are input to 2nd step


    #Match Step
    #C_his_pattern_list = [['e', 'f', 'g'], ['i', 'k', 'l'], ['m', 'n', 'f']]
    global C_his_pattern_list

    num = len(C_his_pattern_list)
    #print ("I am printing num")
    #print (num)


    if(num==0):
        C_his_pattern_list.append(s)
        num+=1
        return s


    # ing = ''.join(s)
    C_his_pattern_string = ''
    for x in C_his_pattern_list:
        for y in x:
            C_his_pattern_string += y

    # converting to strings
#    print ("Printing C_his_pattern_string")
 #   print(C_his_pattern_string)

    # Initializing dis[] with zeroes
    dis = []

    for index in range(num):
        dis.append(0)
#    print ("Printing dis")
 #   print (dis)

    s_size = len(s) - 1
    #length = C_his_pattern_list[num-1]

    while (num != 0):

        length = len(C_his_pattern_list[num-1])

        # s is smaller string, C_his_pattern_list[num-1] is bigger one
        tag = KMP(C_his_pattern_list[num-1], s)
#        print(tag)

        if (tag != -1):
            return (C_his_pattern_list[num-1])

        else:

                dis[num-1] = float('inf')
 #               print ("Range")
  #              print (length - s_size)
                flag = 0
                for i in range(length - s_size):
   #                 print("before Dis_l")
                    dis_l = euclidean_distance(s, C_his_pattern_list[num-1][i])
    #                print("Dis_l")
     #               print(dis_l)
                    flag = 1
                if (flag==1):
                    if dis_l < dis[num-1]:
                        dis[num-1] = dis_l

        num -= 1
    C_his_pattern_list.append(s)

   # print ("Printing final history pattern list")
    #print(C_his_pattern_list)

    min_index = dis.index(min(dis))
    '''
    min = dis[0]
    min_index = 0
    for index in range(len(dis)):
        print(index)
        if dis[index] < min:
            min = dis[index]
            min_index = index

    '''

    #print(min)
#    print(min_index)
 #   print(C_his_pattern_list[min_index])
    return C_his_pattern_list[min_index]




def trigger_strategy(predictedstring, timeseriesvalue,threadup):
	timeseriesvalue = psutil.cpu_percent(interval=1)
	length = len(predictedstring)
	upcount = 0
	downcount=0
	for character in predictedstring:
		if(ord(character)>=ord('a')):
			upcount= upcount + 1
		elif(ord(character)<=ord('h')):
			downcount=downcount+1
	if(upcount==length and timeseriesvalue>threadup):
		return 1
	elif(downcount==length and timeseriesvalue<threadup):
		return 0
	else:
		return 0


def migrate():
    cpu_workload = cpu_utilizations()
    # cpu_workload = [94.7, 6.3, 93.3, 0.5, 99]
    # failing for this cpu_workload = [44.7, 16.3, 11.3, 9.9, 11.8, 17.8, 12.0, 12.3, 7.8, 7.5]
    #print(cpu_workload)
    output_list = pattern_matching(cpu_workload)
    #print("Output List")
    #print(output_list)
    timeseriesvalue = psutil.cpu_percent(interval=1)
    migrate = trigger_strategy(output_list, timeseriesvalue, threadup=5)
    #print(migrate)
    # return  migrate
    #print(trigger_strategy('iiiiii', 5.5, 4))
    return migrate

if __name__ == '__main__':
    print migrate()





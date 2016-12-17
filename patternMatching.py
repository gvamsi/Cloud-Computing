
import cpu_util


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
    print ("Euclidean")
    print (str)
    print (ch)
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

    print(cpu_workload)
    #cpu_workload = [3, 15, 18]
    cpu_workload_time_diff = []
    i = 0
    for index in range(len(cpu_workload) - 1):
        y = cpu_workload[index + 1] - cpu_workload[index]
        cpu_workload_time_diff.insert(i, y)
        i += 1
    s = []
    print(cpu_workload_time_diff)
    l = 0
    # building s
    for index in range(len(cpu_workload_time_diff)):
        if (cpu_workload_time_diff[index] == 0):
            s.insert(l, 'i')
        elif (cpu_workload_time_diff[index] == 1):
            s.insert(l, 'k')
        elif (cpu_workload_time_diff[index] == 2 or cpu_workload_time_diff[index] == 3):
            s.insert(l, 'l')
        elif (cpu_workload_time_diff[index] == 4 or cpu_workload_time_diff[index] == 5):
            s.insert(l, 'm')
        elif (int(cpu_workload_time_diff[index]) > 5):
            s.insert(l, 'n')
        elif (cpu_workload_time_diff[index] == -1 or cpu_workload_time_diff[index] == -2):
            s.insert(l, 'g')
        elif (cpu_workload_time_diff[index] == -3 or cpu_workload_time_diff[index] == -4):
            s.insert(l, 'f')
        elif (cpu_workload_time_diff[index] <= -5):
            s.insert(l, 'e')
        l += 1

    # s[1..l] is the output of pre-processing step
    print(s)
    # End of preprocessing step
    # s and C_his_pattern_string are input to 2nd step


    #Match Step
    C_his_pattern_list = [['e', 'f', 'g'], ['i', 'k', 'l'], ['m', 'n', 'f']]
    num = len(C_his_pattern_list) - 1

    # ing = ''.join(s)
    C_his_pattern_string = ''
    for x in C_his_pattern_list:
        for y in x:
            C_his_pattern_string += y

    # converting to strings
    print(C_his_pattern_string)

    # Initializing dis[] with zeroes
    dis = []
    for index in range(num + 1):
        dis.insert(i, 0)

    s_size = len(s) - 1
    while (num != 0):
        length = len(C_his_pattern_list[num])

        # s is smaller string, C_his_pattern_list[num-1] is bigger one
        tag = KMP(C_his_pattern_list[num - 1], s)
        print(tag)

        if (tag != -1):
            return (C_his_pattern_list[num])

        else:

                dis[num] = float('inf')
                for i in range(0, length - s_size):
                    dis_l = euclidean_distance(s, C_his_pattern_list[num][i])
                    print("Dis_l")
                    print(dis_l)
                if dis_l < dis[num]:
                    dis[num] = dis_l
        num -= 1

    min = dis[0]
    min_index = 0
    for index in range(len(dis)):
        print(index)
        if dis[index] < min:
            min = dis[index]
            min_index = index

    print(min)
    print(min_index)
    print(C_his_pattern_list[num])
    return C_his_pattern_list[num]


if __name__ == "__main__":

   output_list = []
   cpu_workload = [13.5, 15.3, 18.9]
   results = cpu_util.cpu_utilizations()
   print(results)
   output_list = pattern_matching(cpu_workload)
   print (output_list)







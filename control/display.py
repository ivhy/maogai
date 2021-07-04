from control.File_get import GetFile
import setting
import os
from control.Read import RExam
import linecache


class display_to_ui:

    First_Char = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self):
        self.s = ""

    def init_random_data(self):  #一次生成一个题型
        # 选出题目存放文件夹
        x = [setting.one,setting.two,setting.three]
        x_num=[setting.one_num,setting.two_num,setting.three_num]
        for k in range(0,3):
            ss = GetFile(x[k], x_num[k])
            ll = ss.getLL()
            each_num = ss.getEch_num()
            each_max_num = ss.getEach_max_num()
            for i in range(0, len(ll)):
                R = RExam(x[k] + "/" + ll[i], each_num[i], each_max_num[i])
                print(ll[i] + "--------" + str(each_num[i]) + "-------" + str(each_max_num[i]))
                R.OpenFile()


    def get_list(self,path):
        if os.path.exists(path):
            content = ''
            cache_data = linecache.getlines(path)[1:]
            list_ques = []
            # return  cache_data
            line = 0
            while line < len(cache_data):
                while cache_data[line] != ',\n':
                    content += cache_data[line]
                    print('--')
                    line += 1
                list_ques.append(content)
                content = ''
                line += 1
            return list_ques
        else:
            print('the path [{}] is not exist!'.format(path))

    def get_list_res(self,path):
        ll = []
        f = open(path,mode='r',encoding='utf-8')
        data = f.readline()
        while data:
            ll.append(data[0:1])
            data = f.readline()


        return ll

    def dele_of_que(self):
        if os.path.exists("../ques.txt"):
            os.remove("../ques.txt")
        if os.path.exists("../reuslt.txt"):
            os.remove("../reuslt.txt")
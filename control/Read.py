import  random
# num 产生题目数
# max_num 文件题目数
# path 文件路径
import setting
from control.File_get import GetFile
class RExam:

    def __init__(self,path,num,max_num):
        self.path = path
        self.num = num
        self.max_num = max_num
        self.flag = 0
        self.First_Char = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def getRadom(self):
        exam  = set()
        while(len(exam)< self.num):
            exam.add(random.randint(1,self.max_num))
        # print(list(exam))
        return list(exam)


    def OpenFile(self):
        exam_list = RExam.getRadom(self) # 获取随机数
        print(exam_list)
        fd = open("../ques.txt", encoding='utf-8', mode="a") # 问题列表
        fg = open("../reuslt.txt", encoding='utf-8', mode="a") #结果列表，作为本地缓存
        with open(self.path,encoding='utf-8',mode='r') as f:
            data = f.readline()
            while(data):
                if data[0] in self.First_Char:
                    n = int(data[0:data.index("、")])
                    # print(n)
                    if n in exam_list:
                        self.flag = 1
                        data = "\n" +data
                if self.flag ==1 and data[0] =="正":
                    self.flag = 2

                if self.flag == 1:
                    fd.write(data)
                if self.flag == 2:
                    fg.write(data[data.index("：")+1: ].strip()+"\n")
                    fd.write(',')
                    self.flag = 0
                data = f.readline()
        fd.close()
        fg.close()
        f.close()

# if __name__ == '__main__':
#     ss = GetFile(setting.two, setting.two_num)
#     ll = ss.getLL()
#     each_num = ss.getEch_num()
#     each_max_num = ss.getEach_max_num()
#     # print(每)
#     for i in range(0,len(ll)):
#         R = RExam(setting.two + "/" + ll[i], each_num[i], each_max_num[i])
#         print(ll[i]+"--------"+str(each_num[i])+ "-------" +str(each_max_num[i]))
#         R.OpenFile()
#     print("生成单选题总数  -------  " + str(sum(each_num)))
#     print(len(ll))

import os
import setting
# path
# path_num 类型题共选多少个

class GetFile:

    def __init__(self,path,path_num):
        self.path = path
        self.ll = [] # 文件目录
        self.path_num = path_num
        self.num = []
        with os.scandir(self.path) as entries:
            for entry in entries:
                self.ll.append(entry.name)
        print(self.ll)

    def getMax_num(self,s):
        return int(s[s.index("（")+1 : s.index("题")])

    def getEch_num(self):  # 每个文件出题目数
        sum = 0
        for i in self.ll:
            # print(GetFile.getMax_num(self,i))
            sum += GetFile.getMax_num(self,i)
        print("题目总数：" + str(sum))
        for k in self.ll:
            self.num.append(round(GetFile.getMax_num(self,k)/sum * self.path_num))
        return self.num


    def getEach_max_num(self): #每个文件最大题目数
        max_num = []
        for i in self.ll:
            max_num.append(GetFile.getMax_num(self,i))
        return max_num

    def getLL(self):  # 每个文件路径
        return self.ll

# if __name__ == '__main__':
#     s = GetFile(setting.two,setting.two_num).getEch_num()
#     print(s)
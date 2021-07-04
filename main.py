# import os
# import linecache
#
# def get_content(path):
#
#     if os.path.exists(path):
#         content = ''
#         cache_data = linecache.getlines(path)[1:]
#         list_ques = []
#         # return  cache_data
#         line = 0
#         while line < len(cache_data):
#             while cache_data[line] != ',\n':
#                 content += cache_data[line]
#                 print('--')
#                 line += 1
#             list_ques.append(content)
#             content = ''
#             line += 1
#         return list_ques
#
#     else:
#         print('the path [{}] is not exist!'.format(path))
#
#
# def get_list_res(path):
#     ll = []
#     f = open(path, mode='r', encoding='utf-8')
#     data = f.readline()
#     while data:
#         ll.append(data[0:1])
#         data = f.readline()
#
#     return ll
#
# def main():
#     path = './reuslt.txt'
#     content = get_list_res(path)
#     print(content)
#
# if __name__ == '__main__':
#     main()


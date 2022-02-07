# coding=utf-8

# 打开入出力文件
file_input=open('./step_02/read.txt',mode='r')
file_output=open('./step_02/write.txt',mode='w')

# 按行读取入力文件，相同日期的金额进行合计
key = {}
i = 0
for line in file_input.read().splitlines():
    i += 1
    if i==1:
        continue
    lineinfo = line.split(',')
    if lineinfo[1] in key:
        key[lineinfo[1]] += int(lineinfo[2])
    else:
        key[lineinfo[1]] = int(lineinfo[2])

# 将合计后的数据排序整理
outputdata = ''
for j in sorted(key):
    outputdata += j + ',' + str(key[j]) + '\n'

# 将排序合计后的数据写入出力文件
file_output.writelines(outputdata)

# 关闭入出力文件
file_input.close()
file_output.close()


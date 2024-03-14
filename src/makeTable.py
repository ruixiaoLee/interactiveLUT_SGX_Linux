# Generate LUT
import numpy as np
import math

# for one-input functions
# slot = 4096 # slot => here is row size but not slot for SEAL
# colSize = pow(2,18)
# rowSize = (int)(colSize/slot)
# # rowSize =1
# input_lut = []
# output_lut = []
# s = (int)(-colSize / 2)
# for i in range(0, colSize):
#     input_lut.append(s)
#     output_lut.append(s)
#     s=s+1

# fi = open("Table/one/vectorOfInLUT_one_18.txt","w")
# fo = open("Table/one/vectorOfOutLUT_one_18.txt","w")
# # k = (int)(slot/colSize)

# # for i in range(0,rowSize):
# #     t=0
# #     for j in range(0,slot):
# #         if(j%k==0):
# #             fi.write(str(input_lut[t])+' ')
# #             fo.write(str(output_lut[t])+' ')
# #             t=t+1
# #             # fi.write(str(input_lut[i*slot+j])+' ')
# #             # fo.write(str(output_lut[i*slot+j])+' ')
# #         else:
# #             fi.write(str(0)+' ')
# #             fo.write(str(0)+' ')
# #     fi.write('\n')
# #     fo.write('\n')
# # fi.close()
# # fo.close()

# for i in range(0,rowSize):
#     for j in range(0,slot):
#         fi.write(str(input_lut[i*slot+j])+' ')
#         fo.write(str(output_lut[i*slot+j])+' ')
#     fi.write('\n')
#     fo.write('\n')
# fi.close()
# fo.close()

# for two-input functions
# slot = 4096 # slot
# colSize = pow(2,12) # input data point
# rowSize = 1 # colSize<slot
# input_lut = []
# output_lut = []
# s = 0
# for i in range(0, rowSize * colSize):
#     input_lut.append(s)
#     s=s+1

# for i in range(0, colSize):
#     f = 0
#     for j in range(0, colSize):
#         output_lut.append(f)
#         f=f+1
       
# fi = open("Table/two/vectorOfInLUT_two_12.txt","w")
# fo = open("Table/two/vectorOfOutLUT_two_12.txt","w")
# k = (int)(slot/colSize)
# t=0
# for i in range(0,slot):
#     if(i%k==0):
#         fi.write(str(input_lut[t])+' ')
#         t=t+1
#     else:
#         fi.write(str(0)+' ')
# fi.close()
# for i in range(0,int(len(output_lut)/colSize)):
#     t=0
#     for j in range(0,slot):
#         if(j%k==0):
#             fo.write(str(output_lut[i*colSize+t])+' ')
#             t=t+1
#         else:
#             fo.write(str(0)+' ')
#     fo.write('\n')
# fo.close()

# for three-input functions
slot = 4096 # slot
colSize = pow(2,4) # input data point
rowSize = 1 # always one row
input_lut = []
output_lut = []
s = 0
for i in range(0, rowSize * colSize):
    input_lut.append(s)
    s=s+1

for i in range(0, colSize):
    for j in range(0, colSize):
        # f = 0
        for z in range(0, colSize):
            output_lut.append(1)
            # f=f+1
       
fi = open("Table/three/vectorOfInLUT_three_4.txt","w")
fo = open("Table/three/vectorOfOutLUT_three_4.txt","w")
k = (int)(slot/colSize)
t=0
for i in range(0,slot):
    if(i%k==0):
        fi.write(str(input_lut[t])+' ')
        t=t+1
    else:
        fi.write(str(0)+' ')
fi.close()
for i in range(0,int(len(output_lut)/colSize)):
    t=0
    for j in range(0,slot):
        if(j%k==0):
            fo.write(str(output_lut[i*colSize+t])+' ')
            t=t+1
        else:
            fo.write(str(0)+' ')
    fo.write('\n')
fo.close()

# for related work test
# InputSize = pow(2,1) # number of slots set as 2^15=32768
# input_lut = []
# s = 0
# for i in range(0,InputSize):
#     input_lut.append(s)
#     s=s+1
# coeff=[]

# for i in range(0,InputSize):
#     y = 0
#     for j in range(0,InputSize):
#         coeff.append(y)
#         y=y+1

# fi = open("build/Table/RelatedWork/relatedwork_in_1.txt","w")
# fc = open("build/Table/RelatedWork/relatedwork_coeff_1.txt","w")
# for i in range(0,InputSize):
#     fi.write(str(input_lut[i])+' ')
#     for j in range(0,InputSize):
#         fc.write(str(coeff[i*InputSize+j])+' ')
#     fc.write('\n')
# fi.close()
# fc.close()

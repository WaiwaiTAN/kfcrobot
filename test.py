import os
c = 'c:\\Users\\ajfik\\Downloads\\kfcrobot\\bib\\thesis.bib'
fo = open(os.path.join(c), mode='rb')
print(fo.readline())
fo.close()
import os
os.system('cls')  # on windows
string=input()
if string.find('he') ==-1:
    wordfound=0
    print('NO')
else:
    h_ind=string.find('he')
    if string.find('lo',h_ind,len(string)):
        print('YES')
    else:
        print('NO')
    #string.find('e',h_ind,len(string))==-1:
 #   e_ind=string.find('e',h_ind,len(string))
 #   if e_ind == -1:
 #       print('NO')
 #   else:
 #       l_ind=string.find('l',e_ind,len(string))
 #       if l_ind == -1:
 #           print('NO')
 #       else:
 #           ll_ind=string.find('l',l_ind,len(string))
 #           if ll_ind== -1:
 #               print('NO')
 #           else:
 #               o_ind=string.find('o',ll_ind,len(string))
 #               if o_ind !=-1 :
#                   print('YES')
#print(h_ind,e_ind,l_ind,ll_ind,o_ind)
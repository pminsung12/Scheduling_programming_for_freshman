# 첫번째 학생의 시간표를 입력받는 함수
def timetable_one(): # 첫 번째 학생의 시간표를 받는 함수
   i = int(0) # i를 0으로 초기화
   print('   \t첫번째 친구 시간표 입력 START')
   print('-'*50)
   print()
   while(True):
      Gong_Gang = input("오늘 설마 공강이냐?(응/아니) or (yes/no) >> ")                  #GongGang 변수 선언. 오늘 공강인지 아닌지 입력 받는다.
      if (Gong_Gang == '응')|(Gong_Gang == 'yes')|(Gong_Gang=='Yes')|(Gong_Gang=='YES'): # 만약에 오늘이 공강이면 밑에 time List에 있는 시간들을 다 timetable1(첫번째 사람이 비는 시간)에 저장한다.
         for i in range(0,53):                                                           #time List 안에 index가 52까지 있으니까 for문을 써서 append 한당.
            timetable1.append(i)
         break
                                                                                         #여기까지가 if문
      elif(Gong_Gang == '아니')|(Gong_Gang == 'no')|(Gong_Gang=='No')|(Gong_Gang=='NO'): #elif를 써서 공강에 대한 질문이 No면 그날의 시간표를 받기 시작한다.
         while(True):
            answer = input("\n\t%s 에 수업이 있나요? >> "%time[i])                       # 9시에 수업이 있는지에 대한 질문. while문의 시작
            if ( answer == 'o')|(answer == 'ㅇ')|(answer=='O')|(answer=='응'):           # 만약에 9시에 수업이 있으면? o or O or ㅇ or 응을 받는다
               print()
               print('='*50)
               print('\t      \t    <주의사항>')
               print('          수업시간을 정확히 입력해주세요..\n   \t★Ex. 1시간 15분, 1시간 50분 등등..★')
               print('='*50)
               ClassTime = input("\n\t수업시간 입력란 >> ")                             #ClassTime 변수는 그 수업이 몇 분 진행되는지는 받는 변수이다.
               if ( ClassTime == '1시간') | ( ClassTime == '1시간 00분'):
                  i = i + 5
               elif ( ClassTime == '1시간 15분'):
                  i = i + 6
               elif ( ClassTime == '1시간 30분'):
                  i = i + 7
               elif ( ClassTime == '1시간 45분'):
                  i = i + 8
               elif ( ClassTime == '2시간') | (ClassTime == '2시간 00분'):
                  i = i + 9
               elif ( ClassTime =='2시간 15분'):
                  i = i + 10
               elif ( ClassTime == '2시간 30분'):
                  i = i + 11+
               elif ( ClassTime == '2시간 45분'):
                  i = i + 12
               elif ( ClassTime == '3시간 00분')|( ClassTime == '3시간'):
                  i = i + 13                                                            # 여기까지가 if 문. 수업이 있다고 대답을 하면 수업시간을 입력 받아
                                                                                        # 수업시간을 더해서 바로 다음에 수업이 있는지 질문이 나올 수 있도록!

            elif ( answer == '수업 끝') | (answer == 'End')|(answer =='end')|(answer=='END')|(answer=='수업끝'): #만약에 수업이 없으면 수업 끝이나 end를 선언 받도록한다.
               for j in range(i, 53):                                                                            #그러면 for문을 돌려서 맨 위에서 지금 while문이 돌아가고있으니까 
                  timetable1.append(j)                                                                           # 수업이 끝난 시점 (i)부터 time List 안에 index 52까지 (22시까지) 학생1의 timetable List에 추가한다.
               
               break                                                                                             # 22시 00까지 처리를 다 햇으니까 시간표 받는 while문을 break!
               

                  
            elif (answer == 'x') | (answer == 'X')|(answer=='ㄴ')|(answer=='아니'):                              # 만약에 9시에 수업 있음? 질문에 x 하면
               k = int(0)                                                                                        # 뒤에 while문 안에 for문에서 변수 i를 저장할 k를 지정하기 위해 int형 변수를 선언해버렸다.
               while(True):                                                                        #while문 시작
                  print('='*50)
                  print('\t      \t    <주의사항>')
                  print('    1시는 13시로, 정각은 00분으로 입력해주세요.\n   \t★시와 분사이에 띄어쓰기 필수!★')
                  print('='*50)
                  NextLecture = input("\n\t다음 수업은 몇시인가요? >> ")                                          # 수업이 없다면 다음 수업이 몇시인지 "NextLecture" 변수에 입력받는다.
                  for j in range (0, 53):                                                         #for문 시작. ★time List 안에 index 0부터 53까지 비교하면서 다음 수업에 해당하는 index[j]를 찾아내는 과정★
                     
                     if ( NextLecture == time[j] ):
                        k = i                                                                                      # k에다가 현재 i값을 저장한다.
                        i = j
                        #여기까지가 for문. 
                  

                  if ( k == i ):                                                                                  # 만약에 k == i이면 for문안에서 time List 안에 같은 시간을 못 찾았다는거니까 다시 입력해달라고 print 한다.
                     print("\n다시 입력해주세요. 주의사항 필!독\n")
                  else :
                     
                     break                                                                                        # 여기까지가 else 문. else에 왔다는건 같은 시간을 찾았다고 하는거니까 break 선언
                  #여기까지가 while문!
               for j in range (k, i):
                  timetable1.append(j)
      
            else:
               print("\t주의 사항을 꼼꼼히 읽고 ^___^")
               print("\t다.시. 입력해주세요 ^___^")
            
           
            if ( i >52 ):
               break          #만약에 i가 52를 넘어가면 이거 첫번쨰 학생의 시간표 받는 함수 끝나게 break!
         break
            
            
      else:
         print("제대로 보고 입력해주세요....")
   
   print()
   print()
   print('-*-'*16)
   print('   \t첫번째 친구 시간표 입력 완료')
   print('-*-'*16)
   print()

# 두 번째 학생의 시간표를 입력받는 함수
def timetable_two():
   i = int(0) # i를 0으로 초기화
   print('   \t두번째 친구 시간표 입력 START')
   print('-'*50)
   print()
   while(True):
      Gong_Gang = input("오늘 설마 공강이냐?(응/아니) or (yes/no) >> ")                  #GongGang 변수 선언. 오늘 공강인지 아닌지 입력 받는다.
      if (Gong_Gang == '응')|(Gong_Gang == 'yes')|(Gong_Gang=='Yes')|(Gong_Gang=='YES'): # 만약에 오늘이 공강이면 밑에 time List에 있는 시간들을 다 timetable1에 저장한다.
         for i in range(0,53):                                                           #time List 안에 index가 52까지 있으니까 for문을 써서 append 한당.
            timetable2.append(i)
         break
                                                                                         #여기까지가 if문
      elif(Gong_Gang == '아니')|(Gong_Gang == 'no')|(Gong_Gang=='No')|(Gong_Gang=='NO'): #elif를 써서 공강에 대한 질문이 No면 그날의 시간표를 받기 시작한다.
         while(True):
            answer = input("\n\t%s 에 수업이 있나요? >> "%time[i])                       # 9시에 수업이 있는지에 대한 질문. while문의 시작
            if ( answer == 'o')|(answer == 'ㅇ')|(answer=='O')|(answer=='응'):           # 만약에 9시에 수업이 있으면? o or O or ㅇ or 응을 받는다
               print()
               print('='*50)
               print('\t      \t    <주의사항>')
               print('          수업시간을 정확히 입력해주세요..\n   \t★Ex. 1시간 15분, 2시간 45분 등등..★')
               print('='*50)
               ClassTime = input("\n\t수업시간 입력란 >> ")                             #ClassTime 변수는 그 수업이 몇 분 진행되는지는 받는 변수이다.
               if ( ClassTime == '1시간') | ( ClassTime == '1시간 00분'):
                  i = i + 5
               elif ( ClassTime == '1시간 15분'):
                  i = i + 6
               elif ( ClassTime == '1시간 30분'):
                  i = i + 7
               elif ( ClassTime == '1시간 45분'):
                  i = i + 8
               elif ( ClassTime == '2시간') | (ClassTime == '2시간 00분'):
                  i = i + 9
               elif ( ClassTime =='2시간 15분'):
                  i = i + 10
               elif ( ClassTime == '2시간 30분'):
                  i = i + 11
               elif ( ClassTime == '2시간 45분'):
                  i = i + 12
               elif ( ClassTime == '3시간 00분')|( ClassTime == '3시간'):
                  i = i + 13                                                            # 여기까지가 if 문. 수업이 있다고 대답을 하면 수업시간을 입력 받아
                                                                                        # 수업시간을 더해서 바로 다음에 수업이 있는지 질문이 나올 수 있도록!

            elif ( answer == '수업 끝') | (answer == 'End')|(answer =='end')|(answer=='END')|(answer=='수업끝'): #만약에 수업이 없으면 수업 끝이나 end를 선언 받도록한다.
               for j in range(i, 53):                                                                            #그러면 for문을 돌려서 맨 위에서 지금 while문이 돌아가고있으니까 
                  timetable2.append(j)                                                                           # 수업이 끝난 시점 (i)부터 time List 안에 index 52까지 (22시까지) 학생1의 timetable List에 추가한다.
               
               break                                                                                             # 22시 00까지 처리를 다 햇으니까 시간표 받는 while문을 break!
               

                  
            elif (answer == 'x') | (answer == 'X')|(answer=='ㄴ')|(answer=='아니'):                              # 만약에 9시에 수업 있음? 질문에 x 하면
               k = int(0)                                                                                        # 뒤에 while문 안에 for문에서 변수 i를 저장할 k를 지정하기 위해 int형 변수를 선언해버렸다.
               while(True):                                                                        #while문 시작
                  print('='*50)
                  print('\t      \t    <주의사항>')
                  print('    1시는 13시로, 정각은 00분으로 입력해주세요.\n   \t★시와 분사이에 띄어쓰기 필수!★')
                  print('='*50)
                  NextLecture = input("\n\t다음 수업은 몇시인가요? >> ")                                          # 수업이 없다면 다음 수업이 몇시인지 "NextLecture" 변수에 입력받는다.
                  for j in range (0, 53):                                                         #for문 시작. ★time List 안에 index 0부터 53까지 비교하면서 다음 수업에 해당하는 index[j]를 찾아내는 과정★
                     
                     if ( NextLecture == time[j] ):
                        k = i                                                                                      # k에다가 현재 i값을 저장한다.
                        i = j
                        #여기까지가 for문. 
                  

                  if ( k == i ):                                                                                  # 만약에 k == i이면 for문안에서 time List 안에 같은 시간을 못 찾았다는거니까 다시 입력해달라고 print 한다.
                     print("\n다시 입력해주세요. 주의사항 필!독\n")
                  else :
                     
                     break                                                                                        # 여기까지가 else 문. else에 왔다는건 같은 시간을 찾았다고 하는거니까 break 선언
                  #여기까지가 while문!
               for j in range (k, i):
                  timetable2.append(j)
      
            else:
               print("\t주의 사항을 꼼꼼히 읽고 ^___^")
               print("\t다.시. 입력해주세요 ^___^")
            
           
            if ( i >52 ):
               break          #만약에 i가 52를 넘어가면 이거 두번쨰 학생의 시간표 받는 함수 끝나게 break!
         break
            
            
      else:
         print("제대로 보고 입력해주세요....")
   
   print()
   print()
   print('-*-'*16)
   print('   \t두번째 친구 시간표 입력 완료')
   print('-*-'*16)
   print()



time = ['09시 00분','09시 15분','09시 30분','09시 45분',
        '10시 00분','10시 15분','10시 30분','10시 45분',
        '11시 00분','11시 15분','11시 30분','11시 45분',
        '12시 00분','12시 15분','12시 30분','12시 45분',
        '13시 00분','13시 15분','13시 30분','13시 45분',
        '14시 00분','14시 15분','14시 30분','14시 45분',
        '15시 00분','15시 15분','15시 30분','15시 45분',
        '16시 00분','16시 15분','16시 30분','16시 45분',
        '17시 00분','17시 15분','17시 30분','17시 45분',
        '18시 00분','18시 15분','18시 30분','18시 45분',
        '19시 00분','19시 15분','19시 30분','19시 45분',
        '20시 00분','20시 15분','20시 30분','20시 45분',
        '21시 00분','21시 15분','21시 30분','21시 45분','22시 00분'] # 4 * 13 = 52 time[0] ~ time[52]

        
        
        
nPeople=input("\t인싸 몇명이 만나나요? : ")

timetable1=[] # 첫번째 학생의 시간표를 o/x 형태로 저장하는 List
timetable2=[] # 두 번째 학생의 시간표를 o/x 형태로 저장하는 List

day = input('\t만나고싶은 요일을 선택하세요 >> ')
print("="*50)
print('\t',day,'시간표 입력을 시작합니다.\n\t    수업이 있다면 >> O/ㅇ/응 \n\t    수업이 없다면 >> X/ㄴ/아니')
print('\n한글 이응(ㅇ),니은(ㄴ), 영어 대소문자 모두 가능합니다.')
print("\n뒤에 수업이 없다면 ""'수업 끝'"" 혹은 ""'end'""를 입력해주세요")
print("\n모든 시간은 15분 단위로 진행됩니다.")
print('='*50)
possible_time=[] #가능한 시간만 모아 놓은 list


timetable_one()

print()
print()
timetable_two() # 함수 이용해서 시간표 받기

nTime1 = len(timetable1)
nTime2 = len(timetable2)
for i in range (0,nTime1):
   for j in range(0,nTime2):
      if (timetable1[i] == timetable2[j]):
         possible_time.append(timetable1[i])



nPossibleTime = len(possible_time)

start_time = int(0)
t = int (0)
if(nPossibleTime == 0):
   print("\t안녕? 난 파란토끼야. 다른 요일 기기")
else:
   while(True):
      if(possible_time[t+1]-possible_time[t] != 1):
         print("\t만날 수 있는 시간은 %s ~ %s 입니다.\n"%(time[possible_time[start_time]],time[possible_time[t]]))
         start_time = t + 1
      t = t + 1
   
      if ( t == len(possible_time)-1 ):
         print("\t만날 수 있는 시간은 %s ~ %s 입니다.\n"%(time[possible_time[start_time]],time[possible_time[t]]))
         print("\t밥약 각을 씨게 잡아봅시다.")
         break


      
         
  
      
   

a = input()
        
        

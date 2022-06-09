# IMPORT ###########################################################################################
import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
import random
import os
import fileinput
import datetime
from tkinter import *

form_mainWindow = uic.loadUiType("mainwindow.ui")[0]
form_calendar = uic.loadUiType("calendarTest.ui")[0]
form_giveup= uic.loadUiType("giveup.ui")[0]
form_finish= uic.loadUiType("finish.ui")[0]
form_input= uic.loadUiType("input.ui")[0]
form_warn= uic.loadUiType("warning.ui")[0]
##################################################################################################

# study_manager ##################################################################################
class study_manager:

    def __init__(self, hw_state):
        self.hakguyeol = 0
        self.hw_state = hw_state
        self.hakguyeol_level = None

    def start(self):
        print("\n\n===============학습매니저 모듈 시작===============")
        self.restore_hakguyeol()

    def restore_hakguyeol(self):  # 지금까지 쌓인 학구열 포인트를 불러오는 모듈

        if os.path.isfile("MANAGER.txt"):
            f = open("MANAGER.txt", 'r')
            line = f.readline()
            self.hakguyeol = int(line)
            f.close()
        else:
            self.hakguyeol = 0

        self.hakguyeol_score(self.hw_state)

    def hakguyeol_score(self, hw_state):  # 학구열 점수를 변동시키는 함수

        if hw_state == 1 or hw_state == 2 or hw_state == 3:  # 과제 미루기
            print("<과제 미룸>")
            self.hakguyeol -= 1
        elif hw_state == 4:  # 과제 포기
            print("<과제 포기>")
            self.hakguyeol -= 10
        elif hw_state == 5:  # 과제 완료
            print("<과제 완료>")
            self.hakguyeol += 1

        print("\n현재 학구열 점수:", self.hakguyeol)

        self.hakguyeol_level_assign()

    def hakguyeol_level_assign(self):  # 학구열 레벨 알려주는 함수

        hakguyeol_level_list = ['출생 전', '고졸', '새내기', '고학번', '대졸', '학과장', '총장']

        if self.hakguyeol < 0:
            self.hakguyeol_level = hakguyeol_level_list[0]
            print("현재 학구열 레벨: {} (사람될 때까지 {} 남음)".format(self.hakguyeol_level, 0 - self.hakguyeol))
        elif self.hakguyeol < 2:
            self.hakguyeol_level = hakguyeol_level_list[1]
            print("현재 학구열 레벨: {} (새내기까지 {} 남음)".format(self.hakguyeol_level, 2 - self.hakguyeol))
        elif self.hakguyeol < 10:
            self.hakguyeol_level = hakguyeol_level_list[2]
            print("현재 학구열 레벨: {} (고학번까지 {} 남음)".format(self.hakguyeol_level, 10 - self.hakguyeol))
        elif self.hakguyeol < 20:
            self.hakguyeol_level = hakguyeol_level_list[3]
            print("현재 학구열 레벨: {} (대졸까지 {} 남음)".format(self.hakguyeol_level, 20 - self.hakguyeol))
        elif self.hakguyeol < 35:
            self.hakguyeol_level = hakguyeol_level_list[4]
            print("현재 학구열 레벨: {} (학과장까지 {} 남음)".format(self.hakguyeol_level, 35 - self.hakguyeol))
        elif self.hakguyeol < 60:
            self.hakguyeol_level = hakguyeol_level_list[5]
            print("현재 학구열 레벨: {} (총장까지 {} 남음)".format(self.hakguyeol_level, 60 - self.hakguyeol))
        elif self.hakguyeol < 100:
            self.hakguyeol_level = hakguyeol_level_list[6]
            print("현재 학구열 레벨: {} (최고 레벨 달성)".format(self.hakguyeol_level))

        self.save_to_file()


    def save_to_file(self):  # 변경된 학구열 포인트 파일에 저장
        f = open("MANAGER.txt", 'w')
        f.write(str(self.hakguyeol))
        f.close()

        
#############################################################################################

# Giveup ####################################################################################
class Giveup (QDialog, form_finish):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('OMG... RIP...')

        if os.path.isfile("MANAGER.txt"):
            f = open("MANAGER.txt", 'r', encoding='UTF-8')
            line = f.readline()
            self.hakguyeol = int(line)
            f.close()
        else:
            self.hakguyeol = 0
         ###
        lines = ['당신은 오늘도 하나의 과제를 죽였습니다.. 잔인한 사람......',
                 '당신이 방금 죽인 과제도, 누군가의 가족입니다.',
                 '당신이 포기한 과제는 교수님의 가슴을 찢습니다... 교수님의 찢어진 가슴을 꼬매주세요.',
                 '당신이 포기한 과제는 지금 어떤 기분일지 생각이라도 해봤나요?',
                 '전 과제 포기한 사람이랑 말 안해요.',
                 '포기를 네 번하면... 식스틴기~']

        line_choice = random.choice(lines)

        self.txtbsr_finish.setText(line_choice)
        ###
        self.hakguyeol_level_list = ['출생 전', '고졸', '새내기', '고학번', '대졸', '학과장', '총장']
        self.statustxt = ["현재 학구열 레벨:"]
        self.nexttxt = ["다음 레벨까지:"]

        if self.hakguyeol < 0:
            self.hakguyeol_level = self.hakguyeol_level_list[0]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 0 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 2:
            self.hakguyeol_level = self.hakguyeol_level_list[1]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 2 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 10:
            self.hakguyeol_level = self.hakguyeol_level_list[2]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 10 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 20:
            self.hakguyeol_level = self.hakguyeol_level_list[3]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 20 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 35:
            self.hakguyeol_level = self.hakguyeol_level_list[4]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 35 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 60:
            self.hakguyeol_level = self.hakguyeol_level_list[5]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 60 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 100:
            self.hakguyeol_level = self.hakguyeol_level_list[6]
            self.statustxt.append(self.hakguyeol_level)
            self.nexttxt[0].replace("최고 레벨 달성")

        self.statusview = " ".join(self.statustxt)
        self.nxtstatusview = " ".join(self.nexttxt)
        print(self.statusview)
        print(self.nxtstatusview)
        self.lbl_status.setText(self.statusview)
        self.lbl_nxtstatus.setText(self.nxtstatusview)


        f = open("MANAGER.txt", 'w')
        f.write(str(self.hakguyeol))
        f.close()





###################################################################################################

# postpone ####################################################################################
class Postpone (QDialog, form_finish):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('OH NO')

        if os.path.isfile("MANAGER.txt"):
            f = open("MANAGER.txt", 'r', encoding='UTF-8')
            line = f.readline()
            self.hakguyeol = int(line)
            f.close()
        else:
            self.hakguyeol = 0

        lines = ['과제 산에 파묻히고 싶나요? 다음에는 시간을 좀 더 효율적으로 써봐요 ^^',
                 '시간이 없으시군요! 시간관리는 현대인의 필.수. 능력이라고요!',
                 '바늘 도둑이 소 도둑 된다는 말 아시죠? 과제 미루다가, 졸업도 미루고, 취업도 미루게 되는 수가 있어요!',
                 '과제는 뒷전으로 미루고 대체 뭘하고 다닌거에요! 가슴에 손 얹고 반성하세요!',
                 '좋아요, 과제 미뤄도 되니까 제발 포기만 하지 말아요.. 과제 나중에 꼭 할거죠?',
                 '전 과제 미룬 사람이랑 말 안해요.',
                 '기억해요.........과제를 미룬다고 사라지는 게 아니야.................. 언젠간 해야해요........................'
                 ]

        line_choice = random.choice(lines)

        self.txtbsr_finish.setText(line_choice)

        self.hakguyeol_level_list = ['출생 전', '고졸', '새내기', '고학번', '대졸', '학과장', '총장']
        self.statustxt = ["현재 학구열 레벨:"]
        self.nexttxt = ["다음 레벨까지:"]

        if self.hakguyeol < 0:
            self.hakguyeol_level = self.hakguyeol_level_list[0]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 0 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 2:
            self.hakguyeol_level = self.hakguyeol_level_list[1]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 2 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 10:
            self.hakguyeol_level = self.hakguyeol_level_list[2]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 10 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 20:
            self.hakguyeol_level = self.hakguyeol_level_list[3]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 20 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 35:
            self.hakguyeol_level = self.hakguyeol_level_list[4]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 35 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 60:
            self.hakguyeol_level = self.hakguyeol_level_list[5]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 60 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 100:
            self.hakguyeol_level = self.hakguyeol_level_list[6]
            self.statustxt.append(self.hakguyeol_level)
            self.nexttxt[0].replace("최고 레벨 달성")

        self.statusview = " ".join(self.statustxt)
        self.nxtstatusview = " ".join(self.nexttxt)
        print(self.statusview)
        print(self.nxtstatusview)
        self.lbl_status.setText(self.statusview)
        self.lbl_nxtstatus.setText(self.nxtstatusview)

        def save_to_file(self):  # 변경된 학구열 포인트 파일에 저장
            f = open("MANAGER.txt", 'w')
            f.write(str(self.hakguyeol))
            f.close()


###################################################################################################

# finish ####################################################################################
class Finish(QDialog, form_finish):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('WELL DONE')

        if os.path.isfile("MANAGER.txt"):
            f = open("MANAGER.txt", 'r', encoding='UTF-8')
            line = f.readline()
            self.hakguyeol = int(line)
            f.close()
        else:
            self.hakguyeol = 0

        lines = ['공부하느라 열 나시죠? 이럴 때는 잠시 시원한 우유에 미숫가루 타서 설탕 솔솔 뿌려 먹으면 어떨까요!',
                 '여름철 면역력도 낮아지는데 면역력 관리를 해보면 어떨까요! 유산균 제품을 추천드려요! (윌, 생크림 요거트, 야쿠르트)',
                 '수고 많았어요! 혹시 머리 과부화 온 거 아니죠? 열이 풀풀 나는 머리를 시원한 물 한 컵으로 식혀 봐요. 정신이 번쩍 들 거예요!',
                 '힘들게 과제한 후에는... 역시 오도독 오도독 씹히는 달콤한 판 초콜릿이죠. 초콜릿은 피로도 풀어주고, 집중도도 높여주고, 우울한 기분도 없애준다고 해요. 초콜릿으로 당 충전하고, 다시 힘내서 과제하자구요~',
                 '공부할 때 뇌는 포도당을 사용해서, 탄수화물을 먹어주면 좋다고 해요. 밥을 먹으면 졸릴 거 같으니까 우리 빵 한 조각 먹으면서 잠깐 쉴까요?',
                 '오랜 시간 동안 책이나 노트북을 보다보면, 머리뿐만이 아니라 눈도 피로해져요. 이때는 눈과 머리 모두에 좋은 블루베리를 먹어보는 건 어때요? 또 파란색이 집중에도 도움이 되고, 눈 피로도 덜어준대요!',
                 '오래 앉아있으셨네요! 거북목과 굽은 등을 예방하는 상체 젖히기를 해볼까요?\n허리와 엉덩이를 의자에 밀착시켜 바로 앉아주세요. 그다음 양팔을 위로 올리고 고개와 상체를 함께 뒤로 젖힌 채 10초간 정지! 이때는 목만 뒤로 젖혀지지 않도록 주의해주세요.',
                 '컴퓨터를 많이 사용하셨어요! 이럴 떄는 손목 터널 증후군을 예방할 수 있는 손목 젖히기 운동을 해볼까요?\n손바닥이 바깥을 향하게 하고 위로 부드럽게 당긴 채, 10초간 유지해주세요. 10초가 지나면 손등이 바깥을 향하도록 아래로 당긴채 10초를 유지하고, 반대쪽도 반복해주세요.',
                 '집중하다보면 눈을 잘 안 깜빡이게 되더라고요... 눈이 뻑뻑하다면 인공 눈물을 넣거나 잠시 눈을 감고 눈의 피로를 풀어주세요! 손을 따듯하게 데워서 눈 위, 아래, 옆, 그리고 관자놀이를 부드럽게 마사지해주면 시력에도 도움이 된다고 해요.',
                 '똑같은 자리에 똑같은 자세로 오래 앉아있으면 답답하게 느껴질 수 있어요. 잠시 밖으로 나가서 시원한 공기도 쐬고, 스트레칭도 하면서 몸을 풀어주세요. 열심히 공부하는 것도 좋지만, 이렇게 나가서 햇빛도 쬐고, 이 근육 저 근육 써줘야 건강도 유지할 수 있다구요!',
                 '잠깐, 혹시 물 마셨나요? 한 연구에서 수분 상태가 기억력과 인지 능력에 영향을 준다고 주장하는 걸 본 적이 있어요. 꼭 공부를 위해서만이 아니라, 공부에 집중하다 보면 물을 잘 마시지 않게 되니, 지금 일어나서 물 한 잔 먹고 오세요. 물 너무 많이 마시면 그만큼 화장실을 가야 하니 한 잔만 먹고 다시 과제해요~',
                 '잠깐만! 혹시 다리 꼬고 앉아 있나요? 아니면 허리가 굽어 있거나, 머리가 거북이처럼 앞으로 쭉 나와 있지는 않나요? 아니면 책에 빠져들 것같이 얼굴을 묻고 있나요? 이런 자세들이 척추 측만증이나 거북목, 골반 뒤틀림으로 이어질 수 있어요. 공부보다 중요한 건 건강인거 알죠? 빨리 허리 펴요!']

        line_choice = random.choice(lines)
        self.txtbsr_finish.setText(line_choice)

        self.hakguyeol_level_list = ['출생 전', '고졸', '새내기', '고학번', '대졸', '학과장', '총장']
        self.statustxt = ["현재 학구열 레벨:"]
        self.nexttxt= ["다음 레벨까지:"]

        if self.hakguyeol < 0:
            self.hakguyeol_level = self.hakguyeol_level_list[0]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 0 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 2:
            self.hakguyeol_level = self.hakguyeol_level_list[1]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 2 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 10:
            self.hakguyeol_level = self.hakguyeol_level_list[2]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 10 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 20:
            self.hakguyeol_level = self.hakguyeol_level_list[3]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 20 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 35:
            self.hakguyeol_level = self.hakguyeol_level_list[4]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 35 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 60:
            self.hakguyeol_level = self.hakguyeol_level_list[5]
            self.statustxt.append(self.hakguyeol_level)
            self.tmp = 60 - self.hakguyeol
            self.nexttxt.append(str(self.tmp))
        elif self.hakguyeol < 100:
            self.hakguyeol_level = self.hakguyeol_level_list[6]
            self.statustxt.append(self.hakguyeol_level)
            self.nexttxt[0].replace("최고 레벨 달성")


        self.statusview = " ".join(self.statustxt)
        self.nxtstatusview = " ".join(self.nexttxt)
        print(self.statusview)
        print(self.nxtstatusview)
        self.lbl_status.setText(self.statusview)
        self.lbl_nxtstatus.setText(self.nxtstatusview)


        def save_to_file(self):  # 변경된 학구열 포인트 파일에 저장
            f = open("MANAGER.txt", 'w')
            f.write(str(self.hakguyeol))
            f.close()






###################################################################################################

# RIP ####################################################################################
class RIP(QDialog, form_giveup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('giveup')

        # 버튼
        self.btn_X.clicked.connect(self.rip)

    def rip(self):
        self.listWidget_rip.clear()
        rip_file = open("RIP.txt", 'r')
        rip_list = rip_file.readlines() #
        tmpname = [text.split(' ') for text in rip_list]
        print(tmpname)
        rip_file.close()
        cnt_rip = len(tmpname)
        for i in range(cnt_rip):
            self.listWidget_rip.addItem(tmpname[i][0])


###################################################################################################

# CALENDAR ########################################################################################
class Calendar(QDialog, form_calendar):

    def __init__(self):
        super().__init__()
        work_file = open("TASKLIST.txt", 'r')
        work_list = work_file.readlines()
        self.tasks = [text.split(' ') for text in work_list]
        work_file.close()

        self.due=['| 마감인 과제:']
        self.setupUi(self)
        self.setWindowTitle('calendar')
        # 시그널
        self.calendarWidget.clicked.connect(self.calendarClicked)
        self.calendarWidget.selectionChanged.connect(self.calendarSelectionChanged)
        self.todayDate = QDate.currentDate()
        self.calendarWidget.setCurrentPage(self.todayDate.year(), self.todayDate.month())
        # 버튼
        self.btn_prevMonth.clicked.connect(self.prevMonth)
        self.btn_nextMonth.clicked.connect(self.nextMonth)
        self.btn_today.clicked.connect(self.today)


    # CalendarWidget의 시그널에 연결된 함수들
    def calendarClicked(self):
        print(self.calendarWidget.selectedDate())
        
    def calendarSelectionChanged(self):
        self.selectedDateVar = self.calendarWidget.selectedDate()
        self.lbl_selectedDate.setText(self.selectedDateVar.toString(Qt.DefaultLocaleLongDate))
        i = 0
        cnt = len(self.tasks)
        for i in range(cnt):
            if self.selectedDateVar.toString("yyyyMMdd") == self.get_year(self.tasks[i][1]):
                self.due.append(self.tasks[i][0])
            else:
                continue
        if len(self.due) == 1:
            self.due.append('없음')
        viewtext = " ".join(self.due)
        self.lbl_view.setText(viewtext)
        self.due = ['| 마감인 과제:']
        
    # 버튼에 연결된 함수들
    def prevMonth(self):
        self.calendarWidget.showPreviousMonth()
        
    def nextMonth(self):
        self.calendarWidget.showNextMonth()
        
    def today(self):
        self.calendarWidget.showToday()

    def get_year(self, strdt):  ### 'MMDD' -> 'YYYYMMDD'

        y = '2020'
        gtyr = y+strdt
        return gtyr
        
##################################################################################################

# input #######################################################################################
class Input(QDialog,form_input):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("INPUT")

        self.btn_input.clicked.connect(self.inputtext)

    def inputtext(self):
        self.inputname = self.lineEdit_inputname.text()
        self.inputduedate = self.lineEdit_duedate.text()
        self.inputmajor = self.lineEdit_major.text()
        self.inputclass = self.lineEdit_class.text()
        self.inputscore = self.lineEdit_score.text()
        self.inputtimetaking= self.lineEdit_timetaking.text()

        self.workList = []
        self.workList.append(self.inputname)
        self.workList.append(self.inputduedate)
        self.workList.append(self.inputmajor)
        self.workList.append(self.inputclass)
        self.workList.append(self.inputscore)
        self.workList.append(self.inputtimetaking)
        self.workList.append('@0')

        self.save_works()

        self.workList = []

        self.lineEdit_inputname.clear()
        self.lineEdit_duedate.clear()
        self.lineEdit_major.clear()
        self.lineEdit_class.clear()
        self.lineEdit_score.clear()
        self.lineEdit_timetaking.clear()

    def save_works(self):  # 새로운 과제를 텍스트 파일에 저장
        work_file = open("TASKLIST.txt", 'a')
        for i in range(0, 7):
            if i == 6:
                data = "%s \n" % self.workList[i]
            else:
                data = "%s " % self.workList[i]  # 문자열 형태로 다 받아옴
            work_file.write(data)
        work_file.close()


########################################################################################

# MAINWINDOW #######################################################################################
class MainWindow(QMainWindow, form_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #배경화면 설정
        oimage=QImage("./bgimg.png")
        self.palette=QPalette()
        self.palette.setBrush(10,QBrush(oimage))
        self.setPalette(self.palette)
        
        ###########
        self.workList = []
        self.allworks = []
        self.today_list = []  # today's tasks => priority queue
        self.delay_list=[]

        self.date = datetime.date.today()  # 날짜 변수 => datetime형 변수
        self.study_time_avl = 0  # '오늘 공부 가능 시간' 변수
        self.study_time_tot = 0  # '오늘 총 공부시간' 변수

        #버튼
        self.btn_calendar.clicked.connect(self.btncalendar)
        self.btn_input.clicked.connect(self.btninput)
        self.btn_giveup.clicked.connect(self.btngiveup)
        self.btn_later.clicked.connect(self.btnlater)
        self.btn_fin.clicked.connect(self.btnfin)
        self.btn_RIP.clicked.connect(self.btnRIP)
        self.btn_renew.clicked.connect(self.btndatechk)

        #화면구성(리스트랑 시간)
        self.lbl_todaytime.setText(str(self.study_time_tot))
        self.lbl_posstime.setText(str(self.study_time_avl))
        self.lbl_curdate.setText(self.for_hyerin(self.date))

        cnt_w = len(self.today_list)
        for i in range(1,cnt_w):
            self.listWidget_others.addItem(self.today_list[i][0])

        #처음인지아닌지

        # 학구열레벨레이블내용바꾸기
        if os.path.isfile("MANAGER.txt"):
            f = open("MANAGER.txt", 'r', encoding='UTF-8')
            line = f.readline()
            self.hakguyeol = int(line)
            f.close()
        else:
            self.hakguyeol = 0

        self.statustxt=[]
        self.statustxt.append(self.lbl_level.text())
        self.statustxt.append(str(self.hakguyeol))
        viewtext = " ".join(self.statustxt)
        self.lbl_level.setText(viewtext)

    def btnrenew(self):
        self.bring_data()
        self.update()
        self.listWidget_others.clear()
        self.lbl_todaytime.setText(str(self.study_time_tot))
        self.lbl_posstime.setText(str(self.study_time_avl))
        self.lbl_curdate.setText(self.for_hyerin(self.date))
        if self.today_list!=[]:
            self.lbl_first.setText(self.app_prior(1)[0])
            print(self.app_prior(1)[0])
        else: self.lbl_first.setText('할 일이 없는데요')

        if self.today_list!=[]:
            cnt_w = len(self.today_list)
            for i in range(1, cnt_w):
                self.listWidget_others.addItem(self.app_prior(i+1)[0])

    def btndatechk(self):
        self.bring_data()
        self.date_chk()

    def btncalendar(self):
        win=Calendar()
        win.show()
        win.exec_()

    def btninput(self):
        win=Input()
        win.show()
        win.exec_()
        self.btnrenew()

    def btngiveup(self):
        if self.today_list!=[]:
            win=Giveup()
            win.show()
            win.exec_()
            hak=study_manager(4)
            hak.start()
            self.state_of_work(self.app_prior(1)[0],4)
            self.add_to_graveyard(self.app_prior(1)[0])
            self.priority()
            self.mklst_main()
            self.listWidget_others.clear()
            self.renew()
        
    def btnlater(self):

        if self.today_list!=[]:
            state=self.show_state(self.app_prior(1)[0])
            if self.show_state(self.app_prior(1)[0])>=3: print('더 이상 미룰 수 없는 과제입니다.') ##메시지박스로 바꿔주셈
            elif 0<=self.show_state(self.app_prior(1)[0])<3:
                win=Postpone()
                win.show()
                win.exec_()
                hak=study_manager(1)
                hak.start()
                self.state_of_work(self.app_prior(1)[0], state+1)
                self.add_to_delay(self.app_prior(1)[0])

                self.delay_list.append(self.app_prior(1))
                print(self.delay_list)
                for i in range(len(self.today_list)):
                    if self.today_list[i]==self.app_prior(1):
                        del self.today_list[i]
                        break
                self.priority()
                self.mklst_main()
                self.listWidget_others.clear()
                self.renew()

    def btnfin(self):
        if self.today_list!=[]:
            win=Finish()
            win.show()
            win.exec_()
            hak=study_manager(5)
            hak.start()
            tmp=self.today_list[0]
            for i in range(len(self.allworks)):
                if self.allworks[i]==tmp:
                    del self.allworks[i]
                    break
            del self.today_list[0]
            work_file = open("TASKLIST.txt", 'w')
            work_file.close()
            work_file = open("TASKLIST.txt", 'a')
            for k in range(len(self.allworks)):
                for j in range(0, 7):
                    if j == 6:
                        data = "%s \n" % self.allworks[k][j]
                    else:
                        data = "%s " % self.allworks[k][j]  # 문자열 형태로 다 받아옴
                    work_file.write(data)
            work_file.close()
            self.priority()
            self.mklst_main()
            self.listWidget_others.clear()
            self.renew()

    def btnRIP(self):
        win=RIP()
        win.show()
        win.exec_()



    def app_prior(self,ind): ######### ""우선순위"" 큐에서 우선순위 뽑아내는 함수!!!! (tmp_work가 사실상 우선순위 큐) #########

        tmp_list=[]
        for i in range(len(self.today_list)):
            tmp_list.append(self.today_list[i])
        tmp_work=tmp_list[0]

        for i in range(ind):
            tmp_work=tmp_list[0]
            
            for j in range(len(tmp_list)):
                    
                if int(tmp_list[j][1]) < int(tmp_work[1]):
                    tmp_work=tmp_list[j]
                        
                elif int(tmp_list[j][1]) == int(tmp_work[1]):
                    if int(tmp_list[j][2]) > int(tmp_work[2]):
                        tmp_work=tmp_list[j]
                            
                    elif int(tmp_list[j][2]) == int(tmp_work[2]):
                        if int(tmp_list[j][3]) * float(tmp_list[j][4]) > int(tmp_work[3]) * float(tmp_work[4]):
                            tmp_work=tmp_list[j]

            for j in range(len(tmp_list)):
                if tmp_work==tmp_list[j]:
                    del tmp_list[j]
                    break

        return tmp_work

    def renew(self):
        self.lbl_todaytime.setText(str(self.study_time_tot))
        self.lbl_posstime.setText(str(self.study_time_avl))
        self.lbl_curdate.setText(self.for_hyerin(self.date))
        if self.today_list!=[]:
            self.lbl_first.setText(self.app_prior(1)[0])
        else: self.lbl_first.setText('할 일이 없는데요')

        if self.today_list!=[]:
            cnt_w = len(self.today_list)
            for i in range(1, cnt_w):
                self.listWidget_others.addItem(self.app_prior(i+1)[0])

    def for_hyerin(self, dt):  ### datetime형의 날짜변수를 'yyyymmdd'의 문자열로 변환하는 함수. => string 자료형으로 반환

        ymd = dt.strftime('%Y년 %m월 %d일')
        return ymd

    def bring_data(self):  # 파일에서 저장된 데이터 리속리로 반환
        work_file = open("TASKLIST.txt", 'r')
        work_list = work_file.readlines()
        self.allworks = [text.split(' ') for text in work_list]  # 리속리 저장
        work_file.close()
        delay_file = open("DELAYED.txt", 'r')
        delay_list = delay_file.readlines()
        self.delay_list = [text.split(' ') for text in delay_list]  # 리속리 저장
        delay_file.close()
        #today_file = open("TODAY.txt", 'r')
        #today_list = today_file.readlines()
        #self.today_list = [text.split(' ') for text in today_list]  # 리속리 저장
        #today_file.close()

    def date_chk(self):  ### 날짜가 지났는지 확인하는 함수

        if self.date != datetime.date.today():
            print('\n[system] : 다음날이 되었습니다.\n') #메시지박스로 바꾸기
            self.date = datetime.date.today
            self.today_list = []
            self.delay_list = []
            self.study_time_tot = 0
            t=open('TODAY.txt', 'w')
            t.close()
            d=open('DELAYED.txt', 'w')
            d.close()
            self.add_to_sttm()
            self.btnrenew()


    ### 날짜 지났을 때 새로고침하는 함수 (날짜 지난 과제 포기 처리) : 혹시나 해서 흔적 남겨둠
    '''
    def refresh(self):  

        count = len(self.allworks)
        i = 0
        while i < count:
            if self.get_rmdt(self.get_dttm(self.allworks[i][1])) < 0:  # 마감일 지난 과제를 리스트에서 제외


                # 과제 무덤석에 추가
                rip = open("RIP.txt", 'a')
                for j in range(0, 6):
                    if j == 5:
                        data = "%s \n" % self.allworks[i][j]
                    else:
                        data = "%s " % self.allworks[i][j]  # 문자열 형태로 다 받아옴
                    rip.write(data)
                rip.close()

                # 원래 파일에서 삭제
                work_file = open("TASKLIST.txt", 'w')
                work_file.close()
                work_file = open("TASKLIST.txt", 'a')
                for k in range(len(self.allworks)):
                    if k == i:
                        continue
                    else:
                        for j in range(0, 6):
                            if j == 5:
                                data = "%s \n" % self.allworks[k][j]
                            else:
                                data = "%s " % self.allworks[k][j]  # 문자열 형태로 다 받아옴
                            work_file.write(data)
                work_file.close()

                # 전체 리스트에서 삭제
                del self.allworks[i]

                i -= 1
                count -= 1
            i += 1
        self.today_list = []
        self.study_time_tot = 0
        self.update()
    '''

    def update(self):  ### 과제 추가했을 때 갱신하는 함수 (다시 정렬)

        self.priority()
        self.stdtm_alloc()
        self.mklst_main()

        print('\n<오늘 공부 가능 시간> : ', self.study_time_avl, '시간')
        print('<오늘 총 공부할 시간> : ', self.study_time_tot, '시간\n\n')

        print('====================================================')
        print('<전체 할 일> : ')
        for i in self.allworks:
            print('>', i)
        print('====================================================\n\n')

        print('====================================================')
        print('<오늘 할 일> : ')
        for i in self.today_list:
            print('>', i[0])
        print('====================================================\n\n')

    def priority(self):  ### '전체 할 일'을 우선순위에 따라 정렬하는 함수 (마감일->전공여부->학점*배점) => 버블정렬사용, 바꿀 의향 있음
        # ※과제 추가할 때!※

        count = len(self.allworks)
        i = 0
        for i in range(count - 1):
            for j in range(count - 1):
                if int(self.allworks[j][1]) > int(self.allworks[j + 1][1]):
                    self.allworks[j], self.allworks[j + 1] = self.allworks[j + 1], self.allworks[j]
                elif int(self.allworks[j][1]) == int(self.allworks[j + 1][1]):
                    if int(self.allworks[j][2]) < int(self.allworks[j + 1][2]):
                        self.allworks[j], self.allworks[j + 1] = self.allworks[j + 1], self.allworks[j]
                    elif int(self.allworks[j][2]) == int(self.allworks[j + 1][2]):
                        if int(self.allworks[j][3]) * float(self.allworks[j][4]) < int(self.allworks[j + 1][3]) * float(
                                self.allworks[j + 1][4]):
                            self.allworks[j], self.allworks[j + 1] = self.allworks[j + 1], self.allworks[j]

    def stdtm_alloc(self):  ### '하루 공부가능시간' 배정하는 함수
        # ※날짜 넘어갈 때!※
        # ※과제 추가할 때!※

        temp = 0
        for i in self.allworks:
            if 0 <= self.get_rmdt(self.get_dttm(i[1])) <= 7: temp += int(i[5])
        temp //= 7
        if temp < 3:
            self.study_time_avl = 3
        else:
            self.study_time_avl = temp

    def mklst_main(self):  ### '오늘 할 일' 우선순위 큐(workList)에 추가하는 함수
        # 과제 추가 시 -> '오늘 할 일 리스트'가 바뀔 수 있으므로 메시지 출력 후 호출.

        self.mklst_prep()
        self.mklst_dl()  # 마감일 오늘인 과제 추가
        self.mklst_nxt()  # 마감일 오늘 아닌 과제 중에서 추가
        

    def mklst_prep(self):  ### 마감일 지난 과제들 추가하는 함수 => 공부가능시간에 관계없이 '오늘 할 일'에 추가

        for i in self.allworks:
            if self.get_dttm(i[1]) < self.date:
                chk1 = 0
                chk2 = 0
                for j in self.today_list:
                    if i == j: chk1 = 1
                for j in self.delay_list:
                    if i[0]==j[0]: chk2 = 1
                if chk1 == 0 and chk2 == 0:
                    print(1)
                    self.today_list.append(i)
                    self.study_time_tot += int(i[5])

    def mklst_dl(self):  ### 오늘 마감인 과제들 추가하는 함수 => 공부가능시간에 관계없이 '오늘 할 일'에 추가

        for i in self.allworks:
            if self.get_dttm(i[1]) == self.date:
                chk1 = 0
                chk2 = 0
                for j in self.today_list:
                    if i == j: chk1 = 1
                for j in self.delay_list:
                    if i[0]==j[0]: chk2 = 1
                if chk1 == 0 and chk2 == 0:
                    print(2)
                    self.today_list.append(i)
                    self.study_time_tot += int(i[5])

    def mklst_nxt(self):  ### 마감일이 오늘이 아닌 과제들 중 추가하는 함수 => 공부가능시간에 맞게끔.

        for i in self.allworks:
            if self.get_dttm(i[1]) != self.date:
                if int(i[5]) <= (self.study_time_avl - self.study_time_tot):  # 남은 공부가능시간보다 적게 걸리는 과제만 걸러내기.
                    chk1 = 0
                    chk2 = 0
                    for j in self.today_list:
                        if i == j: chk1 = 1
                    for j in self.delay_list:
                        if i[0]==j[0]: chk2 = 1
                    if chk1 == 0 and chk2 == 0:
                        print(3)
                        self.today_list.append(i)
                        self.study_time_tot += int(i[5])

    def get_dttm(self, strdt):  ### string 자료형의 '마감일'을 'datetime' 자료형으로 변환하는 함수 => datetime 자료형으로 반환

        y = int(self.date.strftime('%Y'))
        dttm = datetime.date(y, int(strdt[0:2]), int(strdt[2:4]))
        return dttm

    def get_rmdt(self, dt):  ### datetime형의 '마감일'을 '남은 날짜'로 변환하는 함수 => int 자료형으로 반환

        return (dt - self.date).days

    def for_hyerin(self, dt):  ### datetime형의 날짜변수를 'yyyymmdd'의 문자열로 변환하는 함수. => string 자료형으로 반환

        ymd = dt.strftime('%Y%m%d')
        return ymd

    def get_year(self, strdt):  ### 'MMDD' -> 'YYYYMMDD'

        y = str(self.date.strftime('%Y'))
        gtyr = y+strdt
        return gtyr




    def add_to_today(self,lecture):

        for i in range(len(self.allworks)):
            if self.allworks[i][0] == lecture:

                today = open("TODAY.txt", 'a')
                for j in range(0, 7):
                    if j == 6:
                        data = "%s \n" % self.allworks[i][j]
                    else:
                        data = "%s " % self.allworks[i][j]
                    today.write(data)
                today.close()

    def add_to_delay(self,lecture):

        for i in range(len(self.allworks)):
            if self.allworks[i][0] == lecture:

                delay = open("DELAYED.txt", 'a')
                for j in range(0, 7):
                    if j == 6:
                        data = "%s \n" % self.allworks[i][j]
                    else:
                        data = "%s " % self.allworks[i][j]
                    delay.write(data)
                delay.close()


    def add_to_graveyard(self, lecture):
        # 일단 원래 과제 파일에서 포기한 과제 찾아서 삭제 후 과제 무덤석에 추가
        for i in range(len(self.allworks)):
            if self.allworks[i][0] == lecture:
                number = i

                # 오늘 총 공부시간 변경
                self.study_time_tot -= int(self.allworks[i][5])

                # 과제 무덤석에 추가
                rip = open("RIP.txt", 'a')
                for j in range(0, 7):
                    if j == 6:
                        data = "%s \n" % self.allworks[i][j]
                    else:
                        data = "%s " % self.allworks[i][j]  # 문자열 형태로 다 받아옴
                    rip.write(data)
                rip.close()

                # 원래 파일에서 삭제
                work_file = open("TASKLIST.txt", 'w')
                work_file.close()
                work_file = open("TASKLIST.txt", 'a')
                for k in range(len(self.allworks)):
                    if k == number:
                        continue
                    else:
                        for j in range(0, 7):
                            if j == 6:
                                data = "%s \n" % self.allworks[k][j]
                            else:
                                data = "%s " % self.allworks[k][j]  # 문자열 형태로 다 받아옴
                            work_file.write(data)
                work_file.close()

                # 오늘 할 일 리스트에서 삭제
                for j in range(len(self.today_list)):
                    if self.today_list[j][0] == lecture:
                        del (self.today_list[j])
                        break

                # 전체 리스트에서 삭제
                del self.allworks[i]
                break


    def state_of_work(self, lecture, num):
        
        # 미완료 = 0 미루기 1 2 3 포기 = 4 완료 = 5
        filename = "TASKLIST.txt"
        with fileinput.FileInput(filename, inplace=True) as f:
            for line in f:
                if lecture in line:
                    print(line.replace("@0", '@'+str(num)).replace("@1", '@'+str(num)).replace('@2', '@'+str(num)).replace('@3', '@'+str(num)), end = '')

                else:
                    print(line, end='')


    def show_state(self, lecture):
        
        filename = open("TASKLIST.txt", 'r')
        for line in filename:
            if lecture in line:
                ln = line
        state = int(ln[-3:-2])
        return state

    def is_first(self):

        print('\n\n====================================================\n\n')

        if os.path.isfile("TASKLIST.txt") == False:
            # 텍스트 파일 생성
            # 데이터가 있는 상태에서 실행시키면 데이터 다 사라짐
            self.create_file()
            print('[system] : 반가워요! 학습매니저는 처음이시죠?\n\n')
            print('[system] : 오늘부터 같이 열심히 공부해봐요.\n\n')
        else:
            print('[system] : 또 오셨네요!')
            print('[system] : 오늘도 힘내서 공부해보자구요.\n\n')
            self.sttm_read()
            self.lbl_todaytime.setText(str(self.study_time_tot))
            print(self.study_time_tot)
            print(self.study_time_tot)
            today_file = open("TODAY.txt", 'r')
            today_list = today_file.readlines()
            self.today_list = [text.split(' ') for text in today_list]  # 리속리 저장
            today_file.close()
            self.btnrenew()
            if self.today_list!=[]:
                self.lbl_first.setText(self.app_prior(1)[0])
                print(self.app_prior(1)[0])
            else: self.lbl_first.setText('할 일이 없는데요')

            self.listWidget_others.clear()
            if self.today_list!=[]:
                cnt_w = len(self.today_list)
                for i in range(1, cnt_w):
                    self.listWidget_others.addItem(self.app_prior(i+1)[0])
            

    def create_file(self):  # 새파일 생성 (일단은 파이썬 파일 디렉토리에 생성)
        # '처음실행?' Y일 때

        work_file = open("TASKLIST.txt", 'w')
        work_file.close()
        grave_file = open("RIP.txt", 'w')
        grave_file.close()
        delay_file = open("DELAYED.txt", 'w')
        delay_file.close()
        today_file = open("TODAY.txt", 'w')
        today_file.close()

    def sttm_read(self):

        sttm_file = open("STTM.txt", 'r')
        sttm = sttm_file.readlines()
        tm = [text for text in sttm]  # 리속리 저장
        self.study_time_tot=int(tm[0])
        sttm_file.close()

    def add_to_sttm(self):

        sttm_file = open("STTM.txt", 'w')
        sttm_file.write(str(self.study_time_tot))
        print()
        sttm_file.close()



##################################################################################################

# MAIN #############################################################################################

prlg_list=['prologue_1.png','prologue_2.png','prologue_3.png','prologue_4.png','prologue_5.png']
pht_list=[None]*5

ind=0

prlg=Tk()
prlg.title("과제 헌터 : PROLOGUE")

def nxt():
    global ind,pht_list,prlg,lbl

    if 0<=ind<4:
        lbl.config(image=pht_list[ind+1])
        ind+=1
    else:
        prlg.quit()
        prlg.destroy()
        

for i in range(5):
    pht_list[i]=PhotoImage(file=prlg_list[i])

lbl=Label(prlg,image=pht_list[0])
lbl.pack()

btn_n=Button(prlg,text='다음',command=nxt)
btn_n.pack()

prlg.mainloop()

    

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    Window.is_first()
    app.exec_()
    initial=open('TODAY.txt', 'w')
    initial.close()
    for i in Window.today_list:
        Window.add_to_today(i[0])
    Window.add_to_sttm()
    
        
##################################################################################################

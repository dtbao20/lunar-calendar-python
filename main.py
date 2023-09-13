from fltk import *
import datetime
from dateutil.relativedelta import relativedelta
import calendar
from midatelunar import getLunarDate, getYearCanChi
from math import sin, pi

LIST_THANG = ['Tháng Giêng', 'Tháng Hai', 'Tháng Ba', 'Tháng Tư', 'Tháng Năm', 'Tháng Sáu', 'Tháng Bảy', 'Tháng Tám', 'Tháng Chín', 'Tháng Mười', 'Tháng M.Một', 'Tháng M.Hai']
class LICHAM(Fl_Window):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        self.quote = "heloo!"
        self.col = 0
        Fl.add_timeout(0, self.addQuoteCallback, self.quote)
    def addQuoteCallback(self, dat):
        fl_font(FL_HELVETICA_BOLD, 16)
        # fl_color(144+self.col%8 )
        # fl_color(148+int(3.8*sin(10*self.col*pi/180)))
        mcolor = -6*abs(sin(2*5*self.col*pi/180))**0.85+6
        # print(mcolor)
        fl_color(144+8*0+int(mcolor))
        fl_draw(dat, 0, int(dot*0.75), dot*5, int(dot*0.46), FL_ALIGN_INSIDE+FL_ALIGN_LEFT)
        self.col+=1
        # Fl.repeat_timeout(1/30, self.addQuoteCallback, self.quote)
    def draw(self):
        super().draw()
        # fl_color(0, 0, 0)
        # fl_line_style(FL_SOLID,1)
        # fl_line(0, dot, self.w(), dot)
        for x in range(6):
            fl_color(50, 50, 50)
            fl_line_style(FL_SOLID,1)
            if x not in [4,5]: fl_line(dot*(x+1), dot+10, dot*(x+1), dot*2-10)
            else: fl_line(dot*(x+1), dot+20, dot*(x+1), dot*2-10)
        ##

        # for x in range(6):
        #     fl_color(100, 100, 100)
        #     fl_line_style(FL_DASH,1)
        #     fl_line(dot*(x+1), dot, dot*(x+1), self.h())
        #     fl_line_style(FL_DOT,1)
        #     fl_line(0, dot*(x+2), self.w(), dot*(x+2))
        # fl_color(0, 0, 0)
        # fl_line_style(FL_SOLID,1)
        # fl_line(0, dot*2, self.w(), dot*2)
        for y in range(6):
            for x in range(7):
                if (y+1)>len(cal): break
                if cal[y][x].day==tt.day and cal[y][x].month==tt.month:
                    fl_color(25, 25, 25)
                    fl_line_style(FL_DASH,3)
                    # fl_rect(x*dot,dot*(2+y), dot, dot)
                    # fl_circle(x*dot+0.5*dot,dot*(2+y)+0.5*dot,20)
                    fl_circle(x*dot+0.5*dot,dot*(2+y)+0.5*dot,25)


def CalMoon(tt):
    global cal, datmoon
    cal = calendar.Calendar().monthdatescalendar(tt.year, tt.month)
    # print(len(cal))
    # print(cal)
    datmoon = list()
    for i in range(6):
        for j in range(7):
            if (i+1)>len(cal): break
            kk = cal[i][j]
            ll = getLunarDate(kk.day, kk.month,kk.year)
            datmoon+=[tuple(ll[:3])]
    # return cal, datmoon
def controlmonth(ptr):
    global tt
    tt = datetime.datetime.now() + relativedelta(months=1)
    CalMoon(tt)
    addbox()
def tb1(ptr):
    print("hikk")
def addbutton():
    aa = Fl_Box(o, o, dot-2*o, dot-2*o, "@<")
    aa.box(FL_FLAT_BOX)
    aa.labelsize(20)
    aa.color(18)
    aa.callback(controlmonth)
    a2 = Fl_Box(w-dot+o, o, dot-2*o, dot-2*o, "@>")
    a2.box(FL_FLAT_BOX)
    a2.labelsize(20)
    a2.color(18)
    a2.callback(tb1)
def addstruct():
    struct = ["T2","T3","T4","T5","T6","T7","CN"]
    for x in range(len(struct)):
        ll = Fl_Box(dot*x,dot,dot,dot,struct[x])
        ll.labelsize(20)
        ll.labelfont(FL_BOLD)
        ll.labeltype(FL_SYMBOL_LABEL)
        ll.labelcolor(8*4+8*3-1)
        ll.align(FL_ALIGN_INSIDE+FL_ALIGN_BOTTOM)
        if struct[x] in struct[-2:]:
            ll.labelcolor(60--30)
def addbox():
    fl_register_images()
    t=0
    theme0 = (FL_YELLOW, FL_CYAN)#(FL_BLUE, FL_MAGENTA)(FL_FREE_COLOR, FL_RED)
    thisMonth = LIST_THANG[tt.month-1]
    Fl_Box(0,int(dot*0.75),dot*5,int(dot*0.46)).box(FL_GLEAM_UP_FRAME)
    nam = Fl_Box(dot*0,0+9*0,dot*5,int(dot*0.75),thisMonth)#
    # nam.labelsize(int(360/len(thisMonth)))
    nam.box(FL_GLEAM_UP_FRAME)
    nam.labelsize(32)
    nam.labelcolor(95)
    nam.labelfont(FL_COURIER_BOLD_ITALIC)
    # nam.align(FL_ALIGN_INSIDE+FL_ALIGN_BOTTOM)
    Fl_Box(dot*5,0+14*0,dot*2-0,dot+10).box(FL_GLEAM_UP_FRAME)
    nam = Fl_Box(dot*5,0+14*0+17,dot*2-0,dot,str(tt.year))
    nam.labelsize(40)
    nam.labelcolor(128)
    nam.labeltype(FL_ENGRAVED_LABEL)
    nam.labelfont(FL_BOLD)
    nam.align(FL_ALIGN_INSIDE+FL_ALIGN_BOTTOM)
    nam = Fl_Box(dot*0,dot*2,int(dot*7),dot*6+0,'')#🐯👀🦸
    nam.labelsize(160)
    # nam.labelcolor(FL_BLACK)
    nam.labelcolor(219)
    nam.labeltype(FL_SYMBOL_LABEL)
    # nam.box(FL_GLEAM_UP_FRAME)
    for y in range(6):
        for x in range(7):
            if (y+1)>len(cal): break
            daysun = cal[y][x].day
            daysun = str(daysun)
            daymoon = datmoon[t][0]
            monthmoon = datmoon[t][1]
            if daymoon==1: daymoon = str(daymoon)+"/"+str(monthmoon)
            else: daymoon = str(daymoon)
            # print(datmoon[t])
            ls = len(str(daysun))
            lm = len(str(daymoon))
            # Fl_Box(dot*x,dot*(y+2),dot,dot).box(FL_ENGRAVED_FRAME)
            kk = Fl_Box(dot*x-3*ls,dot*(y+2),dot,dot,daysun)
            kk.labelsize(20)
            kk.labelcolor(8*4+8*3-6)
            # kk.labeltype(FL_SHADOW_LABEL)
            kk.labelfont(FL_BOLD)
            # kk.labelfont(FL_COURIER)
            # kk.labelfont(FL_TIMES)
            # kk.labelfont(FL_SCREEN)
            k1 = Fl_Box(dot*x+2*lm+6,dot*(y+2)+7,dot,dot,daymoon)
            k1.labelcolor(8*4+8*3-3)
            k1.labelsize(10)
            k1.labelfont(FL_BOLD_ITALIC)

            if '/' in daymoon: 
                k1_ = Fl_Box(dot*x+2*lm+2,dot*(y+2)+7,dot,dot,"/")
                k1_.labelcolor(8*18+0)
                k1_.labelsize(14)
                k1_.labelfont(FL_BOLD_ITALIC)
            if cal[y][x].day==tt.day and cal[y][x].month==tt.month: 
                # kk.color(42)
                # kk.labelcolor(theme0[0])
                kk.labelcolor(8*4+8*3-1)
                # kk.labelsize(32)
                kk.position(dot*x-4*ls,dot*(y+2))
                # kk.labeltype(FL_ENGRAVED_LABEL)
                # k1.labelcolor(theme0[1])
                k1.labelcolor(8*4+8*3-4)
                # k1.labelsize(18)
                # k1.position(dot*x+4*lm+6,dot*(y+2)+7*2)
                # k1.labeltype(FL_ENGRAVED_LABEL)
            t+=1
dot = 50
Fl.set_font(FL_TIMES_BOLD_ITALIC, 148)
app=LICHAM(x=600,y=200,w=dot*7,h=dot*8)
app.label("hi")
app.default_icon(Fl_PNG_Image('images/afro.png'))

app.box = Fl_Box(0,0,dot*7,dot*8)
# pic = Fl_PNG_Image('images/bg5.png')
# pic = Fl_JPEG_Image('images/bg10.jpg')
pic = Fl_JPEG_Image('images/lucy.jpg')
# pic = Fl_JPEG_Image('images/matth.jpg')
# pic = Fl_JPEG_Image('images/prith.jpg')
pic = pic.copy(int(app.box.h()*pic.w()/pic.h()), app.box.h())
# pic = pic.copy(app.box.w(), int(app.box.w()*pic.h()/pic.w()))
app.box.image(pic)
app.box.color(18)
w,h = app.w(), app.h()
doi = 0# 
o = 0#offset
tt = datetime.datetime.now() + relativedelta(months=0)
CalMoon(tt)

# addbutton()
addbox()
addstruct()
# app.set_override()
app.set_modal()
app.show()
# import win32gui
# win32gui.SetWindowPos(win32gui.GetForegroundWindow(),-1,0,0,0,0,3)
Fl.run()


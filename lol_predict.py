"""
# URL : http://localhost:8080/cgi-bin/lol_predict.py
"""
# 모듈 로딩 ---------------------------------------------------
import cgi, sys, codecs, os
import pandas as pd
import joblib
cmp=pd.read_csv('C:\EXAM_python\MONTH_03\DAY_0316\cmp.csv')
# WEB 인코딩 설정 ---------------------------------------------
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())

# 함수 선언 --------------------------------------------------
# WEB 페이지 출력 --------------------------------------------
def displayWEB(detect_msg):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    html="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>리그 오브 레전드 승부 예측</title>
    </head>
    <body align="center">
    <h2>[ 승부 예측 ]</h2>
    <form>
        <div style='text-align:center; background-color:#D5D5D5;border-radius:10px;width:60%; margin: auto;padding:50px;'>
            <input id="p1" type="text" placeholder="1픽 선택" name="p1"> &nbsp&nbsp
            <input id="p2" type="text" placeholder="2픽 선택" name="p2"> &nbsp&nbsp
            <input id="p3" type="text" placeholder="3픽 선택" name="p3"> &nbsp&nbsp
            <input id="p4" type="text" placeholder="4픽 선택" name="p4"> &nbsp&nbsp
            <input id="p5" type="text" placeholder="5픽 선택" name="p5"> &nbsp&nbsp
            <input id="p6" type="text" placeholder="6픽 선택" name="p6"> &nbsp&nbsp
            <input id="p7" type="text" placeholder="7픽 선택" name="p7"> &nbsp&nbsp
            <input id="p8" type="text" placeholder="8픽 선택" name="p8"> &nbsp&nbsp
            <input id="p9" type="text" placeholder="9픽 선택" name="p9"> &nbsp&nbsp
            <input id="p10" type="text" placeholder="10픽 선택" name="p10"> &nbsp&nbsp
            <br></br>
            <input type="submit" value="예측"></br>
            <p><font color='blue'>{}</font></p>
        </div>
    </form></body></html>""".format(detect_msg)
    print(html)

# 판정 --------------------------------------------------------
def detect_blue_win(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10=int(p1),int(p2),int(p3),int(p4),int(p5),int(p6),int(p7),int(p8),int(p9),int(p10)
    res = lr.predict([[p1,int(cmp.dmg[cmp.num==p1]),p2,int(cmp.dmg[cmp.num==p2]),p3,int(cmp.dmg[cmp.num==p3]),p4,int(cmp.dmg[cmp.num==p4]),p5,int(cmp.dmg[cmp.num==p5]),p6,int(cmp.dmg[cmp.num==p6]),p7,int(cmp.dmg[cmp.num==p7]),p8,int(cmp.dmg[cmp.num==p8]),p9,int(cmp.dmg[cmp.num==p9]),p10,int(cmp.dmg[cmp.num==p10]),]])
    return int(res[0])

# 기능 구현 -----------------------------------------------------
# (1) 학습 데이터 읽기
pklfile = os.path.dirname(__file__) + "/lol_model.pkl"
lr = joblib.load(pklfile)

# (2) WEB 페이지 <Form> -> <INPUT> 리스트 가져오기
form = cgi.FieldStorage()
p1_value = form.getvalue('p1')
# p1_value = int(cmp.num[cmp.champ_name==form.getvalue('p1')])
p2_value = form.getvalue('p2')
# p2_value = int(cmp.num[cmp.champ_name==form.getvalue('p2')])
p3_value = form.getvalue('p3')
# p3_value = int(cmp.num[cmp.champ_name==form.getvalue('p3')])
p4_value = form.getvalue('p4')
# p4_value = int(cmp.num[cmp.champ_name==form.getvalue('p4')])
p5_value = form.getvalue('p5')
# p5_value = int(cmp.num[cmp.champ_name==form.getvalue('p5')])
p6_value = form.getvalue('p6')
# p6_value = int(cmp.num[cmp.champ_name==form.getvalue('p6')])
p7_value = form.getvalue('p7')
# p7_value = int(cmp.num[cmp.champ_name==form.getvalue('p7')])
p8_value = form.getvalue('p8')
# p8_value = int(cmp.num[cmp.champ_name==form.getvalue('p8')])
p9_value = form.getvalue('p9')
# p9_value = int(cmp.num[cmp.champ_name==form.getvalue('p9')])
p10_value = form.getvalue('p10')
# p1_value = int(cmp.num[cmp.champ_name==form.getvalue('p10')])

# (3) 판정 하기
if p1_value is not None and p2_value is not None and p3_value is not None and p4_value is not None and p5_value is not None and p6_value is not None and p7_value is not None and p8_value is not None and p9_value is not None and p10_value is not None:
    result=detect_blue_win(p1_value,p2_value,p3_value,p4_value,p5_value,p6_value,p7_value,p8_value,p9_value,p10_value)
    if result==1:
        result='블루팀 승리'
    elif result==0:
        result='레드팀 승리'
else:
    result ='픽을 해주세요.'
# (4) WEB 출력하기
displayWEB(result)


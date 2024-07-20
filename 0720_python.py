import pygsheets
name_email = 1
#googlesheet密碼(授權)貼檔案名稱就會知道帳號密碼為何
gs = pygsheets.authorize(service_account_file = ".infinite-glow-430001-e9-82f4dd2eb476.json")
#把service_account_file代為utility-unity-430001-u3-87397ce2156a.json讓程式抓取裡面的東西
#下一步開啟googlesheet
sht = gs.open_by_url("https://docs.google.com/spreadsheets/d/1ZZA1Wx6XFdIMKmMf0rl4awiVcCy1FxcnDo9drtpwYkY/edit?gid=0#gid=0")

# a1Value = sht[1].cell("A1").value
#工作表1為0,Cell為欄位
#sht[1].update_value("B1","update by python")
cells = sht[name_email].get_all_values(include_tailing_empty_rows=False,
                              include_tailing_empty=False,
                              returnas = "matrix")
                            #如果是空值就不要讓程式抓他。#讓他回傳是矩陣(matrix)
#print(cells)
#確認幾列
#print(len(cells))

sht1Date = sht[name_email].get_all_values(include_tailing_empty_rows=False,
                              include_tailing_empty=False,
                              returnas = "matrix")

"""

print(a1Value)

print(sht[1].cell("A2").value)
"""
dic={}

# len == 總列

for i in range(len(sht1Date)):
    if i == 0:
        continue
##    key = sht[1].cell("A"+ str(i+1)).value
##   value = sht[1].cell("B"+str(i+1)).value
    key = sht1Date[i][0]
    value = sht1Date[i][1]

    dic[key] = value

print(dic)

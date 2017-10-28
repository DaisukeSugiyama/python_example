#pythonの標準ライブラリを使用します
#基本的な日付方および時間型 datetime
#追記予定

import datetime

#
date = datetime.date



#現在の日時を取得する
today = datetime.date.today()
print(' [ 現在の日時を取得する ] ')
#year
year = today.year
print (' [ 年 ]  : '  +  str(year))
#month
month = today.month
print(' [ 月 ] : ' +  str(month))
#day
day = today.day
print(' [ 日 ] : ' + str(day))


#weekday 月曜日を0,日曜日を6とする
weekday = date(year,month,day).weekday()
print('[ 曜日を整数で返す ] : ' + str(weekday))


#isoweekday
#曜日を整数で返す 月曜日は１,日曜日は７
isoweekday = date(year,month,day).isoweekday()
print('[ 曜日を整数で返す(iso) ] : ' + str(isoweekday))

#指定した日時のオブジェクトを作成
dateObj = datetime.datetime(year,month,day)
print(dateObj)

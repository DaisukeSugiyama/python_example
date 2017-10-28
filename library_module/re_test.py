#pythonの標準ライブラリを使用します
#正規表現モジュール re
import re 
m = re.search('(p(yth|l)|Z)o[pn]e?','python')

#マッチオブジェクトを返します
print(m)

#マッチオブジェクトから値を取り出します
print(m[0])
#もしくは
print(m.group(0))


#グループを指定して文字列の取得
m = re.search('py(thon)','python')
print(' [ グループを指定して文字列の取得 ]')
print(m[0])
print(m[1])

#正規表現にマッチしない場合
m = re.search('py','ruby')
#エラーになるようです
#print(m[0])


#pythonの標準ライブラリ re - 正規表現操作について
#https://docs.python.jp/3/library/re.html


#モジュール
#外部のpythonファイルを読み込み

import calc
addCnt =calc.add(1,2)
print(addCnt)

subCnt = calc.sub(1,2)
print(subCnt)

#関数を直接呼出し
print('[ 関数を直接呼出します ]')
from calc import add
addCnt = add(3,2)
print(addCnt)

from calc import sub
subCnt = sub(3,2)
print(subCnt)

#インポート対象に別名を付けて使用する
#calcを c という名前に変更して使います
print('[ インポート対象に別名を付けて使用します ]')
import calc as c
addCnt = c.add(5,3)
print (addCnt)

subCnt = c.sub(5,3)
print (subCnt)

#複数対象をインポート
print('[ 複数の対象をインポートして使用します ]')
from calc import add,sub
addCnt = add(10,4)
print(addCnt)

subCnt = sub(10,4)
print(subCnt)

#括弧を使って複数の関数をインポート
print('[ 括弧を使って複数の関数をインポート]')
from calc import(
    add,
    sub
)
addCnt = add(30,5)
print(addCnt)

subCnt = sub(30,5)
print(subCnt) 

#直接呼び出す関数にも別名を付ける
print('[ 直接呼び出す関数にも別名を付ける ]')
from calc import add as a
addCnt = a(100,30)
print(addCnt)

'''
実行時に「_pycache_」というディレクトリと,
.pycファイルが作成される場合があります。
これはコンパイル時の結果のバイトコードだそうです。
python3.2以降の使用だそうです。
これを作成しない方法もあります。

参考　
http://docs.python.jp/3/library/py_compile.html?highlight=py_compile#module-py_compile
http://www.python.ambitious-engineer.com/archives/452
http://d.hatena.ne.jp/itasuke/20111215/pyc_file
'''
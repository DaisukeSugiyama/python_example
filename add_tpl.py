#タプル(tuple)型のテスト
'''
タプル型はimmutable(不変)な値であるため、
.append()みたいな追加する処理や、
.remove()して要素を削除する処理はできないそうです。
そのため、新たなタプル型を作成しなくてはいけません。
'''
#taple型をfor文で表示します
def loop(tpl):
    for word in tpl:
        print(word) 

#新しいtupleを返します
def make_newTuple(tpl,addword):
    print('\n [method] : make_newTuple : ' + addword)
   
    #追加したい文字列をtuple型にします
    #1つの値をtuple型にするときは最後にカンマを。
    addwordTpl = (addword,)
    print("[型チェック] : " + str(type(addwordTpl)))

    #tuple型同士だと結合できます。
    newTuple = tpl + addwordTpl
    return newTuple


#ここから処理の流れです
tupleTest = ('μ\'s','Aquors',9)
PDP = '(Nijigasaki)'

loop(tupleTest)

tupleTest = make_newTuple(tupleTest,PDP)

loop(tupleTest)

#（PDPも楽しみですね。）


#ファイル操作系の処理です
def open_file(filepath,encode):
    #fileopen
    f = open(filepath,encoding=encode)
    
    #fileを読み込む
    text = f.read()
    print(text)

    #ファイルを閉じる
    f.close()
    return

def write_file(filepath,mode,encode,wirte):
    #fileopen (モード指定)
    f = open(filepath,mode,encoding=encode)

    #書き込む
    f.write(write);

    #ファイルを閉じる
    f.close()
    

#実行
filepath = 'read_test.txt'
encode = 'utf-8'
#読み込み
print('[ ファイルを開きます ]')
open_file(filepath,encode)

#書き込み
filepath = 'kiseki.txt'
mode = 'w'
write = '起こそう！奇跡を！'
print('[ ファイルに書き込みます ]')
write_file(filepath,mode,encode,write)

print('[ 作成され、書き込まれているか確認 ]')
open_file(filepath,encode)

#追記モード（「a」と指定する）
mode = 'a'
write = 'あがこう精いっぱい！'
print("[ ファイルに追記します ]")
write_file(filepath,mode,encode,write)
print('[ 追記されているか確認 ]')
open_file(filepath,encode)

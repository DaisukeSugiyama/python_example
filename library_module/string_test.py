#pythonの標準ライブラリを使用します
#文字列定数モジュール string
import string
letters = string.ascii_letters
#string.ascii_lettersには以下の定数が入っている
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print('[ ascii letters]')
print(letters)

#アルファベットの小文字が定数
lower = string.ascii_lowercase
print('[ lowercase ]')
print(lower)

#アルファベットの大文字
upper = string.ascii_uppercase
print('[ uppercase ]')
print(upper)

#数字(10進数)
digits = string.digits
print(' [digits] ')
print(digits)

#数字(16進数)
hexdigits = string.hexdigits
print('[ hex digits ]')
print(hexdigits)

#数字(8進数)
octdigits = string.octdigits
print('[ oct  digits ]')
print(octdigits)

#句読点として扱われるASCII文字列
#以下みたいなやつです
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
punctual = string.punctuation
print('[ punctuation ]')
print(punctual)

#印刷可能なASCII文字列で構成される文字列
printable = string.printable
print('[ printable ]')
print(printable)

#空白として扱われるASCII文字
#対象としては、
#スペース (space)、タブ (tab)、改行 (linefeed)、復帰 (return)、改頁 (formfeed)、垂直タブ (vertical tab) 
#だそうです。
whitespace = string.whitespace
print('[ whitespace ]')
print(whitespace)


#参考
#https://docs.python.jp/3/library/string.html
# http://www.lifewithpython.com/2013/04/string.html
# ファイル処理
ファイルの読み書きを行う際にも、定められた手順に沿って、プログラムを書く必要があります。ファイルの読み書きは、次の手順に沿って行います。

1.ファイルを開く　-open()

2.ファイルを読み書きする -read() / write()

3.ファイルを閉じる -close()

開いて作業したら、必ず閉じるという作業

## ファイルを読み込む
open()メソッドでencodingの引数を指定している。
日本語のファイルを読みたいときは、"utf-8"の部分を、"sjis"に変更する

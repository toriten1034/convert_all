Texのmediabb環境を使えう上で画像ファイルを管理してpdfに変換するためのツールです。
実行に必要なもの
・Python3
・convertコマンド
・md5sumコマンド

使い方
1．利用したい画像ファイルをfigs_rawに入れておおきます。
2．convert_all.pyを実行します。
3．files.logを参照してraw_figs内の新たに追加されたファイルと,変更が加えられたファイルをpdfに変換してfigsに保存します。

Texではパスを"figs/使いたい画像.pdf"と指定することで参照できます。

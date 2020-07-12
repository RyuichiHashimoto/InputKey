### READ ME

#### 1. What is the InputKey?

The InputKey automatically input keys by using python 3. 
Please avoid routine work by using the program :)

*I'm sorry, japanese comments is writtein in the program.
So, you should erase these comments before running the program.

#### 2. Needs to run

Please install python 3. 
Moreover, you may need to install the "pyautgui" module.

#### 3. How to use

Comming soon. (If I have a motivation...)

(以下，英語化するのめんどくさいから後程)


#### 4. ファイルの書き方(仕様)

##### 4.1 特定文字列の記載

　間違えて異なる文字列集合をキーボード入力するのを避けるため，ファイルの最前行と最終行に特定の文字列がなければ実行できないようにする．

- ファイルの最前行: ##############start##############
- ファイルの最終行: ##############finish##############

##### 4.2 コメントアウト

　Pythonと同様に，各行の先頭入力文字が#の場合，コメントとして認識される．


##### 4.3 特殊文字の書き方

アルファベット・数字: そのまま入力すればよい（日本語はサポートしていません．）

ShiftやCtrl等の特殊キー入力方法：[]の間に入力したいキーを書く. [Shift]や[ctrl]のように書く

特定の特殊ボタンを押しながらキー入力を行う場合: [shift, ABC]のように書く． 



特殊キー入力方法の参考URL:  [http://bttb.s1.valueserver.jp/wordpress/blog/2017/08/25/pyautogui%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9-%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89%E6%93%8D%E4%BD%9C%E7%B7%A8/](http://bttb.s1.valueserver.jp/wordpress/blog/2017/08/25/pyautoguiの使い方-キーボード操作編/) 


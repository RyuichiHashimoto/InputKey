import pyautogui
from time import sleep
import os
import sys
import copy

START_SIGNAL = "##############start##############"
FINISH_SIGNAL = "##############finish##############"
INPUT_INTERVAL = 0.1;

## 間違えて異なるファイルを読み込ませると非常にまずいので，
## ファイルの拡張子および，最初と最後の文字列が指定したのキーワードでなければそれ以上は実施できないようにする．
def isCorrectFile(commands):
    topCommand = commands[0].replace("\r\n","").replace("\n","");
    bottomCommand = commands[-1].replace("\r\n","").replace("\n","");

    topFlag = (topCommand == START_SIGNAL);
    bottomFlag = (bottomCommand == FINISH_SIGNAL);
    isProperFormat = checkProperFormat(commands);

    return topFlag and bottomFlag and isProperFormat;


def checkProperFormat(commands):

    for _command in commands:

        ## コマンド行を無視する．
        if (_command.startswith("#")):
            continue;

        ## 念のため，参照元が変更されないようにするためディープコピーを行う．
        command = copy.deepcopy(_command);


        leftCount = command.count('[')
        rightCount = command.count(']')

        if not leftCount == rightCount:
            return False;

        if (not leftCount==0):

            for i in range(0,leftCount):
                pos_left = command.find('[')
                pos_right = command.find(']')
                print("left:"+str(pos_left))
                print("right:" + str(pos_right))

                # ]の左側に[が来なければFalse
                # また，=1 の場合，[]内に特殊文字がないためFalseとする．
                if( pos_right + 1  <=  pos_left ):
                        return False;

                command = command[pos_right+1:]
                print(command)

    return True;

## 最終確認として読み込んだファイルの中身を表示させる
def configCommand(commands):
    ## ファイルに記載されたコマンドの確認
    print("下記コマンドを入力します")
    print("--------------------------")
    for c in commands:
        print(c);
    print("--------------------------")


## 単純なファイル読み込み（特殊なことは一切していない）
def getCommandsFromFile(fileName):
    retCommands = ""

    with open(fileName,"r") as fin:
        retCommands = fin.readlines();

    return retCommands;

def inputNormalKey(arg_):
    pyautogui.typewrite(arg_);
    sleep(INPUT_INTERVAL);


def inputSpecialKey(arg_):

    if("," in arg_):
        firstKey = arg_.split(",")[0]
        secondKey = arg_.split(",")[1]

        pyautogui.keyDown(firstKey)
        pyautogui.typewrite(secondKey);
        pyautogui.keyUp(firstKey)

        print(firstKey+":"+secondKey)

        return;

    pyautogui.press(arg_.lower())
    sleep(INPUT_INTERVAL);

##　コマンドとして処理する
def parseCommands(commands):

    ## 下記事項を行う．
    ##      ファイルの最初と最後の行を削除する．(commands[1:-1]にて)
    ##      改行コードが非常に厄介なので削除 (replace関数にて)
    ##      コメント行も削除する． (if ~~にて)
    ##      空白行を削除する.　(== "" にて)
    return [i.replace("\r\n", "").replace("\n", "") for i in commands[1:-1] if not (i.startswith("#") or i.replace("\r\n", "").replace("\n", "") == "" )]


def inputCommand(command):
    argment = "";
    inputKeys = command.split("]");

    ## もし特殊コマンドが一つもなければ引数を愚直にキーボード入力する．
    if(len(inputKeys) == 1):
        inputNormalKey(inputKeys[0]);
        return;

    ## ]毎に区切られた文字列には，必ず[が存在する．
    ## (inputKeysの最終要素には必ず[は含まれていないので削除)
    print(len(inputKeys))
    for inputkey in inputKeys[0:-1]:
        splitedKey = inputkey.split("[");

        normalInput = splitedKey[0];
        specialCommand = splitedKey[1];


        inputNormalKey(normalInput);

        inputSpecialKey(specialCommand)

    inputNormalKey(inputKeys[-1]);

    return;

if __name__ == "__main__":

    """    
    if(not len(sys.argv) == 2):
        print("引数に間違いがあります．")
        print("プログラムを終了します．")
        exit(-1)
        
        
    fileName = sys.argv[1];   
    """
    fileName = "commands.txt"
    print(fileName);
    commands = getCommandsFromFile(fileName);



    ## 入力ファイル確認
    if not isCorrectFile(commands):
        print("設定ファイルではないため，実行されません")
        print("入力ファイルを確認してください");
        exit(-1);

    ## コメント行と空白行を削除する．
    commands = parseCommands(commands);



    ## コマンド
    configCommand(commands)
    
    
    for i in range(0, 5):
        print("あと" + str(5 - i) + "秒")
        sleep(1)

    for command in commands:
        inputCommand(command);
        sleep(INPUT_INTERVAL);


    


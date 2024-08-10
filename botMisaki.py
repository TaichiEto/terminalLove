import time
#P153

your_name = "Manabu"
level_file = open("userlevel.txt")
your_level_str = level_file.read()
your_level = int(your_level_str)
print ("好感度{}".format(your_level))
level_file.close()

#ユーザーのレベルごとに読み込ませるファイルを変える。
if your_level >= 40:
    print ("Higher than 4")
    beginner = 0
    command_file = open("pybot2.txt", encoding = "utf-8")
    raw_data = command_file.read()
    command_file.close()
    lines = raw_data.splitlines()
    talk_count_file = open("talkcount.txt")
    talk_count_str = talk_count_file.read()
    talk_count = int(talk_count_str)
else:
    command_file = open("pybot.txt", encoding = "utf-8")
    beginner = 1
    raw_data = command_file.read()
    command_file.close()
    lines = raw_data.splitlines()
    talk_count_file = open("talkcount.txt")
    talk_count_str = talk_count_file.read()
    talk_count = int(talk_count_str)

if your_level == 0:
    print ("Copyright (C) 2018 衛藤泰地 All rights reserved.")
    time.sleep(2)
    print ("{} > 僕の名前は学! スマホが大好きな高校生さ！".format(your_name))
    time.sleep(1)
    print ("{} > これまで(ほぼ)男子校生活だったけど、ついに共学になる！彼女作るぞ〜！".format(your_name))
    time.sleep(1)
    print ("~数時間後~")
    time.sleep(3)
    print ("{} > 早速あの子に話しかけてみよう！".format(your_name))
    time.sleep(1)


time.sleep(0.5)
bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response


while True:
    command = input("{} > ".format(your_name))
    if your_level <= -1:
        print ("嫌われてしまったので初期化されます。")
        time.sleep(1)
        print ("現実だったらここでおしまいですよ^^")
        time.sleep(1)
        print ("=GAME OVER=")
        your_level = 0
        your_level_str_2 = str(your_level)
        level_file_2 = open("userlevel.txt", "w")
        level_file_2.write(your_level_str_2)
        level_file_2.close()
        time.sleep(5)
        break
    response = ""
    #response(返事)を定義
    for key in bot_dict:
        if key in command:
            response = bot_dict[key]
            your_level += 1
    if not response:
        response = "ごめんなさい..よくわかりませんでした...もっと勉強します！"
    if "好感度" in command:
        your_level += 1
        response = ("現在のあなたのレベルは{}です！".format(your_level))
    if "えへへ" in command:
        if beginner == 1:
            your_level -= 1
    if "debug" in command:
        your_level = 40
    if "ありがとう" in command:
        if beginner == 1:
            your_level += 2
        else:
            your_level += 1
    if "nokia" in command:
        print ("Misaki > ...")
        time.sleep(1)
        print ("嫌われてしまったので初期化されます。")
        time.sleep(1)
        print ("現実だったらここでおしまいですよ^^")
        time.sleep(1)
        print ("=GAME OVER=")
        your_level = 0
        your_level_str_2 = str(your_level)
        level_file_2 = open("userlevel.txt", "w")
        level_file_2.write(your_level_str_2)
        level_file_2.close()
        time.sleep(5)
        break
    if "好きです" in command:
        if your_level <= 39:
            print ("Misaki > その前に...お友達から...")
            time.sleep(1)
            print ("嫌われてしまったので初期化されます。")
            time.sleep(1)
            print ("現実だったらここでおしまいですよ^^")
            time.sleep(1)
            print ("=GAME OVER=")
            your_level = 0
            your_level_str_2 = str(your_level)
            level_file_2 = open("userlevel.txt", "w")
            level_file_2.write(your_level_str_2)
            level_file_2.close()
            time.sleep(5)
            break
        elif your_level <= 59:
            print ("Misaki > ありがとう。")
            time.sleep(1)
            print ("でも･･･")
            time.sleep(1)
            print ("私、実は男なの。")
            time.sleep(1)
            print ("あれ、知ってたかな？とにかく、そういうことだから。よく考え直して、それでもよかったら、そのときは･･･。")
            your_level = 60
        elif your_level <= 120:
            print ("Misaki > はい！喜んで！")
            time.sleep(1)
            print ("あとから取り消そうったってナシだからね！")
        else:
            print ("Misaki > ごめんなさい、友達としてか見れない...")
            print ("嫌われてしまったので初期化されます。")
            time.sleep(1)
            print ("現実だったらここでおしまいですよ^^")
            time.sleep(1)
            print ("=GAME OVER=")
            your_level = 0
            your_level_str_2 = str(your_level)
            level_file_2 = open("userlevel.txt", "w")
            level_file_2.write(your_level_str_2)
            level_file_2.close()
            time.sleep(5)
            break
    time.sleep(0.5)
    print("Misaki > {}".format(response))
    if "です" in command:
        time.sleep(1)
        print("Misaki > それより今更敬語なんてどうしたの！？")
    if "さようなら" in command:
        your_level_str_2 = str(your_level)
        level_file_2 = open("userlevel.txt", "w")
        level_file_2.write(your_level_str_2)
        level_file_2.close()
        break

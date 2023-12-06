from PIL import Image
import json
import csv
import os

def saving(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def what_to_do():
    print("И... что мне делать?")

def yes_choice():
    print("Я открываю глаза и иду на зов.")
    print("\"О, " + n1 + ", ты проснулась! Доброе утро\" - поприветствовала меня какая-то милая женщина. Видимо, я с ней живу, но я почему-то не помню её. ")
    print("\"Завтрак готов, кстати\", - добавила она.")
    input()
                                                                              
    breakfast = Image.open('омлет.jpg')
    breakfast.show() 

    input()
    print("\"Приятного аппетита!\"")
    input()
    while(True):
        print("a.\"СПАСИБО!\"")
        print("b.\"…\"")
        w = input()
        word = w.lower()

        if word == 'a' or word == 'b':
            break
        else:
            what_to_do()
            continue
    print("Я позавтракала.")
    print(n1, ", мне тебя провести до школы или ты пойдёшь сама?")
    while(True):
        print("a.\" Лучше пойти с ней.\"")
        print("b. \"Нет, лучше пойду сама.\"")
        g = input()
        gotosh = g.lower()

        readfile('players.json')
        player[n1]["going to school status"] = gotosh
        saving(player, "players.json")

        if gotosh == 'a':
            go_to_school()
            break
        if gotosh == 'b':
            going_by_yourself()
            break
        else:
            what_to_do()
            continue
        
def go_to_school():
    print("Я отправилась в школу вместе с этой женщиной.")
    print("Стоп, а что такое школа? Куда я иду? Если я у неё это спрошу, то может это будет весьма странно.")
    print("Ну да, это весьма странно, что я ни с того ни с сего потеряла память…")
    print("Я добралась до школы в целости сохранности.")
    input()
    print("\"Пока, " + n1 + "! Удачи тебе в школе!\"")
    input()
    print("А куда она идёт? Мне спрашивать это, или лучше не надо.")
    while(True):
        print("a. \"Можешь спросить, почему бы и нет\"")
        print("b. \"Лучше не надо\"")
        a = input()
        ask = a.lower()

        readfile("players.json")
        player[n1]["ask status"] = ask
        saving(player, "players.json")

        if ask == 'a':
            print("… Я правда это сделала…")
            input()
            print("\"На работу, как обычно.\"")
            print("Я уже не помню, что происходит обычно… Эх…")
            input()
            print("\"Давай, иди в школу, а то опоздаешь.\"")
            break
        elif ask == 'b':
            print("...")
            break
        else:
            what_to_do()
            continue

    input() 

    school = Image.open('школа.jpg')
    school.show()

    input()
    print("А на вид школа вроде ничего. На свой страх и риск войду во врата школы с потерянной памятью…")
    print("Я увидела на табло список всех классов.")
    input()
    class_list()
    input()
    print("Я тихо просидела на уроках. Я ничего не поняла из того, что рассказывали, но к счастью, никто меня не спрашивал.")
    input()
    print("Однако, я ощутила то, что девочка с розовыми волосами явно меня недолюбливает.")
    input()

    girl = Image.open('pink haired girl.PNG')
    girl.show()
    input()
    print("Мне пришло уведомление на телефон.")
    invitation()


def class_list():
    classes = ["1-A","2-A", "3-A", "1-B", "2-B", "3-B", "1-C", "2-C", "3-C", "1-D", "2-D", "3-D", "1-E", "2-E", "3-E"]
    cabs = ["A101", "A201", "A301", "B101", "B201", "B301", "C101", "C201", "C301", "D101", "D201", "D301", "E101", "E201", "E301"]
    print(classes[0], ":", cabs[0], " ", classes[1], ":", cabs[1], " ", classes[2], ":", cabs[2])
    print(classes[3], ":", cabs[3], " ", classes[4], ":", cabs[4], " ", classes[5], ":", cabs[5])
    print(classes[6], ":", cabs[6], " ", classes[7], ":", cabs[7], " ", classes[8], ":", cabs[8])
    print(classes[9], ":", cabs[9], " ", classes[10], ":", cabs[10], " ", classes[11], ":", cabs[11])
    print(classes[12], ":", cabs[12], " ", classes[13], ":", cabs[13], " ", classes[14], ":", cabs[14])

    input()
    while(True):
        c = input("А в каком классе я учусь? \n")
        cl = c.upper()
        if cl == "B-1":
            break
        else:
            print("\"Ты учишься в классе B-1\", - кто-то сказал мне.")
            break
    print("Так как на табло указаны были и кабинеты, я отправилась в кабинет", cabs[3], ".")

        
def going_by_yourself():
    print("Я пошла в школу, не помня, как она выглядит…")
    input()
    print("...")
    print("Прошло полчаса. Я так и не нашла школу.")
    print("Я странствовала по городу.")
    input()
    print("Я пересеклась с одним черноволосым юношей, и мне показалось, что я его знаю…")
    input()
    print("Что мне делать?")
    while(True):
        print("a. \"Продолжай искать школу\"")
        print("b. \"Пойди за юношей. Вдруг вы действительнно знакомы\"")
        s = input()
        sorg = s.lower()

        readfile("players.json")
        player[n1]["searching school status"] = sorg
        saving(player, "players.json")

        if sorg == 'a':
            print("…Ну ладно. Думаю будет странно преследовать человека, которого я смутно помню.")
            input()
            print("...")
            input()

            town = Image.open('город.jpg')
            town.show()

            input()
            print("Школу я так и не нашла… Но зато осмотрела город.")
            after_mail()
            break
        if sorg == 'b':
            print("… Я пошла за ним.")
            input()

            guy = Image.open('guy.PNG')
            guy.show()

            input()
            print("Он весьма симпатичный. ")
            input()
            print("… А не странно ли, что я его преследую? Даже если это и странно, мне действительно интересно, куда он идёт.")
            input()
            print("Какое совпадение! Он пошёл туда, откуда я вышла.")
            input()
            print("Стоп. Получается, я с ним тоже живу? ")
            print("Получается, он меня знает? Прекрасно! Я не так сильно теперь похожа на сталкера.")
            input()
            print("\"" + n1 + ", зайди на почту \", - обратился он ко мне.")
            input()
            print("На почту? На какую? Какую почту он имеет в виду?")
            while(True):
                print("a.\"Традиционную\"")
                print("b.\"Электронную \"")
                m = input()
                mail = m.lower()

                readfile("players.json")
                player[n1]["mail status"] = mail
                saving(player, "players.json")

                if mail == 'a':
                    print("\"Ты куда?\"")
                    input()
                    print("\"На почту.\"")
                    input()
                    print("\"Я имел в виду электронную.\"")
                    print("Упс…")
                    after_mail()
                    break
                elif mail == 'b':
                    after_mail()
                    break
                else:
                    what_to_do()
                    continue
            break
    
def after_mail():
    input()
    print("Я зашла в электронную почту.")
    input()
    invitation()           
            
def no_choice():
    print("… Голоса больше не было слышно. Я решила спать дальше. ")
    input()
    print("Сон был очень долгим…")
    input()
    print("Я стояла в пустоте. Возле меня появилась загадочная дверь.")
    print("Открыть её?")
    print("a. \"Да, давай \"")
    print("b. \"Нет, лучше не стоит\"")
    o = input()
    op = o.lower()

    readfile("players.json")
    player[n1]["opening door status"] = op
    saving(player, "players.json")

    if op == 'a':
        open_the_door()
    elif op == 'b':
        print("Ничего не происходит.")
        input()
        print("...")
        input()
        print("Как-то пустовато. Может, всё-таки открою дверь на свой страх и риск.")
        input()
        open_the_door()
    else:
        what_to_do()
        input()
        print("... Наверное, всё-таки открою дверь...")
        open_the_door()


def open_the_door():
    print("Я открыла дверь. Я оказалась в пространстве, в котором очень много дверей.")

    input()

    doors = Image.open('doors.png')
    doors.show()

    input()
    print("… Это где я? Неужели в мультивселенной?")
    print("Странное место… ")
    input()
    print("\"" + n1 + ".\"")
    input()
    print("!")
    print("Кто-то обратился ко мне.")
    input()
    print("\"Ты слышишь меня?\" - кто-то тихо сказал.")
    input()
    print("Я оборачивалась по сторонам, но никого не видела.")
    while(True):
        print("a. \" Кто это?\"")
        print("b. \"...\"")
        wh = input()
        who = wh.lower()

        readfile("players.json")
        player[n1]["mysterious person"] = who
        saving(player, "players.json")

        if who == 'a':
            break
        elif who == 'b':
            break
        else:
            what_to_do()
            input()
            break
    print("\"Ах… ты и меня забыла… Неудивительно. Тогда познакомимся вновь. Я - Мирай.\"")
    input()
    print("Мирай?")
    input()
    print("\"Ты сейчас спишь. Эти двери - сон.\"")
    input()
    print("Сон?")
    input()
    print("Из одной двери внезапно выбежало зомби…")
    input()

    zomb = Image.open('zombie.JPEG')
    zomb.show()

    input()
    print("Это лицо… Оно вроде знакомо мне…")
    input()
    print("\"Беги, " , n1, "! Не позволь зомби тебя съесть!\" ")
    print("Мирай мне говорит бежать. Однако, у меня нет сил бегать… ")
    while(True):
        print("a.\"БЕГИ\"")
        print("b. \"Можешь не бежать. Это же все равно сон.\"")
        r = input()
        run = r.lower()

        readfile("players.json")
        player[n1]["running away from zombie status"] = run
        saving(player, "players.json")

        if run == 'a':
            print("Я стараюсь бежать из-за всех сил.")
            print("Но я бегу слишком медленно…")
            input()
            break
        elif run == 'b':
            break
        else:
            what_to_do()
            input()
            break
    print("Зомби на меня напало! ")
    input()
    print("\"Открой глаза, " + n1 + "!\"")
    input()
    print("Я открыла глаза. Время 14:30. Ничего себе! Я так долго спала…")
    input()
    print("Пришло уведомление.")
    invitation()


def invitation():
    print("Там я увидела какое-то приглашение куда-то от какой-то корпорации Нео.")
    input()
    print("\"Здравствуйте, " + n1 + "! Мы приглашаем Вас принять участие в интерактивной игре. Это необычная игра. Принимая в ней участие Вы нам поможете провести исследование. Нам это очень важно. Таким образом, Вы, как и мы, сможете внести вклад в развитие человечества. Мы будем очень благодарны Вам! \"")
    input()
    while(True):
        print("a.\"Принимать приглашение\"")
        print("b.\"Отклонить приглашение\"")
        ad = input()
        accdec = ad.lower()

        readfile("players.json")
        player[n1]["agreement status"] = accdec
        saving(player, "players.json")

        if accdec == 'a':
            accept()
            break
        elif accdec == 'b':
            print("Я закрыла телефон.")
            input()
            decline()
            break
        else:
            what_to_do()
            continue

def accept():
    print("Это звучит весьма интересно! Будет здорово внести вклад в развитие ЦЕЛОГО ЧЕЛОВЕЧЕСТВА! ")
    print("Неужели это настолько влиятельная корпорация? Видимо, да. И это здорово!")
    input()
    print("На следующей неделе меня пригласили в главное здание Корпорации Нео.")
    input()

    corp = Image.open('neo corp.JPEG')
    corp.show()

    input()
    print("Я пришла туда.")
    input()
    print("Ого! А там прилично народу! Даже неловко как-то…")
    input()
    print("\"Привет!\"")
    print("Меня кто-то поприветствовал. Я обернулась.")
    input()

    person = Image.open('ginger guy.jpg')
    person.show()

    input()
    while(True):
        print("a. \"Привет!\"")
        print("b. \"...\"")
        h = input()
        hello = h.lower()
        if hello == 'a':
            print("На этом наша беседа закончилась. Он, может, не услышал меня…")
            break
        elif hello == 'b':
            break
        else:
            what_to_do()
            continue
    input()
    print("В здании было очень шумно… ")
    print("Пришёл какой-то человек в костюме. ")
    input()

    head = Image.open('satoru.jpg') 
    head.show()

    input()
    print("\"Тишина в зале!\" - сказал он громко, но без повышения тона.")  
    print("Все сразу затихли. Этот человек меня уже пугает…")
    input()
    print("\"Всем здравствуйте! Вы все здесь, потому что приняли наше приглашение. Ваше согласие всё ещё актуально?\"")
    while (True):
        print("a. \"Да\"")
        print("b. \"Нет\"")
        ag = input()
        agreement = ag.lower()
        
        readfile("players.json")
        player[n1]["agreement status"] = agreement
        saving(player, "players.json")

        if agreement == 'a':
            print("\"Так как я за демократию, я отпускаю всех, кто ответил нет.\"")
            input()
            print("Некоторые начали уходить. Однако, таких было немного.")
            input()
            print("\"Хорошо. Полагаю, мне следует представиться. Моё имя - Сатору Кишо. Я главный директор Корпорации Нео.\"")
            print("Главный директор? Я так и знала, что он важная персона.")
            input()
            print("Я не желаю затягивать свою речь и утомлять вас, поэтому сразу перейду к сути.")
            input()
            print("Идём за мной.")
            input()
            print("Я и остальные участники пошли за ним.")
            print("Продолжение следует…")
            break
        elif agreement == 'b':
            print("\"Так как я за демократию, я отпускаю всех, кто ответил нет.\"")
            input()
            print("Я пошла туда, откуда пришла.")
            decline()
            break
        else:
            print("\" Простите, " + n1 + ", но я не понял вашей точки зрения.\"")
            input()
            print("\"Ваше согласие всё ещё актуально?\"")
            continue


def decline():
    print("И так я дальше жила с потерянной памятью. Жизнью самой обычной школьницы.")
    print("Конец.")


print("\"Где я?... Кто я?...\" - задаюсь я таким вопросом на протяжении недели. \"Я даже забыла свое имя…\"")
input()
if not os.path.exists("players.json"):
    name = input("Как меня зовут? \n")

    n1 = name.title()
    if n1 == '':
        n1 = "Рицу"  

    player = {
        n1 : {
            "name" : n1
        }
    } 

else:
    player = readfile("players.json")

    while(True):
        print("Сохранённые имена:")
        for names in player:
            print(names)

        dp = input("Что вы хотите сделать?\n 1. Удалить файлы.\n 2. Продолжить игру. \n")
        if dp == '1':
            nenter = input("Введите имя из списка выше. \n")
            nameenter = nenter.title()
            try:
                del player[nameenter]
                saving(player, "players.json")
            except(KeyError):
                print("Такого имени нет в списке.")
                print()
        elif dp == '2':
            break
        else:
            what_to_do()


    playname = list(player.keys())[-1]
    while(True):
            print(f"Продолжить игру, как {playname}?")
            pr = input("Да(Y) или Нет(N)? \n")
            proceed = pr.upper()
            if proceed == 'Y':
                n1 = playname
                break
            elif proceed == 'N':
                name = input("Как меня зовут? \n")

                n1 = name.title()
                if n1 == '':
                    n1 = "Рицу"
                
                player = readfile("players.json")

                newplayer = {
                    n1: {
                        "name" : n1
                    }
                }
                player.update(newplayer)
                
                break
            else:
                what_to_do()   
    


saving(player, 'players.json')

myname = f"{n1}... Вот как меня зовут..."
print(myname)
call = f"{n1}!"
print(call)
input()
print("?... Кто это меня зовёт?")
print("Идти на зов?")
while(True):
    a = print("a. \"Да. Лучше отозваться.\"")
    b = print("b. \"Нет. Я думаю, не стоит идти...\"")
    ch = input()
    choice = ch.lower()

    player = readfile('players.json')
    player [n1]["yes/no choice"] = choice
    saving(player, 'players.json')

    if choice == 'a':
        yes_choice()
        input()
        break
    elif choice == 'b':
        no_choice()
        input()
        break   
    else:
        what_to_do()
        continue


player = readfile("players.json")

eke = list(player.values())[-1]
kek = dict(eke)
keys = kek.keys()
data = [ kek ]

with open ("players_output.csv", 'w', newline='') as file:
    fieldnames = keys
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(data)
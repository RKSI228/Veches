while True:
        print("Выбери ученика")
        print("1-Саша Мандрыкин")
        print("2-Чурка на Рамазане")
        print("3-Абоба Абобов")
        print("4-Ростислав Мирошник")
        a=int(input())
        if a==1:
                file=open('111.txt',encoding='utf-8')
                content=file.readlines()
                s=content[0]
                print("Саша Мандрыкин",s)
        elif a==2:
                file=open('111.txt',encoding='utf-8')
                content=file.readlines()
                s=content[1]
                print("Чурка на Рамазане",s)
        elif a==3:	
                file=open('111.txt',encoding='utf-8')
                content=file.readlines()
                s=content[2]
                print("Абоба Абобов",s)
        elif a==4:
                file=open('111.txt',encoding='utf-8')
                content=file.readlines()
                s=content[3]
                print("Ростислав Мирошник",s)
        else:
                print("Таких учеников нет!!1")






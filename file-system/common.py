from datetime import datetime as d


class comm:
    def __init__(self, name, parent, flag):
        self.created = d.now().strftime("%H:%M:%S")
        self.name = name
        self.parent = parent
        self.flag = flag


class file(comm):
    def __inti__(self, name, parent, content, flag):
        super().__init__(name, parent, content, flag)
        self.content = []
        self.content.append(content)


class directory(comm):
    def __inti__(self, name, parent, content, flag):
        super().__init__(name, parent, content, flag)
        self.content = []
        self.content.append(content)


switcher = {
    1: creator


}


list_choice = ["1 create dir & file", "2 list file and directory", "3 update file content", "4 update directory & file",
               "5 delete directory & file", "6 restore directory and deleted file"

               ]


def creator():
    print("folder=1 / file =1")
    file = int(input())
    if(file == 1):
        name = input("name")
        content = input(("enter content\n"))
        parent = input("enter parent")
        file(name, parent, content, 1)
    else:
        name = input("name")
        content = input(("enter content\n"))
        parent = input("enter parent")
        file(name, parent, content, 1)


exit = 0
while(exit != 1):
    for i in list_choice:
        print(i, "\n")
    choice = int(input())

    try:
        func_var = switcher.get(choice, "enter invalid")
        print(func_var())
    except:
        print("enter valid")

    exit = 1

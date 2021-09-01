class Symbol:
    def __init__(self, index=None, name=None, type=None, size=None, dimension=None):
        self.size = size
        self.type = type
        self.name = name
        self.index = index
        self.dimension = dimension


types = ['int', 'id', 'num', 'function']


def printer(obj):
    print('Name:', obj.name)
    print('Type:', obj.type)
    print('Size:', obj.size)
    print('Dimension:', obj.dimension)
    print('Index:', obj.index)


def get_index(param):
    ascii_value = ''.join(str(ord(c)) for c in param)
    index = int(ascii_value) % 8
    return index


def insert():
    print('---Insert Menu---')
    print()
    text = input("Enter your input")
    result = [x.strip() for x in text.split(',')]
    print('After split:', result)
    if len(result) == 2:
        if result[1] in types:
            # will create an object now
            obj = Symbol()
            obj.name = result[0]
            obj.type = result[1]
            obj.size = 4
            obj.index = get_index(result[0])
            obj.dimension = None
            # obj.save()
            print('Symbol Created')
            printer(obj)

    print('Wrong input, try again!')
    return insert()


def show():
    pass


def delete():
    pass


def update():
    pass


def search():
    pass


def starter(option):
    switcher = {
        1: insert(),
        2: show(),
        3: delete(),
        4: update(),
        5: search(),
    }
    return switcher.get(option)


starter(input("Choose option"
              "\n1.Insert"
              "\n2.show"
              "\n3.delete"
              "\n4.update"
              "\n5.search\n"))

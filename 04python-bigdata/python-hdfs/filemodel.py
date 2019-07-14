class File(object):
    # 类属性是指定义在类的内部而且在方法的外部的属性
    filename


    def __init__(self,name,age,gender=1):
        # 对象属性是指定义在方法的内部的属性，例如本例中
        # name，age和gender都是对象属性
        self.name = name
        self.age = age
        self.gender = gender
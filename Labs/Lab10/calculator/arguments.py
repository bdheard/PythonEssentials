class Arguments():
    def __init__(self, first_param, second_param):
        self.first_param = first_param
        self.second_param = second_param

    @property
    def first_param(self):
        return self.__first_param
    
    @first_param.setter
    def first_param(self, value):
        self.__first_param = value

    @property
    def second_param(self):
        return self.__second_param
    
    @second_param.setter
    def second_param(self, value):
        self.__second_param = value
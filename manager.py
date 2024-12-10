from validator import *
from custom_parser import*


class Op:
    def __init__(self,char,un):
        self.__char=char
        self.un=un





def calculate(inpt):
    inpt=string_to_lst_conv(inpt)
    inpt=white_spaces_remover(inpt)

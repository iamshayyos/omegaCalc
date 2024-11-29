def string_to_lst_conv(inpt):
    return list(inpt)

def white_spaces_remover(inpt):
    inpt_lst = [letter for letter in string_to_lst_conv(inpt) if not letter.isspace()]
    return list(''.join(inpt_lst))

def main():
    st = input("Enter something: ")
    print("Converted to list:", string_to_lst_conv(st))
    print("Without whitespaces:", white_spaces_remover(st))

if __name__ == "__main__":
    main()

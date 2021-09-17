def main():
    print(
        """
    ----------------------------
    -     Taschenrechner       -    
    ----------------------------
    Use operators (+,-,*,/)   
    """
    )    

    taschenrechner()

def taschenrechner():
    while True:
        user_input = input(
            """
    Enter: """
        )
        user_list = list(user_input)
        
        for i in range(len(user_list)):
            if user_list[i] == "+" or user_list[i] == "-" or user_list[i] == "*" or user_list[i] == "/":
                first_list = user_list[:i]
                secound_list = user_list[i+1:]
                operator = str(user_list[i])
                math(first_list, secound_list, operator)
            
            
                

def math(first_list, secound_list, operator):
    strings = [str(integer) for integer in first_list]
    a_string = "".join(strings)
    first_integer = int(a_string)

    strings2 = [str(integerr) for integerr in secound_list]
    a_string2 = "".join(strings2)
    secound_integer = int(a_string2)
    

    math2(first_integer, secound_integer, operator)
                

def math2(first_integer, secound_integer, operator):
    if operator == "+":
        ergebnis = first_integer + secound_integer
    elif operator == "-":
        ergebnis = first_integer - secound_integer
    elif operator == "*":
        ergebnis = first_integer * secound_integer
    elif operator == "/":
        ergebnis = first_integer / secound_integer
    else:
        print(
            """
            Error
            """
        )
    
    print(
        f"""
        --------------------------------------------------------------------------
             {first_integer} {operator} {secound_integer} =    {ergebnis}                                                      
        --------------------------------------------------------------------------"""
    )

if __name__ == "__main__":
    main()

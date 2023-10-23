#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length  # Initialize the result list with zeros

    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0
            result[i] = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass

    return result

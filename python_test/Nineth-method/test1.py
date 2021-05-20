from typing import ByteString


def to_jaden_case(string):
    # 详细写法
    '''
    blanklist = []
    new_list = string.split()
    for i in new_list:
        blanklist.append(i.capitalize())
    new_str = ' '.join(blanklist)
    return new_str'''

   # 简化写法  return " ".join(w.capitalize() for w in string.split())


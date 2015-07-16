
#coding=utf-8

def raise_value_exc(msg):
    raise ValueError(msg)


#获取校验码
def getcode(id_card_code):
    count_rule = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    result = reduce(lambda x,y:x+y,map(lambda x,y:x*y,id_card_code,count_rule))
    result = result%11
    return str(result)

"""
def choose_action():
    print "please choose a option."
    print "1:check the Id_card_code.\n others:get a Id_card_code "
    action_code = raw_input("please enter a number:")
    if action_code == '1':
        return getValue()
    else:
        return
"""


#从键盘接受身份证号
def getValue():
    getval = raw_input("\nplease enter the IdCode: ")
    return check_code_valid(getval)

def check_code_valid(getval):
    if len(getval) == 18:
        try:
            check_id_code = getval[-1]
            getval = getval[:-1]
            id_card_code = [int(x) for x in getval]
            return (id_card_code, getval, check_id_code)
        except TypeError, ValueError:
            raise raise_value_exc("the id code include invalid words.\n please check it.and try agin")
    else:
        raise raise_value_exc("the length of number that you entered is not 18.\n please check it.and try again.")

#主流程
def main():
    #full_id_code = choose_action()
    id_code, id_code_part, check_id_code = getValue()
    check_code = getcode(id_code)
    map_rule = {'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'4','9':'3','10':'2'}
    if check_id_code == map_rule[check_code]:
        print "Valide id code."
    else:
        print "invalid id code"
        right_code = id_code_part + map_rule[check_code]
        print "The valid code is: ", right_code, "\n"



if __name__ == "__main__":
    main()

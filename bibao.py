# coding; utf-8
def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print('pass')
        else:
            print('failed')
    return cmp

func_100 = set_passline(60)
func_150 = set_passline(90)
print(func_100.func_closure)
func_100(59)
func_150(89)

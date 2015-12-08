def line_conf(a, b):
#    i = a * b
    def line(x):
#        i = i + x
        return a * x + b
    return line
 
line1 = line_conf(4, 5)
print(line1(5))

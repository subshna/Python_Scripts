import mkypt
def monkey_f(self):
    print "monkey_f()"

mkypt.Myclass.f = monkey_f
obj = mkypt.Myclass()
obj.f()

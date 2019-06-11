import timeit

exec_time1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
exec_time2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
exec_time3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)

print (exec_time1)
print (exec_time2)
print (exec_time3)
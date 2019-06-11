import sys
import timeit
''' To demonstarte that tuple is faster than list and would occupy less memory'''

print('Size occupied by List {}'.format(sys.getsizeof([1,2,3,4,5])))
print('Size occupied by Tuple {}'.format(sys.getsizeof((1,2,3,4,5))))

list_test = timeit.timeit(stmt='[1,2,3,4,5]', number=1000000)
print('Time taken to create 1000000 list: {}'.format(list_test))

tuple_test = timeit.timeit(stmt='(1,2,3,4,5)', number=1000000)
print('Time taken to create 1000000 tuple: {}'.format(tuple_test))
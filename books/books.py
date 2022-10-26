import numpy as np

B = 6
L = 2
D = 7
values = [1,2,3,6,5,4]
signup_times= [2,3]
shipping = [2,1]
library_contents = [[0,1,2,3,4],[3,2,5,0]]
singned_up = set([])
scanned = set([])

def order_books_by_val(books,values):
    arr = sorted(books,key=lambda x: values[books[x]],reverse=True)
    return arr


#RANDOM APPROACH
order = np.random.shuffle(np.arange(L))
# for k in library_contents:
#     print(order_books_by_val(k,values))
for i in library_contents[1]:
    print(values[i])
# print(order_books_by_val(library_contents[1],values))
# library_contents = [ for k in library_contents]
print(library_contents)
# for day in range(D):
#     for library in singned_up:

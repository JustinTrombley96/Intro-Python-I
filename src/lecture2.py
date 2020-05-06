# pass-by-reference vs passing-by-value
# define a function that multiplies its input by 2
# this function passes its input by-value
# if the input is not too memory-expensive, then it's a lot 
# 
def mult_by_2(x):
    return x * 2
y = 12
print(id(y)) #140708980879968
z = mult_by_2(y)
print(z) #24

# passing-by-reference
# typically, data structures passed to a function are passined in by reference,
# in large part because data structures take up a lot of memory, which would mean
# the copying would be expensive.
def mult2_list(l):
    # multiply every int in the list by 2
    # mutate the contents of the list
    for i in range(len(l)):
        l[i] *= 2
l = [1, 2, 3]
print(id(l)) #2910499983944
mult2_list(l)
print(id(l)) #2910499983944
print(l) #[2, 4, 6]

# catalog what we already know
# define what median means
# the middle element of all the elements once they're sorted
# figure out how to calculate it
# how do we deal with an even number of numbers?
# when should we handle the sorting?
# None ~ null, undefined

class MedianFetcher:
    def __init__(self):
        # define all the attributes on 'self'
        self.median = None
        self.numbers = []
    
    
    # inserts the value n into our class
    def insert(self, n):
        # where do you store n?
        # maybe we store it in self.median?
        # what happens when we insert more values?
        self.numbers.append(n)
        self.numbers.sort() # sorts the list in-place
      
    def get_median(self):
        if len(self.numbers) == 0:
            return None
        # figure out if the length of the numbers list is odd or even
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 1:
            # if it's odd, then we can pick the middle number
            # how do we get the middle number of a list
            # take the length, divide it by 2
            # // rounds down as division
            return self.numbers[mid]
        else:
            # if it's even, get the average of the two middle numbers
            # grab the element right before the mid element
            return (self.numbers[mid - 1] + self.numbers[mid]) / 2
    def something(self):
        return 1

medianFetcher = MedianFetcher()
print(medianFetcher.get_median()) #None
medianFetcher.insert(5)
medianFetcher.insert(10)
print(medianFetcher.get_median()) #7.5
medianFetcher.insert(100)
print(medianFetcher.get_median()) #10
print(medianFetcher.something()) #1
medianFetcher.insert(1)
medianFetcher.insert(2)
print(medianFetcher.get_median()) #5


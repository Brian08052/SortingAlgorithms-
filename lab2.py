import time
from random import shuffle
from random import randint
import copy
from copy import deepcopy

def bubble_sort(mylist):
    lstLen = len(mylist)
    for i in range(lstLen):
        for j in range(lstLen-1-i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return(mylist)
    
def selection_sort(mylist):
    n = len(mylist)
    i = 0
    while i < n:
        smallest = i
        j = i + 1
        while j < n:
            if mylist[j] < mylist[smallest]:
                smallest = j
            j += 1
        mylist[i], mylist[smallest] = mylist[smallest], mylist[i]
        i += 1
    return(mylist)

def insertion_sort(mylist):
    n = len(mylist)
    i=1 #? length of the mini list

    while i < n:
        j = i-1
        while mylist[i] < mylist[j] and j > -1:#while min is less that
            j -= 1#goes through list from right hand side to find where i should go
   
        temp = mylist[i]#makes a copy of new item
        k = i-1#right hand side of mini-list
        while k > j: #goes through list copying everything up one untill we get to i's new position
            mylist[k+1] = mylist[k]
            k-=1
        mylist[k+1] = temp
        i += 1
    return(mylist)

#################### Heapsort

def heapsort(inlist):


    length = len(inlist)
    for i in range(length):
        bubbleup(inlist,i)
    for i in range(length):
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist,0, length-2-i)

def bubbleup(inlist, i):
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0

def bubbledown(inlist, i, last):
    while last > (i*2):  
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc   
        if last > lc and inlist[rc] > inlist[lc]:  
            maxc = rc
        if inlist[i] < inlist[maxc]:
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last



####################### BU Mergesort
    
def python_sort(mylist):
    return mylist.sort()
#######################


def quick_sort(mylist):
     n = len(mylist)
     for i in range(len(mylist)):
         j = randint(0, n-1)
         mylist[i], mylist[j] = mylist[j], mylist[i]
     _quicksort(mylist, 0, n-1)

def _quicksort(mylist, first, last):
    if last > first:
        pivot = mylist[first]
        f=first + 1
        b=last
        while f <= b:
            while f<=b and mylist[f]<=pivot:
                f+=1
            while f <=b and mylist[b] >= pivot:
                b -= 1
            if f < b:
                mylist[f], mylist[b] = mylist[b], mylist[f]
                f+= 1
                b-= 1
        mylist[b], mylist[first] = mylist[first], mylist[b]
        _quicksort(mylist, first, b-1)
        _quicksort(mylist, b+1, last)

        
class lister():
    def __init__(self, n):
        self.a = self.a(n)
        self.b = self.b(n)

    def a(self, n):
        return [n for n in range(n)]
    
    def b(self,n):
        return list(reversed(self.a))
        
    def c(self):
        c = deepcopy(self.a)
        n = len(c)
        self.shufflek(c, n//20, n-1)
        return(c)
        
    def d(self):
        d = deepcopy(self.b)
        n = len(d)
        self.shufflek(d, n//5, n-1)
        return(d)
        
    def e(self):
        e = deepcopy(self.a)
        shuffle(e)
        return(e)
        

    def shufflek(self, lst, k, n):
        for e in range(k):
            rand1 = randint(0,n)
            rand2 = randint(0,n)
            lst[rand1], lst[rand2] = lst[rand2], lst[rand1]

        


def test(lst, alg):

    testlist = deepcopy(lst)
    start_time = time.perf_counter()
    alg(testlist)
    end_time = time.perf_counter()
    return(end_time - start_time)

def maintest(algs, n):
    l = lister(n)
    lists = [l.a, l.b, l.c(), l.d(), l.e()]
    lnames = ["a", "b", "c", "d", "e"]


    results = {}
    #{AlgorithmIndex:[[a time],[b time],[21 c times],[21 d times],[21 e times]]}
    m = 21

    algIndex = 0
    listIndex = 0
    resultIndex = 0
    for a in range(len(algs)):
        #creates a list for each algorithm to store its results
        results[a] = []

    for lst in lists:
        if listIndex<2:#0,1-a,b
           for alg in algs:
               #create an empty list to hold the result
               results[algIndex]+=[]
               #creates a variable to hold time taken, easier to understand
               timex = test(lists[listIndex], algs[algIndex])
               #add the time into the alocated space
               results[algIndex].append([timex])
               algIndex += 1

        else:#2,3,4- c,d,e
            for alg in algs:
                result = []
                for i in range(m):
                    #runs funciton m times, in this case 21
                    timex = test(lists[listIndex], algs[algIndex])
                    result += [timex]
                results[algIndex].append([result])
                algIndex += 1
            #print(results)

        listIndex += 1
        resultIndex += 1
        algIndex = 0
    #print(results)

    algIndex = 0
    listIndex = 0
    resultIndex = 0

    

    for lst in lists:
        
        
        print("For list", lnames[listIndex], ":")
        if listIndex<2:#0,1
            print("Algorithm: Time")
            for alg in algs:
               print(alg.__name__, ": ", results[algIndex][listIndex][0])
               algIndex += 1

        else:#2,3,4
            print("Algorithm :Mean: Median")
            for alg in algs:
                resultList = results[algIndex][listIndex][0]
                mean = 0
                for i in range(len(resultList)):
                    mean += resultList[i]
                mean = mean/m
                median = resultList[10]
                print(alg.__name__, ":", mean, ":", median)
                algIndex += 1

        listIndex += 1
        resultIndex += 1
        algIndex = 0

    



#maintest([bubble_sort, selection_sort, insertion_sort, heapsort, python_sort, quick_sort], 10)




# Algorytm sortowania bąbelkowego bez optymalizacji

def bubbleSort(array):
 
 #pętla dostępu do każdego elementu w tablicy
 for i in range(len(array)):
  
  #pętla porównująca elementy w tablicy
  for j in range(0, len(array) - i -1):
   
   #porównanie dwóch sąsiadujących elementów 
   #zmiana > na <, aby posortować w porządku majęlącym
   if array[j] > array[j+1]:

    #zmiana elementów, jeśli elementy nie są w zamierzonej kolejności
    temp = array[j]
    array[j] = array[j+1]
    array[j+1] = temp    

list = [1, 20, 4, 50, 6]
print ('Lista do posortowania:')
print(list)

bubbleSort(list)

print('Posortowana lista:')
print(list)

print('Zamiana tablicy numerycznej na wartość string:')
string = ' '.join(map(str,list))
print(string)    
a = [-23, 5, 8, 0,  20, -8, 1, 45, 10, 16, 4, 12]

def selection_sort(arr):
   for i in range(len(arr)):
       min_index = i
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(a)
print(a)
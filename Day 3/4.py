def swap(lt):

  return [lt[i+1] if i % 2 != 0 else lt[i] for i in range(len(lt))]

lt = [1, 2, 3, 4, 5]
swapped = swap(lt)
print(swapped) 

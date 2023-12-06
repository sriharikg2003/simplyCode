
def monostack(arr):
    stack = []
    solution_arr = [-1]*len(temperatures)
    for i in range(len(arr)):
        print("DONE")
        if stack:
            if arr[len(arr)-i-1] < stack[-1][0]: 
                solution_arr[len(arr)-i-1] = stack[-1][1] - (len(arr)-i-1)
                stack.append([arr[len(arr)-i-1],len(arr)-i-1])
            else:
                solution_arr[len(arr)-i-1]=0
                while(stack and arr[len(arr)-i-1] >= stack[-1][0]):
                    stack = stack[:-1]
                if stack:
                    solution_arr[len(arr)-i-1] = stack[-1][1] - (len(arr)-i-1)

                stack.append([arr[len(arr)-i-1],len(arr)-i-1])

        else:
            solution_arr[len(arr)-i-1] = 0
            stack.append([arr[len(arr)-i-1],len(arr)-i-1])
    print(solution_arr)            
    return stack



temperatures = [73,74,75,71,69,72,76,73]
print(monostack(temperatures))

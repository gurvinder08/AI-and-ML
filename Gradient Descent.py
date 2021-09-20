x = int(input("Enter a random value for x:"))  # Random guess
rate = 0.01  # Learning rate
precision = 0.0001
pstep_size = 1
max_iters = 1000
iters = 0  #iteration counter
#function = lambda x : ((x+7)**2)
df = lambda x: 2*(x+7)  #Gradient of the function

while pstep_size > precision :
    prev_x = x
    x = x - rate * df(prev_x)  # Gradient descent
    pstep_size = abs(x - prev_x)
    iters = iters+1  # iteration count

print("No. of iterations:", iters)
print("The local minimum occurs at", x)

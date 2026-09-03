import numpy as np  # numpy arrays are hetrogenous 
myNumpyArray = np.array([1, 2, 3], float)
numpyArrayWithPartitions = np.linspace(10,20,5) # both 10 and 20 are inclusive
numpyArrayWithPartitionsArange = np.arange(10,20) # here 10 is inclusive but 20 is exclusive

numpyArrayZeros = np.zeros(10)
numpyArrayOnes = np.ones(10)
numpyArrayFullWithSpecificNumber = np.full(50, 5)
print(myNumpyArray)
print(numpyArrayWithPartitions)
print(numpyArrayWithPartitionsArange)
print(numpyArrayZeros)
print(numpyArrayOnes)
print(numpyArrayFullWithSpecificNumber)


print("\n\n\n")

## Zero Dimensional Array
zero = np.array(10)
print(f"\nZero Dimensional Array: {zero}")

## One Dimensional Array
one = np.array([10, 20, 30, 40, 50, 60])
print(f"\nOne Dimensional Array: {one}")

## Two Dimensional Array
two = np.array(
    [
        [10, 20, 30, 40, 50, 60], 
        [110, 120, 130, 140, 150, 160]
    ])
print(f"\nTwo Dimensional Array: {two}")

## Three Dimensional Array: Collection of 2D arrays
three = np.array(
    [
        [
            [10, 20, 30, 40, 50, 60], 
            [110, 120, 130, 140, 150, 160]
        ],
        [
            [210, 220, 230, 240, 250, 260], 
            [310, 320, 330, 340, 350, 360]
        ]
    ]
)
print(f"\nThree Dimensional Array: {three}")
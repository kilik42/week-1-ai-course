# Python & NumPy Fundamentals Brush-Up 
 

## Collections

Python has several built-in types that are useful for storing and manipulating data: list, tuple, dict. Here is the official Python documentation on these types (and many others): https://docs.python.org/3/library/stdtypes.html.

### Lists

Lists are mutable arrays. Let's see how they work.
"""

# Create a list called 'names' that contains two string elements: "A" and "B"
# In Python, lists are ordered collections that can store multiple values.
# Each value in a list has a position (called an index), starting at 0.
# So here: "A" is at index 0, and "B" is at index 1.
names = ["A", "B"]

# Print the first element of the list 'names'
# Remember: Python lists use zero-based indexing,
# so index 0 gives us the first element.
print(names[0])   # This will output: A

# Append to list (adds a new element at the END of the list)
# The append() method modifies the list in-place.
# Here we are adding the string "C" to the existing list 'names'.
names.append("C")

# Print the updated list to see the result.
# Now 'names' contains: ["A", "B", "C"]
print(names)

# The len() function returns the number of items in a list (its length).
# Since our list 'names' currently has three elements ["A", "B", "C"],
# len(names) will return 3.
print(len(names))   # Output: 3

# Concatenate (join together) two lists.
# The += operator here means: take the existing list 'names' and add the new list ["D", "E"] to the end.
# This is shorthand for: names = names + ["D", "E"]
# Note: += works not only with lists, but also with numbers (addition), strings (concatenation), etc.

names += ["D", "E"]

# Print the updated list to see the result.
# Now 'names' contains: ["A", "B", "C", "D", "E"]
print(names)

# Two common ways to create an empty list in Python:

# 1. Using square brackets []
#    This is the most common and concise way.
more_names = []

# 2. Using the list() constructor
#    This is equivalent, but a little more explicit.
more_names = list()

# At this point, 'more_names' is an empty list: []

# Create a list that contains different data types.
# In Python, unlike some other languages, lists can hold elements of ANY type.
# Here, our list contains:
#   - an integer: 1
#   - another list: ["hi", "bye"] (yes, lists can even hold other lists!)
#   - a floating-point number: -0.12
#   - the special value None, which represents "nothing" or "no value"

stuff = [1, ["hi", "bye"], -0.12, None]

# Print the list to see its contents.
# Output: [1, ['hi', 'bye'], -0.12, None]
print(stuff)

"""List slicing is a useful way to access a slice of elements in a list."""

numbers = [0, 1, 2, 3, 4, 5, 6]

# A slice extracts a portion of the list.
# Syntax: list[start : end]
#   - The start index is **inclusive** (included).
#   - The end index is **exclusive** (stops right before this index).
# So numbers[0:3] takes elements at index 0, 1, and 2 — but NOT index 3.
# That means we’ll get: [0, 1, 2]

print(numbers[0:3])   # Output: [0, 1, 2]

# When the start index is omitted, Python assumes you mean "from the very beginning".
# So numbers[:3] means: take elements from the start up to index 3 (exclusive).
# That gives us [0, 1, 2].
print(numbers[:3])   # Output: [0, 1, 2]

# When the end index is omitted, Python assumes you mean "all the way to the end".
# So numbers[5:] means: take elements starting at index 5 through the end of the list.
# That gives us [5, 6].
print(numbers[5:])   # Output: [5, 6]

# The slice operator ":" with nothing before or after means "take everything".
# So numbers[:] returns ALL the elements in the list.
# In this simple case, it's basically the same as just writing 'numbers'.
#
# But this becomes VERY useful when working with numpy arrays or multi-dimensional data:
#   - [:] means "all elements"
#   - For 2D arrays, [:, 0] means "all rows, column 0"
#   - For 2D arrays, [0, :] means "row 0, all columns"

print(numbers[:])   # Output: [0, 1, 2, 3, 4, 5, 6]

# Negative indices let you count backwards from the end of the list.
# -1 refers to the LAST element, -2 is the second-to-last, and so on.

# numbers[-1] → last element in the list, which is 6.
print(numbers[-1])    # Output: 6

# numbers[-3:] → slice starting from the 3rd element from the end through the end.
# That gives [4, 5, 6].
print(numbers[-3:])   # Output: [4, 5, 6]

# numbers[3:-2] → slice starting at index 3 (inclusive) and stopping at -2 (exclusive).
# Index 3 is element 3, and -2 means "stop before the second-to-last element".
# So we get [3, 4].
print(numbers[3:-2])  # Output: [3, 4]

"""### Tuples

Tuples are immutable arrays. Let's see how they work.
"""

# In Python, parentheses () are used to create a tuple,
# while square brackets [] are used to create a list.

# A tuple is very similar to a list, but with one big difference:
# - Lists are MUTABLE (you can change, append, or remove elements).
# - Tuples are IMMUTABLE (once created, their contents cannot be changed).

# Here, we create a tuple with two string elements: "A" and "B".
names = ("A", "B")

# Now 'names' is a tuple, not a list.
# If you try to do names.append("Richard"), it will raise an error,
# because tuples do not support modification.

# Tuples and lists share the same syntax for indexing and measuring length.

# Access the first element (index 0) of the tuple.
# Since names = ("A", "B"), names[0] will give "A".
print(names[0])    # Output: A

# The len() function works the same way for tuples as for lists.
# Here, len(names) will return 2 because the tuple has two elements.
print(len(names))  # Output: 2

# Unlike lists, tuples do NOT allow item reassignment.
# Tuples are immutable, meaning once you create them, you cannot change their contents.
# So trying to do this:
names[0] = "C"

# will raise a TypeError:
# TypeError: 'tuple' object does not support item assignment

# Create an empty tuple.
# You can use the tuple() constructor with no arguments to make a tuple with nothing in it.
empty = tuple()
print(empty)   # Output: ()

# Create a tuple with a single item.
# IMPORTANT: you must include a comma after the single element, otherwise Python just sees it as a number in parentheses.
# Without the comma → (10) is just the integer 10, not a tuple.
single = (10,)
print(single)  # Output: (10,)

"""## Dictionary

Dictionaries are hash maps. Let's see how they work.
"""

# Two common ways to create an empty dictionary in Python:

# 1. Using curly braces {}
#    This is the most common and concise way.
phonebook = {}

# 2. Using the dict() constructor
#    This does the same thing in a more explicit way.
phonebook = dict()

# At this point, 'phonebook' is an empty dictionary: {}

# Create a dictionary with one key–value pair.
# In this case: the key is "A" and the value is "12-37".
phonebook = {"A": "12-37"}

# Add another key–value pair to the dictionary.
# Keys must be unique. If the key already exists, this would overwrite the old value.
phonebook["B"] = "34-23"

# Now the dictionary looks like: {"A": "12-37", "B": "34-23"}

# You can check if a key exists in a dictionary using the 'in' keyword.
# This checks only the KEYS (not the values).

# "A" is a key in the phonebook, so this will print True.
print("A" in phonebook)   # Output: True

# "C" is NOT a key in the phonebook, so this will print False.
print("C" in phonebook)   # Output: False

# To get the value associated with a key in a dictionary,
# use square bracket indexing with the key name.

# Here, we look up the value for key "B".
print(phonebook["B"])   # Output: 34-23

# You can remove a key–value pair from a dictionary using the 'del' statement.

# This deletes the entry with key "A" from the dictionary.
del phonebook["A"]

# Print the dictionary to confirm the change.
# Now only {"B": "34-23"} remains.
print(phonebook)

"""## Loops"""

# A basic for-loop in Python.
# The range(5) function generates a sequence of numbers: 0, 1, 2, 3, 4
# (it goes up to 5 but does NOT include 5).

for i in range(5):
    # Each time through the loop, 'i' takes the next value in the range.
    print(i)   # This will print 0, then 1, then 2, then 3, then 4

# You can also use a for-loop to iterate directly over the items in a list.

names = ["A", "B", "C"]

# Each time through the loop, the variable 'name' takes on the next element in the list.
for name in names:
    print(name)   # Prints "A", then "B", then "C"

# To iterate over indices *and* values in a list, you have two common approaches.

names = ["A", "B", "C"]

# Way 1: Use range(len(names)) to loop over the indices.
# Here 'i' will go from 0 → 2, and we use names[i] to access the element.
for i in range(len(names)):
    print(i, names[i])   # Prints: 0 A, then 1 B, then 2 C

print("---")  # Just separates the output for clarity

# Way 2: Use the built-in enumerate() function.
# enumerate(names) gives pairs (index, value).
# This is the more Pythonic (cleaner) way.
for i, name in enumerate(names):
    print(i, name)       # Prints: 0 A, then 1 B, then 2 C

# We can also loop through a dictionary in different ways.

phonebook = {"A": "12-37", "B": "34-23"}

# Iterate over KEYS (this is the default when looping through a dictionary).
# Here, 'name' will take "A", then "B".
for name in phonebook:
    print(name)   # Output: A, B

print("---")

# Iterate over VALUES only.
# The .values() method gives just the dictionary values ("12-37", "34-23").
for number in phonebook.values():
    print(number)   # Output: 12-37, 34-23

print("---")

# Iterate over both KEYS and VALUES at the same time.
# The .items() method gives pairs (key, value).
for name, number in phonebook.items():
    print(name, number)   # Output: A 12-37, then B 34-23

"""## NumPy
NumPy is a Python library, which adds support for large, multi-dimensional arrays and matrices, along with a large collection of optimized, high-level mathematical functions to operate on these arrays.

You may need to install numpy first before importing it in the next cell.

There are many ways to manage your packages, but the workflow we suggest for this class is to use Anaconda.
 - Download Anaconda. Create a conda environment when you work on a new project.
 - Activate your conda environment and install libraries using conda or pip if they are not available in conda.
 - If you are running scripts on command line, run inside your conda environment.
 - If you are using a Jupyter notebook, add your conda environment to your Jupyter notebook: https://towardsdatascience.com/get-your-conda-environment-to-show-in-jupyter-notebooks-the-easy-way-17010b76e874. Create your Jupyter notebook and verify you're in your conda environment kernel (top right of notebook should display the name). If you're not, go to the Kernel tab on the top left and click Change kernel to change to your conda environment kernel.
"""

# Import the NumPy library, which is the fundamental package for scientific computing in Python.
# By convention, we import it as 'np' so we can use shorter names like np.array(), np.mean(), etc.
# NumPy is especially powerful for working with arrays, matrices, and performing fast numerical computations.

import numpy as np

# Create numpy arrays from Python lists

# A 1D array (vector) with 3 elements.
x = np.array([1, 2, 3])

# A 2D array with 1 row and 3 columns.
# Notice the extra square brackets around the list → this makes it 2D.
a = np.array([[1, 2, 3]])

# Another 2D array with 1 row and 3 columns.
y = np.array([[3, 4, 5]])

# A 2D array with 2 rows and 2 columns.
z = np.array([[6, 7],
              [8, 9]])

# Let's inspect their shapes using .shape
# .shape tells us the dimensions of the array (rows, columns).
print(x.shape)   # (3,) → 1D array with 3 elements
print(y.shape)   # (1, 3) → 2D array: 1 row, 3 columns

print()          # Just prints a blank line for readability

print(z)         # Prints the actual array contents
# Output:
# [[6 7]
#  [8 9]]

print(z.shape)   # (2, 2) → 2D array: 2 rows, 2 columns

"""Vectors can be represented as 1-D arrays of shape (N,) or 2-D arrays of shape (N, 1) or (1, N). But it's important to note that the shapes (N,), (N, 1), and (1,N) are not the same and may result in different behavior (we'll see some examples below involving matrix multiplication and broadcasting).

Matrices are generally represented as 2-D arrays of shape (M, N).

The best way to ensure your code gives you the behavior you expect is to keep track of your array shapes and try out small test cases or refer back to documentation when you are unsure.
"""

# Create a NumPy array with values from 0 up to (but not including) 10.
# np.arange(10) gives: [0 1 2 3 4 5 6 7 8 9]
a = np.arange(10)

# Reshape the array into a new shape (5 rows, 2 columns).
# The data stays the same, only the "view" (shape) changes.
# So now it becomes a 2D array:
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]
b = a.reshape((5, 2))

# Print the original 1D array
print(a)

print()   # blank line for readability

# Print the reshaped 2D array
print(b)

"""### Array Operations

There are many NumPy operations that can be used to reduce a numpy array along an axis.

Let's look at the np.max operation (documentation: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html).
"""

# Create a 2D NumPy array (a matrix) with 3 rows and 2 columns.
x = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Print the array.
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
print(x)

print()   # prints a blank line for readability

# Print the shape of the array.
# (3, 2) → 3 rows, 2 columns
print(x.shape)

# np.max finds the maximum value in an array.
# The 'axis' argument controls *how* the maximum is computed:

# axis = 0 → go DOWN the rows (column-wise maximums).
# axis = 1 → go ACROSS the columns (row-wise maximums).

# Since x = [[1 2],
#            [3 4],
#            [5 6]]
# Using axis=1 means: take the maximum value from each row.
# Row 1: max(1, 2) = 2
# Row 2: max(3, 4) = 4
# Row 3: max(5, 6) = 6

print(np.max(x, axis=1))   # Output: [2 4 6]

# Recall: np.max(x, axis=1) gives the row-wise maximums.
# For x = [[1 2],
#          [3 4],
#          [5 6]]
# → np.max(x, axis=1) = [2 4 6]

# Now, let's check the shape of that result.
print(np.max(x, axis=1).shape)

# Output: (3,)
# Explanation:
#   - The result has 3 values (one max per row).
#   - Since it's just a 1D array, its shape is (3,), not (3,1).

# np.max with keepdims=True keeps the reduced dimension as size 1
# instead of collapsing it away into a 1D array.

# Recall:
# x = [[1 2],
#      [3 4],
#      [5 6]]

# np.max(x, axis=1) → [2 4 6]   (shape = (3,))
# With keepdims=True, we get:
# [[2]
#  [4]
#  [6]]   (shape = (3,1))

print(np.max(x, axis=1, keepdims=True))

# Using keepdims=True keeps the dimension we reduced (axis=1) in the result.
# So instead of collapsing to a 1D array, NumPy preserves the 2D structure.

# For x = [[1 2],
#          [3 4],
#          [5 6]]
# np.max(x, axis=1, keepdims=True) gives:
# [[2]
#  [4]
#  [6]]

# Let's check its shape:
print(np.max(x, axis=1, keepdims=True).shape)

# Output: (3, 1)
# Explanation:
#   - 3 rows (one max per row),
#   - 1 column (because keepdims=True keeps the column dimension).

"""Next, let's look at some matrix operations. Let's take an element-wise product (Hadamard product)."""

# Create two 2D NumPy arrays (matrices)
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[3, 3],
              [3, 3]])

print(A)
# [[1 2]
#  [3 4]]

print(B)
# [[3 3]
#  [3 3]]

print("---")

# In NumPy, the * operator does ELEMENT-WISE multiplication (not matrix multiplication).
# That means each element in A is multiplied by the element in the same position in B.

# So:
# [[1*3  2*3]
#  [3*3  4*3]]
# → [[3 6]
#    [9 12]]

print(A * B)

"""We can do matrix multiplication with np.matmul or @."""

# One way to do matrix multiplication in NumPy is with np.matmul().
# This follows the rules of linear algebra:
#   (m x n) @ (n x p) → (m x p)
# So here, A and B are both 2x2, and the result is also 2x2.
print(np.matmul(A, B))

# Another way to do matrix multiplication is using the @ operator (Python 3.5+).
# This is just shorthand for np.matmul(A, B).
print(A @ B)

"""We can take the dot product or a matrix vector product with np.dot."""

# Create two 1D NumPy arrays (vectors).
u = np.array([1, 2, 3])
v = np.array([1, 10, 100])

# np.dot(u, v) computes the dot product of the two vectors.
# Dot product = (1*1) + (2*10) + (3*100)
#             = 1 + 20 + 300
#             = 321
print(np.dot(u, v))   # Output: 321

# You can also call the dot product directly as a method on the array.
# This is the same calculation as above, just a different style.
print(u.dot(v))       # Output: 321

# Create a 2D NumPy array (matrix) with shape (3, 2) → 3 rows, 2 columns
W = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Let's check the shapes of our vectors/matrices.
print(v.shape)   # (3,) → a 1D vector with 3 elements
print(W.shape)   # (3, 2) → a matrix with 3 rows and 2 columns

# Now compute np.dot(v, W).
# Rules of matrix multiplication: (1 x 3) dot (3 x 2) → (1 x 2)
# So our result will be a 1D array with 2 elements.

print(np.dot(v, W))
# Calculation:
# v = [  1,  10, 100 ]
# W = [[1, 2],
#      [3, 4],
#      [5, 6]]
#
# Result = [ (1*1 + 10*3 + 100*5),  (1*2 + 10*4 + 100*6) ]
#        = [ (1 + 30 + 500),        (2 + 40 + 600) ]
#        = [531, 642]

# Let's check the shape of the result.
print(np.dot(v, W).shape)   # (2,) → 1D array with 2 elements

# Let's try the reverse: np.dot(W, v)

# Recall:
# W has shape (3, 2) → 3 rows, 2 columns
# v has shape (3,)   → behaves like (3, 1) for dot products

print(np.dot(W, v))

# We can fix the shape mismatch by transposing W.
# W has shape (3, 2). Transposing (W.T) flips it to (2, 3).
# v has shape (3,) → behaves like (3,1).
# Now the multiplication is valid: (2,3) × (3,1) → (2,1)

print(np.dot(W.T, v))
# Calculation:
# W.T = [[1, 3, 5],
#        [2, 4, 6]]
#
# v   = [  1,  10, 100 ]
#
# Result = [
#   (1*1 + 3*10 + 5*100),
#   (2*1 + 4*10 + 6*100)
# ]
# = [531, 642]

# Check the shape of the result.
print(np.dot(W.T, v).shape)   # (2,) → 1D array with 2 element

"""###  Indexing

Slicing / indexing numpy arrays is a extension of the Python concept of slicing (lists) to N dimensions.
"""

# Create a 2D NumPy array with random values between 0 and 1.
# Shape = (3, 4) → 3 rows, 4 columns
x = np.random.random((3, 4))

# Using [:] selects *all elements* of x.
# For a 2D array, [:] means "all rows, all columns".
# So this simply prints the entire array (same as just print(x)).
print(x[:])

# Selects the 0th and 2nd rows of x.
# np.array([0, 2]) creates an index array → [0, 2].
# The colon (:) means "all columns."
# So this selects rows 0 and 2, and all their columns.
print(x[np.array([0, 2]), :])

print("---")

# Selects the 1st row (remember: Python uses zero-based indexing, so row 1 = the second row).
# Then takes columns 1 through 2 (end index 3 is exclusive).
# So x[1, 1:3] means:
#   - row index 1 (second row),
#   - slice of columns starting at index 1 up to (but not including) index 3.
# This returns a 1D vector with 2 elements from that row.
print(x[1, 1:3])

# Boolean indexing in NumPy:
# Instead of selecting elements by position, we can select them by condition.

# x > 0.5 creates a Boolean mask (an array of True/False values).
# For example, if x = [[0.2, 0.7], [0.9, 0.1]], then
# x > 0.5 → [[False, True], [True, False]]

# When we use this mask inside x[ ... ],
# NumPy returns ONLY the elements where the condition is True.

print(x[x > 0.5])
# Output: A 1D array of all values in x that are greater than 0.5

# Here we add a new axis to our array using np.newaxis.
# Recall: x has shape (3, 4) → 3 rows, 4 columns (2D array).

# x[:, :, np.newaxis] means:
#   - ":" → take all rows
#   - ":" → take all columns
#   - "np.newaxis" → add a new dimension at the end

# So the shape changes from (3, 4) to (3, 4, 1).

print(x[:, :, np.newaxis])

"""### Broadcasting

The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

**General Broadcasting Rules**

When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimensions and works its way left. Two dimensions are compatible when:
- they are equal, or
- one of them is 1 (in which case, elements on the axis are repeated along the dimension)

More details: https://numpy.org/doc/stable/user/basics.broadcasting.html
"""

# Create a 2D array (3x4) filled with random numbers between 0 and 1
x = np.random.random((3, 4))

# Create another array with shape (3,1) → 3 rows, 1 column
y = np.random.random((3, 1))

# Create another array with shape (1,4) → 1 row, 4 columns
z = np.random.random((1, 4))

# --- Broadcasting examples ---

# Adding x (3x4) and y (3x1)
# y has only 1 column, but NumPy automatically "stretches" it across 4 columns
# so that it matches the shape of x.
# This is called broadcasting along dimension 1 (the columns).
s = x + y

# Multiplying x (3x4) and z (1x4)
# z has only 1 row, but NumPy automatically "stretches" it down 3 rows
# so that it matches the shape of x.
# This is broadcasting along dimension 0 (the rows).
p = x * z

# Check the shapes of the arrays after broadcasting.

# x was created as (3,4) → 3 rows, 4 columns
print(x.shape)   # Output: (3, 4)

print()          # just a blank line for readability

# y was created as (3,1) → 3 rows, 1 column
print(y.shape)   # Output: (3, 1)

# s = x + y
# Here y (3,1) was broadcasted to (3,4) before addition.
# So s has the same shape as x: (3,4).
print(s.shape)   # Output: (3, 4)

# Let's check the shapes of x, s, and p.

# x was created as a (3,4) array → 3 rows, 4 columns
print(x.shape)   # Output: (3, 4)

print()          # prints a blank line for readability

# s = x + y
# y had shape (3,1), but it was broadcast across columns → (3,4)
# So s has shape (3,4)
print(s.shape)   # Output: (3, 4)

# p = x * z
# z had shape (1,4), but it was broadcast down rows → (3,4)
# So p also has shape (3,4)
print(p.shape)   # Output: (3, 4)

# Create a 3x3 array filled with zeros
a = np.zeros((3, 3))

# Create a 1x3 array (1 row, 3 columns)
b = np.array([[1, 2, 3]])

print(a)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

print()

# Add a (3x3) and b (1x3).
# NumPy broadcasts b across the 3 rows to match a's shape.
# So it's like adding [1,2,3] to each row of a.
print(a + b)
# Output:
# [[1. 2. 3.]
#  [1. 2. 3.]
#  [1. 2. 3.]]

"""Let's look at a more complex example."""

# Create a 2D NumPy array with random numbers.
# Shape: (3,4) → 3 rows, 4 columns
a = np.random.random((3, 4))

# Create another array with shape (3,1) → 3 rows, 1 column
# This can broadcast across columns when combined with 'a'.
b = np.random.random((3, 1))

# Create a 1D array with 3 elements → shape (3,)
# This behaves differently from (3,1) because it has no explicit column dimension.
c = np.random.random((3,))

"""What is the expected broadcasting behavior for these operations? What do the following operations give us? What are the resulting shapes?"""

# Recall: b has shape (3,1) → 3 rows, 1 column (a column vector)

result1 = b + b.T
# b.T is the transpose of b.
# So if b has shape (3,1), then b.T has shape (1,3).

# When we add (3,1) + (1,3), NumPy broadcasts them into a (3,3) array.
# Each element is the sum of the row value (from b) and the column value (from b.T).

print(b.shape)        # (3, 1)
print(b.T.shape)      # (1, 3)
print(result1.shape)  # (3, 3)
print(result1)

# Recall:
# a has shape (3,4) → 3 rows, 4 columns
# c has shape (3,)  → a flat vector with 3 elements

result2 = a + c
# When we add (3,4) + (3,), NumPy tries to broadcast c.
# But since c is 1D, its shape is treated as (1,3) → this does NOT align with (3,4).
# Broadcasting requires dimensions to either be equal OR one of them to be 1.

print(a.shape)        # (3, 4)
print(c.shape)        # (3,)
print(result2.shape)  # ❌ This will raise a ValueError in NumPy
print(result2)

# Recall:
# b has shape (3,1) → 3 rows, 1 column (a column vector)
# c has shape (3,)  → a 1D vector with 3 elements

result3 = b + c
# NumPy tries to broadcast the shapes (3,1) and (3,).
#
# - (3,1) means 3 rows, 1 column
# - (3,) is treated like (1,3) for broadcasting
#
# Together, (3,1) + (1,3) → broadcast to (3,3)
# So the result is a 3x3 matrix where each row of b
# is added to each column of c.

print(b.shape)        # (3, 1)
print(c.shape)        # (3,)
print(result3.shape)  # (3, 3)
print(result3)

"""### Efficient NumPy Code

When working with numpy arrays, avoid explicit for-loops over indices/axes at all costs. For-loops will dramatically slow down your code (~10-100x).

We can time code using the %%timeit magic. Let's compare using explicit for-loop vs. using numpy operations.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# # The %%timeit "cell magic" is a Jupyter feature.
# # It runs the whole cell multiple times and reports the average execution time.
# # Very useful for performance comparisons.
# 
# # Create a 1000 x 1000 array of random floats between 0 and 1.
# x = np.random.rand(1000, 1000)
# 
# # Loop through rows 100 → 999 (so, 900 rows total).
# for i in range(100, 1000):
#     # Loop through every column in the current row.
#     for j in range(x.shape[1]):   # x.shape[1] = 1000 columns
#         # Add 5 to each element of the array in that row and column.
#         x[i, j] += 5

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# # Again, use Jupyter's %%timeit magic to measure execution speed.
# 
# # Create a 1000 x 1000 array of random numbers between 0 and 1
# x = np.random.rand(1000, 1000)
# 
# # Use advanced (fancy) indexing with np.arange(100,1000).
# # np.arange(100,1000) creates [100, 101, ..., 999].
# # This selects rows 100 through 999 (900 rows total).
# # The ":" means "all columns."
# 
# # Then add 5 to every element in those selected rows.
# x[np.arange(100,1000), :] += 5


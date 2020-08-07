#!/usr/bin/env python
# coding: utf-8

# In[1]:


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
print(quicksort([3,6,8,10,1,2,1]))


# In[2]:


x = 3
print(x + 1)   # Addition
print(x - 1)   # Subtraction
print(x * 2)   # Multiplication
print(x ** 2)  # Exponentiation


# In[3]:


t, f = True, False
print(t and f) # Logical AND;
print(t or f)  # Logical OR;
print(not t)   # Logical NOT;
print(t != f)  # Logical XOR;


# In[4]:


s = "hello"
print(s.capitalize())  # Capitalize a string
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces
print(s.center(7))     # Center a string, padding with spaces
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with anoth
print('  world '.strip())  # Strip leading and trailing whitespace


# In[5]:


xs = [3, 1, 2]   # Create a list
print(xs, xs[2])
print(xs[-1]) 


# In[6]:


xs[2] = 'foo'    # Lists can contain elements of different types
print(xs)


# In[7]:


xs.append('bar') # Add a new element to the end of the list
print(xs) 


# In[8]:


x = xs.pop()     # Remove and return the last element of the list
print(x, xs)


# In[ ]:





# Lecture 1
Today we learned about basics of List, time complexity and Space Complexity

**List:** It is a built-in data type which is equivalent to an array of some other programming language. It is used to store an ordered collection of items of various data types.
- list.append() -  inserts an element in the end of the list
- list.pop() -  removes the item at the given index from the list and returns the removed item. By default it removes the last item of the list.

**Dynamic array in python:**  We don’t need to specify the length of a list beforehand because the size of the python list can be dynamically modified. When we declare a list python automatically allocates a chunk of memory . If this list is filled and we want to add more elements then python will allocate a bigger chunk of memory and copy the contents from the previous list to this new list. 

**Time Complexity:**  Amount of time required to run a task.

 **Big O :**   It represents the number of operations needed in the worst case.
- O(1) = constant time
- O(c * n) or O(n +/- c) or O(n/c) = O(n)
- O(1) + O(n) + O(1) = O(n)

**Space Complexity:**  It represents the size of memory needed to run an algorithm. 
To reverse a n-sized list if I allocate another n-sized list then space complexity will be O(n) 
If I don’t allocate another list then space complexity is O(1)

**In place swap:**  a, b = b, a

**Reversing a list using two pointer approach:**  
```python
a = [2, 1]
front= 0
end = len(a) -1

while front <= end :
    a[front], a[backward] = a[backward], a[front]
    front += 1
    backward -= 1
    print(a)
print(a)
```
 **Time Complexity:**   O(n)  
 
  **Space Complexity:** O(1)


## HomeWork:

I tried to solve this from 2 weeks back. I worked several  hours on this. My last solution’s runtime beated **99.84%** of python3 submissions
- First I tried to brute force the problem. I solved it in the first attempt with a time complexity of O(n^2). Time complexity of this solution was 27% better than others and memory usages beated 80% of other submissions. https://leetcode.com/submissions/detail/517721465/
- Then I tried to improve the solution. I looked at the tips couldn't figure out a way to improve the time complexity. But I found a solution which reduced the runtime and this solution’s runtime was better than 36.58% of python submissions. Memory usages was still the same. https://leetcode.com/submissions/detail/517742728/ 
- Then I saw their solution which was in java. I mimicked their solution in python and my runtime was better than 76% of python submission. https://leetcode.com/submissions/detail/517765799/
- I continued working on the problem. I fine tuned it. At last my solution’s runtime beated **99.84%** of python3 submissions but the memory usages increase. 
 https://leetcode.com/submissions/detail/517774520/







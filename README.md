# Group Theory in Python
Some Group theory classes and functions I've been using in my studies of MATH320@UoA.

## Creating a Group
When creating a new group, it must be provided with a list of group elements in the form of a list, as well as a group binary operation, in the form of a Python lambda function.
```
Z = Group([0, 1, 2, 3, 4, 5], lambda x,y: (x + y) % 6)
```

Hope you enjoy! Feel free to provide any feedback or changes/improvements.

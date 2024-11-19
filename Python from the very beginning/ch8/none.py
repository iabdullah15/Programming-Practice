'''The last statement explains why the is operator is used instead of == when checking for None. Here's a detailed breakdown:

1. Understanding None
None is a special singleton object in Python that represents the absence of a value or a null result.
If a function doesn't explicitly return a value using the return statement, Python automatically returns None.
2. Difference Between is and ==
is: Checks for identity, i.e., whether two references point to the exact same object in memory.
==: Checks for equality, i.e., whether two objects have the same value, regardless of whether they are the same object in memory.
Since None is a singleton (there's only one instance of None in Python), using is is the most appropriate way to check for it. This ensures that you’re checking whether a value is exactly the None object, not just something "equal" to it.

3. Why not use ==?
While == might work for checking None in practice, it's not the recommended way:

Someone could define a custom object or class where == evaluates to True for None, but it isn't actually None.
is ensures you're comparing identities, which avoids such edge cases.'''

a = None
b = None
c = None

print(a is b)  # True, both a and b point to the same None object
print(b is c)  # True, both b and c point to the same None object
print(id(a), id(b), id(c))  # All will have the same memory address
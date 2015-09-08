# Python-Refresher

##General

Why did you choose this subject?
  I chose this subject because it has been many years since I have written code in Python, and I would like a refresher.

How were you first made aware of it?
  Approximately 5 years ago, some collaborators and I programmed a Roomba in Python to follow a basic corrective movement algorithm.

What problem does it solve? How does it solve the problem (conceptually)? Why does one use it?
  It is used to create everything from video games to inventory management systems as it is great for rapid application development.
    -www.pythontutorial.org

What are the alternatives? What is it similar to, if anything?
  Python is “an interpreted, interactive, object oriented programming language” similar in form and function to Pearl and Java programming languages.
    -www.pythontutorial.org

What is the history of this technology? Who built it and why? Who is maintaining it?
  Python was originally created by Guido van Rossum in the late 1980’s and early 1990’s. It is now maintained by be a development team of which Rossum is still an integral part.
    -www.pythontutorial.org

What are the biggest conceptual hurdles (if any) you encountered when researching this?

What resources do you recommend for interested students?
  www.pythontutorial.org is a great reference for finding different kinds of Python tutorials/refreshers.

What article or forum was most helpful to you in learning this?
  www.sthurlow.com offers a great refresher tutorial to reconnect with the syntax and basic concepts, ranging from installation to error handling.

What are 3 interview questions one might be asked about this technology?

Use:
  Download stable release of Python.
    Check version with terminal 'python -V'
  Run .py extension files by first typing 'python'.
    e.g. 'python helloworld.py'

##Interview Question 1
What will be the output of the code below? Explain your answer.
```
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
```
How would you modify the definition of extendList to produce the presumably desired behavior?

###Answer
Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:
```
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
```
With this revised implementation, the output would be:
```
list1 = [10]
list2 = [123]
list3 = ['a']
```
  -http://www.toptal.com/python/interview-questions

##Interview Question 2
What will be the output of the code below? Explain your answer.
```
def multipliers():
    return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]
```
How would you modify the definition of multipliers to produce the presumably desired behavior?

###Answer
The output of the above code will be [6, 6, 6, 6] (not [0, 2, 4, 6]).

The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by multipliers() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by 3, so since a value of 2 is passed in the above code, they all return a value of 6 (i.e., 3 x 2).

(Incidentally, as pointed out in The Hitchhiker’s Guide to Python, there is a somewhat widespread misconception that this has something to do with lambdas, which is not the case. Functions created with a lambda expression are in no way special and the same behavior is exhibited by functions created using an ordinary def.)

Below are a few examples of ways to circumvent this issue.

One solution would be use a Python generator as follows:
```
def multipliers():
     for i in range(4): yield lambda x : i * x
```
Another solution is to create a closure that binds immediately to its arguments by using a default argument. For example:
```
def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]
```
Or alternatively, you can use the functools.partial function:
```
from functools import partial
from operator import mul

def multipliers():
    return [partial(mul, i) for i in range(4)]
```
  -http://www.toptal.com/python/interview-questions

##Interview Question 3
What will be the output of the code below? Explain your answer.
```
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x
```

###Answer
The output of the above code will be:
```
1 1 1
1 2 1
3 2 3
```
What confuses or surprises many about this is that the last line of output is 3 2 3 rather than 3 2 1. Why does changing the value of Parent.x also change the value of Child2.x, but at the same time not change the value of Child1.x?

The key to the answer is that, in Python, class variables are internally handled as dictionaries. If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an AttributeError occurs).

Therefore, setting x = 1 in the Parent class makes the class variable x (with a value of 1) referenceable in that class and any of its children. That’s why the first print statement outputs 1 1 1.

Subsequently, if any of its child classes overrides that value (for example, when we execute the statement Child1.x = 2), then the value is changed in that child only. That’s why the second print statement outputs 1 2 1.

Finally, if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), that change is reflected also by any children that have not yet overridden the value (which in this case would be Child2). That’s why the third print statement outputs 3 2 3.
  -http://www.toptal.com/python/interview-questions

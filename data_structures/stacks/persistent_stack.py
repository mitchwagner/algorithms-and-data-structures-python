'''
Implements an immutable stack.

Define a stack recursively as follows: a stack is either the
empty tuple, or a tuple (x, n), where e is the top element of the
stack, and n is a pointer to another stack.

Note: we can't really help Python's mutability; a tuple's elements
cannot be modified, but if they are references, the data pointed at
certainly can be.

Note: right now, this will result in an error when one pops or tops the
empty stack. If we want to avoid this, we need conditional logic...
if we want to make it efficient, we also have to efficiently track
the size of the stack.

Kevlin Henney shows an interesting way around the conditional
logic in his talk "Refactoring to Immutability": have an
interface "Stack" and have NonEmptyStack and EmptyStack implement
it. Polymorphism handles the conditional logic (no IF
statements)!

Unfortunately, he still throws exceptions when a stack is empty.
I much prefer the Haskellian approach of not interrupting control
flow for such an anticable case. It's better for top and pop to
return Maybe Stacks.

Note:
It's also interesting to observe the different calling conventions.

The functional design, e.g.,

    push(pop(push(push(push(create())))))

is what this implementation results in. Henney's object-oriented
approach winds up looking more like

    create().push().push().push().pop().push()

Which of these is better would seem to be a matter of taste. The
first is analagous to peering into a stack, while the latter is
analgous to watching it be constructed.
'''

from collections import namedtuple

Stack = namedtuple('Stack', ['x', 'n'])

def create(x, n=()):
    return Stack(x, n)


def top(s):
    return s.x


def pop(s):
    return s.n


def push(x, s):
    return create(x, s)

print("STACK FRAME VISUALIZER")

#1: LINEAR RECURSION
def linear_recursion(n):
    if n == 0:
        return #return means exit the function and go back to the previous stack frame
    print("Linear call at level:", n)
    linear_recursion(n - 1)

print("\nLinear Recursion")
linear_recursion(5)


#2: TAIL RECURSION
# Tail recursion does the work first. The recursive call is the last step.
def tail_recursion(n):
    if n == 0:
        return
    print("Tail work before call:", n)
    tail_recursion(n - 1)

print("\nPART 2: Tail Recursion")
tail_recursion(5)


#3: HEAD RECURSION
#Head recursion calls itself first. The work happens while the call stack unwinds.
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print("Head work after call:", n)

print("\nHead Recursion")
head_recursion(5)

#4: INCREASING-DECREASING RECURSION
#This prints while going down and again while coming back.
def increasing_decreasing(n):
    if n == 0:
        return

    print("Going down:", n)
    increasing_decreasing(n - 1)
    print("Coming back:", n)

print("\nIncreasing-Decreasing Recursion")
increasing_decreasing(5)


#5: TREE RECURSIO
# Tree recursion makes more than one recursive call at each level.
def tree_recursion(n):
    if n == 0:
        return

    print("Tree node:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)


print("Tree Recursion")
tree_recursion(3)

print("\nRECURSION PATTERN SUMMARY")
print("Linear Recursion: One recursive call at each level.")
print("Tail Recursion: Work happens before the recursive call.")
print("Head Recursion: Work happens after the recursive call.")
print("Increasing-Decreasing: Work happens before and after the call.")
print("Tree Recursion: More than one recursive call at each level.")
'''mysum('abc', 'def') will be the string abcdef, and the result of mysum([1,2,3], [4,5,6]) 
will be the six-element list [1,2,3,4,5,6]. Of course, it should also still return 
the integer 6 if we invoke mysum(1,2,3).'''
def mysum(*seq):
    if not seq:
        return seq
    output = seq[0]
    for item in seq[1:]:
        output += item
    return output

# print(mysum('abc', 'def'))
# print(mysum([1,2,3],[4,5,6], 'abc'))
# print(mysum(5,6))
# print(mysum())
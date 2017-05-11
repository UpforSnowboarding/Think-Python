def recurse(n,s):

    if n == 0:
        print(s)
    else:
        recurse(n-1, n + s)

recurse(-1, 0)

"""
recurse(3, 0) results in calling recurse (3 - 1, 3 + 0) --> recurse (2, 3(s1)). recurse(2, 3) call leads to
recurse (2 - 1, 3 + 2) --> recurse (1, 5(s2). recurse (1,5) leads to calling recurse (1-1, 5 + 1) --> recurse(0,6(s3)).
With the if == 0, the recursion stops and prints s which is 6 which is the result of (s3).
"""

# 1) recurse(-1, 0) would lead to infinite recursion calls resulting in a recursionerror.

# 2) see above comments in triple quotes.

import sys, math

nums = map(int, sys.stdin.readlines()[1:])
gauss = lambda x: (x/2.0)*(1+x)
total = gauss(len(nums)-1)

a = max(nums)
nums.remove(a)
b = max(nums)
nums.remove(b)

if a == b:
    cnt = gauss(1 + nums.count(a))
else:
    cnt = 1 + nums.count(b)

shit_fmt = lambda x: math.floor(x*100.0)/100.0  # b/c hackerrank is dumb.
print '{:.2f}'.format(shit_fmt(cnt/total))
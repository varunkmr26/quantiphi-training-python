import textwrap
def merge_the_tools(string, k):
    # your code goes here
    arr = textwrap.wrap(string,k)
    results = []
    for ss in arr:
        ss = list(ss)
        a = []
        for i in ss:
            if i not in a:
                a.append(i)        
        results.append("".join(a))
    for result in results:
        print result
    return

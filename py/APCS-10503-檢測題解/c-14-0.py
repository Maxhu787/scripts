#1050305-14


def foo(i):
    print("foo",i)
    if (i <= 5):
        print("foo:  %d\n"  %i)
    else:
        bar(i-10)
    return

def bar(i):
    print("bar",i)
    if (i <= 10):
        print("bar:  %d\n"  %i)
    else:
        foo(i-5)
    return

#main
foo(15106)  # recursive stack  
# bar(3091)  # recursive stack  
# foo(6693)  # recursive stack  

# foo(106)
# bar(91)
# foo(93)



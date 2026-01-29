def pattern(n):
    if(n==0):
        return # agr kesi function m return dhika toh wo function ke call wahi over ho jai ge
    print("*" * n)
    pattern(n-1)

pattern(3)
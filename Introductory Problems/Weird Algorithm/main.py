# CSES - Introductory Problems - Weird Algorithm #

def main(n):
    output = [n]
    
    if n == 1: return output
    
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = n * 3 + 1
        output.append(n)
        
    return output


if __name__ == '__main__':
    n = int(input())
    output = main(n)
    print(*output, sep=' ')
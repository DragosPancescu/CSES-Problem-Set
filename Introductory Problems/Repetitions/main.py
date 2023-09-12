# CSES - Introductory Problems - Repetitions #

def main(dna):
    cur_len, max_len = 1, 0
    
    if len(set(dna)) == 1:
        return len(dna)
    
    for idx in range(1, len(dna)):
        if dna[idx] != dna[idx - 1]:
           max_len = max(max_len, cur_len)
           cur_len = 0
        
        cur_len += 1
        
    return max(max_len, cur_len)

if __name__ == '__main__':
    dna = input()

    output = main(dna)
    print(output)
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character;
    string = ''.join(l);
    return string
string = input()
line = input().split()
i, c = int(line[0]), line[1]
print(string[:i] + c + string[i+1:])
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
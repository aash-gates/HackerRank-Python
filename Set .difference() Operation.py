E = int(raw_input())
English = set(raw_input().split())

F = int(raw_input())
French = set(raw_input().split())

print len(English - French)
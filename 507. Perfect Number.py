#filename = "D:\\Программирование\\Python\\Однострочники-Python\\input.txt"
## Старый код
# f = open(filename)
# lines = []
# for line in f:
#     lines.append(line.strip())

# print(lines)

## Новый код
print([line.strip() for line in open("D:\\Программирование\\Python\\Однострочники-Python\\input.txt")])
## Старый код)])
def progress(n):
    d = 2
    a = 5
    return a + n * d

if __name__ == '__main__':
    while True:
        a = int(input("Введіть номер шуканого елементу: "))
        print(a,"й елемент прогресії = ",progress(a))
   


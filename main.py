import os

def main():
    with open("file.txt", "r") as f:
        output = f.readlines()
    output[0] = 'testing'
    with open("file.txt", "w") as f:
        f.writelines(output)

if __name__ == '__main__':
    main()

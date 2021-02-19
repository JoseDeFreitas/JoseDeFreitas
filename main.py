import os

def main():
    with open("file.txt", "r") as f:
        output = f.readlines()
    for i, j in enumerate(output):
        if j.startswith("---"):
            output[i] = i.upper()
    with open("file.txt", "w") as f:
        f.writelines(output)

if __name__ == '__main__':
    main()

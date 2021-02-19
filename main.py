import os

def main():
    if not os.path.isdir("generated"):
        os.mkdir("generated")
    with open("templates/overview.txt", "r") as f:
        output = f.readlines()
    output[0] = 'testing'
    with open("generated/overview.txt", "w") as f:
        f.writelines(output)

if __name__ == '__main__':
    main()

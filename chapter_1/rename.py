import os

for filename in os.listdir(os.getcwd()):
    if filename == "__pycache__":
        pass
    filename2 = filename.split(".py")
    filename2 = list(filename2[0])
    print(filename2)
    for i in range(len(filename2)):
        if filename2[i] == "-" or filename2[i] == ".":
            filename2[i] = "_"
    filename2 = filename2 + [".py"]
    filename3 = "".join(filename2)
    # print(filename)
    os.rename(filename, filename3)

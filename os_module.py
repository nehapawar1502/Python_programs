import os
# os.mkdir("data")


# for i in range(0, 10):
#     os.mkdir(f"data/Day{i+1}")

# for i in range(0, 10):
#     os.rename(f"data/Tutorial-{i+1}",f"Data/Tutorial-{i+1}")
    
# for i in range(1,4):
#     os.mkdir(f"data/Tutorial-1/day{i+1}")

folders = os.listdir("data")

print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    
print(os.getcwd())


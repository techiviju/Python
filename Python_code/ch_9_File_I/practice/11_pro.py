# 11. Write a python program to rename a file to “renamed_by_ python.txt.
import os

# with open("old.txt") as f:
#     content=f.read()

# with open("rename_old.txt","w") as f:
#     f.write(content)

        # Or

current_file="old.txt"
renamed_file="re_old.txt"

command=f"mv {current_file} {renamed_file}"
print(f"Command is {command}")

# os.system(command)

create="create.txt"

# Fire any command to your system

# command2=(f"touch {create}")
# os.system(command2)

# command3=(f"sudo apt-get update -y")
# os.system(command3)


command3=(f"ps aux | grep chromium")
os.system(command3)
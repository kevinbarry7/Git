import os
import glob

output_file = open('hello.txt', 'w')
lines_to_write = [
	"This is the file.\n",
	"There are many like it.\n",
	"but this one is mine.",
]
output_file.writelines(lines_to_write)
output_file.close()

output_file = open('hello.txt', 'a')
output_file.writelines("\nNON SEQUITUR")
output_file.close()


# reading from a file

input_file = open('hello.txt', 'r')
# print(input_file.readlines())
for line in input_file.readlines():
	print(line, end='')
input_file.close()

# alternate reading method
with open('hello.txt', 'r') as input_file:
	for line in input_file.readlines():
		print(line)

with open('hello.txt', 'r') as source, open('hi.txt', 'w') as dest:
	for line in source.readlines():
		dest.write(line)

# File Operations
path = "/users/kevin/test-repo/python-basics-exercises/test_directory"
# os.mkdir("test_directory")
# os.mkdir(os.path.join(path, "test_directory"))
# os.rmdir(os.path.join(path, "test_directory"))
print(os.listdir(path))

# for file_name in os.listdir(path):
# 	if file_name.lower().endswith(".gif"):
# 		full_path = os.path.join(path, file_name)
# 		new_file_name = full_path[:-4] + "_backup.py"
# 		os.rename(full_path, new_file_name)

print(glob.glob("*.txt"))

# possible_files = os.path.join(path, "*.py")
# for file_name in glob.glob(possible_files):
# 	full_path = os.path.join(path, file_name)
# 	new_file_name = full_path[:-4] + "+backup.gif"
# 	os.rename(full_path, new_file_name)

for current_folder, subfolders, file_names in os.walk(path):
	for file_name in file_names:
		print(os.path.join(current_folder, file_name))




f = open("D:\\testt\sample3.txt","w")
f.write("This is my file")
# print(str2)cmd
f.close()


a = "Hello"
b = "World"
print(a or b)

"""Modes & Description
r---Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

rb---Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
This is the default mode.
 
r+---Opens a file for both reading and writing.
The file pointer placed at the beginning of the file.
 
rb+---Opens a file for both reading and writing in binary format.
The file pointer placed at the beginning of the file.
 
w---Opens a file for writing only. Overwrites the file if the file exists.
If the file does not exist, creates a new file for writing.
 
wb---Opens a file for writing only in binary format. Overwrites the file if the file exists.
If the file does not exist, creates a new file for writing.

w+---Opens a file for both writing and reading. Overwrites the existing file if the file exists.
If the file does not exist, creates a new file for reading and writing.
 
wb+---Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists.
If the file does not exist, creates a new file for reading and writing.
 
a---Opens a file for appending. The file pointer is at the end of the file if the file exists.
That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

ab---Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists.
That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
 
a+---Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists.
The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

ab+---Opens a file for both appending and reading in binary format.
The file pointer is at the end of the file if the file exists. The file opens in the append mode.
If the file does not exist, it creates a new file for reading and writing.
"""
# Read the Contents of the file
f = open("D:\\testt\hello.txt","r")
print(f.read())
print(f.readable())  # it will show boolean value like true or false
print(f.writable()) # it will show boolean value like true or false
print(f.mode)
f.close()

"""
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""
"""a will append to the end of the file
f = open("D:\\testt\hello.txt","a")
f.write("Wecoming you all to this program")
f.close()"""

# w will overwrite the contents of the file
f = open("D:\\testt\sample.txt","w")
f.write("This is training session")
f.close()

f = open("D:\\testt\sample2.txt","a")
abc = ["Hai", "Hello", "Welcome"]
f.writelines(abc)

"""#  x for exclusive file creation if the file already exists operation failes
f = open("D:\\testt\exercise.txt","x")
f.write("This is exclusively created file")
f.close()"""

# w+ indicates both read and write for Python create file operation
f = open("D:\\testt\sample.txt","w+")
f.write("Hai all What's going on")
f.read()
f.close()

# r+ Opens a file for reading and writing
f = open("D:\\testt\sample2.txt","r+")
f.write("This is the new file")
f.read()
f.close()

# a+ Opens a new file and write the content in to the file
f = open("D:\\testt\sample5.txt","a+")
f.write("This is the new file")
f.read()
f.close()

# a+ opens the already existing file and add the contents in the file
f = open("D:\\testt\sample3.txt","a+")
f.write("Overwrite the content in the file")
f.read()
f.close()



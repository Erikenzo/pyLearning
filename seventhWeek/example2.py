#this is a comment 1

"""
Script should return 7
"""

def reading_file_v1(filename):
    with open(filename) as file:
        code_lines_count = 0
        for line in file:
            if not (line.startswith("#") or line.startswith(" #") or line.startswith(" ")) and line.lstrip():
                code_lines_count += 1
    print(code_lines_count)

file_pages = {}

for name_file in "1.txt", "2.txt", "3.txt":
    with open(name_file, "r", encoding="utf-8") as file:
        count_pages = len(file.readlines())
        file_pages[name_file] = count_pages

file_pages = sorted(file_pages.items(), key=lambda x: x[1])

for name, count_pages in file_pages:
    with open("total.txt", "a", encoding="utf-8") as file:
        file.write(name + "\n")
        file.write(str(count_pages) + "\n")
        file.flush()
        with open(name, "r", encoding="utf-8") as old_file:
            data = old_file.read()
        file.write(data + "\n")

# task 1 - porovnání řádků dvou souborů
print("---------------TASK 1---------------------")
f = open ("file1.txt", "w")
f.write("Hello world file")
f.close()

f2 = open ("file2.txt", "w")
f2.write("Hello world file 2\nHello world file 2 ")
f2.close()

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()  
        lines2 = f2.readlines()
        

    for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        if line1.strip() != line2.strip():  
            print(f"Mismatch on line {i}:")
            print(f"File1: {line1.strip()}")
            print(f"File2: {line2.strip()}")

    
    
    if len(lines1) != len(lines2):
        print("The files have a different number of lines.")


compare_files('file1.txt', 'file2.txt')


#task 2 - statistika souboru
print("---------------TASK 2---------------------")

f3 = open("source.txt", "w")
f3.write ("fneihroigghghpi grwagr25g56688heheo jrogjrogj grogrggrl575grglrmkgg5ggrlgr45grsglú")
f3.close()
f3 = open("source.txt", "r")
data = f3.read()
print(data)


def write_statistics(input_file, output_file):
    with open(input_file, 'r') as f4:
        content = f4.read()  

    
    num_chars = len(content)  # Počet znaků
    num_lines = content.count('\n') + 1  # Počet řádků (počítáme konce řádků)
    num_vowels = sum(1 for char in content.lower() if char in 'aeiou')  # Počet samohlásek
    num_consonants = sum(1 for char in content.lower() if char.isalpha() and char not in 'aeiou')  # Počet souhlásek
    num_digits = sum(1 for char in content if char.isdigit())  # Počet číslic

    # Zápis do souboru
    with open(output_file, 'w') as f_out:
        f_out.write(f"Number of characters: {num_chars}\n")
        f_out.write(f"Number of lines: {num_lines}\n")
        f_out.write(f"Number of vowels: {num_vowels}\n")
        f_out.write(f"Number of consonants: {num_consonants}\n")
        f_out.write(f"Number of digits: {num_digits}\n")

# Test funkce
write_statistics('source.txt', 'statistics.txt')
f5 = open ("statistics.txt", "r")
data2 = f5.read()
f5.close()
print(data2)

# task 3 - odstraneni posledniho radku
print("---------------TASK 3---------------------")

def remove_last_line(input_file, output_file):
    with open(input_file, 'r') as f6:
        lines = f6.readlines()  # Načte všechny řádky

    # Zápis všech řádků kromě posledního
    with open(output_file, 'w') as f2_out:
        f2_out.writelines(lines[:-1])  # Všechny kromě posledního řádku

# Test funkce
remove_last_line('text1.txt', 'text2_bez_radku.txt')

f7 = open ("text2_bez_radku.txt", "r")
data3 = f7.read()
f7.close()
print(data3)

#task 4 - delka nejdelsiho radku

print("---------------TASK 4---------------------")


def longest_line_length(input_file):
    with open(input_file, 'r') as f8:
        max_length = max(len(line.strip()) for line in f8) 
    return max_length

# Test funkce
print(f"The longest line has: {longest_line_length('text1.txt')} characters.")  

# task 5 - pocet vyskytu slova

print("---------------TASK 5---------------------")


def count_word_occurrences(input_file, word):
    with open(input_file, 'r') as f9:
        content = f9.read().lower()  
    return content.count(word.lower())  


word_to_find = "ahoj"
print(f"pocet slov {word_to_find} je {count_word_occurrences('source2.txt', word_to_find)}")


# task 6 - najit a nahradit

print("---------------TASK 6---------------------")

def find_and_replace(input_file, old_word, new_word, output_file):
    with open(input_file, 'r') as f10:
        content = f10.read()  

    
    updated_content = content.replace(old_word, new_word)

    
    with open(output_file, 'w') as f3_out:
        f3_out.write(updated_content)


old = "ahoj"
new = "******"
find_and_replace('source2.txt', old, new, 'output_find_replace.txt')
f11 = open("output_find_replace.txt", "r")
data4 = f11.read()
f11.close()
print(data4)


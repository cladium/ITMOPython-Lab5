import re
import csv


def first_task(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    words_starting_with_c = re.findall(r"\b[cC]\w*", text)
    words_preceded_by_the = re.findall(r"\b[tT]he\s+(\w+)", text)
    print("Words starting with 'c':")
    for w in set(words_starting_with_c):
        print(w, end=" ")
    print("\n\nWords preceded by 'the':")
    for w in set(words_preceded_by_the):
        print(w, end=" ")
    print()


def second_task(filename):
    with open(filename, "r", encoding="utf-8") as file:
        html_content = file.read()
    font_family_pattern = r"font-family\s*:\s*([^;]+);"
    matches = re.findall(font_family_pattern, html_content, re.IGNORECASE)
    # print only unique font names
    print(f"Fonts in {filename}:")
    for f in set(matches):
        print(f)


def third_task(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    id_pattern = re.compile(r"\b\d+\b")
    last_name_pattern = re.compile(r"\b[A-Za-z]+\b")
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-z0-9]+\.[a-z]{2,63}")
    date_pattern = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")  # YYYY-MM-DD format
    website_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )

    ids = id_pattern.findall(content)
    last_names = last_name_pattern.findall(content)
    emails = email_pattern.findall(content)
    dates = date_pattern.findall(content)
    websites = website_pattern.findall(content)

    # prepare the data in the correct order
    min_length = min(len(ids), len(last_names), len(emails), len(dates), len(websites))
    data = []
    for i in range(min_length):
        data.append([ids[i], last_names[i], emails[i], dates[i], websites[i]])

    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Last Name", "Email", "Registration Date", "Website"])
        writer.writerows(data)

    print("Data has been successfully written to output.csv")


def main():
    first_task("task1-en.txt")
    print()
    second_task("task2.html")
    print()
    third_task("task3.txt")


if __name__ == "__main__":
    main()

from genericpath import exists
import click
import os
import os.path
import csv
import re
from collections import defaultdict
from prettytable import PrettyTable


@click.command()
@click.option('--dir', default="package")
def main(dir):
    if(os.path.exists(os.getcwd()+f'\{dir}') == False):
        print("Could not find the package directory! Make sure its in the project folder and is unzipped into one \"package\" folder.")
        return

    messages = defaultdict(int)
    emojisUsed = defaultdict(int)
    mentionedUsers = defaultdict(int)
    cumulativeChars = 0
    cumulativeWords = 0

    for path, _, files in os.walk(dir+"\messages"):
        for name in files:
            if name.endswith(".csv"):
                with open(os.path.join(path, name), "r", encoding='cp437') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        date = re.match(r'\d{4}-\d{2}-\d{2}', row[1])[0]
                        messages[date] += 1

                        emojis = re.findall(r'<:\w+:[0-9]+>', row[2])
                        if emojis:
                            for match in emojis:
                                emojisUsed[match] += 1

                        mentions = re.findall(r'<@!*&*[0-9]+>', row[2])
                        if mentions:
                            for match in mentions:
                                mentionedUsers[match] += 1

                        cumulativeChars += len(row[2])
                        cumulativeWords += len(re.findall(r'\w+', row[2]))

    cumulativeMessages = sum(messages.values())

    table = PrettyTable(['Stat', 'Value'])

    table.add_row(
        ['Cumulative Messages', f'{"{:,}".format(cumulativeMessages)} messages, {"{:,}".format(cumulativeWords)} words'])
    table.add_row(['Average Message Length',
                  f'{str(round(cumulativeWords/cumulativeMessages, 2))} words, {str(round(cumulativeChars/cumulativeMessages, 2))} characters'])

    table.add_row(
        ["Chattiest Day", f'{max(messages, key=messages.get)} ({max(messages.values())} messages)'])

    if len(emojisUsed) > 0:
        table.add_row(
            ["Most Used Emoji", f'{max(emojisUsed, key=emojisUsed.get)} ({max(emojisUsed.values())} uses)'])
    table.add_row(["Most Mentioned User",
                  f'{max(mentionedUsers, key=mentionedUsers.get)} ({max(mentionedUsers.values())} mentions)'])

    print(table)
    print("Due to certain limitations on Discord's end, only id's can be printed for the values of some rows.")


if __name__ == '__main__':
    main()

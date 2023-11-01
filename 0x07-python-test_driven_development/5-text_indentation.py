#!/usr/bin/python3
"""
This prints text identification.
"""


def text_indentation(text):
    """
    Print a text with two new lines after each '.', '?', and ':' characters.

    :param text: The input text as a string.
    :raises TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            print()
            continue

        words = line.split()
        output_line = words[0]

        for word in words[1:]:
            if word.endswith(('.', '?', ':')):
                output_line += ' ' + word
                print(output_line)
                output_line = ""
            else:
                output_line += ' ' + word

        if output_line:
            print(output_line)


if __name__ == "__main__":
    text_indentation("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

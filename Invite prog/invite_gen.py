import csv

with open('save_the_date.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if row[2] == 'y':
            if row[1] == 'A1':
                paragraph = '''Dear [Guest's Name],

We are thrilled to announce and invite you to join us for the joyous occasion of our Solemnisation and Wedding dinner!

🗓️ Date: 28 July 2024
📍 Venue: Marina Bay Sands Ballroom

We would love to share this momentous occasion with our families, and your presence will add immense happiness to our celebration!

To assist with our event planning, please let us know if you will be attending. Formal invitations with detailed information will follow soon. Until then, mark your calendar, and we can't wait to start the countdown!

With love,
Jasper & Rachel'''

        
            elif row[1] == 'A2':
                paragraph = '''Dear [Guest's Name],

We are thrilled to announce and invite you to join us for the joyous occasion of our Solemnisation and Wedding dinner!

🗓️ Date: 28 July 2024
📍 Venue: Marina Bay Sands Ballroom

We would love to share this momentous occasion with our families, and your presence will add immense happiness to our celebration!

To assist with our event planning, please let us know if you will be attending with your plus one. Formal invitations with detailed information will follow soon. Until then, mark your calendar, and we can't wait to start the countdown!

With love,
Jasper & Rachel'''

            elif row[1] == 'B1':
                paragraph = '''Dear [Guest's Name],

We are thrilled to announce and invite you to join us for the joyous occasion of our Wedding dinner!

🗓️ Date: 28 July 2024
📍 Venue: Marina Bay Sands Ballroom

You have been of significant value in our lives and your presence will add immense happiness to our celebration on this day!

To assist with our event planning, please let us know if you will be attending. Formal invitations with detailed information will follow soon. Until then, mark your calendar, and we can't wait to start the countdown!

With love,
Jasper & Rachel'''

            elif row[1] == 'B2':
                paragraph = '''Dear [Guest's Name],

We are thrilled to announce and invite you to join us for the joyous occasion of our Wedding dinner!

🗓️ Date: 28 July 2024
📍 Venue: Marina Bay Sands Ballroom

You have been of significant value in our lives and your presence will add immense happiness to our celebration on this day!

To assist with our event planning, please let us know if you will be attending with your plus one. Formal invitations with detailed information will follow soon. Until then, mark your calendar, and we can't wait to start the countdown!

With love,
Jasper & Rachel'''

            updated_paragraph = paragraph.replace("[Guest's Name]", row[0])

            with open(row[0] +'.txt', 'w') as file:
                    file.write(updated_paragraph)
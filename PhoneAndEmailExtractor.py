#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses based on the clipboard (ctrl+C).

import pyperclip
import re 

# Code below is regex for phone number 
phoneNumberForRegex = re.compile(r'''(
   (\d{3}|\(\d{3}\))?                 # area code
   (\s|-|\.)?                         # separator
   (\d{3})                            # 3 digits
   (\s|-|\.)?                         # separator
   (\d{4})                            # 4 digits
   (\s*(ext|x|ext.)\s*(\d{2,5}))?     # ext
   )''', re.VERBOSE)

# Code below is regex for email (username + @ + domain + .co,.com.edu in VERBOSE Format)
emailForRegex = re.compile(r'''(
   ([a-zA-Z0-9_\-\.]) +                     # username
   @ +                                      # @
   [a-zA-Z0-9_\-\.] +                       # domain name
   (\.[a-zA-Z]{2,5})                        # Looking for 2 to 5 characters according to the Regex syntax
   )''', re.VERBOSE)                         

# Below code will find matches in clipboard text (pyperclip).
text = str(pyperclip.paste())
matches = []

for groups in phoneNumberForRegex.findall(text):
   phoneNumber = '-'.join([groups[1],groups[3], groups[5]])
   if groups[8] != '':
      phoneNumber += ' x' + groups[8]
   matches.append(phoneNumber)

for groups in emailForRegex.findall(text):
   matches.append(groups[0])

#Copy results to clipboard

#If the length of the matches variable it greater than 0 then the first statement runs
#Paste the text and the code will run through and find the matches via regex   
if len(matches) > 0:
   pyperclip.copy('\n'.join(matches))
   print('Copied to Clipboard:')
   print('\n'.join(matches))
else:
   print('No phone numbers or emails found.')

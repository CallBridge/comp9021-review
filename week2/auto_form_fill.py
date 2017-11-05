'''
运行相关程序的时候需要install两个module，一个是PyPDF2，另一个是pyautogui，方法如下：

pip3 install PyPDF2
pip3 install pyobjc-core
pip3 install pybojc
pip3 install pyautogui
实际上打开这个程序的python源文档，并不难理解，大部分是字符串操作。

作者：Sisyphus235
链接：http://www.jianshu.com/p/a036a8a14a4c
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
'''
I agree with KEDAIBIAO, it is quite a easy work with no challenages there.
Although I think it could be quite useful sometimes.
So I will add some notations on Martin's code
'''
import os.path
import sys
import os
import datetime
import time

import PyPDF2
import pyautogui

#
program_authority_name = 'Eric Martin'
# delay time before the focus injection start, second as time unit
sleeping_time = 5
# the name of source
original_form_name = 'Academic_Standing_Interview_Form.pdf'
# judge if the file exist in current path
if not os.path.isfile(original_form_name):
    print(f'I could not find {original_form_name}. Giving up...')
    sys.exit()
# information 1 sid
student_number = input('What is your student id? ')
if student_number.startswith('z'):
    student_number = student_number[1: ]
if not student_number.isdigit() or len(student_number) != 7:
    print('Incorrect student number, giving up...')
    sys.exit()
student_id = 'z' + str(student_number)
form_name = student_id + '_' + original_form_name
# judge if the information has been stored by file name
if os.path.isfile(form_name):
    print(f'There is already a file named {form_name}. Giving up...')
    sys.exit()
# information 2
family_name = input('What is your family name? ')
# information 3
given_names = input('What are your given names? ')
# information 4
program = input('What is your program/plan? ')
# information 5
phone_number = input('What is your phone number? ')
# information 6
academic_standing_level = input('What is your academic standing level? ')
# information 7 get current time using now()
date = datetime.datetime.now()
# Assumes that academic standing interviews for poor results in session 1
# always and exclusively take place between June and September.
if 5 < date.month < 10:
    semester_and_year = 'Semester 1, ' + str(date.year)
else:
    semester_and_year = 'Semester 2, ' + str(date.year - 1)
submission_date = date.strftime('%d/%m/%y')
try:
    #  using pyPDF2 to duplicate the pdf file
    with open(form_name, 'wb') as output_file:
        original_pdf = PyPDF2.PdfFileReader(original_form_name)
        new_pdf = PyPDF2.PdfFileWriter()
        new_pdf.addPage(original_pdf.getPage(0))
        new_pdf.addPage(original_pdf.getPage(1))
        new_pdf.write(output_file)
except FileNotFoundError:
    print(f'Could not open {form_name}. Giving up...')
    sys.exit()
print(f'\nOpen the file {form_name}.')

print('When you are ready to position the mouse above the Student ID field')
input(f'within {sleeping_time} seconds (not moving the mouse then), press return... ')
time.sleep(sleeping_time)
student_id_field = pyautogui.position()

pyautogui.click(student_id_field[0], student_id_field[1], clicks = 2)
# through tab to switch to next form cell
pyautogui.typewrite(student_id + '\t' +  family_name + '\t' + given_names + '\t' +  program + '\t' +
                                              phone_number + '\t' + academic_standing_level + '\t' +
                                           semester_and_year + '\t' * 3 + submission_date + '\t' * 9
                   )
print('\nI assume student has provided type of issue and reasons for poor performance,')
print('and advisor has provided recommendation and comments.')
print('When ready to position the mouse above the program authority name field')
input(f'within {sleeping_time} seconds, press return... ')
time.sleep(sleeping_time)
program_authority_name_field = pyautogui.position()
pyautogui.click(program_authority_name_field[0], program_authority_name_field[1], clicks = 2)
pyautogui.typewrite(program_authority_name + '\t' + submission_date)
print('\nNow save the form. Thanks!')

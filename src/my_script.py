# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())
print("Hello World")

#User Input If Else Example
while True:
    prompt1=input('What is 10 divided by 2?').lower()

    if prompt1 == '5':
       print('Correct, good job!')
    else:
       print('No, the correct answer is 5.')
import streamlit as st
import time
from PIL import Image, ImageDraw

st.write('*This calculator was made by Hania Arif*')
st.write('''
        ### Available Shapes:
        - S - Square
        - R - Rectangle
        ''')
shape = st.text_input('Select a shape:')
if shape == 'S':
    st.write('You have selected a square')
    img = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 90, 90], outline='blue', width=3)
    st.image(img)
    length = st.text_input('Enter length of one side of square:')
    if length:
        try:
             st.write(f'The area of square is: {length} x {length} = {float(length)*float(length)} ')
        except:
             st.write('You did not write a number 😑')


if shape == 'R':
    st.write('You have selected a rectangle')
    img = Image.new('RGB', (200, 100), 'white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 10, 180, 90], outline='blue', width=3)
    st.image(img)
    length = st.text_input('Enter length of one side of rectangle:')
    if length:
        width = st.text_input('Enter width of one side of rectangle:')
        if width:
             try:
                st.write(f'The area of rectangle is: {length} x {width} = {float(length)*float(width)} ')
             except:
                st.write('You did not write a number 😑')

if shape and shape != 'R' and shape != 'S':
     st.write('Please select a valid option...')
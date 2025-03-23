#How to run the streamlit
#cd \Users\gusbe\Desktop\Asian Learner\Korean_learn\Kor_1>
# streamlit run hangeulit.py

import numpy as np
import streamlit as st
from hangfunc import importation1
from hangfunc import importation2
from hangfunc import importation3
from hangfunc import choice
from hangfunc import gethangeul

st.title('Lesson 1 : Hangeul characters')

#------------------------------------------------------------
#Part 1
#------------------------------------------------------------

st.markdown('''
            ## Vowels \n

#### Regular vowels \n
ㅏ se prononce [a]\n  
ㅑ se prononce [ya]\n
ㅓ se prononce comme un son [o] ouvert, comme dans le mot « bonne ».\n
ㅕ se prononce comme un son [yo] ouvert, comme dans le mot « Yosh ».\n
ㅗ se prononce comme un son [ô] fermé, comme dans le mot « Bro ».\n
ㅛ se prononce comme un son [yô] fermé, comme dans le mot « Yo ».\n
ㅜ se prononce [ou]\n
ㅠ se prononce [you]\n
ㅡ Elle se prononce comme un son [eu], tout en étirant les lèvres plutôt qu’en les arrondissant.\n
ㅣ se prononce [i], comme dans le mot « idée ».\n
#### Composed vowels\n
In Korean, simple vowels can be assembled to make composed vowels'''
         )

all_hangeul1, all_alphageul1, all_hangeul_dict1 = importation1()

# Initialize session state
if 'hangeul1' not in st.session_state:
    st.session_state.hangeul1 = None
if 'selected_vowel1' not in st.session_state:
    st.session_state.selected_vowel1 = None
if 'right_ans1' not in st.session_state:
    st.session_state.right_ans1 = 0
if 'wrong_ans1' not in st.session_state:
    st.session_state.wrong_ans1 = 0
if 'tot_ans1' not in st.session_state:
    st.session_state.tot_ans1 = 0


# Guessing hangeul -----------------------------------------------------------------------------------------------------

    #Get a hangeul ------------------------------------------------------------
#if st.session_state.hangeul is None:
hangeul_button1 = st.button('Generate Hangeul')
if hangeul_button1:
    rand_hangeul1 = gethangeul(all_hangeul1,all_hangeul_dict1)
    st.session_state.hangeul1 = rand_hangeul1
    st.session_state.selected_vowel1 = None


#Display hangeul ----------------------------------------------------------------
if st.session_state.hangeul1:
    st.write('How do you translate :', st.session_state.hangeul1)

    #Ask user for translation-----------µ---------------------------------------------
    selected_vowel1 = ''
    all_alphageul_selection1 = all_alphageul1
    all_alphageul_selection1.insert(0, '')
    selected_vowel1 = st.selectbox('Select translation', all_alphageul_selection1)
    st.session_state.selected_vowel1 = selected_vowel1
    if st.session_state.hangeul1 and st.session_state.selected_vowel1:

        submit_button1 = st.button('Submit')

        if submit_button1:
            if st.session_state.selected_vowel1 != '':
                
                #Verify if the user got the right awnser --------------------------------------------------
                status1 = choice(st.session_state.hangeul1,st.session_state.selected_vowel1,all_hangeul_dict1)

                #User is corect ---------------------------------------------------------------------------
                if status1 == True:
                    st.write('Correct,', st.session_state.hangeul1, 'is pronunced :', st.session_state.selected_vowel1) 
                    st.session_state.right_ans1 += 1
                    st.session_state.tot_ans1 += 1

                #User is wrong -----------------------------------------------------------------------------
                if status1 == False:
                    st.write('False,', st.session_state.hangeul1, 'is pronunced :', all_hangeul_dict1[st.session_state.hangeul1])
                    st.session_state.wrong_ans1 += 1
                    st.session_state.tot_ans1 += 1

                # Reset selected translation and hide submit button
                
                st.session_state.selected_vowel1 = None    
                st.session_state.hangeul1 = None
                
                continue_button1 = st.button('Continue')
                if continue_button1:
                    st.session_state.selected_vowel1 = None    
                    st.session_state.hangeul1 = None



if st.session_state.tot_ans1 >= 1:
    st.write('You got', st.session_state.right_ans1, 'correct awnsers out of ', st.session_state.tot_ans1, 'questions')


#------------------------------------------------------------
#Part 2
#------------------------------------------------------------

st.markdown('''\n
            ## Consonnes \n
ㄱ se prononce : [g]k\n
ㅋ se prononce : [k]\n
ㄷ se prononce : [d]t\n
ㅌ se prononce : [t]\n
ㅂ se prononce : [b]p\n
ㅍ se prononce : [p]\n
ㅈ se prononce : [dj]\n
ㅊ se prononce : [tch]\n
ㅅ se prononce : [s]\n
ㅎ se prononce : [h]\n
ㄴ se prononce : [n]\n
ㅁ se prononce : [m]\n
ㅇ se prononce : [ng]\n
ㄹ se prononce : [r]l
            ''')

all_hangeul2, all_alphageul2, all_hangeul_dict2 = importation2()

# Initialize session state
if 'hangeul2' not in st.session_state:
    st.session_state.hangeul2 = None
if 'selected_vowel2' not in st.session_state:
    st.session_state.selected_vowel2 = None
if 'right_ans2' not in st.session_state:
    st.session_state.right_ans2 = 0
if 'wrong_ans2' not in st.session_state:
    st.session_state.wrong_ans2 = 0
if 'tot_ans2' not in st.session_state:
    st.session_state.tot_ans2 = 0


# Guessing hangeul -----------------------------------------------------------------------------------------------------

    #Get a hangeul ------------------------------------------------------------
#if st.session_state.hangeul is None:
hangeul_button2 = st.button('Generate Hangeul2')
if hangeul_button2:
    rand_hangeul2 = gethangeul(all_hangeul2,all_hangeul_dict2)
    st.session_state.hangeul2 = rand_hangeul2
    st.session_state.selected_vowel2 = None


#Display hangeul ----------------------------------------------------------------
if st.session_state.hangeul2:
    st.write('How do you translate :', st.session_state.hangeul2)

    #Ask user for translation--------------------------------------------------------
    selected_vowel2 = ''
    all_alphageul_selection2 = all_alphageul2
    all_alphageul_selection2.insert(0, '')
    selected_vowel2 = st.selectbox('Select translation', all_alphageul_selection2)
    st.session_state.selected_vowel2 = selected_vowel2
    if st.session_state.hangeul2 and st.session_state.selected_vowel2:

        submit_button2 = st.button('Submit')

        if submit_button2:
            if st.session_state.selected_vowel2 != '':
                
                #Verify if the user got the right awnser --------------------------------------------------
                status2 = choice(st.session_state.hangeul2,st.session_state.selected_vowel2,all_hangeul_dict2)

                #User is corect ---------------------------------------------------------------------------
                if status2 == True:
                    st.write('Correct,', st.session_state.hangeul2, 'is pronunced :', st.session_state.selected_vowel2) 
                    st.session_state.right_ans2 += 1
                    st.session_state.tot_ans2 += 1

                #User is wrong -----------------------------------------------------------------------------
                if status2 == False:
                    st.write('False,', st.session_state.hangeul2, 'is pronunced :', all_hangeul_dict2[st.session_state.hangeul2])
                    st.session_state.wrong_ans2 += 1
                    st.session_state.tot_ans2 += 1

                # Reset selected translation and hide submit button
                
                st.session_state.selected_vowel2 = None    
                st.session_state.hangeul2 = None
                
                continue_button2 = st.button('Continue')
                if continue_button2:
                    st.session_state.selected_vowel2 = None    
                    st.session_state.hangeul2 = None



if st.session_state.tot_ans2 >= 1:
    st.write('You got', st.session_state.right_ans2, 'correct awnsers out of ', st.session_state.tot_ans2, 'questions')



#-------------------------------------
# PART 3
#-------------------------------------

all_hangeul, all_alphageul, all_hangeul_dict = importation3()

# Initialize session state
if 'hangeul3' not in st.session_state:
    st.session_state.hangeul3 = None
if 'selected_vowel3' not in st.session_state:
    st.session_state.selected_vowel3 = None
if 'right_ans3' not in st.session_state:
    st.session_state.right_ans3 = 0
if 'wrong_ans3' not in st.session_state:
    st.session_state.wrong_ans3 = 0
if 'tot_ans3' not in st.session_state:
    st.session_state.tot_ans3 = 0


# Guessing hangeul -----------------------------------------------------------------------------------------------------

    #Get a hangeul ------------------------------------------------------------
#if st.session_state.hangeul is None:
hangeul_button3 = st.button('Generate Hangeul3')
if hangeul_button3:
    rand_hangeul3 = gethangeul(all_hangeul,all_hangeul_dict)
    st.session_state.hangeul3 = rand_hangeul3
    st.session_state.selected_vowel3 = None


#Display hangeul ----------------------------------------------------------------
if st.session_state.hangeul3:
    st.write('How do you translate :', st.session_state.hangeul3)

    #Ask user for translation--------------------------------------------------------
    selected_vowel3 = ''
    all_alphageul_selection = all_alphageul
    all_alphageul_selection.insert(0, '')
    selected_vowel3 = st.selectbox('Select translation', all_alphageul_selection)
    st.session_state.selected_vowel3 = selected_vowel3
    if st.session_state.hangeul3 and st.session_state.selected_vowel3:

        submit_button3 = st.button('Submit')

        if submit_button3:
            if st.session_state.selected_vowel3 != '':
                
                #Verify if the user got the right awnser --------------------------------------------------
                status = choice(st.session_state.hangeul3,st.session_state.selected_vowel3,all_hangeul_dict)

                #User is corect ---------------------------------------------------------------------------
                if status == True:
                    st.write('Correct,', st.session_state.hangeul3, 'is pronunced :', st.session_state.selected_vowel3) 
                    st.session_state.right_ans3 += 1
                    st.session_state.tot_ans3 += 1

                #User is wrong -----------------------------------------------------------------------------
                if status == False:
                    st.write('False,', st.session_state.hangeul3, 'is pronunced :', all_hangeul_dict[st.session_state.hangeul3])
                    st.session_state.wrong_ans3 += 1
                    st.session_state.tot_ans3 += 1

                # Reset selected translation and hide submit button
                
                st.session_state.selected_vowel3 = None    
                st.session_state.hangeul3 = None
                
                continue_button3 = st.button('Continue')
                if continue_button3:
                    st.session_state.selected_vowel3 = None    
                    st.session_state.hangeul3 = None



if st.session_state.tot_ans3 >= 1:
    st.write('You got', st.session_state.right_ans3, 'correct awnsers out of ', st.session_state.tot_ans3, 'questions')


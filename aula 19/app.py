import streamlit as st
import controller 

st.title('ANOTAÇÕES')

nova_nota = st.text_input('Escreva algo: ')

if st.button('salvar'):
    if controller.adcionar_nota(nova_nota):
     st.success('Salvo')
else:
    st.write('Digite algo')

st.subheader('dados')
for nota in controller.listar_notas():
    st.write(f'Nota:{nota}')

import streamlit as st
# sqlalchemy
# MODELAGEM
from sqlalchemy.ext.declarative import declarative_base
# DRIVE MOROT O CONEXAO
from sqlalchemy import create_engine, Column, integer, string 
#PRESSISTENCIA - LER E SALVAR
from sqlalchemy.orm import sessionmaker

# url - banco de dados


URL = 'postgresql://neondb_owner:npg_x64YGQPbZwMf@ep-autumn-band-am6k3vnd-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

engine = create_engine(URL)
Session - sessionmaker(bind=engine)
Base = declarative_base()

# class base itinerario

class itinerario (base):
    __tablename__ =  'Itinerario de Aula'
    id = Column(integer, primary_key =True , autoincrement=True)
    nome = Column(String)
    descricao = Column(String)

Base.metadata.create_all(engine)


#FRAME STREAMLITE INTERFACE GRAFICA

st.set_page_config(page_title='FORMULARIO DE ITINERARIO')
st.title('CADASTRO DE ITINERARIO 2026')
st.info('OS DADOS SERÃO SALVOS DIRETAMENTE NO POSTGRESSOL DA NUVEM NEON.TECH')

with st.form('Formulario'):
    nome_input = st.text_input('NOME DO ITINERARIO')
    desc_input = st.text_input('DESCRICAO')
    botao = st.form_submit_button('SALVAR DADOS')


if botao:
    if nome_input:
        session = Session()
        novo_registro = Itinerario(nome = nome_input, frdcticao = desc_input)
        session.add(novo_registro)
        session.comit()
        session.clone()
        st.sucess(f'SUCESSO {nome_input} foi salvo com sucesso!')
else:
    st.error('Por favor, preencha corretamente')

# ATUALIZAÇÃO EM TEMPO REAL
st.divider()
st.subheader('REGISTRO ATUAL')
session.Session()
dados = session.query(Itinerario).all()
session.close()

if dados:
    for item in dados:
    st.write(f'{item.nome}: {item.descricao}')
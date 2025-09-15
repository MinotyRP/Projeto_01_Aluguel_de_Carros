import streamlit as st
import pandas as pd
# python -m streamlit run app.py

#-------------------------------------- Sidebar


st.sidebar.image("logo.png")
st.sidebar.title('Nikolas VrumVrum')

carros = ['BMW', 'Mustang', 'Porsche', 'Fusca', 'Toro', 'Blaze', 'Camaro']

opcao = st.sidebar.selectbox('Escolha o carroque foi alugado', carros)



#--------------------------------------- Principal
st.title('Olá querido vendedor, vamos pra onde????🗿👌')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

### Copia até aqui antes do IF

if opcao == 'BMW':
    diaria = 450
    
elif opcao == 'Mustang':
    diaria = 500
    
elif opcao == 'Porsche':
    diaria = 300
    
elif opcao == 'Fusca':
    diaria = 250
    
elif opcao == 'Toro':
    diaria = 550
    
elif opcao == 'Blaze':
    diaria = 2.000

elif opcao == 'Camaro':
    diaria = 1.000
    
    
if st.button('Calcular'):
    dias = int(dias)
    km = float(km)
    
    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km
    
    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km} km. Ovalor totoal a pagar é R${aluguel_total:.2f}')
import streamlit as st

st.title("Calculadora de IMC")
st.text("Informe sua altura e seu peso para saber o seu peso! (Em metros e kg)")
st.markdown("---")

peso = float(st.text_input("Qual é o seu peso?", 80))
altura = float(st.text_input("Qual é a sua altura?", 1.6))

botao = st.button("Calcular IMC")
st.markdown("---")

def IMC(peso,altura):
    return round((peso / altura **2),2)

if botao == True:
    st.subheader("Abaixo estão os seus resultados:")
    valor = IMC(peso,altura)
    if valor <= 18.5:
        st.markdown(f"O seu IMC é de {valor}, você está abaixo do seu peso ideal! :pensive:")
    elif valor >= 25:
        st.markdown(f"O seu IMC é de {valor}, você está acima do seu peso ideal! :dizzy_face:")
    else:
        st.markdown(f"O seu IMC é de {valor}, você está dentro do seu peso ideal! :grin:")


"#teste_adicao_git" 
"#teste_git" 

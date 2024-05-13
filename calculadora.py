import streamlit as st

st.title("Calculadora")
num1 = st.number_input("insira o primeiro número: ")
num2 = st.number_input("insira o segundo numero: ")

operacao = st.selectbox("Selecione a operação:", ["Soma", "Subtração", "Multiplicação", "Divisão",])
if st.button("Calcular"):
        if operacao == "Soma":
            resultado = num1 + num2
        elif operacao == "Subtração":
            resultado = num1 - num2
        elif operacao == "Multiplicação":
            resultado = num1 * num2
        else:
            resultado = num1 / num2

        st.write("Resultado:", resultado)



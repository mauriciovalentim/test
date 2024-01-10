import streamlit as st
import Model

st.set_page_config(page_title="Modelador")

temperatura = st.number_input("TEMPERATURA - ENTRADA", format="%.2f")
ph = st.number_input("PH - ENTRADA", format="%.2f")
ssd = st.number_input("SÓLIDOS SUSPENSOS DISSOLVIDOS - ENTRADA", format="%.2f")
sst = st.number_input("SÓLIDOS SUSPENSOS TOTAIS - ENTRADA", format="%.2f")
solidosTotais = st.number_input("SÓLIDOS TOTAIS - ENTRADA", format="%.2f")
dqo = st.number_input("DEMANDA QUÍMICA DE OXIGÊNIO - ENTRADA", format="%.2f")
dbo = st.number_input(
    "DEMANDA BIOQUÍMICA DE OXIGÊNIO - ENTRADA", format="%.2f")
og = st.number_input("ÓLEOS E GRAXAS - ENTRADA", format="%.2f")


calc = st.button("Calcular", type="primary")
if calc:
    result = Model.get_saida_dbo(temperatura, ph, ssd, sst, solidosTotais, dqo, dbo, og)
    st.write(f"DQO Saída: {result}")
    # st.write(f"DQO Saída: {'test'}")

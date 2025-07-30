import streamlit as st
import os

ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        f.write("\n".join(tarefas))

st.title("📋 Gerenciador de Tarefas")
st.markdown("Adicione, visualize e remova suas tarefas!")

tarefas = carregar_tarefas()

# Adicionar tarefa
nova_tarefa = st.text_input("Adicionar nova tarefa:")
prazo = st.text_input("Prazo (opcional):")

if st.button("➕ Adicionar"):
    if nova_tarefa.strip():
        tarefas.append(f"{nova_tarefa} | {prazo if prazo else 'Sem prazo'}")
        salvar_tarefas(tarefas)
        st.success("Tarefa adicionada com sucesso!")
        st.experimental_rerun()

# Ver tarefas
if tarefas:
    st.subheader("Tarefas:")
    for i, t in enumerate(tarefas):
        tarefa, *resto = t.split(" | ")
        prazo = resto[0] if resto else "Sem prazo"
        col1, col2 = st.columns([4, 1])
        col1.markdown(f"**{i+1}.** {tarefa} _(prazo: {prazo})_")
        if col2.button("❌", key=i):
            tarefas.pop(i)
            salvar_tarefas(tarefas)
            st.experimental_rerun()
else:
    st.info("Nenhuma tarefa ainda. Adicione acima!")

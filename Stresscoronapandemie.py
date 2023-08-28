import streamlit as st
import pandas as pd
import altair as alt

st.header("Anteil der Kinder und Jugendlichen, der die Corona-Pandemie als stressig empfand")
st.subheader("Deutschland im Zeitraum von 2020 und 2022")

source = pd.DataFrame({
        'Anteil(%)': [70.6, 82.9, 81.9, 80.3, 73],
        'Zeitraum': ['1. Welle Mai - Jun 2020', '2. Welle Dez 2020 -Jan 21', '3. Welle Sep - Okt 2021', '4.Welle Feb 2022','5. Welle Sep - Okt 2022']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Zeitraum:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 1673 Befragte; 11 bis 17 Jahre; Januar 2023
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  COPSY-Längschnittstudie")
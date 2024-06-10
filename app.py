import streamlit as st
import pandas as pd
import datetime

# Exemple de données de visiteurs
data = {
    'Timestamp': [datetime.datetime.now()],
    'Visitor ID': [560092345],
    'Room ID': [7015338174445824037],
    'Code': [6893554100]
}

# Conversion des données en DataFrame
df = pd.DataFrame(data)

# Titre de l'application
st.title("Dashboard des Visiteurs")

# Affichage des données
st.subheader("Détails des Visiteurs")
st.write(df)

# Ajout de nouvelles entrées par l'utilisateur (exemple simplifié)
visitor_id = st.number_input('Visitor ID', min_value=0)
room_id = st.number_input('Room ID', min_value=0)
code = st.number_input('Code', min_value=0)
if st.button('Ajouter Visiteur'):
    new_data = {
        'Timestamp': datetime.datetime.now(),
        'Visitor ID': visitor_id,
        'Room ID': room_id,
        'Code': code
    }
    df = df.append(new_data, ignore_index=True)
    st.write(df)

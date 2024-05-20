import streamlit as st
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

# Charger le modèle de prédiction
model = joblib.load(r'C:\Users\baihich\Desktop\application\modelLog.joblib')

# Titre de l'application
st.title('Prédiction du Diagnostic de la Tumeur Mammaire')

# Instructions
st.write("""
Veuillez entrer les mesures cliniques de la biopsie pour obtenir une prédiction sur le diagnostic.
""")

# Créer des champs pour saisir les mesures cliniques
radius_mean = st.number_input('Rayon moyen')
texture_mean = st.number_input('Texture moyenne')
perimeter_mean = st.number_input('Périmètre moyen')
area_mean = st.number_input('Surface moyenne')
smoothness_mean = st.number_input('Lissité moyenne')
compactness_mean = st.number_input('Compacité moyenne')
concavity_mean = st.number_input('Concavité moyenne')
concave_points_mean = st.number_input('Points concaves moyens')
symmetry_mean = st.number_input('Symétrie moyenne')
fractal_dimension_mean = st.number_input('Dimension fractale moyenne')
radius_se = st.number_input('Rayon SE')
texture_se = st.number_input('Texture SE')
perimeter_se = st.number_input('Périmètre SE')
area_se = st.number_input('Surface SE')
smoothness_se = st.number_input('Lissité SE')
compactness_se = st.number_input('Compacité SE')
concavity_se = st.number_input('Concavité SE')
concave_points_se = st.number_input('Points concaves SE')
symmetry_se = st.number_input('Symétrie SE')
fractal_dimension_se = st.number_input('Dimension fractale SE')
radius_worst = st.number_input('Rayon pire')
texture_worst = st.number_input('Texture pire')
perimeter_worst = st.number_input('Périmètre pire')
area_worst = st.number_input('Surface pire')
smoothness_worst = st.number_input('Lissité pire')
compactness_worst = st.number_input('Compacité pire')
concavity_worst = st.number_input('Concavité pire')
concave_points_worst = st.number_input('Points concaves pires')
symmetry_worst = st.number_input('Symétrie pire')
fractal_dimension_worst = st.number_input('Dimension fractale pire')



# Bouton pour soumettre les mesures
if st.button('Prédire'):
    if (radius_mean == 0 or texture_mean == 0 or perimeter_mean == 0 or area_mean == 0 or smoothness_mean == 0):
        st.error("Veuillez remplir toutes les mesures cliniques.")
    else:
        # Feedback visuel
        with st.spinner('Prédiction en cours...'):
            # Rassembler les mesures dans un tableau numpy
            input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                                    concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
                                    radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se,
                                    concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                                    radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                                    compactness_worst, concavity_worst, concave_points_worst, symmetry_worst,
                                    fractal_dimension_worst]])

            try:
                # Faire la prédiction
                prediction = model.predict(input_data)

                # Afficher le résultat
                if prediction[0] == 1:
                    st.success("Le modèle prédit que la tumeur est maligne.")
                else:
                    st.success("Le modèle prédit que la tumeur est bénigne.")
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de la prédiction : {str(e)}")

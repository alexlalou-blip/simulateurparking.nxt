import streamlit as st

st.set_page_config(page_title="Nexity Parking", page_icon="🚗", layout="centered")

# Hero Section
st.title("🚗 Votre place vous attend")
st.write(
    "Que vous cherchiez un parking pour **simplifier votre quotidien** "
    "ou un **investissement malin**, Nexity vous propose des parkings "
    "sécurisés, accessibles et situés partout en France."
)

# Choix de l'utilisateur
option = st.radio(
    "Que souhaitez-vous faire ?",
    ("🔑 Trouver une place près de chez moi", "💰 Simuler un investissement"),
)

# Trouver une place (démonstration simple)
if option == "🔑 Trouver une place près de chez moi":
    st.subheader("🔎 Trouvez votre parking")
    ville = st.selectbox(
        "Choisissez votre ville :",
        ["Paris", "Lyon", "Marseille", "Toulouse", "Montpellier"],
    )
    st.success(f"✅ Des parkings Nexity sont disponibles à {ville} !")

# Simulateur d'investissement
elif option == "💰 Simuler un investissement":
    st.subheader("📊 Simulateur d'investissement parking")

    prix = st.number_input("Prix du parking (€)", min_value=5000, max_value=33000, value=10000, step=1000)
    loyer = st.number_input("Loyer mensuel estimé (€)", min_value=30, max_value=200, value=60, step=5)

    revenu_annuel = loyer * 12
    rentabilite = (revenu_annuel / prix) * 100

    st.write(f"**Revenu annuel estimé :** {revenu_annuel:.0f} €")
    st.write(f"**Rentabilité brute :** {rentabilite:.1f} %")

    st.info("💡 Exemple : un parking acheté 10 000 € avec un loyer de 60 €/mois rapporte 720 € par an, soit une rentabilité brute de 7,2 %.")    

# CTA
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>"
    "<a href='https://www.nexity.fr' target='_blank'>"
    "<button style='background-color:#1e40af;color:white;padding:15px 30px;border:none;border-radius:10px;font-size:18px;'>"
    "🚀 Découvrir tous les parkings Nexity"
    "</button></a></div>",
    unsafe_allow_html=True,
)

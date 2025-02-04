import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/00_cryptography.py",
    title="Criptografia",
    icon=":material/home:",
    default=True,
)


project_2_page = st.Page(
    "views/01_ofuscacion_text.py",
    title="Ofuscador y Estenografia",
    # icon=":material/smart_toy:",
    icon=":material/article:",
)

project_3_page = st.Page(
    "views/02_ofuscacion_img.py",
    title="Ofuscacion de Imagenes",
    icon=":material/image:",
)

project_4_page = st.Page(
    "views/04_cryptografia_clasica.py",
    title="Criptografia Clasica",
    icon=":material/lock:",
)

project_5_page = st.Page(
    "views/05_conceptos.py",
    title="Conceptos",
    icon=":material/lock:",
)

project_6_page = st.Page(
    "views/06_criptografia_simetrica.py",
    title="Conceptos: AES-HASH",
    icon=":material/key:",
)


project_7_page = st.Page(
    "views/07_criptografia_asimetrica.py",
    title="Conceptos: RSA",
    icon=":material/vpn_key:",
)

project_8_page = st.Page(
    "views/08_criptografia_curva_eliptica.py",
    title="Conceptos y aplicacion",
    icon=":material/line_curve:",
)


project_9_page = st.Page(
    "views/09_criptografia_moderna.py",
    title="Criptografia Cuantica y mas",
    icon=":material/search_insights:",
)


project_10_page = st.Page(
    "views/10_criptografia_ransomware.py",
    title="Ransomware",
    icon=":material/coronavirus:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projectos-Herramientas": [ project_2_page, project_3_page],
        "Criptografia-Conceptos":[project_4_page, project_5_page],
        "Criptografia-Simetrica":[project_6_page],
        "Criptografia-Asimetrica":[project_7_page],
        "Criptografia-Curva Eliptica":[project_8_page],
        "Criptografia-Moderna":[project_9_page],
        "Criptografia-Ransomware":[project_10_page]
    }
)


# # --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")
# st.sidebar.markdown("Made with ❤️ by [Rfeb](https://www.linkedin.com/in/rodrigo-bogado-a64b4925b/)")


# --- RUN NAVIGATION ---
pg.run()
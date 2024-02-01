import streamlit as st
import streamlit_authenticator as stauth

COOCKI_EXPIRY_DAYS = 30

def main():
    authenticator = stauth.Authenticate(
        {'usernames': {'teste': {'name': 'testando', 'password': 'blabla'}}},
        'random_cookie_name',
        'random_signature_key',

        COOCKI_EXPIRY_DAYS,

    )

    if 'clicou_registrar' not in st.session_state:
        st.session_state['clicou_registrar'] = False

    if st.session_state['clicou_registrar'] == False:
        login_form(authenticator=authenticator)
    else:
        usuario_form()

def login_form(authenticator):
    name, authenticator_status, username = authenticator.login('Login')
    if authenticator_status:
        authenticator.logout('Logout', main)
        st.title('Área do Dashboard')
        st.write(f'*{name} está logado(a)!')
    elif authenticator_status == False:
        st.error('Usuário / Senha incorretos.')
    elif authenticator_status == None:
        st.warning('Por favor informe um usuário e senha.')
        clicou_em_registrar = st.button("Registrar")
        if clicou_em_registrar:
            st.session_state['clicou_registrar'] == True
            st.rerun()

def confirm_msg():
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senha não confere')
    elif 'consulta_nome()':
        st.warning('Nome de usuários já existe.')
    else:
        'add_registro()'
        st.success('Registro efetuado!')

def usuario_form():
    with st.form(key="formulario", clear_on_submit=True):
        nome = st.text_input("Nome",key="nome")
        username = st.text_input("Usuário",key="user")
        password = st.text_input("Senha",key="pswrd",type="password")
        confirm_password = st.text_input("Confirme senha",key="confirm_pswrd", type="password")
        submit = st.form_submit_button(
            "salvar", on_click=confirm_msg,
        )

    clicou_em_fazer_login = st.button("Fazer Login")
    if clicou_em_fazer_login:
        st.session_state['clicou_registrar'] = False
        st.rerun()

if __name__ == '__main__':

    main()
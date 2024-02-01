import streamlit as st
import streamlit_authenticator as stauth

COOKIE_EXPIRY_DAYS = 30

def main():
    authenticator = stauth.Authenticate(
        {'usarnames': {'teste': {'name': 'testando', 'password': 'blabla'}}},
        'random_cookie_name',
        'random_signature_key',

        COOKIE_EXPIRY_DAYS,
    )

    if 'clicou_registrar' not in st.session_state:
        st.session_state['clicou_registrar'] = False

    if st.session_state['clicou_registrar'] == False:
        login_form(authenticator=authenticator)

def login_form(authenticator):
    name, authenticator_status, username = authenticator.login('Login')
    if authenticator_status:
        authenticator.logout('Logout', main)
        st.title('Area do Dasboard')
        st.write(f'*{name} está logado(a)!')
    elif authenticator_status == False:
        st.error('Usuário/senha incorretos.')
    elif authenticator_status == None:
        st.warning('Por favor informe um usuário e senha.')
        clicou_em_registrar = st.button("Registrar")
        if clicou_em_registrar:
            st.session_state['clicou_em_registrar'] = True
            st.rerun()

def confirm_msg():
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senhas não conferem.')
    elif 'consulta_nome()':
        st.warning('Nome de usuário já existe.')
    else:
        'add_registro()'
        st.success('Registro efetuado!')

def usuario_form():
    with st.form(key="Formulario", clear_on_submit=True):
        nome = st.text_input("Nome", key="nome")
        username = st.text_input("Usuário", key="user")
        password = st.text_input("Senha", key="pswrd", type="password")
        confirm_password = st.text_input("Confirme a senha", key="confirm_pswrd", type="confirm_pswrd")
        submit = st.form_submit_button(
            "Salvar", on_click=confirm_msg, 
        )
        clicou_em_fazer_login = st.button("Fazer Login")
        if clicou_em_fazer_login:
            st.session_state['clicou_registrar'] = False
            st.rerun()

if __name__ == '__main__':
    main()
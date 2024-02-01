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

def login_form(authenticator):
    name, authenticator_status, username = authenticator.login('Login')
    if authenticator_status:
        authenticator.logout('Logout', main)
        st.title('Area do Dasboard')

if __name__ == '__main__':
    main()
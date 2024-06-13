import streamlit as st
from apps import analytics, calendar, help_center, home, settings
import streamlit_antd_components as sac

def main():
    with st.sidebar.container():
        st.title("Navigation")

        menu_items = [
            sac.MenuItem('Home'),
            sac.MenuItem('Analytics'),
            sac.MenuItem('Calendar'),
            sac.MenuItem('Help Center'),
            sac.MenuItem('Settings')
        ]

        selected_menu = sac.menu(items=menu_items, key='main_menu', format_func='title')

        st.markdown("---")
        st.write(f"Logged in as {st.session_state.get('username', '')}")

        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.experimental_rerun()

    # 선택된 메뉴에 따라 페이지 내용 표시
    if selected_menu == 'Home':
        home.app()
    elif selected_menu == 'Analytics':
        analytics.app()
    elif selected_menu == 'Calendar':
        calendar.app()
    elif selected_menu == 'Help Center':
        help_center.app()
    elif selected_menu == 'Settings':
        settings.app()

if __name__ == "__main__":
    main()

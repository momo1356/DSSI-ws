import streamlit as st
from src.inference import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Cupon subscribe')
    options = ['0','1']
    is_female = st.sidebar.selectbox("Gender", options)
    is_married = st.sidebar.selectbox("Married", options)
    colg_edu = st.sidebar.selectbox("Collage Education", options)
    is_professional = st.sidebar.selectbox("Profession", options)
    is_retired = st.sidebar.selectbox("Retired", options)
    is_unemployed = st.sidebar.selectbox("Unemployed", options)
    dual_income = st.sidebar.selectbox("dual_income", options)
    have_minors = st.sidebar.selectbox("have_minors", options)
    own_house = st.sidebar.selectbox("own_house", options)
    race_white = st.sidebar.selectbox("race_white", options)
    speak_english = st.sidebar.selectbox("speak_english", options)
    yearly_income = st.sidebar.text_input("Annual Income")
    months_residence = st.sidebar.text_input('months_residence')
    def get_input_features():
        input_features = {'is_female': is_female,
                          'is_married': is_married,
                          'is_professional': is_professional,
                          'is_retired': is_retired,
                          'is_unemployed': is_unemployed,
                          'dual_income': dual_income,
                          'have_minors': have_minors,
                          'own_house': own_house,
                          'race_white': race_white,
                          'speak_english': speak_english,
                          'yearly_income': int(yearly_income),
                          'colg_edu': colg_edu,
                          'months_residence': int(months_residence)
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to DSSI Coupon Assessment</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(is_female=st.session_state['input_features']['is_female'],
                                    is_married=st.session_state['input_features']['is_married'],
                                    is_professional=st.session_state['input_features']['is_professional'],
                                    is_retired=st.session_state['input_features']['is_retired'],
                                    is_unemployed=st.session_state['input_features']['is_unemployed'],
                                    dual_income=st.session_state['input_features']['dual_income'],
                                    have_minors=st.session_state['input_features']['have_minors'],
                                    own_house=st.session_state['input_features']['own_house'],
                                    race_white=st.session_state['input_features']['race_white'],
                                    speak_english=st.session_state['input_features']['speak_english'],
                                    yearly_income=st.session_state['input_features']['yearly_income'],
                                    colg_edu=st.session_state['input_features']['colg_edu'],
                                    months_residence=st.session_state['input_features']['months_residence'])
        if assessment == 1:
            st.success(default_msg.format('Subscribed'))
        else:
            st.warning(default_msg.format('Unsubscribed'))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()
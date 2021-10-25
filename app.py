import streamlit as st
import pandas as pd
import pickle
import random

# ------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title='IPL Score Predictor', page_icon=None,
                   layout='centered', initial_sidebar_state='auto')
# Set page title
st.title('IPL Score Predictor')
# ------------------------------------------------------------------------------------------------------------
# change the model type to see lil changes in prediction
filename = 'ipl_score_predict_model.pkl'
reg = pickle.load(open(filename, 'rb'))
# ------------------------------------------------------------------------------------------------------------
############################################################################################################
bat_team = st.selectbox('Select batting team : ',
                        options=['Chennai Super Kings', 'Delhi Daredevils',
                                 'Kings XI Punjab', 'Kolkata Knight Riders',
                                 'Mumbai Indians', 'Rajasthan Royals',
                                 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])
if bat_team == 'Chennai Super Kings':
    bat_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Delhi Daredevils',
                                      'Kings XI Punjab', 'Kolkata Knight Riders',
                                      'Mumbai Indians', 'Rajasthan Royals',
                                      'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])
    if bowl_team == 'Delhi Daredevils':
        bowl_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kings XI Punjab':
        bowl_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kolkata Knight Riders':
        bowl_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == 'Mumbai Indians':
        bowl_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == 'Rajasthan Royals':
        bowl_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == 'Royal Challengers Bangalore':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowl_team == 'Sunrisers Hyderabad':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 0, 1]

 ############################################################################################################

elif bat_team == 'Delhi Daredevils':
    bat_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Chennai Super Kings',
                                      'Kings XI Punjab', 'Kolkata Knight Riders',
                                      'Mumbai Indians', 'Rajasthan Royals',
                                      'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

    if bowl_team == 'Chennai Super Kings':
        bowl_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kings XI Punjab':
        bowl_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kolkata Knight Riders':
        bowl_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == 'Mumbai Indians':
        bowl_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == 'Rajasthan Royals':
        bowl_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == 'Royal Challengers Bangalore':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowl_team == 'Sunrisers Hyderabad':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 0, 1]

############################################################################################################


elif bat_team == 'Kings XI Punjab':
    bat_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Chennai Super Kings', 'Delhi Daredevils',
                                      'Kolkata Knight Riders',
                                      'Mumbai Indians', 'Rajasthan Royals',
                                      'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

    if bowl_team == 'Chennai Super Kings':
        bowl_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Delhi Daredevils':
        bowl_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kolkata Knight Riders':
        bowl_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == 'Mumbai Indians':
        bowl_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == 'Rajasthan Royals':
        bowl_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == 'Royal Challengers Bangalore':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowl_team == 'Sunrisers Hyderabad':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 0, 1]


############################################################################################################

elif bat_team == 'Kolkata Knight Riders':
    bat_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Chennai Super Kings', 'Delhi Daredevils',
                                      'Kings XI Punjab',
                                      'Mumbai Indians', 'Rajasthan Royals',
                                      'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

    if bowl_team == 'Chennai Super Kings':
        bowl_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Delhi Daredevils':
        bowl_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kings XI Punjab':
        bowl_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == 'Mumbai Indians':
        bowl_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == 'Rajasthan Royals':
        bowl_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == 'Royal Challengers Bangalore':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowl_team == 'Sunrisers Hyderabad':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 0, 1]

############################################################################################################

elif bat_team == 'Mumbai Indians':
    bat_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Chennai Super Kings', 'Delhi Daredevils',
                                      'Kings XI Punjab', 'Kolkata Knight Riders',
                                      'Rajasthan Royals',
                                      'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

    if bowl_team == 'Chennai Super Kings':
        bowl_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Delhi Daredevils':
        bowl_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kings XI Punjab':
        bowl_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kolkata Knight Riders':
        bowl_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == 'Rajasthan Royals':
        bowl_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == 'Royal Challengers Bangalore':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowl_team == 'Sunrisers Hyderabad':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 0, 1]

############################################################################################################

elif bat_team == 'Rajasthan Royals':
    bat_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Chennai Super Kings', 'Delhi Daredevils',
                                      'Kings XI Punjab', 'Kolkata Knight Riders',
                                      'Mumbai Indians',
                                      'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

    if bowl_team == 'Chennai Super Kings':
        bowl_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Delhi Daredevils':
        bowl_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kings XI Punjab':
        bowl_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kolkata Knight Riders':
        bowl_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == 'Mumbai Indians':
        bowl_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == 'Royal Challengers Bangalore':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowl_team == 'Sunrisers Hyderabad':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 0, 1]


############################################################################################################

elif bat_team == 'Royal Challengers Bangalore':
    bat_team_list = [0, 0, 0, 0, 0, 0, 1, 0]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Chennai Super Kings', 'Delhi Daredevils',
                                      'Kings XI Punjab', 'Kolkata Knight Riders',
                                      'Mumbai Indians', 'Rajasthan Royals',
                                      'Sunrisers Hyderabad'])

    if bowl_team == 'Chennai Super Kings':
        bowl_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Delhi Daredevils':
        bowl_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kings XI Punjab':
        bowl_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kolkata Knight Riders':
        bowl_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == 'Mumbai Indians':
        bowl_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == 'Rajasthan Royals':
        bowl_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == 'Sunrisers Hyderabad':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 0, 1]


############################################################################################################

elif bat_team == 'Sunrisers Hyderabad':
    bat_team_list = [0, 0, 0, 0, 0, 0, 0, 1]
    bowl_team = st.selectbox('Select bowling team : ',
                             options=['Chennai Super Kings', 'Delhi Daredevils',
                                      'Kings XI Punjab', 'Kolkata Knight Riders',
                                      'Mumbai Indians', 'Rajasthan Royals',
                                      'Royal Challengers Bangalore'])

    if bowl_team == 'Chennai Super Kings':
        bowl_team_list = [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Delhi Daredevils':
        bowl_team_list = [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kings XI Punjab':
        bowl_team_list = [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowl_team == 'Kolkata Knight Riders':
        bowl_team_list = [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowl_team == 'Mumbai Indians':
        bowl_team_list = [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowl_team == 'Rajasthan Royals':
        bowl_team_list = [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowl_team == 'Royal Challengers Bangalore':
        bowl_team_list = [0, 0, 0, 0, 0, 0, 1, 0]

# ------------------------------------------------------------------------------------------------------------
# Bowling team
# bowl_team = st.selectbox('Select bowling team : ',
#                  options=['Chennai Super Kings', 'Delhi Daredevils',
#                           'Kings XI Punjab', 'Kolkata Knight Riders',
#                           'Mumbai Indians', 'Rajasthan Royals',
#                           'Royal Challengers Bangalore','Sunrisers Hyderabad'])

# if bowl_team == 'Chennai Super Kings':
#     bowl_team_list = [1,0,0,0,0,0,0,0]
# elif bowl_team == 'Delhi Daredevils':
#     bowl_team_list = [0,1,0,0,0,0,0,0]
# elif bowl_team == 'Kings XI Punjab':
#     bowl_team_list = [0,0,1,0,0,0,0,0]
# elif bowl_team == 'Kolkata Knight Riders':
#     bowl_team_list = [0,0,0,1,0,0,0,0]
# elif bowl_team == 'Mumbai Indians':
#     bowl_team_list = [0,0,0,0,1,0,0,0]
# elif bowl_team == 'Rajasthan Royals':
#     bowl_team_list = [0,0,0,0,0,1,0,0]
# elif bowl_team == 'Royal Challengers Bangalore':
#     bowl_team_list = [0,0,0,0,0,0,1,0]
# elif bowl_team == 'Sunrisers Hyderabad':
#     bowl_team_list = [0,0,0,0,0,0,0,1]

# ------------------------------------------------------------------------------------------------------------
runs_list = st.number_input('Total Runs till now : ', step=1, min_value=0)
wickets_list = st.number_input(
    'Total Wickets till now : ', step=1, max_value=11, min_value=0)
# overs_list = st.number_input('Overs passed',step = 0.1,min_value=4.0)
overs_list = st.slider("Overs passed : ", min_value=0.0,
                       max_value=21.0, value=0.0, step=0.1)
runs_last_5_list = st.number_input(
    'Runs scored in previous 5 Overs : ', step=1, min_value=0)
wickets_last_5_list = st.number_input(
    'Wickets in previous 5 Overs : ', step=1, max_value=11, min_value=0)
# ------------------------------------------------------------------------------------------------------------
bat_and_bowl_team = bat_team_list + bowl_team_list


# overs = st.slider("Select number of words (default is 3 words) : ",
#                          min_value=1, max_value=10, value=0, step = 0.1)

# bat_and_bowl_team = [0,0,0,1,0,0,0,0,
#        1,0,0,0,0,0,0,0,
#        64,4,7.2,42,3]

predict_df = pd.DataFrame([bat_and_bowl_team], columns=['bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils',
                                                        'bat_team_Kings XI Punjab', 'bat_team_Kolkata Knight Riders',
                                                        'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
                                                        'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
                                                        'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils',
                                                        'bowl_team_Kings XI Punjab', 'bowl_team_Kolkata Knight Riders',
                                                        'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
                                                        'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad'])
# 'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5']
predict_df1 = pd.DataFrame([[runs_list, wickets_list, overs_list, runs_last_5_list, wickets_last_5_list]], columns=[
    'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5'])
predict_df = pd.concat([predict_df, predict_df1], axis=1)

if (runs_list == 0) | (overs_list == 0):
    my_prediction = 0
    st.info(f'\nPredicted score range : **_0_**  to **_{my_prediction+10}_**')
else:
    my_prediction = int(reg.predict(predict_df)[0])
    st.info(
        f'\nPredicted score range : **_{my_prediction-10}_**  to **_{my_prediction+10}_**')

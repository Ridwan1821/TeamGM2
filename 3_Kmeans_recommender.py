"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import PIL
from PIL import Image

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","General Info","Exploratory Data Analysis (EDA)", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "General Info":
        img = Image.open('Kmeans.PNG')
        img1 = img.resize((2000,300))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.text("")
        with col2:
                st.image(img1, caption=None, use_column_width=True)
        with col3:
                st.text("")
        st.subheader("KMeans Movie Recommender")
        st.markdown("Kmeans movie recommender is a web app that recommend movies to its users. In this system, users are asked to rate movies they just finished seeing and the ratings are used to recommend other movies to them.")
        img2 = Image.open('Moviepic')
        st.image(img2, caption=None)

        st.markdown("This app is built towards increasing users satisfaction of streaming apps by identifying movies users love through their ratings and recommending similar movies to them. In the same vein, the app identify movies users do not like and make sure similar movies to that are not recommended to such users. The recommendations take diffferent forms such as email notifications, in app notifications or making the recommended movies appear on the frontpage of the user's account.")
        st.markdown("As a way of showing the power of this app to our potential partners, we have provided an interface that allows people to select movies and get lists of movies similar to what they have selected.")
        st.subheader("Using The Kmeans Recommender")
        st.markdown("Go to the KMeans Recommender page.  \nSelect your favourite movies.  \nClick on Recommend to see a list of similar movies")

    if page_selection == "Exploratory Data Analysis (EDA)":

        img = Image.open('Kmeans.PNG')
        img1 = img.resize((2000,300))
        df = pd.read_csv('movies.csv')
        col1, col2, col3 = st.columns(3)
        with col1:
                st.text("")
        with col2:
                st.image(img1, caption=None, use_column_width=True)
        with col3:
                st.text("")
        st.subheader("Data Exploration")
        st.markdown("The dataset used for the set up of this movie recommendation system is a dataset gotten from the internet movie database (imdb).  The dataset contains 62423 movies spanning various movie genres. Below are informations about the dataset:")
        st.dataframe(df)
        
        st.markdown("Below are insights from the dataset used for the preparation of this recommender:")
        img3 = Image.open('Most common movies.png')
        img3 = img3.resize((2000,1000))
        st.image(img3, caption = "Most Common Movies",use_column_width=True)

        img4 = Image.open('Top Ten Movies.png')
        img4 = img4.resize((2000,1000))
        st.image(img4, caption = "Top Ten Movies",use_column_width=True)
        
        img5 = Image.open('WORD CLOUD.png')
        img5 = img5.resize((2000,1000))
        st.image(img5, caption = "Word Cloud",use_column_width=True)
      
    if page_selection == "About Us":
        img = Image.open('Kmeans.PNG')
        img1 = img.resize((2000,300))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.text("")
        with col2:
                st.image(img1, caption=None, use_column_width=True)
        with col3:
                st.text("")

        st.subheader("About Us")
        st.markdown("KMeans AI is an Artificial Integlligence and Data Analytics services company with its headquarter in Lagos, Nigeria. In over 10 years of its existence as a tech company, KMeans has served over 5 thousand businesses globally, leveraging on robust technologies in the Data and AI space. With a strong and an experienced team of Data professionals, KMeans bring solutions to real life problems using data driven techniques. For more information about us, visit https://www.kmeansAI.com")
        st.subheader("Meet the team")

        img2 = Image.open('KmeansTeam.png')
        img3 = img2.resize((1500,1000))
        st.image(img3, caption=None, use_column_width=True)
        st.markdown("Asides helping businesses solve real life problems, KMeans AI also have a network of aspiring data professionals from Africa. Being that the entire KMeans AI team is made up of Africans and the organization has gone globally, KMeans AI created the network as a way of giving back to the society that made them. The KMeans AI team train young Africans on various tech paths such as Data Analytics, Data Science, Software Development to mention but a few. KMeans AI also give them the opportunity to intern with them, giving them the opportunity of expereincing how the working environment works.")


        
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()

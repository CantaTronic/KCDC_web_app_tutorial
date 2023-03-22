#/bin/python3

#import the necessary libraries
import streamlit as st
import joblib
import pandas as pd
import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def title(text,size,color):
    st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:center;">{text}</h1>',unsafe_allow_html=True)

def header(text):
    st.markdown(f"<p style='color:grey;'>{text}</p>",unsafe_allow_html=True)

#SET UP THE MAIN WINDOW
st.title('This is a template for your application, based on KCDC open data')

#st.subheader('Introduction')
st.markdown(
"""

<br><br/>
Here is an example of how you can create a simple intro screen for your application. 

Let's remember some basic information about <a href='https://kcdc.iap.kit.edu/'>KCDC</a> here. 

KCDC stands for KASCADE Cosmic Ray Data Centre. It is web portal, where data of KASCADE and other astroparticle physics experiments are published in open access. 

KASCADE was a very successful large detector array which recorded data for over 15 years on site of the KIT-Campus North, Karlsruhe, Germany (formerly Forschungszentrum, Karlsruhe)
at 49,1°N, 8,4°E; 110m a.s.l. KASCADE collected within its lifetime more than 1.7 billion events of which some 433.000.000 survived all quality cuts. 
A two small subsets of these data one can fine in the 'data' folder of the repository you're working with


"""
, unsafe_allow_html=True)
image = Image.open('static/KCDC_Logo.png')
image.thumbnail((295, 213),Image.ANTIALIAS)
st.image(image)

st.markdown('---')

title("Work with datasets", 30, 'black')

header('This is how one can organize an interactive choice of datasets:')

option_1_s = st.selectbox('',[1,2])

title("Dataframe's structure", 24, 'black')

st.write("""
Can be described here. 

Below one can see how can we show some data to our users:
""")
#сread data in the dataframe
if option_1_s == 1:
    df = pd.read_csv('./data/dataset1.csv')
elif option_1_s == 2:
    df = pd.read_csv('./data/dataset2.csv')
else:
    pass
st.write(df.head(10))


title("Dataset parameter distributions", 24, 'black')

st.write("""
Here one can put some code to interactively draw plots of your choice, based of the given data
""")
##################################################################################
option_2_s_2d = st.selectbox('', ['Histogram', 'Electron-muon distribution'])
fig, ax = plt.subplots()
if option_2_s_2d == "Histogram":
    hist = df.lgE.hist(bins=30, alpha=0.5, color = 'r')
    hist.set_title("E spectrum")
    hist.set_xlabel("E")
    hist.set_ylabel("number of events");
elif option_2_s_2d == 'Electron-muon distribution':
    xbins = np.arange(df.lgNmu.min(), df.lgNmu.max(), 0.05) # muons
    ybins = np.arange(df.lgNe.min(), df.lgNe.max(), 0.05) # electrons
    plt.hist2d(df.lgNmu, df.lgNe, bins=[xbins,ybins], cmap = plt.cm.rainbow, norm=mcolors.LogNorm())
    cbar = plt.colorbar()
    ax.set_xlabel("$\\rm{log}_{10}(N_{\\mu})$")
    ax.set_ylabel("$\\rm{log}_{10}(N_{e})}$")
st.pyplot(fig)

st.write('Developed by [V. Tokareva](https://www-kseta.ttp.kit.edu/fellows/Victoria.Tokareva/) for [KCDC](https://kcdc.iap.kit.edu/).')


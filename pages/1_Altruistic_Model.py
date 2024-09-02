#!/usr/bin/env python

import streamlit as st
from misc.numpyro_model import model_main
from misc.prepare_data import get_data
import numpyro
import numpy as np
from streamlit_pdf_viewer import pdf_viewer


st.markdown("# Main Model")

# Get Latex Equation for Model E=mc^2


st.markdown("We model the probability to choose $self$ as the outcome from the following equation:")
         
st.latex(r'''
\begin{equation}
{Pr}[(self; \beta) \succ other]=\Phi\left(\frac{\alpha \times \ln \left(\frac{self}{other}\right)- \gamma \times \ln \left(\frac{\beta}{1-\beta}\right) -\ln (\delta)}{\nu \sqrt{\gamma^2+\alpha^2}}\right)
\end{equation}
    ''')

st.markdown(r"where $\gamma = \frac{\sigma_{\beta}^2}{\sigma_{\beta}^2+\nu^2}$, $\alpha = \frac{\sigma_r^2}{\sigma_r^2+\nu^2}$ and $\hat{b} = \frac{\widehat{\beta}}{1-\widehat{\beta}}$ and $\hat{r} = \frac{\widehat{self}}{\widehat{other}}$.")

# get list of files in plots/individual_predictions_lkj/main
import os
files = os.listdir("plots/individual_predictions_lkj/main")
subject_id = [f.split(".")[0] for f in files]
# sort alphabetically
subject_id = sorted(subject_id)

# drop down menu for subject_ids
subject_id = st.selectbox("Select Subject ID",subject_id)

# print pdf of the subject, located in plots/individual_predictions_lkj/main
st.markdown("## Individual Predictions")
#st.image(f"plots/individual_predictions_lkj/main/{subject_id}.pdf")
pdf_viewer(f"plots/individual_predictions_lkj/main/{subject_id}.pdf")






st.sidebar.markdown("Altruistic Model  ")
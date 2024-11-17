#!/usr/bin/env python

import streamlit as st
import numpy as np
from streamlit_pdf_viewer import pdf_viewer


st.markdown("# Main Model")

# Get Latex Equation for Model E=mc^2


st.markdown("We model the probability to choose $\\text{self}$ as the outcome from the following equation:")
         
st.latex(r'''
\begin{equation}
{Pr}([\text{self} \succ \text{other}])=\Phi\left(\frac{\alpha \times \ln \left(\frac{\text{self}}{\text{other}}\right)- \ln \left(\frac{\beta}{1-\beta}\right) -\ln (\delta)}{\sqrt{\nu_{\frac{\text{self}}{\text{other}}}^2\alpha^2 + \nu_{\frac{\beta}{1-\beta}}^2}}\right)
\end{equation}
    ''')

st.markdown(r"where $\alpha = \frac{1}{1+\nu_{\frac{\text{self}}{\text{other}}}^2}$ and $\delta = \frac{1}{\mu^{\hat{r}^{1-\alpha}}}$")

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
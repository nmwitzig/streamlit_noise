#!/usr/bin/env python

import streamlit as st
import numpy as np
from streamlit_pdf_viewer import pdf_viewer


st.markdown("# Number Comparison Model")

# Get Latex Equation for Model E=mc^2


st.markdown("For number comparison, we model the probability to choose $\text{A}$ as the outcome from the following equation:")
         
st.latex(r'''
\begin{equation}
{Pr}([\text{A} \succ \text{B}]) \times \frac{1}{2}]=\Phi\left(\frac{\alpha' \times \ln \left(\frac{\text{A}}{\text{B}}\right)- \times \ln \left(\frac{1}{2}\right) -\ln (\delta')}{\nu_{\frac{\text{A}}{\text{B}}} \alpha}\right)
\end{equation}
    ''')

st.markdown(r"where $\alpha' = \frac{1}{1+\nu_{\frac{\text{A}}{\text{B}}}^2}$ and $\delta' = \frac{1}{\mu^{\hat{r'}^{1-\alpha'}}}$")

# get list of files in plots/individual_predictions_lkj/main
import os
files = os.listdir("plots/individual_predictions_lkj/number")
subject_id = [f.split(".")[0] for f in files]
# sort alphabetically
subject_id = sorted(subject_id)

# drop down menu for subject_ids
subject_id = st.selectbox("Select Subject ID",subject_id)

# print pdf of the subject, located in plots/individual_predictions_lkj/main
st.markdown("## Individual Predictions")
#st.image(f"plots/individual_predictions_lkj/main/{subject_id}.pdf")
pdf_viewer(f"plots/individual_predictions_lkj/number/{subject_id}.pdf")






st.sidebar.markdown("Number Comparison Model  ")
import streamlit as st
import numpy as np
from scipy.stats import betabinom
import pandas as pd

left_column, right_column = st.columns(2)

with left_column:
    N = st.number_input(
        "Total Turnout",
        value=50_000,
        placeholder="Type a number...",
    )

with right_column:
    n = st.number_input("Sample Size", value=5_000, placeholder="Type a number...")

sample_percent_labour = st.slider(
    "Percentage of Labour vote in the sample",
    min_value=0,
    max_value=100,
    value=50,
    step=1,
)

x = round(sample_percent_labour / 100 * n)

left_2, right_2 = st.columns(2)

with left_2:
    alpha = st.slider(
        "alpha",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
    )

with right_2:
    beta = st.slider(
        "beta",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
    )


st.header("Prior Distribution of Labour Votes")
# calculate prior
k_values = np.arange(0, N + 1)
k_prior = betabinom.pmf(k_values, N, alpha, beta)

prior_chart = pd.DataFrame({"k": k_values, "prior prob": k_prior})
st.line_chart(
    prior_chart,
    x="k",
    y="prior prob",
    x_label="Number of Labour Votes",
    y_label="Prior Probability",
)


st.header("Posterior Distribution of Labour Votes\n Given our sample.")
# calculate posterior
posterior_k_values = np.arange(x, N - n + x + 1)
# or write np.arange(0, N-n+1)
posterior_k_minus_x_values = posterior_k_values - x
k_posterior = betabinom.pmf(posterior_k_minus_x_values, N - n, alpha + x, beta + n - x)

posterior_chart = pd.DataFrame({"k": posterior_k_values, "posterior prob": k_posterior})
st.line_chart(
    posterior_chart,
    x="k",
    y="posterior prob",
    x_label="Number of Labour Votes",
    y_label="Posterior Probability",
)

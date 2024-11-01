import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Function to generate the 3x3 bivariate palette
def generate_bivariate_palette(color_1, color_2, color_3):
    color_1_rgb = mcolors.to_rgb(color_1)
    color_2_rgb = mcolors.to_rgb(color_2)
    color_3_rgb = mcolors.to_rgb(color_3)
    palette = np.zeros((3, 3, 3))

    for i in range(3):
        for j in range(3):
            vertical_blend = np.array(color_1_rgb) * (1 - i / 2) + np.array(color_3_rgb) * (i / 2)
            horizontal_blend = np.array(color_1_rgb) * (1 - j / 2) + np.array(color_2_rgb) * (j / 2)
            palette[i, j] = (vertical_blend + horizontal_blend) / 2

    return palette

# Function to visualize the palette
def visualize_palette(palette):
    fig, ax = plt.subplots(figsize=(3, 3))
    for i in range(3):
        for j in range(3):
            color = palette[i, j]
            hex_color = mcolors.to_hex(color)
            ax.add_patch(plt.Rectangle((j, 2 - i), 1, 1, color=hex_color))
            ax.text(j + 0.5, 2 - i + 0.5, hex_color, ha='center', va='center', fontsize=10,
                    color="white" if np.mean(color) < 0.5 else "black")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Generated Bivariate Palette", fontsize=14)
    plt.gca().invert_yaxis()
    st.pyplot(fig)

# Streamlit app layout
st.title("Bivariate Palette Generator")
st.write("Select three anchor colors to generate a 3x3 bivariate color palette.")

# Color pickers for anchor colors
color_1 = st.color_picker("Select color for 1-1 (low x, low y):", "#dddddd")
color_2 = st.color_picker("Select color for 3-1 (high x, low y):", "#cc0024")
color_3 = st.color_picker("Select color for 1-3 (low x, high y):", "#016eae")

# Generate and display the palette
if st.button("Generate Palette"):
    bivariate_palette = generate_bivariate_palette(color_1, color_2, color_3)
    visualize_palette(bivariate_palette)

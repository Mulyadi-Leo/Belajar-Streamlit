import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Contoh data
data = {
    'Age': [25, 30, 45, 50, 60, 70, 80, 55, 40, 35],
    'Admission Type': ['Emergency', 'Scheduled', 'Scheduled', 'Emergency', 'Emergency', 
                       'Scheduled', 'Emergency', 'Scheduled', 'Emergency', 'Scheduled'],
    'Length of Stay (Days)': [5, 3, 10, 8, 7, 4, 6, 5, 9, 3],
}

df = pd.DataFrame(data)

# Sidebar filter untuk memilih Admission Type
admission_type = st.sidebar.selectbox('Select Admission Type', df['Admission Type'].unique())

# Filter data berdasarkan pilihan Admission Type
filtered_data = df[df['Admission Type'] == admission_type]

# Judul
st.title('Length of Stay (Durasi Rawat Inap)')

# Tampilkan data yang sudah difilter
st.write(f"Showing data for {admission_type} admissions:")
st.write(filtered_data)

# Visualisasi
fig, ax = plt.subplots()
sns.boxplot(x='Admission Type', y='Length of Stay (Days)', data=filtered_data, ax=ax)
ax.set_title(f'Duration of Stay for {admission_type} Admissions')
st.pyplot(fig)

# Saran untuk analisis lanjutan
st.write("You can explore different Admission Types using the filter on the sidebar.")

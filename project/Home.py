import streamlit as st
from PIL import Image
import base64
    
# Injecting CSS for custom fonts, background, and layout
st.markdown(
    """

   <style>
    .main {
        background-color: #FFF4EA
    }
    </style>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap');
    
    /* Button styles */
    .stButton > button {
    background-color: #982B1C; 
    border-radius: 12px;
    padding: 10px 24px;
    color: white; /* Text color */
    font-size: 16px;
    font-family: 'Quicksand', sans-serif;
    font-weight: bold;
    border: none; 
    }

    /* Hover effect for buttons */
    .stButton > button:hover {
    background-color: #800000; 
    color: white; 
    }

    /* Header style */
    header {
        background-color: #800000;
        padding: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    header img {
        max-height: 60px;
        margin-right: 20px;
    }

    header h1 {
        font-family: 'Libre Baskerville', sans-serif;
        font-size: 2.3em;
        color: white;
        text-shadow: 1px 1px 2px #000000;
        margin: 0;
    }
    
    h3 {
        font-family: 'Libre Baskerville', sans-serif;
        font-size: 2em;
        color: #800000;
        justify-content: center;
    }

    p {
        font-family: "Quicksand", system-ui;
        font-size: 1em;
        line-height: 1.5em;
        color: black;
    }

    /* Expander styling */
        .expanderHeader {
            font-family: "Quicksand", sans-serif;
            font-size: 1em;
            color: black;
        }
     .expanderContent {
            font-family: "Quicksand", sans-serif;
            font-size: 1em;
            color: black;
            margin: 10px 0;
        }

    /* Footer styles */
    footer {
        font-family: "Quicksand", system-ui;
        text-align: center;
        padding: 15px;
        background-color: #800000;
        color: white;
        margin-top: 20px;
        font-size: 1em;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Function to convert the image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Convert your logo image to base64
logo_base64 = image_to_base64("logo.png")

st.markdown(f"""
<header style="display: flex; align-items: center;">
    <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="max-height: 60px; margin-right: 20px;">
    <h1>Dengue Outbreak Forecast</h1>
</header>
""", unsafe_allow_html=True)

# Tabs for navigation
tab1, tab2 = st.tabs(["Home", "Factors"])

with tab1:
    # Introduction and images
    with st.container():
     col1, col2 = st.columns([1, 1.3])

     with col1:
            st.image("water_scarcity.jpg", caption="© World Wildlife", width=300)

    with col2:
            st.markdown("""
            ### What is Dengue?
            Dengue, also known as break-bone fever, is a viral infection that spreads and is transmitted through mosquito bites to people. It commonly occurs in tropical and subtropical climates. In addition, it was known to have no specific treatment, therefore, early detection and access to proper medical care can greatly lower fatality rates of dengue, (World Health Organization, 2024).
            """)
    with st.expander("Learn More"):
                            st.markdown("""
            Moreover, dengue fever is considered to be one of the top ten threats to global health (Lowe et al., 2021). Thus, it was reported that there are millions of cases of dengue infection occurring worldwide each year (Mayo Clinic staff, 2024). Therefore, immediate action for prevention and detection must be established.
            """)
    # Global and local water scarcity details
    with st.container():
        col1, col2 = st.columns([1.3, 1])

        with col1:
                st.markdown("""
            ### Dengue in the World
            Dengue fever is an arboviral virus that is considered one of the top ten risks to global health (Lowe et al., 2021). Additionally, according to the World Health Organization (2024) half of the world's population is now at risk of dengue, with an estimated 100–400 million infections occurring each year.
                            """)
            
        with col2:
            st.image("world.jpg", caption="© Unicef", width=300)
        with st.expander("Learn More"):
                            st.markdown("""
            In addition, according to the European Centre for Disease Prevention and Control (2024), there has been a substantial increase in the number of imported cases of dengue to the EU/EEA since the beginning of 2024, resulting in over 12 million dengue cases, and over 8000 dengue-related deaths have been reported from 86 countries. However, there are many endemic countries that have no strong detection and reporting mechanisms, resulting in underestimated detection of dengue globally (World Health Organization, 2024)
            """)
            
    # Philippine water scarcity details
    with st.container():
        col1, col2 = st.columns([1, 1.3])

        with col1:
            st.image("philippine.jpg", caption="© Cebu City Councilor Joel Garganera", width=300)

        with col2:
            st.markdown("""
            ### Dengue in the Philippines
            Dengue still remains as a serious health concern in the Philippines. It was considered to be endemic and during 2008–2012, the country's Department of Health reported an annual average of 117,065 dengue cases which placed the country fourth in dengue burden in southeast Asia (Edillo et al., 2024).
            """)
       
        with st.expander("Learn More"):
            st.markdown("""
        While, from January to December of year 2023 have been reported 657 deaths (case fatality rate, 0.34%). Thus, there is still a need for continued dengue prevention, as the programs for dengue prevention established by the stakeholders were not effective in decreasing the dengue cases. (Cordero, D., 2024). In addition, according to the Department of Health (2024) there is an increase of dengue cases in the Philippines for about 15 %, including 77,867 dengue cases have been logged with 205 deaths as the month of June.
        """)


with tab2:

# Information about the factors

    st.markdown("""    
    ### Waste

    The total amount of rain falling in a specific area within a particular time frame.
    """)

    st.markdown("""    
    ### Flood

    A flood is defined as an overflow of water that submerges land that is usually dry, most of the time as a result of excessive rainfall or storm surges. Floods in the Philippines are some of the common natural occurrences that pose significant risk to people and their physical structures within the region. For instance, as of 2024, areas in the Philippines especially Mindanao are currently affected by significant experiencing floods and landslides due continuous rainfall which has affected 882,861 people of whom 612,234 are displaced. Some of the factors that causes flooding includes deforestation, ineffective waste disposal methods, poor drainage channel and structure designs, Inadequate maintenance of drainage facilities, blockage by debris brought by flood waters and the effects of climate change, which increase rainfall intensity and frequency. Floods are recorded through various methods, including satellite imagery, river gauge or steam gauge readings, and meteorological data collected from weather stations. Such tools are effective towards certain agencies like PAGASA, in determining the water level and forecasting possible flood occurrences. As a result, it has been clear that flood is indeed measurable, as their impact can be quantified in terms of water level or depth, volume of area affected, and duration, providing essential information for an effective disaster response.
    """)

    st.markdown("""        
    ### Rainfall

    The total amount of rain falling in a specific area within a particular time frame.
    """)
    
    st.markdown("""    
    ### Regression Analysis
""")
    
    if st.button("Regression Analysis"):
        st.switch_page("pages/Regression Analysis.py")

# Custom footer
st.markdown("""
<footer>
   Gen. Juan Castaneda Senior High School | © 2025
</footer>
""", unsafe_allow_html=True)

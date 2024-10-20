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
logo_base64 = image_to_base64("dengue_logo.png")

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
            st.image("dengue.jpg", caption="© GMA Integrated News", width=300)

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
            st.image("dengue_world.jpg", caption="© World Health Organization", width=300)
        with st.expander("Learn More"):
                            st.markdown("""
            In addition, according to the European Centre for Disease Prevention and Control (2024), there has been a substantial increase in the number of imported cases of dengue to the EU/EEA since the beginning of 2024, resulting in over 12 million dengue cases, and over 8000 dengue-related deaths have been reported from 86 countries. However, there are many endemic countries that have no strong detection and reporting mechanisms, resulting in underestimated detection of dengue globally (World Health Organization, 2024)
            """)
            
    # Philippine water scarcity details
    with st.container():
        col1, col2 = st.columns([1, 1.3])

        with col1:
            st.image("dengue_philippines.jpg", caption="© GMA Integrated News", width=300)

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

    Everything that no longer serves a purpose and requires disposal is considered waste. The term particularly applies to discarded materials however, there are specific classifications for waste with respect on how they are regulated and handled, especially in professional settings. Additionally, many solid wastes are liquid, semi-solid, or contain gaseous material. Solid wastes are any material that is discarded by being abandoned or thrown away. Furthermore, the Philippine National Statistics Office (NSO) estimated the country's population in 2012 to be around 97 million with an annual growth rate of 1.87%. According to this figure, the Philippines is the 12th largest country in the world today, making the country more prominent to pollution caused by solid wastes. Furthermore, the Ecological Solid Waste Management Act of 2000, Republic Act 9003, was approved on January 26, 2001 and came into effect on February 16, 2001. Ecological Solid Waste Management under the law refers to the systematic administration of activities which provide for segregation at source, segregated transportation, storage, transfer, processing, treatment, and disposal of solid waste and all other waste management activities which do not harm the environment. Consequently, the country has been in several actions to lessen wastes and mitigates the phenomenon they trigger.st
    """)
    
    if st.button("Linear Regression Analysis for Amount of Waste"):
        st.switch_page("pages/Amount of Waste.py")
        
    st.markdown("""    
    ### Heat Index

    Heat Index is also known as the apparent temperature defined as the temperature felt to the human body due to the combined effects of air temperature and humidity. As humidity increases, the heat index also increases, and when the humidity decreases, the heat index also decreases (Arayata, 2024). In addition, according to the Cabato (2024) the heat index in the Philippines is at the peak, scorching 42 to 48 degrees Celsius last May 2024 stated by Philippine Atmospheric, Geophysical, and Astronomical Services Administration (PAGASA). Moreover, according to Baizas (2024) as they analyzed the recorded data from PAGASA, it indicates the extreme temperature of heat index may result in heat stroke if directly exposed to the sun. Thus, if global temperatures continue to rise by 2ºC and repeatedly occur, extreme heat may be expected every two to three years in the Philippines that may lead to various climate issues.
    """)
    
    if st.button("Linear Regression Analysis for Heat Index"):
        st.switch_page("pages/Heat Index.py")
        
    st.markdown("""        
    ### Rainfall

    Rainfall is defined as a measure of rain in a certain period of time. It is considered as one of the main drivers of dengue transmission as mosquitoes require water to reproduce (Benedum, et al., 2018). Moreover, according to Hong (2022) the Philippines is highly vulnerable to the impacts of climate change with the increased frequency of heavy rainfall. This resulted in landslides and floods along with a loss of life and damages to infrastructure. In addition, according to Sherwood (2024) there are past studies which focused on long-term average rain which is not systematically changing globally, and have difficulty measuring the changes of extreme rainfall with accuracy.

    """)
    
    if st.button("Linear Regression Analysis for Amount of Rainfall"):
        st.switch_page("pages/Amount of Rainfall.py")
        
    st.markdown("""    
    ### Regression Analysis
""")
    
    if st.button("Multiple Linear Regression Analysis"):
        st.switch_page("pages/Multiple Linear Regression Analysis.py")
         
# Custom footer
st.markdown("""
<footer>
   Gen. Juan Castañeda Senior High School | © 2025
</footer>
""", unsafe_allow_html=True)

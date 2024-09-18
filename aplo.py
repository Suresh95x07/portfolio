import streamlit as st

# Setting up the page layout and color scheme
st.set_page_config(page_title="Suresh Kumar's Portfolio", layout="wide")


# Function to display the first page (Education and Skills)
def page_one():
    st.title("P T Suresh Kumar")

    # Introduction section with custom background color
    with st.container():
        st.markdown("<h3 style='color: #3498db;'>Dynamic IT Professional | Computer Science Engineer</h3>",
                    unsafe_allow_html=True)
        st.write(
            "A passionate problem-solver with a solid foundation in programming and innovation. "
            "Skilled in AI, Machine Learning, Data Analysis, and Web Development, I am eager to leverage my abilities to tackle complex challenges."
        )

    # Two columns for Education and Contact Info
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Education")
        st.markdown("<h4 style='color: #e74c3c;'>B.E. Computer Science Engineering</h4>", unsafe_allow_html=True)
        st.write("Dr. Ambedkar Institute of Technology (2020 - 2024) - **CGPA: 8.70**")

        st.markdown("<h4 style='color: #e74c3c;'>Pre-University College (Class 12)</h4>", unsafe_allow_html=True)
        st.write("Carmel Pre University College (2018 - 2020) - **Percentage: 90%**")

    with col2:
        st.subheader("Contact Information")
        st.write("- **Email:** [ptsureshkumar2003@gmail.com](mailto:ptsureshkumar2003@gmail.com)")
        st.write("- **Phone:** +91 9986709164")
        st.write("- **Location:** Bengaluru Urban, India")
        st.write("- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/sureshkumar-sureshkumar-b07523202)")

    # Display the Google Drive link for downloading the resume
    st.markdown(
        "<a href='https://drive.google.com/file/d/1ET91OG1FGIxeYtZf8W7WTm4Qe0dgXTb3/view?usp=drive_link' style='color: #27ae60;'>📄 View or Download My Resume</a>",
        unsafe_allow_html=True)

    # Skill Progress Bars with color customization
    st.subheader("Technical Skills")
    st.write("### Skill Proficiency")
    st.markdown("<h5 style='color: #9b59b6;'>Python</h5>", unsafe_allow_html=True)
    st.progress(0.9)
    st.markdown("<h5 style='color: #f39c12;'>Data Structures & Algorithms</h5>", unsafe_allow_html=True)
    st.progress(0.85)
    st.markdown("<h5 style='color: #3498db;'>Machine Learning & Deep Learning</h5>", unsafe_allow_html=True)
    st.progress(0.8)
    st.markdown("<h5 style='color: #2ecc71;'>Database Management (MySQL)</h5>", unsafe_allow_html=True)
    st.progress(0.75)


# Function to display the second page (Projects)
def page_two():
    st.title("P T Suresh Kumar - Projects")

    st.subheader("Projects Overview")
    st.write(
        "Explore some of the key projects I have worked on. These projects showcase my ability to implement complex solutions using various technologies.")

    # Use selectbox for interactive project selection
    project = st.selectbox("Choose a project to view details:",
                           ["Cipher Mine", "Hostel Management System", "Railway Track Fault Detection System"])

    if project == "Cipher Mine":
        st.markdown("<h4 style='color: #8e44ad;'>Cipher Mine: Decrypting Hidden Knowledge from Complex Data Sets</h4>",
                    unsafe_allow_html=True)
        st.write("**Timeframe:** Sept 2022 - Oct 2022")
        st.write("Focused on data mining techniques to uncover valuable insights from hidden datasets.")

    elif project == "Hostel Management System":
        st.markdown("<h4 style='color: #d35400;'>Hostel Management System Using Database System</h4>",
                    unsafe_allow_html=True)
        st.write("**Timeframe:** May 2023 - Jun 2023")
        st.write("Developed a hostel management system using PHP, HTML, and MySQL for efficient hostel operations.")

    elif project == "Railway Track Fault Detection System":
        st.markdown("<h4 style='color: #2980b9;'>Railway Track Fault Detection System Using Deep Learning</h4>",
                    unsafe_allow_html=True)
        st.write("**Timeframe:** Mar 2024 - Jun 2024")
        st.write(
            "Designed and developed a fault detection system for railways using deep learning techniques and Python.")


# Function to display the third page (Internships, Certifications, and Contact)
def page_three():
    st.title("P T Suresh Kumar - Internships & Certifications")

    st.subheader("Internships")
    st.markdown("<h4 style='color: #e74c3c;'>IBM-Edunet Foundation</h4>", unsafe_allow_html=True)
    st.write("**Role:** Artificial Intelligence Intern (Aug 2023 - Oct 2023)")
    st.write("Worked on AI research and applied machine learning models to solve real-world problems.")

    st.markdown("<h4 style='color: #2ecc71;'>AmberTAG Analytics Private Limited</h4>", unsafe_allow_html=True)
    st.write("**Role:** Data Analyst & Developer (Mar 2024 - Jun 2024)")
    st.write("Analyzed data and developed solutions for content curation using data-driven insights.")

    st.subheader("Certifications")
    st.write("- **Data Mining** (Jun 2022 - Sept 2022)")
    st.write("- **Programming with C and C++** (Mar 2022 - Jun 2022)")
    st.write("- **Deep Learning** (Dec 2024)")
    st.write("- **Python** (Jan 2023 - Mar 2023)")

    # Contact Form section
    st.subheader("Contact Me")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        st.success(f"Thank you {name}! Your message has been sent.")


# Sidebar navigation to switch between pages
st.sidebar.title("Portfolio Navigation")
page = st.sidebar.radio("Go to:",
                        ["Page 1: Education & Skills", "Page 2: Projects", "Page 3: Internships & Certifications"])

# Rendering the selected page
if page == "Page 1: Education & Skills":
    page_one()
elif page == "Page 2: Projects":
    page_two()
elif page == "Page 3: Internships & Certifications":
    page_three()

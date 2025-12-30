import streamlit as st

st.set_page_config(
    page_title="Numerology Prediction 2026",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default menu and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("🔮 Numerology Prediction 2026")

# ---------- INPUT ----------
name = st.text_input("Enter your name")
day_input = st.text_input("Enter day of birth (1–31)")
month_input = st.text_input("Enter month of birth (1–12)")

if st.button("Get Prediction"):

    # ---------- VALIDATION ----------
    if not name:
        st.warning("Please enter your name.")
    elif not day_input.isdigit() or int(day_input) < 1 or int(day_input) > 31:
        st.warning("Enter a valid day (1–31).")
    elif not month_input.isdigit() or int(month_input) < 1 or int(month_input) > 12:
        st.warning("Enter a valid month (1–12).")
    else:
        day = f"{int(day_input):02d}"
        month = f"{int(month_input):02d}"

        # ---------- DRIVER NUMBER ----------
        driver = int(day[0]) + int(day[1])
        while driver > 9:
            driver = sum(int(d) for d in str(driver))

        # ---------- PERSONAL YEAR 2026 ----------
        day_sum = int(day[0]) + int(day[1])
        month_sum = int(month[0]) + int(month[1])
        year_sum = 2 + 0 + 2 + 6
        personal_year = day_sum + month_sum + year_sum
        while personal_year > 9:
            personal_year = sum(int(d) for d in str(personal_year))

        # ---------- PREDICTIONS ----------
        predictions = {
            1:{1:"A powerful year to start fresh Leadership and new beginnings.",2:"Progress comes through patience, Partnerships need patience.",3:"Creativity, communication and social success.",4:"Hard work, discipline required. Strong foundation for future.",5:"Sudden Change and travel, and opportunities demand flexibility and courage.",6:"Focus on family, responsibility and relationships.",7:"Inner growth, learning, spirituality.",8:"Career power, authority, and financial gains.",9:"Completion year, release of the past and new cycle preparation."},
            2:{1:"Balanced leadership, require confidence and independent decision.",2:"Strong relationships, emotional growth, patience bring success.",3:"Joy and communication, improve relationship.",4:"Slow steady work, discipline and consistent effort.",5:"Emotional changes, change in lifestyle.",6:"Family harmony. Love and responsibilities take priority.",7:"Spiritual growth. Inner healing, intuition.",8:"Financial balance improve, career progress.",9:"Emotional closure, forgiveness, letting go bring peace."},
            3:{1:"Confident start, A strong year to launch idea.",2:"Diplomacy wins, Cooperation and patience help creative plans grow.",3:"Best creative year, Success through communication and social recognition.",4:"Focus and Discipline are needed to turn talent into result.",5:"Fun and movement. Exciting changes, travel and new opportunities boost growth.",6:"Love grows. Family responsibility and emotional balance become important.",7:"Self-reflection, learning, spiritual.",8:"Recognition, authority and financial rewards increase.",9:"Creative endings, completion of projects."},
            4:{1:"Foundation building. Begin new projects with focus, determination and planning.",2:"Team support and patience helps in growth.",3:"Delayed rewards. Creativity and communication bring progress but discipline is needed.",4:"Very demanding year. Hard work and structure lead to solid achievements.",5:"Sudden disruptions, Adapt to change.",6:"Home duties. Family and community require care and attention.",7:"Learning phase.",8:"Money discipline. Career advancement and financial rewards come through effort.",9:"Work completion. Letting go and preparation for a new cycle."},
            5:{1:"Fresh energy. A dynamic year to start new adventures and take bold steps.",2:"Emotional balance and patience for relationships and partnerships.",3:"Enjoyment and travel. Creativity, socializing, and communication bring opportunities.",4:"Restrictions. Focus and discipline needed.",5:"Major transformation. Freedom and travel.",6:"Relationship focus. Responsibilities require attention.",7:"Pause year. Learning and spiritual growth.",8:"Career and financial success come from strategy and effort.",9:"Release past. Letting go and preparation for transformation."},
            6:{1:"New Responsible start. Relationship or career with care.",2:"Emotional care. Patience, cooperation and diplomacy strengthen partnerships and bond.",3:"Family happiness. Express creativity and communicate love to attract harmony.",4:"Heavy duties. Hard work and discipline bring stability in home and career.",5:"Domestic change. Changes in lifestyle and responsibilities require flexibility and balance.",6:"Best family year. Focus on Family.",7:"Healing year. Personal growth.",8:"Material success. Authority, career progress.",9:"Completion, letting go, and emotional closure prepare for new cycle."},
            7:{1:"Wise beginnings and personal growth.",2:"Trust intuition. Focus on patience, partnerships and emotional balance.",3:"Spiritual creativity bring unexpected joy.",4:"Hard work and discipline stabilize your foundation.",5:"Inner change, travel and new experiences.",6:"Emotional healing. Responsibilities toward family and community take priority.",7:"Deep spirituality.",8:"Career planning. Material success peak, power must be balanced.",9:"Letting go. Preparing for new cycle."},
            8:{1:"Authority rises. Launch new ventures with confidence.",2:"Collaboration and diplomacy are key, avoid impulsive decisions.",3:"Public recognition. Creativity and communication bring growth.",4:"Hard-earned gains.",5:"Risk brings reward. Stay flexible.",6:"Work-life balance. Focus on responsibilities.",7:"Inner strength. Reflection and strategy improve long term goals.",8:"Peak success year. Handle authority wisely.",9:"Goal completion. Release what no longer serves you, prepare for transformation."},
            9:{1:"New vision. Begin a journey of personal growth and humanitarian pursuits.",2:"High sensitivity. Patience, cooperation and emotional understanding are essential.",3:"Creative closure. Joy and social connections expand.",4:"Finish duties. Hard work and discipline strengthen foundations and responsibilities.",5:"Embrace freedom, change, and new experience with adaptability.",6:"Service year. Focus on family, community and compassionate service.",7:"Detachment. Reflection, spiritual growth and deep introspection define this year.",8:"Results year. Leadership and material rewards come through strategic action.",9:"Major transformation. Completion, letting go, humanitarian impact peaks."}
        }

        st.success(f"Hello {name}")
        st.write("**Driver Number:**", driver)
        st.write("**Personal Year (2026):**", personal_year)
        st.write("### 🔮 Prediction")
        st.info(predictions[driver][personal_year])


import streamlit as st
import altair as alt
import pandas as pd
import json

st.set_page_config(
    page_title="AI Transformation Timeline",
    page_icon=":material/timeline:",
    layout="wide",
)

st.title("AI Transformation News Hub")
st.caption("Headlines from 2027-2030 · Powered by Snowflake Cortex Agents")

# Main navigation
main_tab1, main_tab2 = st.tabs(["Timeline", "Cortex Agents"])

# Embedded data from Snowflake
ARTICLES_DATA = [
    {"article_id":8,"author_name":"Sophie Laurent","days_trending":18,"economic_optimism":0.42,"employment_outlook":0.15,"fear_index":0.52,"geographic_focus":"United States","headline":"Anthropic's Claude-5 Passes Bar Exam, Medical Boards Simultaneously","hope_index":0.65,"overall_sentiment":0.55,"publication_name":"Wired","publish_date":"2027-02-14","publish_year":2027,"reading_time_minutes":9,"social_shares":1245000,"subheadline":"Latest AI system demonstrates professional-level competence across multiple domains","topic_category":"AI Development","total_views":5620000,"word_count":2100},
    {"article_id":2,"author_name":"Elena Kowalski","days_trending":8,"economic_optimism":0.25,"employment_outlook":-0.78,"fear_index":0.68,"geographic_focus":"Global","headline":"Goldman Sachs Replaces 40% of Analysts with AI Systems","hope_index":0.32,"overall_sentiment":-0.42,"publication_name":"Financial Times","publish_date":"2027-03-22","publish_year":2027,"reading_time_minutes":8,"social_shares":456000,"subheadline":"Wall Street's largest workforce reduction in history signals new era for finance","topic_category":"Finance","total_views":2340000,"word_count":1800},
    {"article_id":1,"author_name":"Marcus Williams","days_trending":14,"economic_optimism":-0.72,"employment_outlook":-0.85,"fear_index":0.82,"geographic_focus":"United States","headline":"The Great Displacement Begins: 2.3 Million US Jobs Lost to AI in Q1 2027","hope_index":0.18,"overall_sentiment":-0.65,"publication_name":"The New York Times","publish_date":"2027-04-15","publish_year":2027,"reading_time_minutes":14,"social_shares":892000,"subheadline":"White-collar workers bear the brunt as AI agents transform corporate America overnight","topic_category":"Employment","total_views":4850000,"word_count":3200},
    {"article_id":3,"author_name":"Liu Wei","days_trending":6,"economic_optimism":0.52,"employment_outlook":-0.45,"fear_index":0.42,"geographic_focus":"China","headline":"China Unveils Fully Automated Port, Zero Human Workers","hope_index":0.58,"overall_sentiment":0.38,"publication_name":"South China Morning Post","publish_date":"2027-06-08","publish_year":2027,"reading_time_minutes":11,"social_shares":312000,"subheadline":"Shanghai's new terminal processes 50,000 containers daily without human intervention","topic_category":"Infrastructure","total_views":1560000,"word_count":2500},
    {"article_id":4,"author_name":"Rachel Thompson","days_trending":11,"economic_optimism":-0.25,"employment_outlook":-0.35,"fear_index":0.55,"geographic_focus":"Europe","headline":"Universal Basic Income Trials Expand to 15 Countries","hope_index":0.52,"overall_sentiment":0.15,"publication_name":"The Guardian","publish_date":"2027-08-19","publish_year":2027,"reading_time_minutes":12,"social_shares":578000,"subheadline":"Finland leads Europe in responding to AI-driven unemployment crisis","topic_category":"Policy","total_views":3210000,"word_count":2800},
    {"article_id":6,"author_name":"James Okonkwo","days_trending":12,"economic_optimism":0.45,"employment_outlook":-0.15,"fear_index":0.58,"geographic_focus":"Global","headline":"The $50 Trillion Question: How AI Will Reshape Global GDP by 2030","hope_index":0.48,"overall_sentiment":0.28,"publication_name":"The Economist","publish_date":"2027-09-14","publish_year":2027,"reading_time_minutes":23,"social_shares":534000,"subheadline":"Economists scramble to model unprecedented productivity gains","topic_category":"Economics","total_views":2780000,"word_count":5200},
    {"article_id":7,"author_name":"Thomas Müller","days_trending":7,"economic_optimism":-0.68,"employment_outlook":-0.82,"fear_index":0.78,"geographic_focus":"Germany","headline":"Germany's Mittelstand Faces Extinction as AI Disrupts Manufacturing","hope_index":0.22,"overall_sentiment":-0.72,"publication_name":"Der Spiegel","publish_date":"2027-11-28","publish_year":2027,"reading_time_minutes":17,"social_shares":278000,"subheadline":"Family-owned businesses struggle to compete with AI-powered megafactories","topic_category":"Manufacturing","total_views":1450000,"word_count":3800},
    {"article_id":5,"author_name":"Dr. Amelia Foster","days_trending":9,"economic_optimism":0.75,"employment_outlook":0.35,"fear_index":0.15,"geographic_focus":"Global","headline":"AI Drug Discovery Produces 47 New Compounds in Single Year","hope_index":0.88,"overall_sentiment":0.82,"publication_name":"Nature","publish_date":"2027-12-03","publish_year":2027,"reading_time_minutes":20,"social_shares":423000,"subheadline":"Pharmaceutical industry transformed as machine learning accelerates research timelines by 90%","topic_category":"Healthcare","total_views":1890000,"word_count":4500},
    {"article_id":9,"author_name":"Dr. Ahmed Hassan","days_trending":15,"economic_optimism":-0.55,"employment_outlook":-0.62,"fear_index":0.75,"geographic_focus":"United States","headline":"The Productivity Paradox: GDP Soars While Middle Class Shrinks","hope_index":0.28,"overall_sentiment":-0.48,"publication_name":"The Atlantic","publish_date":"2028-01-23","publish_year":2028,"reading_time_minutes":28,"social_shares":678000,"subheadline":"Economic growth masks deepening inequality as AI wealth concentrates","topic_category":"Economics","total_views":3450000,"word_count":6200},
    {"article_id":10,"author_name":"Dr. Yuki Tanaka","days_trending":6,"economic_optimism":0.28,"employment_outlook":0.18,"fear_index":0.45,"geographic_focus":"Japan","headline":"Japan Deploys 500,000 Care Robots as Population Ages","hope_index":0.58,"overall_sentiment":0.42,"publication_name":"Nikkei Asia","publish_date":"2028-03-11","publish_year":2028,"reading_time_minutes":13,"social_shares":234000,"subheadline":"Elder care crisis met with unprecedented automation initiative","topic_category":"Healthcare","total_views":1280000,"word_count":2900},
    {"article_id":12,"author_name":"Priya Sharma","days_trending":9,"economic_optimism":0.18,"employment_outlook":0.28,"fear_index":0.42,"geographic_focus":"Europe","headline":"EU Passes Landmark AI Workforce Transition Act","hope_index":0.55,"overall_sentiment":0.35,"publication_name":"Reuters","publish_date":"2028-04-29","publish_year":2028,"reading_time_minutes":14,"social_shares":512000,"subheadline":"Mandatory retraining programs and AI taxation reshape European labor markets","topic_category":"Policy","total_views":2890000,"word_count":3100},
    {"article_id":11,"author_name":"Isabella Rodriguez","days_trending":10,"economic_optimism":0.82,"employment_outlook":0.25,"fear_index":0.35,"geographic_focus":"United States","headline":"OpenAI Valued at $800 Billion, Surpasses Saudi Aramco","hope_index":0.72,"overall_sentiment":0.65,"publication_name":"Bloomberg","publish_date":"2028-05-07","publish_year":2028,"reading_time_minutes":7,"social_shares":892000,"subheadline":"AI company becomes world's most valuable private enterprise","topic_category":"Business","total_views":4120000,"word_count":1500},
    {"article_id":13,"author_name":"Marcus Williams","days_trending":21,"economic_optimism":-0.42,"employment_outlook":-0.88,"fear_index":0.85,"geographic_focus":"Global","headline":"The Death of the Entry-Level Job","hope_index":0.15,"overall_sentiment":-0.58,"publication_name":"The New York Times","publish_date":"2028-07-16","publish_year":2028,"reading_time_minutes":18,"social_shares":1120000,"subheadline":"How AI eliminated the first rung on the corporate ladder","topic_category":"Employment","total_views":5890000,"word_count":4100},
    {"article_id":14,"author_name":"David Park","days_trending":7,"economic_optimism":0.55,"employment_outlook":-0.65,"fear_index":0.58,"geographic_focus":"United States","headline":"Autonomous Trucks Now Handle 60% of US Freight","hope_index":0.42,"overall_sentiment":0.22,"publication_name":"TechCrunch","publish_date":"2028-08-22","publish_year":2028,"reading_time_minutes":8,"social_shares":389000,"subheadline":"Trucking industry transformation complete years ahead of predictions","topic_category":"Transportation","total_views":2150000,"word_count":1900},
    {"article_id":15,"author_name":"Dr. Sarah Chen","days_trending":8,"economic_optimism":0.62,"employment_outlook":0.35,"fear_index":0.38,"geographic_focus":"United States","headline":"AI-Generated Patents Now Outnumber Human Inventions","hope_index":0.65,"overall_sentiment":0.48,"publication_name":"MIT Technology Review","publish_date":"2028-10-05","publish_year":2028,"reading_time_minutes":15,"social_shares":312000,"subheadline":"USPTO struggles with flood of machine-created intellectual property","topic_category":"Innovation","total_views":1680000,"word_count":3400},
    {"article_id":16,"author_name":"James Okonkwo","days_trending":11,"economic_optimism":0.78,"employment_outlook":0.45,"fear_index":0.28,"geographic_focus":"Singapore","headline":"Singapore Becomes First 'AI-Native' Economy","hope_index":0.82,"overall_sentiment":0.72,"publication_name":"The Economist","publish_date":"2028-11-18","publish_year":2028,"reading_time_minutes":21,"social_shares":478000,"subheadline":"City-state achieves 80% AI integration across all government services","topic_category":"Policy","total_views":2450000,"word_count":4800},
    {"article_id":17,"author_name":"Rachel Thompson","days_trending":13,"economic_optimism":0.15,"employment_outlook":0.35,"fear_index":0.55,"geographic_focus":"Global","headline":"The Great Retraining: 50 Million Workers Begin AI Adaptation Programs","hope_index":0.48,"overall_sentiment":0.25,"publication_name":"The Guardian","publish_date":"2029-01-09","publish_year":2029,"reading_time_minutes":16,"social_shares":712000,"subheadline":"Largest workforce transformation in human history enters second phase","topic_category":"Employment","total_views":3890000,"word_count":3600},
    {"article_id":18,"author_name":"Elena Kowalski","days_trending":7,"economic_optimism":0.45,"employment_outlook":-0.28,"fear_index":0.62,"geographic_focus":"Global","headline":"AI Hedge Funds Control 45% of Global Trading Volume","hope_index":0.38,"overall_sentiment":0.18,"publication_name":"Financial Times","publish_date":"2029-02-28","publish_year":2029,"reading_time_minutes":12,"social_shares":356000,"subheadline":"Human traders become supervisory minority in financial markets","topic_category":"Finance","total_views":1980000,"word_count":2700},
    {"article_id":19,"author_name":"Priya Sharma","days_trending":9,"economic_optimism":0.72,"employment_outlook":-0.35,"fear_index":0.35,"geographic_focus":"Global","headline":"Farming Without Farmers: AI Agriculture Feeds 2 Billion","hope_index":0.72,"overall_sentiment":0.58,"publication_name":"Reuters","publish_date":"2029-04-14","publish_year":2029,"reading_time_minutes":17,"social_shares":512000,"subheadline":"Automated vertical farms and robotic harvesters transform food production","topic_category":"Agriculture","total_views":2680000,"word_count":3900},
    {"article_id":20,"author_name":"Sophie Laurent","days_trending":22,"economic_optimism":0.35,"employment_outlook":-0.55,"fear_index":0.65,"geographic_focus":"United States","headline":"Hollywood's AI Actors Generate $12 Billion in Revenue","hope_index":0.42,"overall_sentiment":-0.22,"publication_name":"Wired","publish_date":"2029-06-21","publish_year":2029,"reading_time_minutes":10,"social_shares":1450000,"subheadline":"Synthetic performers dominate box office as Screen Actors Guild negotiates survival","topic_category":"Entertainment","total_views":6250000,"word_count":2300},
    {"article_id":21,"author_name":"Isabella Rodriguez","days_trending":18,"economic_optimism":-0.82,"employment_outlook":-0.45,"fear_index":0.88,"geographic_focus":"Global","headline":"The New Gilded Age: AI Billionaires Now Control 40% of Global Wealth","hope_index":0.12,"overall_sentiment":-0.75,"publication_name":"Bloomberg","publish_date":"2029-07-30","publish_year":2029,"reading_time_minutes":24,"social_shares":978000,"subheadline":"Wealth concentration accelerates as technology founders amass unprecedented fortunes","topic_category":"Economics","total_views":4580000,"word_count":5500},
    {"article_id":22,"author_name":"James Okonkwo","days_trending":10,"economic_optimism":0.85,"employment_outlook":0.55,"fear_index":0.22,"geographic_focus":"India","headline":"India Leapfrogs to AI Economy, Adds 200 Million to Middle Class","hope_index":0.85,"overall_sentiment":0.78,"publication_name":"The Economist","publish_date":"2029-09-08","publish_year":2029,"reading_time_minutes":19,"social_shares":423000,"subheadline":"Developing nation bypasses traditional industrialization with AI-first strategy","topic_category":"Economics","total_views":2150000,"word_count":4200},
    {"article_id":23,"author_name":"Dr. Amelia Foster","days_trending":8,"economic_optimism":0.25,"employment_outlook":0.18,"fear_index":0.52,"geographic_focus":"Global","headline":"AI Therapists Now Treat 30% of Mental Health Patients","hope_index":0.55,"overall_sentiment":0.32,"publication_name":"Nature","publish_date":"2029-10-17","publish_year":2029,"reading_time_minutes":13,"social_shares":345000,"subheadline":"Shortage of human practitioners drives adoption of AI counseling systems","topic_category":"Healthcare","total_views":1890000,"word_count":3000},
    {"article_id":24,"author_name":"Dr. Sarah Chen","days_trending":9,"economic_optimism":0.68,"employment_outlook":0.22,"fear_index":0.42,"geographic_focus":"Global","headline":"The Algorithm That Runs the World's Supply Chains","hope_index":0.62,"overall_sentiment":0.52,"publication_name":"MIT Technology Review","publish_date":"2029-11-25","publish_year":2029,"reading_time_minutes":20,"social_shares":456000,"subheadline":"How one AI system coordinates global logistics with superhuman efficiency","topic_category":"Logistics","total_views":2340000,"word_count":4600},
    {"article_id":25,"author_name":"Dr. Ahmed Hassan","days_trending":28,"economic_optimism":0.22,"employment_outlook":-0.18,"fear_index":0.48,"geographic_focus":"Global","headline":"Five Years Later: The Winners and Losers of AI Transformation","hope_index":0.52,"overall_sentiment":0.15,"publication_name":"The Atlantic","publish_date":"2030-01-15","publish_year":2030,"reading_time_minutes":36,"social_shares":1680000,"subheadline":"Comprehensive analysis of how AI reshaped the global economy since 2025","topic_category":"Economics","total_views":7850000,"word_count":8200},
    {"article_id":26,"author_name":"Dr. Amelia Foster","days_trending":12,"economic_optimism":0.72,"employment_outlook":0.45,"fear_index":0.18,"geographic_focus":"Global","headline":"AI Scientists Make Nobel-Worthy Discovery Without Human Input","hope_index":0.92,"overall_sentiment":0.85,"publication_name":"Nature","publish_date":"2030-03-04","publish_year":2030,"reading_time_minutes":17,"social_shares":678000,"subheadline":"Machine learning system identifies New physics principles independently","topic_category":"Science","total_views":3250000,"word_count":3800},
    {"article_id":27,"author_name":"Rachel Thompson","days_trending":11,"economic_optimism":0.55,"employment_outlook":0.48,"fear_index":0.28,"geographic_focus":"Denmark","headline":"The Post-Work Society: Denmark's Universal Basic Services Model","hope_index":0.78,"overall_sentiment":0.68,"publication_name":"The Guardian","publish_date":"2030-04-22","publish_year":2030,"reading_time_minutes":23,"social_shares":545000,"subheadline":"Scandinavian nation pioneers life beyond traditional employment","topic_category":"Policy","total_views":2890000,"word_count":5100},
    {"article_id":28,"author_name":"Priya Sharma","days_trending":10,"economic_optimism":0.35,"employment_outlook":0.42,"fear_index":0.52,"geographic_focus":"Global","headline":"Global Unemployment Peaks at 18%, Then Stabilizes","hope_index":0.55,"overall_sentiment":0.28,"publication_name":"Reuters","publish_date":"2030-05-31","publish_year":2030,"reading_time_minutes":15,"social_shares":612000,"subheadline":"Labor economists see signs of new equilibrium in transformed job market","topic_category":"Employment","total_views":3450000,"word_count":3300},
    {"article_id":29,"author_name":"Elena Kowalski","days_trending":8,"economic_optimism":0.22,"employment_outlook":0.15,"fear_index":0.55,"geographic_focus":"United States","headline":"AI Governance: How Algorithms Now Write Most Business Regulations","hope_index":0.45,"overall_sentiment":-0.15,"publication_name":"Financial Times","publish_date":"2030-07-09","publish_year":2030,"reading_time_minutes":19,"social_shares":398000,"subheadline":"Regulatory agencies increasingly rely on AI to draft and enforce rules","topic_category":"Policy","total_views":2150000,"word_count":4400},
    {"article_id":30,"author_name":"Marcus Williams","days_trending":16,"economic_optimism":0.28,"employment_outlook":0.52,"fear_index":0.45,"geographic_focus":"Global","headline":"The Children of AI: First Generation Raised with AI Tutors Enters Workforce","hope_index":0.55,"overall_sentiment":0.35,"publication_name":"The New York Times","publish_date":"2030-08-18","publish_year":2030,"reading_time_minutes":26,"social_shares":892000,"subheadline":"Cohort educated entirely by AI systems shows remarkable capabilities and gaps","topic_category":"Education","total_views":4250000,"word_count":5800},
    {"article_id":31,"author_name":"Liu Wei","days_trending":19,"economic_optimism":0.35,"employment_outlook":0.25,"fear_index":0.58,"geographic_focus":"Global","headline":"China and US Reach AI Arms Control Agreement","hope_index":0.52,"overall_sentiment":0.45,"publication_name":"South China Morning Post","publish_date":"2030-09-27","publish_year":2030,"reading_time_minutes":11,"social_shares":1250000,"subheadline":"Superpowers agree to limit autonomous weapons development after near-miss incidents","topic_category":"Geopolitics","total_views":5680000,"word_count":2600},
    {"article_id":34,"author_name":"Michael O'Brien","days_trending":9,"economic_optimism":0.68,"employment_outlook":0.65,"fear_index":0.18,"geographic_focus":"United States","headline":"The Quiet Revolution: How Small Towns Thrived in the AI Era","hope_index":0.88,"overall_sentiment":0.75,"publication_name":"AI Weekly","publish_date":"2030-10-20","publish_year":2030,"reading_time_minutes":15,"social_shares":356000,"subheadline":"Remote work and AI tools enable rural renaissance across America","topic_category":"Society","total_views":1890000,"word_count":3500},
    {"article_id":32,"author_name":"Sophie Laurent","days_trending":11,"economic_optimism":0.58,"employment_outlook":0.78,"fear_index":0.22,"geographic_focus":"Global","headline":"The Human Premium: Why Some Jobs Became More Valuable","hope_index":0.85,"overall_sentiment":0.72,"publication_name":"Wired","publish_date":"2030-11-06","publish_year":2030,"reading_time_minutes":14,"social_shares":589000,"subheadline":"Craftspeople, therapists, and artists command unprecedented salaries in AI age","topic_category":"Employment","total_views":3120000,"word_count":3200},
    {"article_id":33,"author_name":"Isabella Rodriguez","days_trending":8,"economic_optimism":0.78,"employment_outlook":0.35,"fear_index":0.32,"geographic_focus":"Global","headline":"AI Economy Reaches $25 Trillion: Larger Than US GDP","hope_index":0.72,"overall_sentiment":0.62,"publication_name":"Bloomberg","publish_date":"2030-12-12","publish_year":2030,"reading_time_minutes":9,"social_shares":534000,"subheadline":"Artificial intelligence industry becomes world's biggest economic sector","topic_category":"Business","total_views":2780000,"word_count":2000},
]

df = pd.DataFrame(ARTICLES_DATA)
df["publish_date"] = pd.to_datetime(df["publish_date"])

# ============================================
# TAB 1: Timeline
# ============================================
with main_tab1:
    st.subheader("AI Transformation Headlines: 2027-2030")
    st.caption("Mouse over any article to see details")
    
    # Sidebar filters
    with st.sidebar:
        st.header("Filters")
        
        years = st.multiselect(
            "Year",
            options=sorted(df["publish_year"].unique()),
            default=sorted(df["publish_year"].unique()),
        )
        
        topics = st.multiselect(
            "Topic",
            options=sorted(df["topic_category"].unique()),
            default=sorted(df["topic_category"].unique()),
        )
        
        sentiment_range = st.slider(
            "Sentiment range",
            min_value=-1.0,
            max_value=1.0,
            value=(-1.0, 1.0),
            step=0.1,
        )

    # Apply filters
    filtered_df = df[
        (df["publish_year"].isin(years)) &
        (df["topic_category"].isin(topics)) &
        (df["overall_sentiment"] >= sentiment_range[0]) &
        (df["overall_sentiment"] <= sentiment_range[1])
    ].copy()

    # Format views for tooltip
    filtered_df["views_formatted"] = filtered_df["total_views"].apply(
        lambda x: f"{x/1_000_000:.1f}M" if x >= 1_000_000 else f"{x/1_000:.0f}K"
    )

    # Create sentiment category for coloring
    def sentiment_label(val):
        if val <= -0.3:
            return "Negative"
        elif val >= 0.3:
            return "Positive"
        return "Neutral"

    filtered_df["sentiment_label"] = filtered_df["overall_sentiment"].apply(sentiment_label)

    # Summary stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Articles", len(filtered_df))
    with col2:
        st.metric("Total views", f"{filtered_df['total_views'].sum()/1_000_000:.1f}M")
    with col3:
        avg_sentiment = filtered_df["overall_sentiment"].mean()
        st.metric("Avg sentiment", f"{avg_sentiment:.2f}")
    with col4:
        st.metric("Social shares", f"{filtered_df['social_shares'].sum()/1_000_000:.1f}M")

    st.write("")

    # Timeline chart with Altair
    base = alt.Chart(filtered_df).encode(
        x=alt.X(
            "publish_date:T",
            title="Publication date",
            axis=alt.Axis(format="%b %Y", labelAngle=-45),
        ),
        y=alt.Y(
            "topic_category:N",
            title="Topic",
            sort=sorted(filtered_df["topic_category"].unique()),
        ),
        color=alt.Color(
            "sentiment_label:N",
            title="Sentiment",
            scale=alt.Scale(
                domain=["Negative", "Neutral", "Positive"],
                range=["#e74c3c", "#95a5a6", "#27ae60"],
            ),
            legend=alt.Legend(orient="top"),
        ),
        size=alt.Size(
            "total_views:Q",
            title="Views",
            scale=alt.Scale(range=[100, 1000]),
            legend=None,
        ),
        tooltip=[
            alt.Tooltip("headline:N", title="Headline"),
            alt.Tooltip("subheadline:N", title="Summary"),
            alt.Tooltip("publication_name:N", title="Publication"),
            alt.Tooltip("author_name:N", title="Author"),
            alt.Tooltip("publish_date:T", title="Date", format="%B %d, %Y"),
            alt.Tooltip("topic_category:N", title="Topic"),
            alt.Tooltip("views_formatted:N", title="Views"),
            alt.Tooltip("overall_sentiment:Q", title="Sentiment", format=".2f"),
            alt.Tooltip("reading_time_minutes:Q", title="Read time (min)"),
        ],
    )

    points = base.mark_circle(opacity=0.8, stroke="white", strokeWidth=1)

    chart = (
        points
        .properties(height=500)
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    # Year breakdown
    st.subheader("Articles by year")

    year_tabs = st.tabs([str(y) for y in sorted(filtered_df["publish_year"].unique())])

    for tab, year in zip(year_tabs, sorted(filtered_df["publish_year"].unique())):
        with tab:
            year_df = filtered_df[filtered_df["publish_year"] == year].sort_values("publish_date")
            
            for _, row in year_df.iterrows():
                sentiment = row["overall_sentiment"]
                if sentiment <= -0.3:
                    badge_color = "red"
                    badge_text = "Negative"
                elif sentiment >= 0.3:
                    badge_color = "green"
                    badge_text = "Positive"
                else:
                    badge_color = "gray"
                    badge_text = "Neutral"
                
                with st.container(border=True):
                    st.markdown(f"**{row['headline']}**")
                    st.caption(f"{row['publication_name']} · {row['author_name']} · {row['publish_date'].strftime('%B %d, %Y')}")
                    st.write(row["subheadline"])
                    
                    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
                    with mcol1:
                        if badge_color == "red":
                            st.markdown(f":red[{badge_text}]")
                        elif badge_color == "green":
                            st.markdown(f":green[{badge_text}]")
                        else:
                            st.markdown(f":gray[{badge_text}]")
                    with mcol2:
                        st.caption(f"{row['views_formatted']} views")
                    with mcol3:
                        st.caption(f"{row['social_shares']:,} shares")
                    with mcol4:
                        st.caption(f"{row['reading_time_minutes']} min read")

# ============================================
# TAB 2: Cortex Agents
# ============================================
with main_tab2:
    st.subheader("Snowflake Cortex Agents")
    st.markdown("""
    This application is powered by **two Snowflake Cortex Agents** that provide intelligent 
    analysis capabilities. These agents run on-demand (no idle costs) and use natural language 
    to query the underlying data.
    """)
    
    # Agent cards
    agent_col1, agent_col2 = st.columns(2)
    
    # CEO Briefing Agent
    with agent_col1:
        with st.container(border=True):
            st.markdown("### :material/analytics: CEO Briefing Agent")
            st.caption("`AI_TRANSFORMATION_NEWS.AGENTS.CEO_BRIEFING`")
            
            st.markdown("""
            **Purpose:** Executive intelligence assistant providing strategic briefings 
            on AI transformation trends for C-level executives.
            """)
            
            st.markdown("**Capabilities:**")
            st.markdown("""
            - Analyze sentiment trends (economic optimism, employment outlook)
            - Track engagement metrics (views, social shares, LinkedIn shares)
            - Identify topic momentum across Employment, Finance, Policy, etc.
            - Compare geographic patterns (US, China, Europe, Global)
            - Weight insights by publication credibility scores
            """)
            
            with st.expander("Example Questions"):
                st.code("""
• What topics are generating the most engagement?
• How has economic sentiment shifted over time?
• Which regions show the most fear vs hope about AI?
• What are the top headlines by social shares?
• Show me the sentiment breakdown by topic category
                """, language=None)
            
            with st.expander("Data Sources"):
                st.markdown("""
                | Table | Description |
                |-------|-------------|
                | `CEO_INSIGHTS` | 34 articles with sentiment & engagement |
                | `ARTICLE_INFLUENCE` | Cross-citation analysis |
                | `CEO_NEWS_ANALYTICS` | Semantic view for NL queries |
                """)
            
            st.markdown("**Metrics Available:**")
            metrics_df = pd.DataFrame({
                "Category": ["Sentiment", "Sentiment", "Sentiment", "Engagement", "Engagement", "Engagement"],
                "Metric": ["overall_sentiment", "economic_optimism", "employment_outlook", 
                          "total_views", "social_shares", "linkedin_shares"],
                "Range": ["-1 to +1", "-1 to +1", "-1 to +1", "Count", "Count", "Count"]
            })
            st.dataframe(metrics_df, hide_index=True, use_container_width=True)
    
    # Cost Optimizer Agent
    with agent_col2:
        with st.container(border=True):
            st.markdown("### :material/savings: Cost Optimizer Agent")
            st.caption("`AI_TRANSFORMATION_NEWS.AGENTS.COST_OPTIMIZER`")
            
            st.markdown("""
            **Purpose:** Snowflake cost optimization expert that analyzes warehouse 
            usage and recommends ways to minimize compute costs.
            """)
            
            st.markdown("**Capabilities:**")
            st.markdown("""
            - Analyze warehouse credit consumption patterns
            - Identify expensive queries and usage patterns
            - Recommend auto-suspend and sizing optimizations
            - Track hour-of-day and day-of-week usage trends
            - Assess queue times to detect undersized warehouses
            """)
            
            with st.expander("Example Questions"):
                st.code("""
• Which warehouses consume the most credits?
• What are the peak usage hours?
• Show me query execution times by warehouse
• Are there any warehouses with high queue times?
• What's the credit consumption trend by day of week?
                """, language=None)
            
            with st.expander("Data Sources"):
                st.markdown("""
                | View | Description |
                |------|-------------|
                | `WAREHOUSE_COSTS` | 90 days of credit consumption |
                | `QUERY_COSTS` | 30 days of query performance |
                | `WAREHOUSE_COST_ANALYTICS` | Semantic view for analysis |
                """)
            
            st.markdown("**Optimization Recommendations:**")
            st.markdown("""
            - **Auto-suspend:** 1-5 minutes for most workloads
            - **Sizing:** Right-size based on queue time
            - **Scheduling:** Move jobs to off-peak hours
            - **Queries:** Optimize high bytes_scanned queries
            """)
    
    # How to use section
    st.markdown("---")
    st.subheader("How to Use These Agents")
    
    st.markdown("""
    Cortex Agents can be invoked via SQL or the Snowflake UI. They process natural language 
    questions and automatically query the underlying semantic views.
    """)
    
    use_col1, use_col2 = st.columns(2)
    
    with use_col1:
        st.markdown("**Via SQL:**")
        st.code("""
SELECT SNOWFLAKE.CORTEX.AGENT_RUN(
  '{"agent": "AI_TRANSFORMATION_NEWS.AGENTS.CEO_BRIEFING", 
    "messages": [{"role": "user", "content": [
      {"type": "text", "text": "Your question here"}
    ]}]}'
) AS response;
        """, language="sql")
    
    with use_col2:
        st.markdown("**Via Snowflake UI:**")
        st.markdown("""
        1. Navigate to **AI & ML** → **Cortex Agents**
        2. Select the agent (`CEO_BRIEFING` or `COST_OPTIMIZER`)
        3. Type your question in natural language
        4. Review the response and any generated SQL
        """)
    
    # Architecture diagram
    st.markdown("---")
    st.subheader("Architecture")
    
    st.markdown("""
    ```
    ┌─────────────────────────────────────────────────────────────────────┐
    │                        User Question                                 │
    │                 "What topics have the most fear?"                    │
    └─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────────┐
    │                      Cortex Agent                                    │
    │  ┌─────────────────┐    ┌─────────────────┐    ┌────────────────┐  │
    │  │  Orchestration  │───▶│  Tool Selection │───▶│  LLM Response  │  │
    │  │     Model       │    │                 │    │   Generation   │  │
    │  └─────────────────┘    └─────────────────┘    └────────────────┘  │
    └─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────────┐
    │                     Semantic View                                    │
    │         CEO_NEWS_ANALYTICS / WAREHOUSE_COST_ANALYTICS               │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐  │
    │  │  Dimensions  │  │   Metrics    │  │  AI SQL Generation Hints │  │
    │  │  (topic,     │  │  (sentiment, │  │  (business context &     │  │
    │  │   region)    │  │   views)     │  │   query patterns)        │  │
    │  └──────────────┘  └──────────────┘  └──────────────────────────┘  │
    └─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────────┐
    │                    Underlying Views                                  │
    │     CEO_INSIGHTS ◄── HEADLINES + SENTIMENT + CONSUMPTION            │
    │     WAREHOUSE_COSTS ◄── SNOWFLAKE.ACCOUNT_USAGE                     │
    └─────────────────────────────────────────────────────────────────────┘
    ```
    """)
    
    # Cost information
    st.markdown("---")
    st.subheader("Cost Model")
    
    cost_col1, cost_col2, cost_col3 = st.columns(3)
    
    with cost_col1:
        with st.container(border=True):
            st.markdown("**Idle Cost**")
            st.markdown("# $0")
            st.caption("Agents only run when invoked")
    
    with cost_col2:
        with st.container(border=True):
            st.markdown("**Per Invocation**")
            st.markdown("# Credits + Tokens")
            st.caption("Warehouse compute + LLM usage")
    
    with cost_col3:
        with st.container(border=True):
            st.markdown("**Storage**")
            st.markdown("# Minimal")
            st.caption("Agent definitions are metadata only")

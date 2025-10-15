import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Michigan Pioneer Settlement Explorer",
    page_icon="🏕️",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["🎓 Lecturer Slides", "🗺️ Student Activity", "📖 Resources & Library"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Course Module**\n\nChapter 9: The Error of the Pioneers\n\n*Michigan: A History of the Wolverine State*")

# ==================== LECTURER SLIDES PAGE ====================
if page == "🎓 Lecturer Slides":
    st.title("🎓 Lecturer Presentation: The Error of the Pioneers")
    
    # Slide selector
    slide_num = st.select_slider(
        "Select Slide:",
        options=list(range(1, 11)),
        format_func=lambda x: f"Slide {x}"
    )
    
    st.markdown("---")
    
    # Slide 1: Title
    if slide_num == 1:
        st.markdown("<h1 style='text-align: center; color: #2E86AB;'>Chapter 9: The Error of the Pioneers</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Michigan Territory Settlement, 1815-1837</h2>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>From 'Uninhabitable Swampland' to Agricultural Powerhouse</h3>", unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Michigan_in_United_States.svg/1200px-Michigan_in_United_States.svg.png", width=400)
        
    # Slide 2: The Survey Crisis
    elif slide_num == 2:
        st.header("The Survey That Changed History")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### 📋 The 1815 Tiffin Survey
            
            **Key Facts:**
            - **Who:** Surveyor General Edward Tiffin
            - **When:** 1815, after War of 1812
            - **Purpose:** Find land for war veterans
            - **Result:** Devastating report
            
            **Tiffin's Assessment:**
            > "Not more than one acre in a hundred, 
            > if there is one out of a thousand, 
            > that would admit of cultivation"
            """)
        
        with col2:
            st.markdown("""
            ### 🚫 Consequences
            
            **Immediate Impact:**
            - ❌ War of 1812 veterans given land in Illinois and Missouri instead
            - ❌ Michigan labeled "uninhabitable"
            - ❌ Settlement delayed by a decade
            - ❌ National reputation damaged
            
            **Why the Error?**
            - Limited exploration of interior
            - Focused on swampy areas
            - Surveyed during mosquito season
            - Didn't see cleared land potential
            """)
    
    # Slide 3: The Geography Reality
    elif slide_num == 3:
        st.header("Michigan's Hidden Treasures")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 🌾 Southern Lower Peninsula
            **Reality:** Prime farmland
            
            - Rich glacial soil
            - Perfect for wheat
            - Became national leader in grain
            - Diverse crop capability
            """)
        
        with col2:
            st.markdown("""
            ### 🍎 Lake Michigan Coast
            **Reality:** Fruit paradise
            
            - Moderated climate
            - Perfect for orchards
            - Apples, peaches, cherries
            - Still top producer today
            """)
        
        with col3:
            st.markdown("""
            ### 💧 "Swamplands"
            **Reality:** Richest soil
            
            - When drained = gold
            - Celery production (Kalamazoo)
            - Sugar beets
            - Premium agricultural land
            """)
        
        st.success("💡 **The Lesson:** Surface appearances deceived the surveyors. The 'useless' land was actually one of America's most valuable territories!")
    
    # Slide 4: The Turning Point
    elif slide_num == 4:
        st.header("1825: Everything Changes")
        
        st.markdown("""
        ### 🚢 The Erie Canal Opens
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Before the Canal (pre-1825):**
            - Detroit to NYC: 3-4 weeks overland
            - Expensive, dangerous journey
            - Limited access to markets
            - Population: ~8,000 in territory
            """)
        
        with col2:
            st.markdown("""
            **After the Canal (1825+):**
            - Detroit to NYC: 8-10 days by water
            - Affordable transportation
            - Direct market access
            - By 1837: 175,000+ residents!
            """)
        
        st.info("📊 **Migration Surge:** 'It seemed as if all New England were coming' - Contemporary observer")
        
        st.markdown("""
        ### 🏃 The Pioneer Rush
        
        **Who came?**
        - New England farmers seeking new land
        - European immigrants (Dutch, German, Irish)
        - Former soldiers curious about reports
        - Entrepreneurs seeing opportunity
        
        **What they found:**
        - Reports were wrong
        - Land was incredibly fertile
        - Opportunities everywhere
        - A 'promised land'
        """)
    
    # Slide 5: Pioneer Challenges
    elif slide_num == 5:
        st.header("Life on the Michigan Frontier")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 😰 Real Challenges
            
            **Physical Obstacles:**
            - Dense old-growth forests
            - Actual swamps and wetlands
            - Mosquito-borne "ague" (malaria-like illness)
            - Harsh winters
            - Isolation from civilization
            
            **Survival Needs:**
            - Clear land (backbreaking work)
            - Build shelter before winter
            - Establish water source
            - Plant crops immediately
            - Create relationships with Native Americans
            """)
        
        with col2:
            st.markdown("""
            ### 💪 Pioneer Solutions
            
            **Community Response:**
            - Barn-raising gatherings
            - Shared labor and tools
            - Trading with existing settlements
            - Learning from Native techniques
            - Gradual land clearing
            
            **Economic Strategies:**
            - Wheat as cash crop
            - Timber sales
            - Fur trading
            - Fruit cultivation
            - Mill operations
            """)
    
    # Slide 6: Settlement Patterns
    elif slide_num == 6:
        st.header("Where Did Pioneers Settle?")
        
        settlement_data = {
            'Region': ['Detroit Area', 'Grand River Valley', 'Saginaw Valley', 'Lake Michigan Coast', 'Ann Arbor Area'],
            'Early Settlers': [5000, 2000, 800, 1500, 1200],
            'By 1837': [9000, 8000, 3500, 6000, 4500],
            'Primary Activity': ['Trade/Commerce', 'Farming/Mills', 'Lumber/Farming', 'Fruit Orchards', 'Education/Farming']
        }
        
        df = pd.DataFrame(settlement_data)
        
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("""
        ### 🎯 Settlement Priorities
        
        **Most Successful Settlements Had:**
        1. **Water Access** - Rivers or lakes for transportation
        2. **Mixed Economy** - Not just farming
        3. **Community** - Mutual support systems
        4. **Trade Routes** - Connection to markets
        5. **Diverse Resources** - Timber, farmland, water power
        """)
    
    # Slide 7: Native American Impact
    elif slide_num == 7:
        st.header("The Native American Perspective")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### 🌍 Original Inhabitants
            
            **Michigan's Native Nations:**
            - Anishinaabe (Ojibwe/Chippewa)
            - Odawa (Ottawa)
            - Potawatomi
            - Wyandot (Huron)
            - Miami
            
            **Their Relationship with the Land:**
            - Lived here for thousands of years
            - Sustainable hunting and agriculture
            - Sacred sites throughout territory
            - Complex trade networks
            - Deep environmental knowledge
            """)
        
        with col2:
            st.markdown("""
            ### 📜 Treaty Era (1819-1842)
            
            **Land Cessions:**
            - 1819-1822: Lewis Cass treaties
            - Gradual loss of territory
            - By 1842: Most land ceded
            - Forced relocations
            - Broken promises
            
            **Impact on Pioneers:**
            - Native knowledge crucial to survival
            - Trade relationships essential
            - Trails became roads
            - Place names preserved
            - Cultural exchange occurred
            """)
        
        st.warning("⚠️ **Important Context:** Pioneer success came at devastating cost to Native communities through forced removal and broken treaties.")
    
    # Slide 8: Economic Transformation
    elif slide_num == 8:
        st.header("From 'Worthless' to Wealthy")
        
        st.markdown("""
        ### 📈 Michigan's Economic Evolution
        """)
        
        # Create timeline
        timeline_data = {
            'Year': ['1815', '1825', '1830', '1835', '1837', '1840'],
            'Population': [8000, 15000, 32000, 85000, 175000, 212000],
            'Key Development': [
                'Tiffin Report: "Uninhabitable"',
                'Erie Canal Opens',
                'Wheat Boom Begins',
                'Statehood Push',
                'Michigan Becomes State!',
                'Agricultural Powerhouse'
            ]
        }
        
        df_timeline = pd.DataFrame(timeline_data)
        st.dataframe(df_timeline, use_container_width=True, hide_index=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 🌾 Agriculture
            - Wheat production leader
            - Fruit orchards boom
            - Dairy farming
            - Sugar beets
            - Mint production
            """)
        
        with col2:
            st.markdown("""
            ### 🏭 Industry
            - Lumber mills
            - Flour mills
            - Furniture (Grand Rapids)
            - Mining (Upper Peninsula)
            - Manufacturing centers
            """)
        
        with col3:
            st.markdown("""
            ### 🏙️ Urban Growth
            - Detroit: Major port
            - Grand Rapids: Furniture
            - Kalamazoo: Celery/paper
            - Saginaw: Lumber
            - Ann Arbor: Education
            """)
    
    # Slide 9: Statehood Achievement
    elif slide_num == 9:
        st.header("The Road to Statehood")
        
        st.markdown("""
        ### 🏛️ Michigan Becomes the 26th State
        **January 26, 1837**
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### Requirements Met
            
            **Constitutional Requirements:**
            - ✅ 60,000 residents (had 175,000!)
            - ✅ Territorial government functioning
            - ✅ State constitution written
            - ✅ Congressional approval
            
            **The Obstacle:**
            - Toledo Strip boundary dispute with Ohio
            - Lost Toledo (valuable port)
            - Gained Upper Peninsula as compensation
            - Initially seen as bad deal!
            """)
        
        with col2:
            st.markdown("""
            ### Historical Irony
            
            **From Rejection to Success:**
            - 1815: "Not worth defending"
            - 1837: 26th state of the Union
            - 22 years from despair to statehood!
            
            **The Upper Peninsula 'Consolation':**
            - Seemed worthless at first
            - Discovered: Massive copper deposits
            - Discovered: Rich iron ore
            - Became mining powerhouse
            - Another "expert error" corrected!
            """)
    
    # Slide 10: Lessons and Legacy
    elif slide_num == 10:
        st.header("Lessons from the Error of the Pioneers")
        
        st.markdown("""
        ### 🎓 What Can We Learn?
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### Historical Lessons
            
            **1. Don't Trust Limited Observations**
            - Tiffin surveyed during worst season
            - Didn't explore thoroughly
            - Lacked agricultural perspective
            
            **2. Perception vs. Reality**
            - Surface conditions misleading
            - Potential hidden beneath challenges
            - Time reveals true value
            
            **3. Human Determination Matters**
            - Pioneers didn't give up
            - Transformed "worthless" land
            - Innovation overcame obstacles
            """)
        
        with col2:
            st.markdown("""
            ### Modern Applications
            
            **Critical Thinking:**
            - Question expert opinions
            - Seek multiple perspectives
            - Verify with primary sources
            - Consider biases and context
            
            **Environmental Understanding:**
            - Wetlands actually valuable
            - "Wastelands" often ecosystems
            - Development has tradeoffs
            - Historical wisdom matters
            
            **Opportunity Recognition:**
            - Others' rejections = your opportunity
            - Look beyond obvious
            - Challenge conventional wisdom
            """)
        
        st.success("""
        ### 🌟 Bottom Line
        
        The "Error of the Pioneers" wasn't made by the pioneers themselves—it was made by the experts who 
        dismissed Michigan without truly understanding it. The pioneers who ignored the negative reports 
        and explored for themselves discovered one of America's greatest treasures.
        
        **Ask your students:** Where in your life might expert opinion be wrong? What "useless" opportunities 
        might actually be valuable if explored with fresh eyes?
        """)
    
    # Navigation buttons
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ Previous Slide", disabled=(slide_num == 1)):
            st.rerun()
    with col3:
        if st.button("Next Slide ➡️", disabled=(slide_num == 10)):
            st.rerun()

# ==================== STUDENT ACTIVITY PAGE ====================
elif page == "🗺️ Student Activity":
    st.title("🏕️ Michigan Pioneer Settlement Challenge")
    st.markdown("### Chapter 9: The Error of the Pioneers")

    # Historical context
    with st.expander("📖 Historical Background - Click to Read"):
        st.markdown("""
        **The Mistake That Changed Michigan's History**
        
        In 1815, government surveyor Edward Tiffin was sent to explore Michigan Territory. His report was devastating: 
        he claimed most of the land was swampy and uninhabitable. Because of this negative assessment, War of 1812 
        veterans were given land in Illinois and Missouri instead of Michigan.
        
        **But the surveyors were wrong!**
        
        When pioneers finally ventured into Michigan's interior in the 1820s-1830s, they discovered:
        - The southern Lower Peninsula had incredibly fertile soil
        - Michigan became a national leader in wheat production
        - The Lake Michigan shoreline was perfect for fruit orchards (apples, peaches, cherries)
        - Even the swamplands, when drained, revealed some of the richest farmland
        
        This "error of the pioneers" delayed Michigan's growth by a decade but ultimately couldn't stop the flood 
        of settlers once word got out about the true nature of the land.
        """)

    # Create two columns for layout
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.subheader("🗺️ Michigan Territory Map (1825)")
        
        # Create Michigan map with regions
        fig = go.Figure()
        
        # Michigan outline (simplified coordinates for Lower Peninsula)
        michigan_outline_x = [-87, -86, -84.5, -83, -82.5, -82.3, -83, -84, -85, -86, -87, -87]
        michigan_outline_y = [41.7, 41.7, 41.9, 42, 41.7, 43.5, 45.9, 45.9, 45.5, 45, 43, 41.7]
        
        # Add Michigan outline
        fig.add_trace(go.Scatter(
            x=michigan_outline_x,
            y=michigan_outline_y,
            fill="toself",
            fillcolor="lightgreen",
            line=dict(color="darkgreen", width=2),
            name="Michigan Territory",
            hoverinfo="name"
        ))
        
        # Major settlements
        settlements = pd.DataFrame({
            'name': ['Detroit', 'Sault Ste. Marie', 'Fort Mackinac', 'Monroe', 'Ann Arbor (est. 1824)'],
            'lat': [42.33, 46.50, 45.85, 41.92, 42.28],
            'lon': [-83.05, -84.35, -84.62, -83.40, -83.74],
            'size': [15, 10, 10, 8, 8]
        })
        
        fig.add_trace(go.Scatter(
            x=settlements['lon'],
            y=settlements['lat'],
            mode='markers+text',
            marker=dict(size=settlements['size'], color='red', symbol='star'),
            text=settlements['name'],
            textposition="top center",
            name="Settlements",
            hovertemplate='<b>%{text}</b><br>Existing settlement<extra></extra>'
        ))
        
        # Rivers (simplified)
        rivers_data = [
            {"name": "Detroit River", "x": [-83.1, -83.0], "y": [42.0, 42.4]},
            {"name": "Grand River", "x": [-86.2, -85.7, -85.0, -84.5], "y": [43.0, 42.9, 42.8, 42.9]},
            {"name": "Saginaw River", "x": [-84.0, -83.9], "y": [43.6, 43.4]},
        ]
        
        for river in rivers_data:
            fig.add_trace(go.Scatter(
                x=river["x"],
                y=river["y"],
                mode='lines',
                line=dict(color='blue', width=3),
                name=river["name"],
                hovertemplate=f'<b>{river["name"]}</b><extra></extra>'
            ))
        
        # Lake Michigan shoreline highlight
        lake_x = [-87, -87, -86.5, -86, -85.5, -86, -86.5, -87]
        lake_y = [42, 45, 45.5, 45.3, 44.5, 43.5, 42.5, 42]
        
        fig.add_trace(go.Scatter(
            x=lake_x,
            y=lake_y,
            fill="toself",
            fillcolor="rgba(173, 216, 230, 0.3)",
            line=dict(color="blue", width=1, dash='dash'),
            name="Lake Michigan Coast",
            hovertemplate='Lake Michigan Shoreline<br>Good for: Fruit orchards, Trade<extra></extra>'
        ))
        
        # Swampland areas (example areas)
        swamp_areas = [
            {"x": [-83.5, -83.5, -84.0, -84.0], "y": [43.0, 43.5, 43.5, 43.0], "name": "Saginaw Swamps"},
            {"x": [-85.5, -85.5, -86.0, -86.0], "y": [42.3, 42.8, 42.8, 42.3], "name": "Grand River Wetlands"}
        ]
        
        for swamp in swamp_areas:
            fig.add_trace(go.Scatter(
                x=swamp["x"],
                y=swamp["y"],
                fill="toself",
                fillcolor="rgba(139, 69, 19, 0.2)",
                line=dict(color="brown", width=1, dash='dot'),
                name=swamp["name"],
                hovertemplate=f'<b>{swamp["name"]}</b><br>Surveyor Report: "Uninhabitable"<br>Reality: Rich soil when drained<extra></extra>'
            ))
        
        fig.update_layout(
            showlegend=True,
            legend=dict(x=0, y=1),
            height=600,
            xaxis=dict(title="Longitude", range=[-87.5, -82]),
            yaxis=dict(title="Latitude", range=[41.5, 46.5], scaleanchor="x", scaleratio=1),
            hovermode='closest',
            plot_bgcolor='lightblue',
            paper_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("💡 **Tip:** Hover over different areas to learn about them. Click on legend items to show/hide layers.")

    with col2:
        st.subheader("🎯 Your Settlement Plan")
        
        # Student input form
        with st.form("settlement_form"):
            st.markdown("**As a pioneer explorer in 1825, plan your settlement:**")
            
            student_name = st.text_input("Your Name:", placeholder="Enter your name")
            
            settlement_name = st.text_input("Settlement Name:", placeholder="e.g., New Plymouth")
            
            # Location selection
            region = st.selectbox(
                "Choose Your Region:",
                [
                    "Select a region...",
                    "Southeast Michigan (near Detroit)",
                    "Lake Michigan Coast (Western)",
                    "Grand River Valley",
                    "Saginaw Valley (Swamplands)",
                    "Northern Lower Peninsula",
                    "Between Detroit and Ann Arbor",
                    "St. Joseph River Valley"
                ]
            )
            
            latitude = st.slider("Latitude (approximate):", 41.7, 46.0, 42.5, 0.1)
            longitude = st.slider("Longitude (approximate):", -87.0, -82.5, -84.5, 0.1)
            
            st.markdown("---")
            st.markdown("**Why this location?**")
            
            # Factors considered
            st.markdown("**Select your top 3 priorities:**")
            col_a, col_b = st.columns(2)
            
            with col_a:
                water_access = st.checkbox("Water access (river/lake)")
                fertile_soil = st.checkbox("Potential fertile soil")
                timber = st.checkbox("Abundant timber")
                trade_routes = st.checkbox("Near trade routes")
            
            with col_b:
                existing_settlements = st.checkbox("Near existing settlements")
                defense = st.checkbox("Defensible location")
                native_relations = st.checkbox("Good Native American relations")
                ignore_reports = st.checkbox("Ignoring negative reports")
            
            st.markdown("---")
            
            # Challenges
            challenges = st.text_area(
                "What challenges do you expect?",
                placeholder="Describe the obstacles you'll face (forest clearing, swamps, isolation, etc.)",
                height=100
            )
            
            # Resources
            resources = st.text_area(
                "What resources are available?",
                placeholder="List the natural resources and advantages of your location",
                height=100
            )
            
            # Vision
            vision = st.text_area(
                "What will your settlement become in 20 years?",
                placeholder="Describe your community's future (farming hub, trading post, mill town, etc.)",
                height=100
            )
            
            # First year strategy
            strategy = st.text_area(
                "Your first year survival strategy:",
                placeholder="What are your priorities? (shelter, clearing land, crops, relationships, etc.)",
                height=100
            )
            
            submitted = st.form_submit_button("📝 Submit Your Settlement Plan", use_container_width=True)
            
            if submitted:
                if student_name and settlement_name and region != "Select a region...":
                    st.success(f"✅ Settlement plan submitted for {settlement_name}!")
                    
                    # Display summary
                    st.markdown("### 📋 Your Plan Summary")
                    st.markdown(f"""
                    **Pioneer:** {student_name}  
                    **Settlement:** {settlement_name}  
                    **Location:** {region}  
                    **Coordinates:** {latitude}°N, {longitude}°W
                    
                    **Key Priorities:**
                    """)
                    
                    priorities = []
                    if water_access: priorities.append("Water access")
                    if fertile_soil: priorities.append("Fertile soil")
                    if timber: priorities.append("Timber")
                    if trade_routes: priorities.append("Trade routes")
                    if existing_settlements: priorities.append("Near settlements")
                    if defense: priorities.append("Defense")
                    if native_relations: priorities.append("Native relations")
                    if ignore_reports: priorities.append("Ignoring negative reports")
                    
                    if priorities:
                        for p in priorities:
                            st.markdown(f"- {p}")
                    
                    # Option to download
                    report = f"""
MICHIGAN PIONEER SETTLEMENT PLAN
================================

Student: {student_name}
Settlement Name: {settlement_name}
Region: {region}
Location: {latitude}°N, {longitude}°W

PRIORITIES:
{chr(10).join('- ' + p for p in priorities)}

EXPECTED CHALLENGES:
{challenges}

AVAILABLE RESOURCES:
{resources}

20-YEAR VISION:
{vision}

FIRST YEAR STRATEGY:
{strategy}
"""
                    
                    st.download_button(
                        label="📄 Download Your Plan",
                        data=report,
                        file_name=f"settlement_plan_{settlement_name.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
                else:
                    st.error("⚠️ Please fill in your name, settlement name, and choose a region!")

    # Discussion questions section
    st.markdown("---")
    st.subheader("💭 Class Discussion Questions")

    with st.expander("Click to view discussion questions"):
        st.markdown("""
        1. **Why did the government surveyors misjudge Michigan's potential?**
           - Consider: Limited exploration, focusing on swamps, time of year visited
        
        2. **What would make you trust your own observations over official government reports?**
           - Think about: Incentives, firsthand experience, risk vs. reward
        
        3. **How did the Erie Canal (completed 1825) change Michigan settlement?**
           - Impact on: Transportation, access to markets, flow of settlers
        
        4. **What role did wetlands play in both helping and hindering settlement?**
           - Negative: Disease, difficult travel, harder to farm initially
           - Positive: Rich soil when drained, wildlife, fishing
        
        5. **How did early settlers' choices shape modern Michigan cities?**
           - Think about: Detroit, Grand Rapids, Kalamazoo, Saginaw
        
        6. **What can we learn from the "error of the pioneers" for today?**
           - Lessons about: First impressions, persistence, expert opinions, exploring beyond reports
        """)

    # Historical outcome section
    st.markdown("---")
    st.subheader("📚 What Actually Happened?")

    with st.expander("Click to see the historical outcome"):
        st.markdown("""
        **The Truth Revealed (1825-1837)**
        
        Once the Erie Canal opened in 1825, thousands of New England settlers poured into Michigan. 
        They discovered:
        
        - **Southern Michigan** became prime wheat country and one of America's agricultural powerhouses
        - **Lake Michigan Coast** developed thriving fruit orchards (Michigan is still a top fruit producer today!)
        - **Grand Rapids** grew around furniture manufacturing using Michigan's abundant timber
        - **Detroit** exploded as a gateway city and later became the automotive capital
        - **Kalamazoo area** - Dutch immigrants turned swamplands into celery-growing regions
        - **Saginaw Valley** - The "uninhabitable swamps" became some of the richest farmland after drainage
        
        By 1837, Michigan had enough population to become a state - just 12 years after being dismissed as worthless swampland!
        
        **The Lesson:** Sometimes the experts are wrong. The pioneers who ignored the negative reports and explored 
        for themselves discovered one of America's most valuable territories.
        """)

# ==================== RESOURCES PAGE ====================
elif page == "📖 Resources & Library":
    st.title("📖 Resources & Library Research")
    st.markdown("### Explore More About Michigan History")
    
    # WCCCD Library Section
    st.header("🎓 Wayne County Community College District Library")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Access Your WCCCD Library Resources
        
        The WCCCD Library provides extensive resources for researching Michigan history, 
        primary sources, and historical documents.
        
        **Library Services Available:**
        - 📚 Historical books and textbooks
        - 🔍 Online databases and archives
        - 📰 Historical newspapers and periodicals
        - 🗺️ Maps and geographic resources
        - 👥 Research assistance from librarians
        - 💻 Digital collections
        """)
    
    with col2:
        st.info("""
        **WCCCD Library Hours**
        
        Visit your campus library or access online resources 24/7
        
        [Library Website](https://www.wcccd.edu/students/library.html)
        """)
    
    # Quick Links to WCCCD Resources
    st.markdown("### 🔗 Quick Links to WCCCD Library")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Main Library Portal**
        - [WCCCD Library Home](https://www.wcccd.edu/students/library.html)
        - [Library Catalog Search](https://www.wcccd.edu/students/library.html)
        - [Ask a Librarian](https://www.wcccd.edu/students/library.html)
        """)
    
    with col2:
        st.markdown("""
        **Online Databases**
        - [JSTOR Historical Archive](https://www.jstor.org/)
        - [ProQuest Historical](https://www.proquest.com/)
        - [EBSCOhost Research](https://www.ebsco.com/)
        """)
    
    with col3:
        st.markdown("""
        **Research Help**
        - [Citation Guide](https://www.wcccd.edu/students/library.html)
        - [Research Tutorials](https://www.wcccd.edu/students/library.html)
        - [Schedule Appointment](https://www.wcccd.edu/students/library.html)
        """)
    
    st.markdown("---")
    
    # Primary Sources Section
    st.header("📜 Primary Source Collections")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Michigan Historical Collections
        
        **Digital Archives:**
        - [Library of Michigan Digital Collections](https://www.michigan.gov/libraryofmichigan)
        - [Bentley Historical Library (U of M)](https://bentley.umich.edu/)
        - [Clarke Historical Library (CMU)](https://www.cmich.edu/library/clarke)
        - [Michigan State University Archives](https://archives.msu.edu/)
        - [Detroit Public Library Digital Collections](https://digitalcollections.detroitpubliclibrary.org/)
        
        **National Archives:**
        - [National Archives Catalog](https://catalog.archives.gov/)
        - [Library of Congress Michigan Collection](https://www.loc.gov/collections/)
        - [American Memory Project](https://memory.loc.gov/)
        """)
    
    with col2:
        st.markdown("""
        ### Historical Societies & Museums
        
        **Michigan Organizations:**
        - [Historical Society of Michigan](https://hsmichigan.org/)
        - [Michigan History Center](https://www.michigan.gov/mhc)
        - [Detroit Historical Society](https://detroithistorical.org/)
        - [Grand Rapids Public Museum](https://www.grpm.org/)
        
        **Virtual Museums:**
        - [Smithsonian National Museum of American History](https://americanhistory.si.edu/)
        - [Michigan Historical Museum Virtual Tour](https://www.michigan.gov/mhc)
        """)
    
    st.markdown("---")
    
    # Recommended Books Section
    st.header("📚 Recommended Reading")
    
    st.markdown("""
    ### Essential Books on Michigan History
    
    **Primary Text:**
    - **"Michigan: A History of the Wolverine State"** by Willis F. Dunbar and George S. May
      - *The definitive textbook on Michigan history*
      - Available at WCCCD Library
      - ISBN: 978-0802870551
    
    **Additional Recommended Books:**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **General Michigan History:**
        - "A Most Superior Land: Life in the Upper Peninsula of Michigan" by Daniel J. Fountain
        - "Michigan: A History" by Bruce A. Rubenstein & Lawrence E. Ziewacz
        - "The Great Book of Michigan" by J. Alexander
        - "Detroit: An American Autopsy" by Charlie LeDuff
        
        **Pioneer and Settlement Era:**
        - "Pioneer Life in Michigan" by Mildred M. Comfort
        - "The Old Northwest" by R. Carlyle Buley
        - "The Land Looks After Us" by Miranda Belarde-Lewis
        """)
    
    with col2:
        st.markdown("""
        **Native American History:**
        - "The Anishinaabeg of Michigan" by Michael Witgen
        - "Master of the Great Lakes" by Michael A. McDonnell
        - "Colonialism and the Ojibwe" by Dwayne Donald
        
        **Economic & Social History:**
        - "Frontier Industrialization" by R. Douglas Hurt
        - "The Great Lakes Frontier" by John Anthony Caruso
        - "Michigan: Visions of Our Past" by Richard J. Hathaway
        """)
    
    st.markdown("---")
    
    # Online Resources
    st.header("🌐 Free Online Resources")
    
    tab1, tab2, tab3 = st.tabs(["Historical Documents", "Maps & Geography", "Educational Sites"])
    
    with tab1:
        st.markdown("""
        ### Primary Historical Documents
        
        **Government Documents:**
        - [Michigan Territorial Papers](https://quod.lib.umich.edu/m/michiganhistory/)
        - [U.S. Land Survey Records](https://glorecords.blm.gov/)
        - [Congressional Records - Michigan Territory](https://www.congress.gov/)
        
        **Newspapers & Periodicals:**
        - [Chronicling America (Historic Newspapers)](https://chroniclingamerica.loc.gov/)
        - [Michigan Newspapers on Google News Archive](https://news.google.com/newspapers)
        - [Detroit Free Press Historical Archive](https://www.newspapers.com/)
        
        **Journals & Academic Articles:**
        - [Michigan Historical Review](https://www.hsmichigan.org/michigan-historical-review/)
        - [Michigan History Magazine Archive](https://www.michigan.gov/mhc)
        - [JSTOR Open Access Articles](https://www.jstor.org/)
        """)
    
    with tab2:
        st.markdown("""
        ### Maps and Geographic Resources
        
        **Historical Maps:**
        - [David Rumsey Map Collection](https://www.davidrumsey.com/)
        - [Library of Congress Map Collections](https://www.loc.gov/maps/)
        - [Michigan Historical Map Collection](https://quod.lib.umich.edu/m/michmaps/)
        - [USGS Historical Topographic Maps](https://www.usgs.gov/programs/national-geospatial-program)
        
        **Interactive Geography:**
        - [Michigan Geographic Alliance](https://geo.msu.edu/)
        - [USGS Earth Explorer](https://earthexplorer.usgs.gov/)
        - [Historic Detroit Map Portal](https://detroithistorical.org/learn)
        """)
    
    with tab3:
        st.markdown("""
        ### Educational Websites
        
        **Michigan History Education:**
        - [Michigan History for Kids](https://www.michigan.gov/mhc/education/for-kids)
        - [National Park Service - Michigan Sites](https://www.nps.gov/state/mi/index.htm)
        - [PBS Learning Media - Michigan History](https://www.pbslearningmedia.org/)
        
        **Pioneer and Frontier Life:**
        - [National Geographic - Pioneer Life](https://www.nationalgeographic.org/)
        - [American Experience - Frontier Life](https://www.pbs.org/wgbh/americanexperience/)
        - [Smithsonian Learning Lab](https://learninglab.si.edu/)
        
        **Native American Resources:**
        - [National Museum of the American Indian](https://americanindian.si.edu/)
        - [Native Knowledge 360°](https://americanindian.si.edu/nk360)
        """)
    
    st.markdown("---")
    
    # Research Tips
    st.header("💡 Research Tips for Students")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### How to Research Michigan History
        
        **Step 1: Start Broad**
        - Read overview chapters in Dunbar & May
        - Get the big picture timeline
        - Identify specific topics that interest you
        
        **Step 2: Find Primary Sources**
        - Look for firsthand accounts
        - Check historical newspapers
        - Read letters, diaries, and documents
        - Examine maps from the period
        
        **Step 3: Consult Multiple Sources**
        - Compare different perspectives
        - Look for corroboration
        - Note contradictions
        - Consider biases
        """)
    
    with col2:
        st.markdown("""
        ### Evaluating Historical Sources
        
        **Ask These Questions:**
        - Who created this source?
        - When was it created?
        - Why was it created?
        - Who was the intended audience?
        - What biases might exist?
        - Is it corroborated by other sources?
        
        **Citation Formats:**
        - [MLA Format Guide](https://owl.purdue.edu/owl/research_and_citation/mla_style/mla_formatting_and_style_guide/mla_formatting_and_style_guide.html)
        - [Chicago Manual Style](https://www.chicagomanualofstyle.org/)
        - [APA Format](https://apastyle.apa.org/)
        """)
    
    st.markdown("---")
    
    # Assignment Ideas
    st.header("✍️ Research Project Ideas")
    
    with st.expander("Click for research project suggestions"):
        st.markdown("""
        ### Project Options
        
        1. **Primary Source Analysis**
           - Analyze letters from Michigan pioneers
           - Compare government surveys with settler accounts
           - Study newspaper articles from 1820s-1830s
        
        2. **Local History Research**
           - Research the founding of your Michigan city/town
           - Interview local historians
           - Visit local historical societies
        
        3. **Comparative Study**
           - Compare Michigan settlement to other states
           - Analyze different regions of Michigan
           - Study immigrant group contributions
        
        4. **Biography Project**
           - Research a Michigan pioneer
           - Study Native American leaders
           - Investigate government officials
        
        5. **Digital Humanities Project**
           - Create an interactive timeline
           - Map migration patterns
           - Build a digital exhibit
        
        6. **Creative Projects**
           - Write a historical fiction diary
           - Create a museum exhibit proposal
           - Develop an educational video
        """)
    
    # Contact Information
    st.markdown("---")
    st.info("""
    ### 📧 Need Help?
    
    **Contact Your WCCCD Librarian:**
    - Visit the library reference desk
    - Email: library@wcccd.edu
    - Call: Contact your campus library
    - Schedule a research consultation
    
    **Research Support Hours:**
    Monday-Friday: 8am-5pm  
    Online resources: Available 24/7
    """)

# Footer
st.markdown("---")
st.markdown("*Based on Chapter 9 of 'Michigan: A History of the Wolverine State' by Willis F. Dunbar and George S. May*")
st.markdown("*Wayne County Community College District | History Department*")

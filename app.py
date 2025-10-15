import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Michigan Pioneer Settlement Explorer",
    page_icon="🏕️",
    layout="wide"
)

# Title and introduction
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

# Footer
st.markdown("---")
st.markdown("*Based on Chapter 9 of 'Michigan: A History of the Wolverine State' by Willis F. Dunbar and George S. May*")

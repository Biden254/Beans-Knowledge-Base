# app.py
import streamlit as st
import pandas as pd
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Set, Optional, Tuple
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import io
from PIL import Image
import base64
import pymysql
pymysql.install_as_MySQLdb()


# Enums and Data Classes
class Severity(Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class RiskLevel(Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class ControlType(Enum):
    CHEMICAL = "Chemical"
    BIOLOGICAL = "Biological"
    BOTANICAL = "Botanical"
    CULTURAL = "Cultural"

@dataclass
class Pest:
    name: str
    severity: Severity
    symptoms: List[str]
    description: str
    
    def __hash__(self):
        return hash(self.name)

@dataclass
class Pesticide:
    name: str
    control_type: ControlType
    target_pests: List[str]
    pre_harvest_interval: int  # days
    risk_level: RiskLevel
    description: str
    
    def __hash__(self):
        return hash(self.name)

class BeanPestKnowledgeBase:
    def __init__(self):
        self.pests = {}
        self.pesticides = {}
        self.symptoms_to_pests = {}
        self.semantic_network = nx.Graph()
        self._initialize_knowledge_base()
    
    def _initialize_knowledge_base(self):
    # Initialize pests
        self.pests = {
            "aphid": Pest(
                name="Aphid",
                severity=Severity.HIGH,
                symptoms=["leaf_curling", "sticky_leaves", "stunted_growth", "honeydew_presence"],
                description="Small sap-sucking insects that cause leaf curling and transmit viruses."
            ),
            "whitefly": Pest(
                name="Whitefly",
                severity=Severity.HIGH,
                symptoms=["yellowing_leaves", "sticky_leaves", "sooty_mold", "stunted_growth"],
                description="Tiny white insects that feed on plant sap and excrete honeydew."
            ),
            "spider_mite": Pest(
                name="Spider Mite",
                severity=Severity.MODERATE,
                symptoms=["yellow_speckling", "fine_webbing", "leaf_drop"],
                description="Tiny arachnids that cause yellow stippling on leaves."
            ),
            "bean_beetle": Pest(
                name="Bean Beetle",
                severity=Severity.MODERATE,
                symptoms=["holes_in_leaves", "skeletonized_leaves", "defoliation"],
                description="Small beetles that feed on bean leaves and pods."
            ),
            "thrips": Pest(
                name="Thrips",
                severity=Severity.MODERATE,
                symptoms=["silvery_streaks", "distorted_growth", "black_feces"],
                description="Tiny insects that scrape plant cells and suck the contents."
            )
        }
    
        # Initialize pesticides
        self.pesticides = {
            "neem_oil": Pesticide(
                name="Neem Oil",
                control_type=ControlType.BOTANICAL,
                target_pests=["aphid", "whitefly", "spider_mite", "thrips"],
                pre_harvest_interval=0,
                risk_level=RiskLevel.LOW,
                description="Natural oil that disrupts insect growth and repels pests. Safe for beneficial insects when used as directed."
            ),
            "pyrethrin": Pesticide(
                name="Pyrethrin",
                control_type=ControlType.BOTANICAL,
                target_pests=["bean_beetle", "aphid", "thrips"],
                pre_harvest_interval=1,
                risk_level=RiskLevel.MODERATE,
                description="Natural insecticide derived from chrysanthemum flowers. Fast-acting but can harm beneficial insects."
            ),
            "spinosad": Pesticide(
                name="Spinosad",
                control_type=ControlType.BIOLOGICAL,
                target_pests=["thrips", "bean_beetle", "aphid", "whitefly", "spider_mite"],
                pre_harvest_interval=1,
                risk_level=RiskLevel.LOW,
                description="Naturally occurring substance toxic to many insects. Derived from soil bacteria."
            ),
            "insecticidal_soap": Pesticide(
                name="Insecticidal Soap",
                control_type=ControlType.CHEMICAL,
                target_pests=["aphid", "whitefly", "spider_mite"],
                pre_harvest_interval=0,
                risk_level=RiskLevel.LOW,
                description="Contact insecticide that works by breaking down the insect's outer shell."
            ),
            "crop_rotation": Pesticide(
                name="Crop Rotation",
                control_type=ControlType.CULTURAL,
                target_pests=["aphid", "whitefly", "spider_mite", "thrips", "bean_beetle"],
                pre_harvest_interval=0,
                risk_level=RiskLevel.LOW,
                description="Practice of growing different crops in sequence to disrupt pest life cycles."
            )
        }
    
        # Build symptom to pest mapping
        for pest_id, pest in self.pests.items():
            for symptom in pest.symptoms:
                if symptom not in self.symptoms_to_pests:
                    self.symptoms_to_pests[symptom] = []
                self.symptoms_to_pests[symptom].append(pest_id)
    
        # Build semantic network
        for pest_id in self.pests:
            self.semantic_network.add_node(pest_id, type='pest')
    
        for pesticide_id, pesticide in self.pesticides.items():
            self.semantic_network.add_node(pesticide_id, type='pesticide')
        for target_pest in pesticide.target_pests:
            if target_pest in self.pests:  # Only add edge if pest exists
                self.semantic_network.add_edge(
                    pesticide_id, target_pest,
                    relationship=f"controls_{pesticide.risk_level.value.lower()}"
                )

# ... (rest of the implementation)

def main():
    st.set_page_config(
        page_title="Bean Pest Management Advisor",
        page_icon="🌱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
        .main-header {color: #2c7b5f; font-size: 2.5rem; font-weight: 700;}
        .section-header {color: #2c7b5f; font-size: 1.8rem; margin-top: 1.5rem;}
        .risk-low {color: #28a745; font-weight: 600;}
        .risk-moderate {color: #ffc107; font-weight: 600;}
        .risk-high {color: #dc3545; font-weight: 600;}
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'diagnosis_results' not in st.session_state:
        st.session_state.diagnosis_results = None
    if 'selected_pests' not in st.session_state:
        st.session_state.selected_pests = []
    
    # Initialize knowledge base
    kb = BeanPestKnowledgeBase()
    
    # Sidebar navigation
    st.sidebar.title("🌱 Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Pest Diagnosis", "Pest Library", "Control Methods", "About"])
    
    # Page routing
    if page == "Home":
        show_home(kb)
    elif page == "Pest Diagnosis":
        show_diagnosis(kb)
    elif page == "Pest Library":
        show_pest_library(kb)
    elif page == "Control Methods":
        show_control_methods(kb)
    else:
        show_about()

def show_home(kb):
    st.markdown("<h1 class='main-header'>🌱 Bean Pest Management Advisor</h1>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to the Bean Pest Management Advisor, an intelligent system designed to help you identify 
    and manage common bean pests using integrated pest management (IPM) principles.
    
    ### Key Features:
    - 🔍 **Pest Diagnosis**: Identify pests based on observed symptoms
    - 📚 **Pest Library**: Detailed information about common bean pests
    - 🛡️ **Control Methods**: Find safe and effective pest control options
    - 🌍 **Sustainable Practices**: Recommendations that prioritize environmental safety
    """)

# ... (previous code remains the same until the show_home function)

def show_diagnosis(kb):
    st.markdown("<h1 class='main-header'>🔍 Pest Diagnosis</h1>", unsafe_allow_html=True)
    st.markdown("Select the symptoms you're observing to identify potential pests.")
    
    # Get all unique symptoms from the knowledge base
    all_symptoms = sorted(list(kb.symptoms_to_pests.keys()))
    
    # Convert symptom names to more readable format for display
    symptom_display_names = [s.replace('_', ' ').title() for s in all_symptoms]
    symptom_mapping = dict(zip(symptom_display_names, all_symptoms))
    
    # Multiselect for symptoms
    selected_symptom_displays = st.multiselect(
        "Select observed symptoms:",
        options=symptom_display_names,
        help="Choose all symptoms you're observing on your bean plants"
    )
    
    # Convert back to internal symptom names
    selected_symptoms = [symptom_mapping[s] for s in selected_symptom_displays]
    
    if st.button("Diagnose Pests", type="primary"):
        if not selected_symptoms:
            st.warning("Please select at least one symptom")
            return
            
        # Simple diagnosis logic (can be enhanced)
        pest_matches = {}
        for symptom in selected_symptoms:
            if symptom in kb.symptoms_to_pests:
                for pest_id in kb.symptoms_to_pests[symptom]:
                    if pest_id not in pest_matches:
                        pest_matches[pest_id] = 0
                    pest_matches[pest_id] += 1
        
        # Calculate confidence scores
        results = []
        for pest_id, count in pest_matches.items():
            total_symptoms = len(kb.pests[pest_id].symptoms)
            confidence = (count / len(selected_symptoms)) * (count / total_symptoms) * 100
            results.append((pest_id, min(100, confidence)))
        
        # Sort by confidence
        results.sort(key=lambda x: x[1], reverse=True)
        st.session_state.diagnosis_results = results
        
        if not results:
            st.info("No pests match the selected symptoms. Try selecting different symptoms.")
            return
            
        # Display results
        st.markdown("### 🐛 Potential Pests")
        for pest_id, confidence in results[:3]:  # Show top 3
            pest = kb.pests[pest_id]
            st.markdown(f"#### {pest.name} ({confidence:.1f}% match)")
            st.progress(confidence/100)
            st.markdown(f"**Severity:** {pest.severity.value}")
            st.markdown(f"**Description:** {pest.description}")
            st.markdown("**Common Symptoms:**")
            for symptom in pest.symptoms:
                st.markdown(f"- {symptom.replace('_', ' ').title()}")
            st.markdown("---")

def show_pest_library(kb):
    st.markdown("<h1 class='main-header'>📚 Pest Library</h1>", unsafe_allow_html=True)
    
    # Create tabs for each pest
    tabs = st.tabs([pest.name for pest in kb.pests.values()])
    
    for tab, (pest_id, pest) in zip(tabs, kb.pests.items()):
        with tab:
            col1, col2 = st.columns([1, 3])
            with col1:
                # Placeholder for pest image (you can add actual images later)
                st.image("https://via.placeholder.com/300x200?text=" + pest.name.replace(" ", "+"),
                        width=300)
            with col2:
                st.markdown(f"### {pest.name}")
                st.markdown(f"**Severity:** {pest.severity.value}")
                st.markdown("#### Description")
                st.markdown(pest.description)
                
                st.markdown("#### Common Symptoms")
                for symptom in pest.symptoms:
                    st.markdown(f"- {symptom.replace('_', ' ').title()}")
                
                # Show recommended controls
                st.markdown("#### Recommended Controls")
                controls = []
                for pesticide_id, pesticide in kb.pesticides.items():
                    if pest_id in pesticide.target_pests:
                        risk_class = f"risk-{pesticide.risk_level.value.lower()}"
                        controls.append(f"- **{pesticide.name}** (<span class='{risk_class}'>{pesticide.risk_level.value} Risk</span>) - {pesticide.description}")
                
                if controls:
                    st.markdown("\n".join(controls), unsafe_allow_html=True)
                else:
                    st.info("No specific controls found for this pest.")

def show_control_methods(kb):
    st.markdown("<h1 class='main-header'>🛡️ Control Methods</h1>", unsafe_allow_html=True)
    
    # Group pesticides by control type
    pesticides_by_type = {}
    for pesticide in kb.pesticides.values():
        if pesticide.control_type not in pesticides_by_type:
            pesticides_by_type[pesticide.control_type] = []
        pesticides_by_type[pesticide.control_type].append(pesticide)
    
    # Create tabs for each control type
    tabs = st.tabs([t.value for t in pesticides_by_type.keys()])
    
    for tab, (control_type, pesticides) in zip(tabs, pesticides_by_type.items()):
        with tab:
            st.markdown(f"### {control_type.value} Controls")
            
            for pesticide in sorted(pesticides, key=lambda x: x.risk_level.value):
                risk_class = f"risk-{pesticide.risk_level.value.lower()}"
                
                with st.expander(f"**{pesticide.name}**"):
                    st.markdown(f"**Risk Level:** <span class='{risk_class}'>{pesticide.risk_level.value}</span>", 
                               unsafe_allow_html=True)
                    st.markdown(f"**Pre-harvest Interval:** {pesticide.pre_harvest_interval} days")
                    st.markdown("**Effective Against:**")
                    for pest_id in pesticide.target_pests:
                        st.markdown(f"- {kb.pests[pest_id].name} ({kb.pests[pest_id].severity.value})")
                    st.markdown("**Description:**")
                    st.markdown(pesticide.description)

def show_about():
    st.markdown("<h1 class='main-header'>ℹ️ About</h1>", unsafe_allow_html=True)
    st.markdown("""
    ### Bean Pest Management Advisor
    
    This application helps farmers and agricultural professionals identify and manage common bean pests 
    using integrated pest management (IPM) principles.
    
    **Key Features:**
    - Symptom-based pest identification
    - Detailed pest information
    - Risk-based control recommendations
    - Sustainable pest management strategies
    
    **Disclaimer:** This tool is for informational purposes only. Always follow local agricultural 
    guidelines and consult with local agricultural extension services for specific recommendations.
    """)
    
    st.markdown("---")
    st.markdown("🌱 **Version 1.0.0**  \n"
                "© 2025 Bean Pest Management System")

if __name__ == "__main__":
    main()
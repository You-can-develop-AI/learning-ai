import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="AI/ML Learning Tracker",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .progress-complete {
        color: green;
        font-weight: bold;
    }
    .progress-incomplete {
        color: orange;
        font-weight: bold;
    }
    .category-header {
        font-size: 24px;
        font-weight: bold;
        color: #1f77b4;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .resource-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-left: 4px solid #1f77b4;
        border-radius: 5px;
        margin: 10px 0;
    }
    .resource-link {
        color: #0066cc;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# File paths
SCRIPT_DIR = Path(__file__).parent
TOPICS_FILE = SCRIPT_DIR / "topics.json"

# User list
USERS = ["babu", "adhi", "gokul"]
USER_NAMES = {"babu": "Babu", "adhi": "Adhi", "gokul": "Gokul"}

# Load JSON files
@st.cache_resource
def load_topics():
    with open(TOPICS_FILE, 'r') as f:
        return json.load(f)

def get_progress_file(username):
    """Get the progress file path for a user"""
    return SCRIPT_DIR / f"progress_{username}.json"

def load_user_progress(username):
    """Load progress for a specific user"""
    progress_file = get_progress_file(username)
    if progress_file.exists():
        with open(progress_file, 'r') as f:
            return json.load(f)
    else:
        return {
            "username": username,
            "name": USER_NAMES.get(username, username),
            "email": f"{username}@example.com",
            "started_date": datetime.now().strftime("%Y-%m-%d"),
            "progress": {}
        }

def save_user_progress(username, progress_data):
    """Save progress for a specific user"""
    progress_file = get_progress_file(username)
    with open(progress_file, 'w') as f:
        json.dump(progress_data, f, indent=2)

# Initialize data
topics_data = load_topics()

# Sidebar
st.sidebar.title("🎓 Learning Tracker")
st.sidebar.divider()

# User selection
selected_user_id = st.sidebar.selectbox(
    "Select User",
    options=USERS,
    format_func=lambda x: USER_NAMES.get(x, x)
)

# Load current user's progress
user_progress = load_user_progress(selected_user_id)

st.sidebar.divider()

# Navigation
page = st.sidebar.radio(
    "Navigation",
    options=["📊 Dashboard", "📚 Learning Path", "📈 Statistics"],
    index=0
)

st.sidebar.divider()

# Display app title
st.title("🚀 AI & ML Learning Tracker")
st.markdown("A comprehensive learning path for mastering AI and ML from basics to advanced topics")

# ==================== DASHBOARD PAGE ====================
if page == "📊 Dashboard":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "User",
            USER_NAMES.get(selected_user_id, selected_user_id),
            selected_user_id
        )
    
    with col2:
        start_date = datetime.strptime(user_progress['started_date'], '%Y-%m-%d')
        days_learning = (datetime.now() - start_date).days
        st.metric(
            "Days Learning",
            f"{days_learning} days",
            f"Started: {user_progress['started_date']}"
        )
    
    with col3:
        # Calculate overall progress
        total_topics = sum(len(cat['topics']) for cat in topics_data['learning_path'])
        completed_topics = sum(
            1 for cat in topics_data['learning_path']
            if str(cat['id']) in user_progress['progress']
            and user_progress['progress'][str(cat['id'])].get('completed', False)
        )
        progress_pct = (completed_topics / total_topics * 100) if total_topics > 0 else 0
        st.metric(
            "Overall Progress",
            f"{progress_pct:.1f}%",
            f"{completed_topics}/{total_topics} categories"
        )
    
    st.divider()
    
    # Progress by category
    st.subheader("📊 Progress by Category")
    
    category_progress = []
    for category in topics_data['learning_path']:
        cat_id = str(category['id'])
        if cat_id in user_progress['progress']:
            cat_progress = user_progress['progress'][cat_id]
            completion_pct = cat_progress.get('completion_percentage', 0)
            category_progress.append({
                'Category': category['category'],
                'Progress': completion_pct,
                'Status': '✅ Complete' if cat_progress.get('completed', False) else '🔄 In Progress' if completion_pct > 0 else '⏳ Not Started'
            })
        else:
            category_progress.append({
                'Category': category['category'],
                'Progress': 0,
                'Status': '⏳ Not Started'
            })
    
    df_progress = pd.DataFrame(category_progress)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(
            df_progress,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Progress": st.column_config.ProgressColumn(
                    "Progress %",
                    min_value=0,
                    max_value=100,
                    format="%d%%"
                ),
                "Status": st.column_config.TextColumn(
                    "Status"
                )
            }
        )
    
    with col2:
        # Summary stats
        st.metric("Total Categories", len(topics_data['learning_path']))
        st.metric("Total Topics", sum(len(cat['topics']) for cat in topics_data['learning_path']))
        total_subtopics = sum(
            len(topic['subtopics']) 
            for cat in topics_data['learning_path'] 
            for topic in cat['topics']
        )
        st.metric("Total Subtopics", total_subtopics)


# ==================== LEARNING PATH PAGE ====================
elif page == "📚 Learning Path":
    st.subheader(f"Learning Path for {USER_NAMES.get(selected_user_id, selected_user_id)}")
    
    for category in topics_data['learning_path']:
        cat_id = str(category['id'])
        cat_name = category['category']
        cat_description = category['description']
        
        # Get category progress
        if cat_id in user_progress['progress']:
            cat_progress = user_progress['progress'][cat_id]
            is_cat_complete = cat_progress.get('completed', False)
            cat_completion_pct = cat_progress.get('completion_percentage', 0)
        else:
            is_cat_complete = False
            cat_completion_pct = 0
        
        # Category header with expandable section
        with st.expander(
            f"{'✅' if is_cat_complete else '📖'} {cat_name} ({cat_completion_pct:.0f}% complete)",
            expanded=False
        ):
            st.markdown(f"*{cat_description}*")
            
            # Category completion status
            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(cat_completion_pct / 100)
            with col2:
                if st.checkbox(
                    "Mark category complete",
                    value=is_cat_complete,
                    key=f"cat_complete_{cat_id}"
                ):
                    user_progress['progress'][cat_id] = user_progress['progress'].get(cat_id, {})
                    user_progress['progress'][cat_id]['completed'] = True
                    user_progress['progress'][cat_id]['category_name'] = cat_name
            
            st.divider()
            
            # Topics in this category
            for topic in category['topics']:
                topic_id = str(topic['id'])
                topic_name = topic['name']
                
                # Get topic progress
                if cat_id in user_progress['progress'] and 'topics' in user_progress['progress'][cat_id]:
                    topic_progress = user_progress['progress'][cat_id]['topics'].get(topic_id, {})
                    is_topic_complete = topic_progress.get('completed', False)
                    completed_subtopics = topic_progress.get('subtopics_completed', [])
                else:
                    is_topic_complete = False
                    completed_subtopics = []
                
                with st.container(border=True):
                    col1, col2 = st.columns([4, 1])
                    
                    with col1:
                        st.markdown(f"**{topic_name}**")
                    with col2:
                        topic_completion = len(completed_subtopics) / len(topic['subtopics']) * 100 if topic['subtopics'] else 0
                        st.metric(
                            "Progress",
                            f"{topic_completion:.0f}%",
                            f"{len(completed_subtopics)}/{len(topic['subtopics'])}"
                        )
                    
                    # Subtopics checkboxes and resources
                    st.markdown("**Subtopics:**")
                    new_completed = []
                    
                    for idx, subtopic in enumerate(topic['subtopics']):
                        subtopic_name = subtopic['name'] if isinstance(subtopic, dict) else subtopic
                        is_checked = subtopic_name in completed_subtopics
                        
                        # Create expander for each subtopic
                        with st.expander(
                            f"{'✅' if is_checked else '⏳'} {subtopic_name}",
                            expanded=False
                        ):
                            # Completion checkbox
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.write("Mark as completed")
                            with col2:
                                is_checked_new = st.checkbox(
                                    "Completed",
                                    value=is_checked,
                                    key=f"{cat_id}_{topic_id}_{idx}_check"
                                )
                                if is_checked_new:
                                    new_completed.append(subtopic_name)
                            
                            st.divider()
                            
                            # Resources section
                            st.write("**📚 Resources:**")
                            
                            # Get current resources for this subtopic
                            subtopic_key = f"{cat_id}_{topic_id}_{subtopic_name}"
                            if 'resources' not in st.session_state:
                                st.session_state.resources = {}
                            
                            if subtopic_key not in st.session_state.resources:
                                if isinstance(subtopic, dict) and 'resources' in subtopic:
                                    st.session_state.resources[subtopic_key] = subtopic.get('resources', [])
                                else:
                                    st.session_state.resources[subtopic_key] = []
                            
                            # Display existing resources
                            resources = st.session_state.resources.get(subtopic_key, [])
                            for res_idx, resource in enumerate(resources):
                                col1, col2 = st.columns([4, 1])
                                with col1:
                                    st.markdown(f"[{resource.get('title', 'Link')}]({resource.get('url', '#')})")
                                    if resource.get('description'):
                                        st.caption(resource.get('description'))
                                with col2:
                                    if st.button("❌", key=f"del_res_{subtopic_key}_{res_idx}"):
                                        resources.pop(res_idx)
                                        st.session_state.resources[subtopic_key] = resources
                                        st.rerun()
                            
                            # Add new resource
                            st.write("**Add Resource:**")
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                res_type = st.selectbox(
                                    "Type",
                                    ["Video", "Article", "Course", "Documentation", "Tutorial", "Other"],
                                    key=f"res_type_{subtopic_key}"
                                )
                            with col2:
                                res_url = st.text_input(
                                    "URL",
                                    placeholder="https://example.com",
                                    key=f"res_url_{subtopic_key}"
                                )
                            
                            res_title = st.text_input(
                                "Resource Title",
                                placeholder="e.g., Introduction to Linear Algebra",
                                key=f"res_title_{subtopic_key}"
                            )
                            res_description = st.text_area(
                                "Description (optional)",
                                placeholder="Brief notes about this resource",
                                height=60,
                                key=f"res_desc_{subtopic_key}"
                            )
                            
                            if st.button("➕ Add Resource", key=f"add_res_{subtopic_key}"):
                                if res_url and res_title:
                                    if subtopic_key not in st.session_state.resources:
                                        st.session_state.resources[subtopic_key] = []
                                    st.session_state.resources[subtopic_key].append({
                                        "type": res_type,
                                        "title": res_title,
                                        "url": res_url,
                                        "description": res_description
                                    })
                                    st.success("Resource added!")
                                else:
                                    st.error("Please fill in URL and Title")
                            
                            st.divider()
                            
                            # Notes section
                            st.write("**📝 Notes:**")
                            
                            # Get current notes for this subtopic
                            notes_key = f"{cat_id}_{topic_id}_{subtopic_name}_notes"
                            if 'notes' not in st.session_state:
                                st.session_state.notes = {}
                            
                            if notes_key not in st.session_state.notes:
                                if isinstance(subtopic, dict) and 'notes' in subtopic:
                                    st.session_state.notes[notes_key] = subtopic.get('notes', '')
                                else:
                                    st.session_state.notes[notes_key] = ''
                            
                            notes = st.text_area(
                                "Your notes for this subtopic",
                                value=st.session_state.notes.get(notes_key, ''),
                                height=100,
                                key=f"notes_{subtopic_key}"
                            )
                            st.session_state.notes[notes_key] = notes
                    
                    # Update progress
                    if not user_progress['progress'].get(cat_id, {}).get('topics'):
                        if cat_id not in user_progress['progress']:
                            user_progress['progress'][cat_id] = {
                                'category_name': cat_name,
                                'topics': {}
                            }
                        else:
                            user_progress['progress'][cat_id]['topics'] = {}
                    
                    user_progress['progress'][cat_id]['topics'][topic_id] = {
                        'topic_name': topic_name,
                        'completed': len(new_completed) == len(topic['subtopics']),
                        'subtopics_completed': new_completed
                    }
                    
                    # Update category progress
                    total_subtopics_in_cat = sum(len(t['subtopics']) for t in category['topics'])
                    completed_subtopics_in_cat = sum(
                        len(user_progress['progress'][cat_id]['topics'].get(str(t['id']), {}).get('subtopics_completed', []))
                        for t in category['topics']
                    )
                    user_progress['progress'][cat_id]['completion_percentage'] = (
                        completed_subtopics_in_cat / total_subtopics_in_cat * 100 if total_subtopics_in_cat > 0 else 0
                    )
    
    # Save progress
    if st.button("💾 Save Progress", type="primary", use_container_width=True):
        # Save resources and notes to topics
        for cat_idx, category in enumerate(topics_data['learning_path']):
            cat_id = str(category['id'])
            for topic_idx, topic in enumerate(category['topics']):
                topic_id = str(topic['id'])
                for subtopic_idx, subtopic in enumerate(topic['subtopics']):
                    if isinstance(subtopic, dict):
                        subtopic_name = subtopic['name']
                        subtopic_key = f"{cat_id}_{topic_id}_{subtopic_name}"
                        
                        if subtopic_key in st.session_state.get('resources', {}):
                            topics_data['learning_path'][cat_idx]['topics'][topic_idx]['subtopics'][subtopic_idx]['resources'] = st.session_state.resources[subtopic_key]
                        
                        notes_key = f"{cat_id}_{topic_id}_{subtopic_name}_notes"
                        if notes_key in st.session_state.get('notes', {}):
                            topics_data['learning_path'][cat_idx]['topics'][topic_idx]['subtopics'][subtopic_idx]['notes'] = st.session_state.notes[notes_key]
        
        # Save to files
        with open(TOPICS_FILE, 'w') as f:
            json.dump(topics_data, f, indent=2)
        save_user_progress(selected_user_id, user_progress)
        st.success(f"Progress saved successfully for {USER_NAMES.get(selected_user_id)}!")
        st.rerun()


# ==================== STATISTICS PAGE ====================
elif page == "📈 Statistics":
    st.subheader("Learning Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Overall Platform Statistics")
        st.metric("Total Users", len(USERS))
        
        avg_progress = 0
        if len(USERS) > 0:
            total_progress = 0
            total_categories = len(topics_data['learning_path'])
            for username in USERS:
                user_data = load_user_progress(username)
                user_progress_sum = sum(
                    user_data['progress'].get(str(cat['id']), {}).get('completion_percentage', 0)
                    for cat in topics_data['learning_path']
                )
                total_progress += user_progress_sum
            avg_progress = total_progress / (len(USERS) * total_categories) if len(USERS) > 0 else 0
        
        st.metric("Average Progress", f"{avg_progress:.1f}%")
        st.metric("Total Categories", len(topics_data['learning_path']))
        st.metric("Total Topics", sum(len(cat['topics']) for cat in topics_data['learning_path']))
    
    with col2:
        st.markdown("### User Comparison")
        
        # Create comparison data
        comparison_data = []
        for username in USERS:
            user_data = load_user_progress(username)
            completed_cats = sum(
                1 for cat in topics_data['learning_path']
                if str(cat['id']) in user_data['progress']
                and user_data['progress'][str(cat['id'])].get('completed', False)
            )
            total_cats = len(topics_data['learning_path'])
            comparison_data.append({
                'User': USER_NAMES.get(username, username),
                'Completed Categories': completed_cats,
                'Total Categories': total_cats,
                'Percentage': (completed_cats / total_cats * 100) if total_cats > 0 else 0
            })
        
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(
            df_comparison,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Percentage": st.column_config.ProgressColumn(
                    "Progress %",
                    min_value=0,
                    max_value=100,
                    format="%d%%"
                )
            }
        )
    
    st.divider()
    
    # Category popularity
    st.markdown("### Category Engagement")
    
    engagement_data = []
    for category in topics_data['learning_path']:
        cat_id = str(category['id'])
        users_started = sum(
            1 for username in USERS
            if cat_id in load_user_progress(username)['progress']
            and load_user_progress(username)['progress'][cat_id].get('completion_percentage', 0) > 0
        )
        users_completed = sum(
            1 for username in USERS
            if cat_id in load_user_progress(username)['progress']
            and load_user_progress(username)['progress'][cat_id].get('completed', False)
        )
        
        engagement_data.append({
            'Category': category['category'],
            'Users Started': users_started,
            'Users Completed': users_completed,
            'Total Users': len(USERS)
        })
    
    df_engagement = pd.DataFrame(engagement_data)
    
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(df_engagement.set_index('Category')['Users Started'], use_container_width=True)
    with col2:
        st.bar_chart(df_engagement.set_index('Category')['Users Completed'], use_container_width=True)

# Footer
st.divider()
st.markdown("""
---
<div style='text-align: center'>
    <p>AI & ML Learning Tracker | Last Updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
</div>
""", unsafe_allow_html=True)

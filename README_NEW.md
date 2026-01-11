# 🚀 AI & ML Learning Tracker

A comprehensive learning tracker web application for mastering Artificial Intelligence and Machine Learning from fundamentals to advanced topics using Streamlit. Supports multiple users with individual progress tracking, resources, and notes.

## 📋 Features

### Multi-User Support ✨
- **Individual User Accounts**: Separate progress files for Babu, Adhi, and Gokul
- **Isolated Progress Tracking**: Each user maintains their own learning path progress
- **Independent Resources & Notes**: Users can add personal resources and notes for each subtopic

### Learning Management 📚
- **14 Major Learning Categories** covering:
  - Mathematics Fundamentals
  - Python & Programming Basics
  - Machine Learning Fundamentals
  - Deep Learning
  - Natural Language Processing (NLP)
  - Vector Databases & Embeddings
  - Retrieval Augmented Generation (RAG)
  - Large Language Models (LLMs)
  - Agentic AI
  - Agentic RAG
  - Fine-tuning and Transfer Learning
  - Model Deployment & MLOps
  - AI Safety & Ethics
  - Practical Projects & Capstone

### Resource Management 🔗
- **Add Multiple Resources per Subtopic**:
  - Links with titles and descriptions
  - Resource types (Video, Article, Course, Documentation, Tutorial, Other)
  - Easy URL references for further learning

- **Personal Notes 📝**:
  - Add detailed notes for each subtopic
  - Track your learning insights and key takeaways
  - Persist notes between sessions

### Dashboard & Analytics 📊
- **Dashboard**: Overall progress metrics and category breakdown
- **Learning Path**: Interactive learning with checkbox tracking
- **Statistics**: Compare progress across all users and categories

## 📊 File Structure

```
learning_tracker/
├── learning_tracker.py          # Main Streamlit application
├── topics.json                  # Complete curriculum with resources structure
├── progress_babu.json           # Babu's progress file
├── progress_adhi.json           # Adhi's progress file
├── progress_gokul.json          # Gokul's progress file
├── transform_topics.py          # Utility to transform subtopic structure
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the project directory:**
```bash
cd e:\product\learning_tracker
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**
```bash
streamlit run learning_tracker.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

### 1. **Select Your User** 👤
- Use the sidebar dropdown to select your user (Babu, Adhi, or Gokul)
- Each user has isolated progress and data

### 2. **Dashboard** 📊
- View your overall progress percentage
- See completion status for all categories
- Track days spent learning
- See total categories, topics, and subtopics available

### 3. **Learning Path** 📚
Navigate through learning with these steps:

1. **Expand a Category**: Click on a category to view all topics
2. **Review Topics**: See progress for each topic within the category
3. **Expand Subtopics**: Click on each subtopic to access:
   - **Completion Checkbox**: Mark as completed
   - **Resources Section**: 
     - View existing resources
     - Add new resources with:
       - Resource type (dropdown)
       - URL (required)
       - Title (required)
       - Description (optional)
     - Delete resources
   - **Notes Section**:
     - Write and edit personal notes
     - Notes save for future reference
4. **Save Progress**: Click "Save Progress" button to persist all changes

### 4. **Statistics** 📈
- View overall platform statistics
- Compare progress across all users
- See category engagement metrics
- Track which topics are most popular

## 💾 Data Structure

### topics.json
Contains the complete curriculum:
```json
{
  "learning_path": [
    {
      "id": <number>,
      "category": "Category Name",
      "description": "Description",
      "topics": [
        {
          "id": <number>,
          "name": "Topic Name",
          "subtopics": [
            {
              "name": "Subtopic Name",
              "resources": [
                {
                  "type": "Video|Article|Course|Documentation|Tutorial|Other",
                  "title": "Resource Title",
                  "url": "https://example.com",
                  "description": "Optional description"
                }
              ],
              "notes": "User's personal notes"
            }
          ]
        }
      ]
    }
  ]
}
```

### User Progress Files (progress_username.json)
Tracks individual user progress:
```json
{
  "username": "babu",
  "name": "Babu",
  "email": "babu@example.com",
  "started_date": "2025-01-01",
  "progress": {
    "1": {
      "category_name": "Mathematics Fundamentals",
      "completed": false,
      "completion_percentage": 45.5,
      "topics": {
        "1.1": {
          "topic_name": "Linear Algebra",
          "completed": false,
          "subtopics_completed": ["Vectors and Matrices", "Matrix Operations"]
        }
      }
    }
  }
}
```

## 🎯 Learning Path Overview

### Core Concepts (Topics 1-3)
- **Linear Algebra, Calculus, Probability & Statistics** (14 subtopics)
- **Python Fundamentals, NumPy, Pandas, Visualization** (12 subtopics)
- **Supervised & Unsupervised Learning, Ensemble Methods** (23 subtopics)

### Advanced Deep Learning (Topic 4)
- **Neural Networks, CNNs, RNNs, Transformers, Generative Models** (31 subtopics)

### NLP & Language (Topic 5)
- **NLP Fundamentals, Language Models, Advanced NLP Tasks** (22 subtopics)

### Modern AI Infrastructure (Topics 6-8)
- **Vector Databases & Embeddings** (10 subtopics)
- **RAG Systems** (17 subtopics)
- **Large Language Models** (13 subtopics)

### Autonomous Systems (Topics 9-10)
- **Agentic AI & Agent Frameworks** (17 subtopics)
- **Agentic RAG Systems** (14 subtopics)

### Deployment & Production (Topics 11-13)
- **Fine-tuning & Transfer Learning** (11 subtopics)
- **Model Deployment & MLOps** (12 subtopics)
- **AI Safety & Ethics** (13 subtopics)

### Capstone (Topic 14)
- **Real-world Projects & Capstone** (22 subtopics)

**Total: 14 Categories | 88+ Topics | 250+ Subtopics**

## 📚 Working with Resources

### Adding Resources
1. Expand a subtopic
2. Scroll to the "📚 Resources" section
3. Fill in the resource details:
   - **Type**: Select from predefined types (Video, Article, Course, Documentation, Tutorial, Other)
   - **URL**: The link to the resource
   - **Title**: Name of the resource
   - **Description**: Optional notes about the resource
4. Click "➕ Add Resource"

### Managing Resources
- **View Resources**: Listed with clickable links
- **Delete Resources**: Click the "❌" button next to any resource
- **Multiple Resources**: Add as many resources as needed per subtopic

### Example Resources
- **Video**: https://www.youtube.com/watch?v=xyz - Andrew Ng's Linear Algebra
- **Article**: https://www.medium.com/... - Understanding Neural Networks
- **Course**: https://www.coursera.org/... - Deep Learning Specialization
- **Documentation**: https://numpy.org/doc/ - NumPy Official Docs

## 📝 Working with Notes

### Adding Notes
1. Expand a subtopic
2. Scroll to the "📝 Notes" section
3. Write your personal notes in the text area
4. Notes are saved when you click "Save Progress"

### Note Ideas
- Key concepts and definitions
- Formula and equations
- Code snippets
- Practice problems
- Personal insights
- Areas that need more review

## 🔄 Multi-User Collaboration

### How It Works
- Each user has their own `progress_username.json` file
- Progress is independent and isolated
- Resources and notes are user-specific
- All changes are saved to individual files

### Sharing Knowledge
1. View other users' progress in Statistics page
2. Coordinate learning through the categories
3. Share notes and resources by discussing them outside the app

## 🛠️ Customization

### Add New Users
To add a new user:
1. Create a new `progress_username.json` file in the directory
2. Add the username to the `USERS` list in `learning_tracker.py`:
```python
USERS = ["babu", "adhi", "gokul", "new_user"]
USER_NAMES = {"babu": "Babu", "adhi": "Adhi", "gokul": "Gokul", "new_user": "New User"}
```
3. Initialize the progress file with:
```json
{
  "username": "new_user",
  "name": "New User",
  "email": "newuser@example.com",
  "started_date": "2025-01-11",
  "progress": {}
}
```

### Add New Topics
Edit `topics.json` and add new categories/topics following the structure:
```json
{
  "id": <new_id>,
  "category": "New Category",
  "description": "Description",
  "topics": [
    {
      "id": <topic_id>,
      "name": "Topic Name",
      "subtopics": [
        {
          "name": "Subtopic Name",
          "resources": [],
          "notes": ""
        }
      ]
    }
  ]
}
```

### Modify Existing Content
- All data is in JSON format for easy editing
- Changes are reflected immediately in the app
- User progress is preserved when editing topics

## 📊 Data Persistence

All data is automatically saved:
- **Topics**: Updated when resources/notes are saved
- **Progress**: Saved to individual user files
- **Resources**: Stored in topics.json within subtopics
- **Notes**: Persisted in topics.json and available across sessions

## ⚙️ Advanced Configuration

### Session State
The app uses Streamlit's session state for:
- Resource management during editing
- Note writing during the session
- Form input preservation

### Caching
- Topics are cached for performance
- Progress files are reloaded on each interaction
- User selection persists across page navigation

## 🐛 Troubleshooting

**Issue: Changes not saved**
- Make sure to click "Save Progress" button on the Learning Path page
- Check file permissions for progress files

**Issue: Slow performance with many resources**
- The app handles large datasets efficiently
- Consider archiving old progress files if tracking many years of data

**Issue: Resources not showing**
- Ensure proper JSON formatting in topics.json
- Verify URL format is correct
- Check that resources were added before saving

**Issue: User data not appearing**
- Verify user files exist in the directory
- Check USERS list in learning_tracker.py includes the username
- Ensure JSON files are not corrupted

## 📈 Future Enhancements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Quiz and assessment modules
- [ ] Spaced repetition scheduling
- [ ] Achievement badges
- [ ] Discussion boards for users
- [ ] Mobile app version
- [ ] Export reports (PDF, Excel)
- [ ] API for external integrations
- [ ] Resource recommendations
- [ ] Learning insights and analytics

## 📧 Support & Contribution

For questions or suggestions:
- Check the troubleshooting section
- Review the file structure
- Examine the JSON data format
- Refer to Streamlit documentation

## 📄 License

Open for personal and educational use.

---

**Happy Learning! 🎓**

Track your progress, master AI/ML concepts, manage your learning resources, and build amazing applications!

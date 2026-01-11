# 🚀 AI & ML Learning Tracker

A comprehensive learning tracker web application for mastering Artificial Intelligence and Machine Learning from fundamentals to advanced topics using Streamlit.

## 📋 Features

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

- **Multi-user Support** with individual progress tracking
- **Dashboard** with overall progress metrics
- **Interactive Learning Path** with checkbox-based completion tracking
- **User Management** to add and manage learners
- **Statistics & Analytics** to compare user progress
- **JSON-based Data Storage** for easy portability

## 📊 File Structure

```
learning_tracker/
├── learning_tracker.py      # Main Streamlit application
├── topics.json              # Learning topics and subtopics data
├── user_progress.json       # User progress tracking data
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd learning_tracker
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

### 1. **Dashboard** 📊
- Select a user from the sidebar
- View overall progress percentage
- See completion status for all categories
- Track days spent learning

### 2. **Learning Path** 📚
- Browse through all 14 learning categories
- Expand each category to see detailed topics
- Mark topics and subtopics as completed
- Track progress within each category
- Automatically calculates completion percentage

### 3. **User Management** 👥
- View all registered users
- Add new learners with username, name, and email
- Each user gets their own independent progress tracking

### 4. **Statistics** 📈
- Compare progress across all users
- View overall platform statistics
- See category engagement metrics
- Track which categories are most/least popular

## 📝 Topics Included

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

## 💾 Data Structure

### topics.json
Contains the complete learning curriculum organized by:
- Category ID and name
- Description
- Topics with their subtopics
- Hierarchical structure for easy navigation

### user_progress.json
Tracks user progress with:
- User information (username, name, email, start date)
- Progress per category (completion percentage, topics)
- Completed subtopics for each topic
- Completion status flags

## 🎯 Learning Path Recommendations

**Suggested Learning Order:**
1. Start with **Mathematics Fundamentals** (Topic 1)
2. Move to **Python & Programming** (Topic 2)
3. Learn **Machine Learning Basics** (Topic 3)
4. Study **Deep Learning** (Topic 4)
5. Explore **NLP** (Topic 5) or apply directly to projects
6. Learn **Vector Databases** (Topic 6) for modern applications
7. Master **RAG** (Topic 7) for building production systems
8. Understand **LLMs** (Topic 8)
9. Build **Agentic AI** (Topic 9) systems
10. Combine with **Agentic RAG** (Topic 10)
11. Learn **Fine-tuning** (Topic 11) for customization
12. Master **MLOps** (Topic 12) for production
13. Study **AI Safety & Ethics** (Topic 13) throughout
14. Build **Capstone Projects** (Topic 14)

## 🛠️ Customization

### Add New Users
1. Go to "User Management" tab
2. Fill in username, name, and email
3. Click "Add User"

### Add New Topics
Edit `topics.json` and add new categories following the same structure:
```json
{
  "id": <new_id>,
  "category": "Category Name",
  "description": "Description",
  "topics": [
    {
      "id": <topic_id>,
      "name": "Topic Name",
      "subtopics": ["Subtopic 1", "Subtopic 2"]
    }
  ]
}
```

### Modify Existing Content
- All data is in JSON format for easy editing
- Changes are reflected immediately in the app
- User progress is preserved

## 📊 Progress Export

Progress data is automatically saved to `user_progress.json` in JSON format, making it easy to:
- Export to other tools
- Create custom reports
- Backup learning progress
- Share progress with others

## 🎓 Use Cases

- **Self-paced Learning**: Track your AI/ML journey independently
- **Study Groups**: Share tracker with study groups and compare progress
- **Educational Institutions**: Use as a curriculum management tool
- **Training Programs**: Monitor trainee progress across multiple users
- **Corporate Training**: Track employee upskilling in AI/ML

## ⚙️ Advanced Configuration

### Session State
The app uses Streamlit's caching system for performance:
- Topics are cached on first load
- Progress data is reloaded on each interaction
- User selection persists across page navigation

### Data Persistence
- All data is stored locally in JSON files
- No cloud dependencies required
- Easy to integrate with databases if needed

## 🐛 Troubleshooting

**Issue: Changes not saved**
- Make sure to click "Save Progress" button on the Learning Path page
- Check file permissions for `user_progress.json`

**Issue: Slow performance**
- The app caches topics.json for performance
- Clear Streamlit cache if you edit topics.json: `streamlit cache clear`

**Issue: Users list not updating**
- Restart the Streamlit app to see new users
- Clear browser cache or open in incognito mode

## 📈 Future Enhancements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Quiz and assessment modules
- [ ] Spaced repetition scheduling
- [ ] Resource links and documentation
- [ ] Achievement badges
- [ ] Social features (discussion boards)
- [ ] Mobile app version
- [ ] Export reports (PDF, Excel)
- [ ] API for external integrations

## 📄 License

Open for personal and educational use.

## 📧 Support

For questions or suggestions, refer to the main documentation or create issues in your project repository.

---

**Happy Learning! 🎓**

Track your progress, master AI/ML concepts, and build amazing applications!

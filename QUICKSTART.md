# 🚀 Quick Start Guide

## Installation

```bash
cd e:\product\learning_tracker
pip install -r requirements.txt
streamlit run learning_tracker.py
```

App opens at: **http://localhost:8501**

---

## First Time Setup

### 1️⃣ Start the App
```bash
streamlit run learning_tracker.py
```

### 2️⃣ Select Your User
- Click dropdown in sidebar
- Choose: Babu, Adhi, or Gokul
- Your data automatically loads

### 3️⃣ View Your Dashboard
- See overall progress
- Check your statistics
- View learning timeline

---

## Common Tasks

### 📊 Track Progress
1. Go to **"📚 Learning Path"**
2. Select your user
3. Expand a category
4. Expand a topic
5. Check ✅ checkbox next to subtopic
6. Click **"Save Progress"**

### 📚 Add a Resource
1. Go to **"📚 Learning Path"**
2. Expand subtopic
3. Scroll to "📚 Resources"
4. Fill in:
   - Type (Video/Article/etc)
   - URL
   - Title
   - Description (optional)
5. Click **"➕ Add Resource"**
6. Click **"Save Progress"**

### 📝 Write Notes
1. Go to **"📚 Learning Path"**
2. Expand subtopic
3. Scroll to "📝 Notes"
4. Type your notes
5. Click **"Save Progress"**

### 📈 Check Statistics
1. Go to **"📈 Statistics"**
2. See your progress vs others
3. View category engagement
4. Compare completion rates

---

## User Files

Each user has their own file:
- `progress_babu.json` - Babu's progress
- `progress_adhi.json` - Adhi's progress
- `progress_gokul.json` - Gokul's progress

Changes auto-save when you click "Save Progress"

---

## Keyboard Shortcuts

| Action | Keyboard |
|--------|----------|
| Expand section | Click or Enter |
| Expand all | Multiple clicks |
| Add resource | Tab + Enter |
| Save progress | Button click |

---

## Tips & Tricks

### 💡 Pro Tips
- **Batch Updates**: Expand multiple subtopics, then save once
- **Resource Organization**: Use descriptions to categorize
- **Note Format**: Use bullet points and formatting
- **Regular Saves**: Click save frequently to avoid loss

### ⏱️ Time Savers
- **Copy URLs**: Resources are clickable links
- **Quick Notes**: Short summaries are fastest
- **Categories**: Work through one category at a time

### 🎯 Best Practices
- **Save Regularly**: Don't lose progress
- **Add Resources**: Build your learning library
- **Take Notes**: Reinforce learning
- **Check Stats**: Track overall progress

---

## Navigation

### Sidebar Menu
- **User Selection**: Choose Babu, Adhi, or Gokul
- **Navigation**: Dashboard, Learning Path, Statistics
- **Status**: Last updated timestamp

### Pages

#### 📊 Dashboard
- Your progress overview
- Category completion status
- Learning timeline

#### 📚 Learning Path
- Interactive learning interface
- Resource management
- Note-taking
- Progress tracking

#### 📈 Statistics
- Compare users
- Category engagement
- Platform metrics

---

## Data Management

### Saving Data
```
Auto-save when you click "💾 Save Progress"
```

### Viewing Data
```
Topics: topics.json
Your Progress: progress_[username].json
```

### Backups
```bash
# Backup your progress
copy progress_babu.json progress_babu_backup.json
```

---

## Troubleshooting

### Issue: Can't find my progress
**Solution**: Select correct user in dropdown

### Issue: Changes not saving
**Solution**: Click "Save Progress" button

### Issue: App not loading
**Solution**: 
```bash
pip install -r requirements.txt
streamlit run learning_tracker.py
```

### Issue: Resources not showing
**Solution**: Click "Save Progress" after adding resource

### Issue: Notes disappeared
**Solution**: 
- Click "Save Progress"
- Check file permissions
- Verify topics.json not corrupted

---

## File Structure

```
learning_tracker/
├── 📄 topics.json              # All learning topics
├── 📄 progress_babu.json       # Babu's data
├── 📄 progress_adhi.json       # Adhi's data
├── 📄 progress_gokul.json      # Gokul's data
├── 🐍 learning_tracker.py      # Main app
├── 📋 requirements.txt         # Dependencies
└── 📖 README.md               # Full documentation
```

---

## Learning Path Structure

```
14 Categories
    ↓
88+ Topics
    ↓
250+ Subtopics
    ↓
Unlimited Resources + Notes
```

---

## User Comparison

View progress comparison in **Statistics** page:
- Babu's completion %
- Adhi's completion %
- Gokul's completion %
- Category-wise engagement

---

## Quick Links

- **Start Learning**: Learning Path page
- **Check Progress**: Dashboard page
- **View Stats**: Statistics page
- **Full Docs**: README.md
- **Features**: FEATURES.md

---

## Next Steps

1. ✅ Install and run app
2. ✅ Select your user
3. ✅ View dashboard
4. ✅ Expand a category
5. ✅ Mark a subtopic complete
6. ✅ Add a resource
7. ✅ Write notes
8. ✅ Check statistics
9. ✅ Share progress with others
10. ✅ Keep learning! 📚

---

## Getting Help

Check these files:
- **README.md** - Full documentation
- **FEATURES.md** - New features explained
- **troubleshooting section** - Common issues

---

**Happy Learning! 🎓**

Track your progress and master AI/ML! 🚀

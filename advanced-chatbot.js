const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Advanced chatbot data structure with regex patterns and responses
const chatbotKnowledgeBase = {
  // Admissions & Applications
  admissions: {
    patterns: [
      /\b(apply|application|applying|admission|admissions|admit)\b/i,
      /\b(how\s+do\s+i\s+apply|application\s+process)\b/i,
      /\b(minimum\s+requirements|entry\s+requirements)\b/i,
      /\b(deadline|missed\s+deadline|late\s+application)\b/i,
      /\b(defer|deferment|postpone)\b/i
    ],
    responses: [
      "🎓 **Application Process**: To apply to our university, visit our online application portal. You'll need to submit your academic transcripts, personal statement, and any required test scores.",
      "📋 **Required Documents**: For your application, you'll typically need: academic transcripts, ID copy, personal statement, and proof of English proficiency (if applicable).",
      "📊 **Entry Requirements**: Minimum entry requirements vary by program. Generally, you need a high school diploma with good grades and may need to meet specific subject requirements.",
      "⏰ **Missed Deadline**: If you missed the application deadline, contact our admissions office immediately. Some programs may have rolling admissions or late application options.",
      "📅 **Admission Deferment**: To defer your admission, submit a written request to the admissions office explaining your circumstances. Deferments are typically granted for valid reasons."
    ]
  },

  // Registration & Academic
  registration: {
    patterns: [
      /\b(register|registration|course\s+registration)\b/i,
      /\b(drop|add|dropping|adding)\s+(course|class)\b/i,
      /\b(schedule|class\s+schedule|timetable)\b/i,
      /\b(transcript|academic\s+transcript|grades)\b/i,
      /\b(exam|missed\s+exam|test)\b/i,
      /\b(grading\s+system|how\s+are\s+we\s+graded)\b/i
    ],
    responses: [
      "📚 **Course Registration**: Register for courses through the student portal during your designated registration period. Check your academic advisor if you need guidance on course selection.",
      "✏️ **Add/Drop Courses**: You can add or drop courses during the add/drop period (usually first 2 weeks of semester) through the student portal without academic penalty.",
      "📋 **Class Schedule**: Access your class schedule through the student portal or mobile app. You can also print a copy from the registrar's office.",
      "📄 **Academic Transcript**: Request your transcript through the registrar's office or student portal. Official transcripts require a fee and take 3-5 business days.",
      "⚠️ **Missed Exam**: If you miss an exam due to valid reasons (illness, emergency), contact your professor immediately and provide documentation. Make-up exams may be arranged.",
      "📊 **Grading System**: We use a standard letter grade system (A, B, C, D, F) with corresponding GPA points. Check your student handbook for detailed grading policies."
    ]
  },

  // Financial & Fees
  financial: {
    patterns: [
      /\b(fees|tuition|payment|pay|money|cost)\b/i,
      /\b(scholarship|bursary|financial\s+aid)\b/i,
      /\b(installments|payment\s+plan)\b/i,
      /\b(refund|withdrawal|withdraw)\b/i,
      /\b(student\s+loan|work\s+study)\b/i,
      /\b(fee\s+structure|invoice)\b/i
    ],
    responses: [
      "💰 **Tuition Payment**: Pay your tuition fees through the student portal, bank transfer, or at the finance office. Payment deadlines are strictly enforced.",
      "🎓 **Scholarships**: Apply for scholarships through our financial aid office. Merit-based and need-based scholarships are available. Check deadlines carefully!",
      "📅 **Payment Plans**: Yes, you can pay tuition in installments. Contact the finance office to set up a payment plan before the semester begins.",
      "💸 **Refunds**: Refunds are available if you withdraw before specific deadlines. The refund amount depends on when you withdraw during the semester.",
      "💵 **Student Loans**: Apply for student loans through your country's student loan agency or our recommended financial partners. Our financial aid office can guide you.",
      "📊 **Fee Structure**: Request your fee structure from the finance office or download it from the student portal. It includes tuition, registration, and other applicable fees."
    ]
  },

  // Graduation & Certification
  graduation: {
    patterns: [
      /\b(graduat(e|ion|ing)|degree|certificate)\b/i,
      /\b(ceremony|graduation\s+ceremony)\b/i,
      /\b(diploma|degree\s+certificate)\b/i,
      /\b(requirements|graduation\s+requirements)\b/i,
      /\b(transcript|academic\s+records)\b/i
    ],
    responses: [
      "🎓 **Graduation Application**: Apply for graduation through the student portal at least one semester before your intended graduation date. There's a graduation fee.",
      "📜 **Graduation Requirements**: Complete all required courses, maintain minimum GPA, settle all financial obligations, and submit graduation application on time.",
      "🎉 **Graduation Ceremony**: Graduation ceremonies are held twice yearly (June and December). You'll receive ceremony details via email after graduation approval.",
      "📄 **Degree Certificate**: Your degree certificate will be available 4-6 weeks after graduation. You can collect it in person or request mailed delivery.",
      "✅ **Academic Verification**: Official transcripts and degree verification can be requested through the registrar's office for employers or other institutions."
    ]
  },

  // Student Services & Campus
  services: {
    patterns: [
      /\b(student\s+id|id\s+card|lost\s+id)\b/i,
      /\b(housing|accommodation|dormitory)\b/i,
      /\b(library|books|borrow)\b/i,
      /\b(health\s+center|medical|clinic)\b/i,
      /\b(clubs|organizations|societies)\b/i,
      /\b(counseling|advisor|academic\s+support)\b/i,
      /\b(lost\s+and\s+found|lost\s+item)\b/i
    ],
    responses: [
      "🆔 **Student ID**: Collect your student ID from the student services office with your admission letter and photo ID. Replacement IDs cost a small fee.",
      "🏠 **Housing**: Check our housing office for on-campus accommodation or approved off-campus housing lists. Apply early as spaces are limited!",
      "📚 **Library Services**: The library is open daily with extended hours during exams. Borrow books with your student ID and access online resources through the portal.",
      "🏥 **Health Center**: Our on-campus health center provides basic medical services, counseling, and health education. Emergency services available 24/7.",
      "🎭 **Student Organizations**: Join clubs through the student activities office. Over 50+ clubs available covering academics, sports, culture, and special interests.",
      "🗣️ **Academic Counseling**: Book appointments with academic advisors through the student portal or visit the counseling center for academic and personal support."
    ]
  },

  // Default/Fallback responses
  general: {
    patterns: [
      /\b(hello|hi|hey|greetings)\b/i,
      /\b(help|assist|support)\b/i,
      /\b(thank\s+you|thanks)\b/i,
      /\b(contact|reach|phone|email)\b/i
    ],
    responses: [
      "👋 Hello! I'm your university assistant chatbot. I can help you with admissions, registration, fees, graduation, and campus services. What would you like to know?",
      "🤝 I'm here to help! Ask me about applications, course registration, payments, graduation requirements, or any other university services.",
      "😊 You're welcome! Is there anything else you'd like to know about our university services?",
      "📞 **Contact Information**: \n- Main Office: +1 (555) 123-4567\n- Email: info@university.edu\n- Student Services: studentservices@university.edu\n- Office Hours: Mon-Fri 8AM-5PM"
    ]
  }
};

// Enhanced message display function
function appendMessage(text, sender, isTyping = false) {
  const message = document.createElement('div');
  message.className = `message ${sender}`;
  
  if (isTyping && sender === 'bot') {
    message.innerHTML = `<div class="typing-indicator">
      <span></span><span></span><span></span>
    </div>`;
    chatWindow.appendChild(message);
    chatWindow.scrollTop = chatWindow.scrollHeight;
    
    setTimeout(() => {
      message.innerHTML = text;
    }, 1000);
  } else {
    message.innerHTML = text;
    chatWindow.appendChild(message);
  }
  
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Advanced pattern matching function
function findBestMatch(input) {
  const normalizedInput = input.toLowerCase().trim();
  let bestMatch = null;
  let bestScore = 0;
  let matchedCategory = null;

  // Check each category for pattern matches
  for (const [category, data] of Object.entries(chatbotKnowledgeBase)) {
    for (const pattern of data.patterns) {
      if (pattern.test(normalizedInput)) {
        // Simple scoring based on pattern specificity
        const score = pattern.source.length;
        if (score > bestScore) {
          bestScore = score;
          bestMatch = data.responses;
          matchedCategory = category;
        }
      }
    }
  }

  return { responses: bestMatch, category: matchedCategory, score: bestScore };
}

// Enhanced keyword extraction for better matching
function extractKeywords(input) {
  const keywords = input.toLowerCase()
    .replace(/[^\w\s]/g, '')
    .split(/\s+/)
    .filter(word => word.length > 2);
  
  return keywords;
}

// Main bot response function
function simulateBotResponse(input) {
  appendMessage('', 'bot', true); // Show typing indicator
  
  setTimeout(() => {
    const match = findBestMatch(input);
    
    if (match.responses && match.score > 0) {
      // Select random response from matched category
      const randomResponse = match.responses[Math.floor(Math.random() * match.responses.length)];
      appendMessage(randomResponse, 'bot');
      
      // Add contextual follow-up
      const followUp = getContextualFollowUp(match.category);
      if (followUp) {
        setTimeout(() => {
          appendMessage(followUp, 'bot');
        }, 1500);
      }
    } else {
      // Fallback response with suggestions
      const fallbackResponse = `🤔 I'm not sure about that specific question, but I can help you with:
        
**🎓 Admissions**: Applications, requirements, deadlines
**📚 Registration**: Course enrollment, schedules, transcripts  
**💰 Financial**: Fees, scholarships, payment plans
**🎉 Graduation**: Requirements, ceremonies, certificates
**🏫 Campus Services**: Student ID, housing, library, health center

Try asking about any of these topics!`;
      
      appendMessage(fallbackResponse, 'bot');
    }
  }, 1200);
}

// Contextual follow-up suggestions
function getContextualFollowUp(category) {
  const followUps = {
    admissions: "💡 **Need more help?** Ask about required documents, deadlines, or entry requirements!",
    registration: "💡 **Pro tip**: Remember to check with your academic advisor before making major schedule changes!",
    financial: "💡 **Money matters**: Don't forget to check scholarship deadlines and payment due dates!",
    graduation: "💡 **Planning ahead**: Start your graduation application process early to avoid delays!",
    services: "💡 **Campus life**: Explore our student organizations and support services for a better university experience!"
  };
  
  return followUps[category] || null;
}

// Event listeners
sendBtn.addEventListener('click', () => {
  const text = userInput.value.trim();
  if (text) {
    appendMessage(text, 'user');
    userInput.value = '';
    simulateBotResponse(text);
  }
});

userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendBtn.click();
});

// Initialize with welcome message
window.addEventListener('load', () => {
  setTimeout(() => {
    appendMessage("👋 **Welcome to University Assistant!** 🎓\n\nI can help you with:\n• **Admissions** & Applications\n• **Course Registration** & Schedules\n• **Fees** & Financial Aid\n• **Graduation** Requirements\n• **Campus Services** & Support\n\nWhat would you like to know?", 'bot');
  }, 500);
});

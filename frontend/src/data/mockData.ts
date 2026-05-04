export interface Skill {
  name: string;
  currentLevel: number;
  requiredLevel: number;
  category: string;
}

export interface JobRole {
  id: string;
  title: string;
  category: string;
  requiredSkills: string[];
  avgSalary: string;
  demand: "High" | "Medium" | "Low";
}

export interface RoadmapStep {
  id: string;
  title: string;
  description: string;
  status: "completed" | "in-progress" | "upcoming";
  progress: number;
  estimatedWeeks: number;
  difficulty: "Beginner" | "Intermediate" | "Advanced";
  skills: string[];
  youtubeResources: YoutubeResource[];
}

export interface YoutubeResource {
  id: string;
  title: string;
  channel: string;
  duration: string;
  thumbnail: string;
  views: string;
  url: string;
}

export interface SkillGap {
  skill: string;
  current: number;
  required: number;
  gap: number;
  priority: "Critical" | "High" | "Medium" | "Low";
}

export interface ProgressData {
  month: string;
  score: number;
}

export const jobRoles: JobRole[] = [
  {
    id: "fullstack-developer",
    title: "Full Stack Developer",
    category: "Engineering",
    requiredSkills: ["React", "Node.js", "TypeScript", "PostgreSQL", "AWS", "Docker"],
    avgSalary: "$120k - $180k",
    demand: "High",
  },
  {
    id: "ml-engineer",
    title: "Machine Learning Engineer",
    category: "AI / ML",
    requiredSkills: ["Python", "TensorFlow", "PyTorch", "Statistics", "Data Pipelines", "MLOps"],
    avgSalary: "$140k - $200k",
    demand: "High",
  },
  {
    id: "data-scientist",
    title: "Data Scientist",
    category: "Data",
    requiredSkills: ["Python", "SQL", "Statistics", "Data Visualization", "Machine Learning", "R"],
    avgSalary: "$110k - $170k",
    demand: "High",
  },
  {
    id: "devops-engineer",
    title: "DevOps Engineer",
    category: "Infrastructure",
    requiredSkills: ["AWS", "Docker", "Kubernetes", "CI/CD", "Terraform", "Linux"],
    avgSalary: "$115k - $175k",
    demand: "Medium",
  },
  {
    id: "frontend-developer",
    title: "Frontend Developer",
    category: "Engineering",
    requiredSkills: ["React", "TypeScript", "CSS", "Testing", "Performance", "Accessibility"],
    avgSalary: "$100k - $160k",
    demand: "High",
  },
  {
    id: "backend-developer",
    title: "Backend Developer",
    category: "Engineering",
    requiredSkills: ["Node.js", "Python", "PostgreSQL", "Redis", "System Design", "API Design"],
    avgSalary: "$110k - $170k",
    demand: "High",
  },
];

export const userSkills: Skill[] = [
  { name: "Python", currentLevel: 72, requiredLevel: 90, category: "Programming" },
  { name: "JavaScript", currentLevel: 85, requiredLevel: 80, category: "Programming" },
  { name: "React", currentLevel: 78, requiredLevel: 85, category: "Framework" },
  { name: "Node.js", currentLevel: 65, requiredLevel: 80, category: "Framework" },
  { name: "SQL", currentLevel: 60, requiredLevel: 75, category: "Database" },
  { name: "System Design", currentLevel: 40, requiredLevel: 70, category: "Architecture" },
  { name: "Data Visualization", currentLevel: 55, requiredLevel: 80, category: "Data" },
  { name: "Docker", currentLevel: 45, requiredLevel: 65, category: "DevOps" },
  { name: "TypeScript", currentLevel: 70, requiredLevel: 85, category: "Programming" },
  { name: "Machine Learning", currentLevel: 35, requiredLevel: 75, category: "AI / ML" },
];

export const skillGaps: SkillGap[] = [
  { skill: "System Design", current: 40, required: 70, gap: 30, priority: "Critical" },
  { skill: "Machine Learning", current: 35, required: 75, gap: 40, priority: "Critical" },
  { skill: "Data Visualization", current: 55, required: 80, gap: 25, priority: "High" },
  { skill: "Python", current: 72, required: 90, gap: 18, priority: "High" },
  { skill: "Docker", current: 45, required: 65, gap: 20, priority: "Medium" },
  { skill: "Node.js", current: 65, required: 80, gap: 15, priority: "Medium" },
  { skill: "TypeScript", current: 70, required: 85, gap: 15, priority: "Medium" },
  { skill: "SQL", current: 60, required: 75, gap: 15, priority: "Low" },
];

export const progressHistory: ProgressData[] = [
  { month: "Sep", score: 42 },
  { month: "Oct", score: 48 },
  { month: "Nov", score: 55 },
  { month: "Dec", score: 58 },
  { month: "Jan", score: 65 },
  { month: "Feb", score: 71 },
  { month: "Mar", score: 78 },
];

export const roadmapSteps: RoadmapStep[] = [
  {
    id: "step-1",
    title: "Assess Current Skills",
    description: "Complete the skill assessment to identify your strengths and areas for improvement.",
    status: "completed",
    progress: 100,
    estimatedWeeks: 1,
    difficulty: "Beginner",
    skills: ["Self-Assessment"],
    youtubeResources: [
      {
        id: "yt-1",
        title: "How to Identify Your Skills for Tech Careers",
        channel: "Joshua Fluke",
        duration: "12:34",
        thumbnail: "https://img.youtube.com/vi/Xg9ihH15Uto/mqdefault.jpg",
        views: "245K",
        url: "https://www.youtube.com/watch?v=Xg9ihH15Uto",
      },
    ],
  },
  {
    id: "step-2",
    title: "Python Advanced Mastery",
    description: "Master advanced Python concepts including decorators, generators, async/await, and design patterns.",
    status: "in-progress",
    progress: 60,
    estimatedWeeks: 4,
    difficulty: "Intermediate",
    skills: ["Python", "Design Patterns", "Async Programming"],
    youtubeResources: [
      {
        id: "yt-2",
        title: "Python for Beginners - Full Course",
        channel: "freeCodeCamp",
        duration: "4:26:52",
        thumbnail: "https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg",
        views: "42M",
        url: "https://www.youtube.com/watch?v=rfscVS0vtbw",
      },
      {
        id: "yt-3",
        title: "Python OOP Tutorial - Full Course",
        channel: "Corey Schafer",
        duration: "1:42:11",
        thumbnail: "https://img.youtube.com/vi/ZDa-Z5JzLYM/mqdefault.jpg",
        views: "3.8M",
        url: "https://www.youtube.com/watch?v=ZDa-Z5JzLYM",
      },
      {
        id: "yt-4",
        title: "Python Asyncio - Full Tutorial",
        channel: "Tech With Tim",
        duration: "24:31",
        thumbnail: "https://img.youtube.com/vi/2IW-ZEui4h4/mqdefault.jpg",
        views: "560K",
        url: "https://www.youtube.com/watch?v=2IW-ZEui4h4",
      },
    ],
  },
  {
    id: "step-3",
    title: "System Design Fundamentals",
    description: "Learn core system design concepts including scalability, load balancing, caching, and database sharding.",
    status: "upcoming",
    progress: 0,
    estimatedWeeks: 6,
    difficulty: "Advanced",
    skills: ["System Design", "Architecture", "Scalability"],
    youtubeResources: [
      {
        id: "yt-5",
        title: "System Design for Beginners",
        channel: "Gaurav Sen",
        duration: "25:28",
        thumbnail: "https://img.youtube.com/vi/MbjObHmDbZo/mqdefault.jpg",
        views: "2.1M",
        url: "https://www.youtube.com/watch?v=MbjObHmDbZo",
      },
      {
        id: "yt-6",
        title: "System Design Interview - Step by Step Guide",
        channel: "ByteByteGo",
        duration: "20:22",
        thumbnail: "https://img.youtube.com/vi/i7twT3x5yv8/mqdefault.jpg",
        views: "890K",
        url: "https://www.youtube.com/watch?v=i7twT3x5yv8",
      },
    ],
  },
  {
    id: "step-4",
    title: "Data Structures & Algorithms",
    description: "Master essential DSA topics: arrays, trees, graphs, dynamic programming, and common interview patterns.",
    status: "upcoming",
    progress: 0,
    estimatedWeeks: 8,
    difficulty: "Intermediate",
    skills: ["Algorithms", "Data Structures", "Problem Solving"],
    youtubeResources: [
      {
        id: "yt-7",
        title: "Data Structures Easy to Advanced Course",
        channel: "freeCodeCamp",
        duration: "8:03:59",
        thumbnail: "https://img.youtube.com/vi/RBSGKlAvoiM/mqdefault.jpg",
        views: "8.4M",
        url: "https://www.youtube.com/watch?v=RBSGKlAvoiM",
      },
      {
        id: "yt-8",
        title: "Dynamic Programming for Beginners",
        channel: "NeetCode",
        duration: "52:43",
        thumbnail: "https://img.youtube.com/vi/oBt53YbR9Kk/mqdefault.jpg",
        views: "2.5M",
        url: "https://www.youtube.com/watch?v=oBt53YbR9Kk",
      },
    ],
  },
  {
    id: "step-5",
    title: "Build Portfolio Projects",
    description: "Apply your skills by building real-world projects to showcase in your portfolio and GitHub profile.",
    status: "upcoming",
    progress: 0,
    estimatedWeeks: 4,
    difficulty: "Intermediate",
    skills: ["Full-Stack", "Git", "Deployment"],
    youtubeResources: [
      {
        id: "yt-9",
        title: "Build and Deploy 5 Full Stack Projects",
        channel: "JavaScript Mastery",
        duration: "4:10:05",
        thumbnail: "https://img.youtube.com/vi/GDa8kZLNhJ4/mqdefault.jpg",
        views: "2.8M",
        url: "https://www.youtube.com/watch?v=GDa8kZLNhJ4",
      },
    ],
  },
];

export const youtubeResources: YoutubeResource[] = [
  {
    id: "rec-1",
    title: "Machine Learning for Everybody - Full Course",
    channel: "freeCodeCamp",
    duration: "3:49:02",
    thumbnail: "https://img.youtube.com/vi/i_LwzRVP7bg/mqdefault.jpg",
    views: "4.2M",
    url: "https://www.youtube.com/watch?v=i_LwzRVP7bg",
  },
  {
    id: "rec-2",
    title: "System Design for Beginners - Course",
    channel: "ByteByteGo",
    duration: "1:02:30",
    thumbnail: "https://img.youtube.com/vi/MbjObHmDbZo/mqdefault.jpg",
    views: "2.1M",
    url: "https://www.youtube.com/watch?v=MbjObHmDbZo",
  },
  {
    id: "rec-3",
    title: "Docker Tutorial for Beginners - Full Course",
    channel: "TechWorld with Nana",
    duration: "3:21:17",
    thumbnail: "https://img.youtube.com/vi/3c-iBn73dDE/mqdefault.jpg",
    views: "8.6M",
    url: "https://www.youtube.com/watch?v=3c-iBn73dDE",
  },
  {
    id: "rec-4",
    title: "TypeScript Full Course for Beginners",
    channel: "freeCodeCamp",
    duration: "1:34:40",
    thumbnail: "https://img.youtube.com/vi/30LWjhZzg50/mqdefault.jpg",
    views: "1.9M",
    url: "https://www.youtube.com/watch?v=30LWjhZzg50",
  },
  {
    id: "rec-5",
    title: "Matplotlib Tutorial - Full Course",
    channel: "freeCodeCamp",
    duration: "3:30:50",
    thumbnail: "https://img.youtube.com/vi/3Xc3CA655Y4/mqdefault.jpg",
    views: "1.4M",
    url: "https://www.youtube.com/watch?v=3Xc3CA655Y4",
  },
  {
    id: "rec-6",
    title: "SQL Tutorial - Full Database Course for Beginners",
    channel: "freeCodeCamp",
    duration: "4:20:36",
    thumbnail: "https://img.youtube.com/vi/HXV3zeQKqGY/mqdefault.jpg",
    views: "18M",
    url: "https://www.youtube.com/watch?v=HXV3zeQKqGY",
  },
];

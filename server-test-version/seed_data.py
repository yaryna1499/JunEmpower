from main.models import Project, CustomUser, Specialization, Technology
from django_seed import Seed
from django.db import transaction



seeder = Seed.seeder() #для фейкових проектів та юзерів


it_specializations = {
    "Web Development",
    "Data Science",
    "Machine Learning",
    "Artificial Intelligence",
    "Cybersecurity",
    "Database Administration",
    "Cloud Computing",
    "DevOps",
    "Mobile App Development",
    "Network Engineering",
    "Game Development",
    "UI/UX Design",
    "Digital Marketing",
    "Blockchain Development",
    "System Administration",
    "Software Testing",
    "Embedded Systems",
    "IoT Development",
    "Big Data Analytics",
    "Computer Vision",
    "Natural Language Processing",
    "Front-end Development",
    "Back-end Development",
    "Full-stack Development",
    "Mobile Game Development",
    "Data Engineering",
    "Quantum Computing",
    "Virtual Reality",
    "Augmented Reality",
    "Bioinformatics",
    "Information Security",
    "Ethical Hacking",
    "Data Visualization",
    "Cloud Architecture",
    "Software Engineering",
    "Automation Testing",
    "Network Security",
    "AI Ethics",
    "Computer Graphics",
    "Parallel Computing",
    "Operating Systems",
    "Embedded Programming",
    "Software Architecture",
    "Geographic Information Systems (GIS)",
    "E-commerce Development",
    "Financial Technology (FinTech)",
    "Healthcare IT",
    "Educational Technology (EdTech)",
    "Business Intelligence",
    "Quantitative Analysis",
    "Machine Vision",
    "Cloud Security",
    "Web Design",
    "Natural Language Understanding",
    "Robotics",
    "Data Mining",
    "Digital Forensics",
    "IT Project Management",
    "IT Governance",
    "Cloud Management",
    "Server Administration",
    "Wireless Networking",
    "Compiler Design",
    "Bioinformatics",
    "Computer Animation",
    "Network Programming",
    "Information Retrieval",
    "Algorithm Design",
    "Biohacking",
    "Quantitative Finance",
    "Geospatial Analysis",
    "Cloud Native Development",
    "Human-Computer Interaction",
    "Serverless Computing",
    "Data Governance",
    "Elasticsearch",
    "Software as a Service (SaaS)",
    "Virtualization",
    "Data Warehousing",
    "Video Game Design",
    "Quantum Cryptography",
    "Autonomous Systems",
    "Industrial IoT",
    "Computer Networking",
    "Cryptography",
    "Bioinformatics",
    "Embedded AI",
    "Chatbot Development",
    "Genomic Data Analysis",
    "Distributed Systems",
    "Blockchain Governance",
    "Computer Vision",
    "Quantum Machine Learning",
    "Space Technology",
    "Quantum Physics",
    "Geographic Information Systems (GIS)",
    "Microservices Architecture",
    "Bioinformatics",
    "Wireless Security",
    "High-Performance Computing",
    "Cloud Migration",
    "Computer Science Education",
    "3D Printing Technology",
    "Quantum Algorithms",
    "Genetic Programming",
    "Business Process Automation",
    "Digital Transformation",
    "Video Game Development",
    "Mobile App Design",
    "Hardware Development",
    "Cloud Computing Security",
    "Quantum Robotics",
    "Information Theory",
    "Bioinformatics",
    "Wireless Communication",
    "Quantum Chemistry",
    "Industrial Automation",
    "Bioinformatics",
    "Genomic Medicine",
    "Quantum Computing Hardware",
    "Neuroinformatics",
}

@transaction.atomic
def seed_specializations():
    for item in it_specializations:
        sp = Specialization(
            specialization=item
        )
        sp.save()


def check_seed():
    seeded_specializations = Specialization.objects.all()

    return seeded_specializations





















import json
import random

# Generate a random name
def generate_random_name():
  first_names = ["John", "Jane", "Peter", "Mary", "David", "Sarah", "Michael", "Susan", "William", "Elizabeth", "Robert", "Linda"]
  last_names = ["Doe", "Smith", "Jones", "Williams", "Brown", "Johnson", "Taylor", "Martin", "Anderson", "Davis", "Miller", "Wilson"]

  return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_people_list():
  people = []

  # Generate 300 data consultants
  data_consultants = []
  for i in range(300):
    data_consultant = {
      "full_name": generate_random_name(),
      "job_title": random.choice(["Data Architect", "Data Engineer", "Data Scientist"]),
      "division": "Data & Analytics",
      "department": random.choice(["Enterprise Data Architecture", "Data Engineering", "Data Science"]),
      "certifications": [random.choice(["Certified Data Architect (CDA)", 'Azure DP-100', "Apache Spark Certified Professional", "Azure Data Engineer","Google Certified Professional Cloud Data Engineer"]), random.choice(["TOGAF 9 Foundation", "AWS Certified Data Engineer", "Microsoft Certified: Azure Data Scientist Associate", "Cloudera CCA"])],
      "advanced_skills": [random.choice(["Data modeling", "Data warehouse design", "Data integration", "Big data technologies"]), random.choice(["SQL", "NoSQL", "Cloud computing platforms"]), random.choice(["Machine learning", "Deep learning", "Statistical analysis", "Data visualization"])],
      "intermediate_skills": [random.choice(["SQL", "Python", "Java"]), random.choice(["R", "Scala", "Spark"]), random.choice(["Linear algebra", "Calculus", "Statistics"])],
      "basic_skills": [random.choice(["Programming languages", "Communication skills", "Problem-solving skills"]), random.choice(["Version control systems", "Communication skills", "Problem-solving skills"]), random.choice(["Communication skills", "Problem-solving skills", "Analytical skills"])]
    }
    data_consultants.append(data_consultant)

  # Generate 100 managing consultants, cyber security consultants, technical consultants and enterprise architects
  other_consultants = []
  for i in range(100):
    consultant = {
      "full_name": generate_random_name(),
      "job_title": random.choice(["Managing Consultant", "Cyber Security Consultant", "Technical Consultant", "Enterprise Architect"]),
      "division": random.choice(["Consulting", "Security", "Technology", "Architecture"]),
      "department": random.choice(["Strategy & Operations", "Network Security", "Cloud Engineering", "Solutions Architecture"]),
      "certifications": [random.choice(["Project Management Professional (PMP)", "Certified Business Analysis Professional (CBAP)"]), random.choice(["Certified Information Systems Security Professional (CISSP)", "GIAC Security Essentials Certification (GSEC)"]), random.choice(["TOGAF 9 Foundation", "AWS Certified Solutions Architect - Professional"]), random.choice(["Certified Enterprise Architect (CEA)", "TOGAF 9 Certified Architect"])],
      "advanced_skills": [random.choice(["Change management", "Business process improvement", "Risk management", "Stakeholder management"]), random.choice(["Vulnerability assessment and penetration testing", "Security incident response", "Security architecture", "Risk management"]), random.choice(["Cloud computing platforms", "Containerization", "DevOps", "Microservices"]), random.choice(["Enterprise architecture design", "Solution architecture design", "System integration", "Business architecture"])],
      "intermediate_skills": [random.choice(["Financial modeling", "Data analysis", "Presentation skills"]), random.choice(["Networking", "Operating systems", "Security tools"]), random.choice(["SQL", "Python", "Java"]), random.choice(["UML", "BPMN", "ArchiMate"])],
      "basic_skills": [random.choice(["Microsoft Office Suite", "Communication skills", "Problem-solving skills"]), random.choice(["Communication skills", "Problem-solving skills", "Analytical skills"]), random.choice(["Programming languages", "Communication skills", "Problem-solving skills"]), random.choice(["Communication skills", "Problem-solving skills", "Teamwork skills"])]
    }
    other_consultants.append(consultant)

  # Combine the two lists
  people.extend(data_consultants)
  people.extend(other_consultants)

  return people

def main():
    with open("data/people.json", "w") as f:
       json.dump(generate_people_list(), f, indent=4)


if __name__ == "__main__":
  main()
import json
import datetime
def extract_skills():
	technology=[]
	skills = []
	unique_skills=set()
	file = open('skills.json')
	data = json.load(file)
	for tech in data['technologies']:
		technology.append(tech['technology'])
		skill_list = []
		for skill in tech['skills'].split(','):
			skill_list.append(skill.strip())
		skills.append(skill_list)
		unique_skills.update(skill_list)
	return technology, skills, unique_skills
def exract_roles():
	role_summaries = []
	pu_role_summaries = []
	companies = []
	tasks = []
	tags = []
	unique_tags = set()
	file = open('roles.json')
	data = json.load(file)
	for role in data['roles']:
		if role['preuni']==False:
			role_summaries.append([role['company'],role['role'],role['start'],role['end']])
		else:
			pu_role_summaries.append([role['company'],role['role'], role['start'],role['end']])
		for task in role['tasks']:
			companies.append(role['company'])
			tasks.append(task['task'])
			skills_list = []
			for skill in task['skills'].split(','):
				skills_list.append(skill.strip())
			tags.append(skills_list)
			unique_tags.update(skills_list)
	return role_summaries, pu_role_summaries, companies, tasks, tags, unique_tags
def extract_courses():
	degree_summaries=[]
	degrees=[]
	courses=[]
	grades = []
	tags = []
	unique_tags=set()
	file=open('degrees.json')
	data = json.load(file)
	for degree in data['degrees']:
		degree_summaries.append([degree['degree'], degree['major'], degree['university'], degree['start'], degree['end'],degree['WAM']])
		for course in degree['courses']:
			degrees.append(degree['degree'])
			courses.append(course['course'])
			grades.append(course['grade'])
			tag_list =[]
			for tag in course['tags'].split(','):
				tag_list.append(tag.strip())
			tags.append(tag_list)
			unique_tags.update(tag_list)
	return degree_summaries,degrees,courses,grades,tags, unique_tags
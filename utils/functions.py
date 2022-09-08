import json


def load_candidates_from_json(file: str) -> list[dict]:
	"""Return list with dicts of candidates from JSON file"""
	with open(file, 'r', encoding='utf-8') as f:
		data = json.load(f)
		return data


def get_candidate(id_: int, data: list[dict]) -> dict | None:
	"""Return candidate for given id, or None if not found"""
	for candidate in data:
		if id_ == candidate['id']:
			return candidate
	return None


def get_candidates_by_name(candidate_name: str, data: list[dict]) -> list[dict]:
	"""Return list of candidates for given name"""
	candidate_list = []
	for candidate in data:
		if candidate_name.lower() == candidate['name'].lower().split()[0]:
			candidate_list.append(candidate)
	return candidate_list


def get_candidates_by_skills(skill_name: str, data: list[dict]) -> list[dict]:
	"""Return list of candidates for given skill"""
	candidate_list = []
	for candidate in data:
		if skill_name.lower() in candidate['skills'].lower().split(', '):
			candidate_list.append(candidate)
	return candidate_list

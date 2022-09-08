from flask import Flask, render_template, request, redirect, url_for
from utils import functions as f

FILE = 'data/candidates.json'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page with candidates"""
    if request.method == 'POST':
        # TODO: error if form is empty
        name: str = request.form.get('name')
        skill_: str = request.form.get('skill')
        if name:
            return redirect(url_for('search', candidate_name=name))
        elif skill:
            return redirect(url_for('skill', skill_name=skill_))
    return render_template('list.html', title='Candidates', candidates=data)


@app.route('/candidate/<int:id_>/')
def profile(id_):
    """Page with candidate profile"""
    candidate: dict | None = f.get_candidate(id_, data)
    if candidate:
        return render_template('candidate.html', title=candidate['name'],
                               candidate=candidate)
    return 'Кандидат не найден'


@app.route('/search/<candidate_name>/')
def search(candidate_name):
    """Search for a candidate matching the given candidate name"""
    candidate_list: list[dict] = f.get_candidates_by_name(candidate_name, data)
    return render_template('search.html', title='Search',
                           candidate_list=candidate_list)


@app.route('/skill/<skill_name>/')
def skill(skill_name):
    """Search for a skill matching the given skill name"""
    skill_list: list[dict] = f.get_candidates_by_skills(skill_name, data)
    return render_template('skill.html', title='Skill', skill_name=skill_name,
                           skill_list=skill_list)


@app.route('/cat/')
def cat():
    """Page with self information"""
    return render_template('cat.html')


data: list[dict] = f.load_candidates_from_json(FILE)

if __name__ == '__main__':
    app.run(debug=True)

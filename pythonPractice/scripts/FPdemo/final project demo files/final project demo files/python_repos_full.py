import requests, re
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
 
for repo_dict in repo_dicts:
    if repo_dict['name'] == 'httpie' or \
    repo_dict['name'] == 'django' or \
    repo_dict['name'] == 'flask':
        names.append(repo_dict['name'])
        plot_dicts.append({'value': repo_dict['stargazers_count'], #height of bar \
                           'label': re.split("[–|,|.]",repo_dict['description'])[0],#pull '-' from shell! \
                           'xlink': repo_dict['html_url'] #try that hyperlink
                          })
        print(plot_dicts)
        #print(repo_dict['description'],repo_dict['stargazers_count'])
 
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    '''plot_dicts.append(plot_dict)
    '''
#for k,v in repo_dict.items():
    #print(k,v)
'''
hard code results for brevity of description, etc.
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
    ]
'''
# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.force_uri_protocol = 'http'
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15 #shown below
my_config.show_y_guides = False
my_config.width = 500

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Top *** Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
 
chart.render_to_file('python_repos4.svg')

from bs4 import BeautifulSoup
import json
from os import path

class projectsWriter():

    def __init__(self, htmlPath: str, configsPath: str) -> None:
        
        with open(htmlPath, encoding='utf-8') as f:
            self.doc = BeautifulSoup(f, 'html.parser')
        
        with open(configsPath, encoding='utf-8') as f:
            self.projects = json.load(f)['Projects']


    def create_projects(self):

        i = 0
        for project in self.projects:

            title = project['title'].replace(" ", "_")
            card = f"""
                <li class="project_card" id="{title}" onclick="openProject({i})">
                    <div class="content">
                        <div class="imgBox">
                            <img src="{self.url_for(project['mainImage'])}" alt="{title} image">
                        </div>
                        <div class="project_card_desc">
                            <img class="icon" src="{self.url_for(project['icon'])}">
                            <h2>{project['title']}</h2>
                        </div>
                    </div>
                </li>
            """

            card = BeautifulSoup(card, "html.parser")
            self.doc.find("ul", {'id':'projects_carousel'}).append(card)

            menu_icon = f"""
                <li class="menu_item" onclick="openProject({i})">
                    <img class="icon" src="{self.url_for(project['icon'])}">
                </li>
            """
            menu_icon = BeautifulSoup(menu_icon, "html.parser")
            self.doc.find("ul", {'id':'popup_menu'}).append(menu_icon)


            desc = f"""
                <div class="project content">
                    <aside class="logo_side">
                        <img class="icon" src="{self.url_for(project['icon'])}">
                    </aside>
                    <article>
                        <h1>{project['title']}<i class="flicker">_</i></h1>
                        <p>{project['description']}</p>
                        {self.add_technologies(project['technologies'])}
                        {self.add_technologies(project['partners'], True)}
                    </article>
                    <aside class="media_column">
                        {self.add_media(project['videos'], project['images'])}
                    </aside>
                </div>
            """

            desc = BeautifulSoup(desc, "html.parser")

            if project['has_demo']:
                demo_btn = f"""
                <form action="{project['action']}" method="post">
                    <button>
                        Demonstração
                        <div class="flicker">
                        </div>           
                    </button>
                </form>
                """
                demo_btn = BeautifulSoup(demo_btn, 'html.parser')
                desc.find("article").append(demo_btn)
            self.doc.find("section", {'id':'projects_popup'}).append(desc)
            
            i += 1

        first_menuItem = self.doc.find('li', {'class':'menu_item'})
        first_project = self.doc.find('div', {'class':'project content'})

        first_menuItem['class'] = first_menuItem.get('class', []) + ['active']
        first_project['class'] = first_project.get('class', []) + ['active']
        

    def add_technologies(self, technologies:list, is_partner:bool = False):

        if len(technologies) <= 0:
            return ''

        tech = ""
        for tech_icon in technologies:
            name = path.basename(tech_icon)
            tech += f"""<img src="{self.url_for(tech_icon)}" alt="{name} image">\n"""

        if not is_partner:
            return f"""
                <h2>Tecnologias:</h2>
                <div id="technologies">
                    {tech}
                </div>
            """
        else:
            return f"""
                <h2>Parceiros:</h2>
                <div id="partners">
                    {tech}
                </div>
            """


    def add_media(self, videos:list, images:list):

        if len(videos) <= 0 and len(images) <= 0:
            return ''
        
        html = ""
        for video in videos:
            html += f"""<video src="{self.url_for(video)}" controls></video>\n"""
            
        for img in images:
            name = path.basename(img)
            html += f"""<img src="{self.url_for(img)}" alt="{name} image">\n"""

        return f"""
        <h1>Mídia</h1>
        <div class="media_content">
            {html}
        </div>
        """


    def url_for(self, path:str, folder: str = 'static'):
        return "{{ " + f"url_for('{folder}', filename='{path}')" + " }}"


    def create(self, filepath:str):

        print("\n\t\033[92;1mGerando documento com os projetos . . .\033[0m\n")
        self.create_projects()

        self.doc.prettify()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(self.doc))


if __name__ == '__main__':
    projectsWriter('templates/template.html', 'config.json').create('out.html')
    
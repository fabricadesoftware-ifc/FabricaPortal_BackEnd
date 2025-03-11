import random
from uuid import uuid4
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

from core.uploader.models import Image
from core.portal.models import Member, Course, CourseMember, Area, Project, New
from core.authentication.models import User

fake = Faker("pt_BR")

class Command(BaseCommand):
    help = "Popula o banco de dados com dados fictícios para Project, New, Member, Course, CourseMember, Area e User."

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando a população do banco de dados...")

        # 1. Cria imagens (usando os campos 'file', 'public_id' e 'description')
        images = []
        for _ in range(10):
            img = Image.objects.create(
                file="sample",  # Substitua por um valor adequado, se necessário
                public_id=str(uuid4()),
                description=fake.text(max_nb_chars=20)
            )
            images.append(img)
        self.stdout.write("Imagens criadas.")

        # 2. Cria usuários (User)
        User = get_user_model()
        if User.objects.count() == 0:
            for _ in range(5):
                User.objects.create_user(
                    email=fake.unique.email(),
                    password="123456",
                    name=fake.name()
                )
            self.stdout.write("Usuários criados.")
        users = list(User.objects.all())

        # 3. Cria membros (Member)
        member_types = ["Docente", "Discente", "TAE", "Externo"]
        member_status = ["Ativo", "Inativo", "Egresso"]
        members = []
        for _ in range(10):
            member = Member.objects.create(
                name=fake.name(),
                social_media={"linkedin": fake.url()},
                type=random.choice(member_types),
                status=random.choice(member_status),
                biography=fake.text(),
                image=random.choice(images)
            )
            members.append(member)
        self.stdout.write("Membros criados.")

        # 4. Cria cursos (Course)
        courses = []
        for _ in range(5):
            course = Course.objects.create(
                name=fake.word().capitalize()
            )
            courses.append(course)
        self.stdout.write("Cursos criados.")

        # 5. Cria associações de CourseMember (ligando Member e Course)
        for member in members:
            # Cada membro associado a 1 a 3 cursos aleatoriamente
            selected_courses = random.sample(courses, random.randint(1, 3))
            for course in selected_courses:
                CourseMember.objects.create(
                    member=member,
                    course=course,
                    initial_year=random.randint(2010, 2020),
                    final_year=random.choice([random.randint(2021, 2023), None])
                )
        self.stdout.write("Associações de CourseMember criadas.")

        # 6. Cria áreas (Area)
        areas = []
        for _ in range(5):
            area = Area.objects.create(
                name=fake.word().capitalize(),
                course=random.choice(courses)
            )
            areas.append(area)
        self.stdout.write("Áreas criadas.")

        # 7. Cria projetos (Project) garantindo relação com membros, áreas e imagens
        project_states = ["Não Iniciado", "Em Desenvolvimento", "Concluído", "Cancelado"]
        projects = []
        for _ in range(5):
            # Seleciona ao menos uma área para o projeto
            selected_areas = random.sample(areas, random.randint(1, len(areas)))
            project = Project.objects.create(
                name=fake.sentence(nb_words=3),
                initial_date=fake.date_this_decade(),
                final_date=fake.date_this_decade(),
                # Armazena os nomes das áreas no JSONField
                areas={"areas": [area.name for area in selected_areas]},
                advisor=random.choice(members),  # O advisor é um membro
                state=random.choice(project_states),
                image=random.choice(images),     # Garante que haja uma imagem associada
                links={"website": fake.url()},
                about=fake.text()
            )
            # Associa ao projeto pelo menos um membro via ManyToManyField
            selected_members = random.sample(members, random.randint(1, len(members)))
            project.members.set(selected_members)
            projects.append(project)
        self.stdout.write("Projetos criados.")

        # 8. Cria notícias (New)
        news_count = 5
        for _ in range(news_count):
            new_obj = New.objects.create(
                title=fake.sentence(nb_words=6),
                subject=fake.word(),
                description=fake.text(),
                author=random.choice(users),
                members={"info": fake.word()},
                areas={"area": fake.word()},
                courses={"course": fake.word()},
                tags={"tag": fake.word()}
            )
            # Associa imagens usando o método .set() para ManyToManyField
            new_obj.images.set(random.sample(images, random.randint(1, min(3, len(images)))))
        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))

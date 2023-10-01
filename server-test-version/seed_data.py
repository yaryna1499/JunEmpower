from main.models import Project, CustomUser, Specialization, Technology, ProjectImage
from django_seed import Seed
from django.db import transaction
import pandas as pd
import re
from random import sample, choice, randint
import os
import cloudinary

seeder = Seed.seeder()  # для фейкових проектів та юзерів

specializations = pd.read_csv("sp.csv", header=0, index_col=False, dtype={"Title": str})
technologies = pd.read_csv("tech.csv", header=0, index_col=False, dtype={"Title": str})


@transaction.atomic
def seed_specializations():
    for item in specializations.Title:
        sp = Specialization(title=item, slug=re.sub("[/()\s\_]", "-", item.lower()))
        sp.save()


@transaction.atomic
def seed_tech():
    for item in technologies.Title:
        try:
            if "+" in item:
                slug = re.sub("\+", "-plus", item.lower())
                tech = Technology(title=item, slug=re.sub("[/()\s\_\.]", "-", slug))
            elif "#" in item:
                slug = re.sub("#", "-sharp", item.lower())
                tech = Technology(title=item, slug=re.sub("[/()\s\_\.]", "-", slug))

            else:
                tech = Technology(
                    title=item, slug=re.sub("[/()\s\_\.]", "-", item.lower())
                )
        finally:
            tech.save()


used_usernames = set()


def generate_unique_username():
    while True:
        username = seeder.faker.user_name()
        if username not in used_usernames:
            used_usernames.add(username)
            return username


used_emails = set()


def generate_unique_email():
    while True:
        email = seeder.faker.email()
        if email not in used_emails:
            used_emails.add(email)
            return email


def select_random_avatar():
    path = "media/fake_avatar"
    if os.path.exists(path) and os.path.isdir(path):
        files = os.listdir(path)
        random_avatar = choice(files)
        return os.path.join(path, random_avatar)
    else:
        return None


def seed_users():
    # Отримуємо всі наявні спеціалізації з таблиці Specialization
    all_specializations = list(
        Specialization.objects.all().values_list("pk", flat=True)
    )
    seeder.add_entity(
        CustomUser,
        50,
        {
            "first_name": lambda x: seeder.faker.first_name(),
            "last_name": lambda x: seeder.faker.last_name(),
            "username": lambda x: generate_unique_username(),
            "email": lambda x: generate_unique_email(),
            "password": lambda x: seeder.faker.password(),
            "is_superuser": lambda x: 0,
            "profile_picture": lambda x: choice([select_random_avatar(), None]),
        },
    )
    inserted_pks = seeder.execute()

    for pk in inserted_pks[CustomUser]:
        user = CustomUser.objects.get(pk=pk)
        random_specializations = sample(
            all_specializations, k=3
        )  # Вибираємо 3 рандомні спеціалізації
        user.specialization.set(
            random_specializations
        )  # Use .set() to assign the many-to-many relationship


def generate_tags():
    pass


def select_random_picture():
    path = "media/fake_pr_pict"
    if os.path.exists(path) and os.path.isdir(path):
        files = os.listdir(path)
        random_avatar = choice(files)
        return os.path.join(path, random_avatar)
    else:
        return None


def seed_projects():
    all_users = list(CustomUser.objects.all().values_list("pk", flat=True))
    seeder.add_entity(
        Project,
        100,
        {
            "title": lambda x: seeder.faker.sentence(),
            "description": lambda x: seeder.faker.paragraph(),
            "tags": lambda x: generate_tags(),
            "link_hub": lambda x: seeder.faker.url(),
            "link_deploy": lambda x: seeder.faker.url(),
            "status": lambda x: choice(["completed", "in_development"]),
        },
    )

    inserted_data = seeder.execute()
    inserted_pks = inserted_data[Project]

    for pk in inserted_pks:
        project = Project.objects.get(pk=pk)
        random_author_pk = choice(
            all_users
        )  # Виберіть випадковий ідентифікатор користувача
        random_author = CustomUser.objects.get(
            pk=random_author_pk
        )  # Отримайте екземпляр користувача за його ідентифікатором
        project.author = (
            random_author  # Присвоєння екземпляра користувача полю project.author
        )
        project.save()


def seed_pr_images():
    all_projects = list(Project.objects.all().values_list("pk", flat=True))
    seeder.add_entity(
        ProjectImage,
        25,
        {
            "project": lambda x: Project.objects.get(pk=choice(all_projects)),
            "image": lambda x: choice([select_random_picture(), None]),
        },
    )

    seeder.execute()


def seed_pr_tech():
    all_tech= list(Technology.objects.all().values_list("pk", flat=True))
    projects_pks = list(Project.objects.all().values_list("pk", flat=True))


    for pk in projects_pks:
        project = Project.objects.get(pk=pk)
        random_tech = sample(
            all_tech, k=randint(2,8)
        )
        project.technology.set(
            random_tech
        ) 


if __name__ == "__main__":
    seed_users()
    seed_projects()
    seed_pr_images()

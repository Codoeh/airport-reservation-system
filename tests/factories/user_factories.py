import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "pass1234")

    @factory.post_generation
    def password(self, create, data, **kwargs):
        if data:
            self.set_password(data)
            if create:
                self.save()

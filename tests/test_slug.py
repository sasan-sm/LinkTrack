from django.test import TestCase
from links.models import ShortLink, generate_unique_slug


class SlugTest(TestCase):

    def test_slug_lenght(self):
        slug = generate_unique_slug()
        self.assertEqual(len(slug), 6)

    def test_slug_unique(self):

        link1 = ShortLink.objects.create(
            original_url='http://example.com/1',
            slug=generate_unique_slug()
        )

        link2 = ShortLink.objects.create(
            original_url='http://example.com/2',
            slug=generate_unique_slug()
        )

        self.assertNotEqual(link1.slug, link2.slug)

    def test_collision_handling(self):

        slug1 = generate_unique_slug()
        ShortLink.objects.create(
            original_url="https://example.com/1",
            slug=slug1
        )

        slug2 = generate_unique_slug()
        self.assertNotEqual(slug1, slug2)

        self.assertFalse(ShortLink.objects.filter(slug=slug2).exists())
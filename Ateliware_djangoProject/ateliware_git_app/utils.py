from .models import TbLanguages


def register_languages():
    """
    This function registers five linguages (chosen by author) into TbLanguages,
    if they aren´t yet.
    """
    languages = ['CSS', 'HTML', 'JavaScript', 'Python', 'Flutter']
    for lang in languages:
        if not(TbLanguages.objects.filter(language=lang)):
            TbLanguages(language=lang).save()


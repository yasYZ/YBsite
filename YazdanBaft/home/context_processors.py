from home.models import SiteSeoTool


def seo_context_processor(request):
    return {'seo': SiteSeoTool.objects.all()}

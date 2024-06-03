def seo_context_processor(request):
    from home.models import SiteSeoTool
    return {'seo': SiteSeoTool.objects.all()}

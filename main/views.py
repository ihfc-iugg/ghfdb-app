from django.views.generic import DetailView, TemplateView
from main.mixins import DownloadMixin 
from database.models import Site
from publications.models import Publication
from .filters import MapFilter
from .forms import DownloadWithChoicesForm
from mapping.forms import MapSettingsForm
from meta.views import Meta
from main.tables import IntervalTable, HeatProductionTable, ConductivityTable, TemperatureTable
from django.views.decorators.http import require_POST
from main.forms import SiteForm

class WorldMap(DownloadMixin, TemplateView):
    template_name = 'mapping/application.html'
    filter = MapFilter
    download_form = DownloadWithChoicesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            filter=self.filter(),
            download_form=self.download_form(),
            settings=MapSettingsForm(),
            ))

        context['meta'] = Meta(
            title='World Map | ThermoGlobe',
            description='Interactive search and download of all data within the ThermoGlobe database. The fastest wasy to find published and unpublished thermal data related to studies of the Earth.',
            keywords=['heat flow',' thermal gradient', 'thermal conductivity','temperature','heat production','ThermoGlobe','data','access']
        )
        return context




class SiteView(DownloadMixin, DetailView):
    template_name = "main/site_details.html"
    model = Site
    fieldset = [ 
        (None, 
            {'fields': [
                'name',
                ('lat','lng'),
                'elevation',
                ]}),
        ("Heat Flow", 
            {'fields': [
                'q',
                'q_unc',
                'method',
                'env',
                'expl',
                'wat_temp',
                'q_comment',
                ]}),
        ('Geographic',
            {'fields': [ 
                'country',
                'political',
                'continent',
                'ocean',
                'province',
                'plate',
                ]}),
            ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = [IntervalTable(self.get_object())]
        context['meta'] = self.get_object().as_meta(self.request)
        context['fieldset'] = self.get_fieldset()
        return context


    def get_fieldset(self):
        obj = self.get_object()
        fieldset = {}
        for fset in self.fieldset:
            fieldset[fset[0]] = []
            for k in fset[1]['fields']:
                if isinstance(k, str):
                    fieldset[fset[0]].append({obj._meta.get_field(k).verbose_name: getattr(obj, k)})
                else:
                    fieldset[fset[0]].append({obj._meta.get_field(sub_k).verbose_name: getattr(obj, sub_k) for sub_k in k})

        return fieldset

    def get_queryset(self):
        return (super().get_queryset()
            .prefetch_related('references')
            .select_related('country','continent','political','province','ocean','plate'))

    def download(self, request, *args, **kwargs):
        response, zf = self.prepare_zip_response(fname=self.get_object())

        references = Publication.objects.none()
        for key, qs in self.get_object().get_data().items():
            if key == 'intervals' and qs.exists():
                # create a csv file and save it to the zip object
                zf.writestr(f"{key}.csv", qs.values_list().to_csv_buffer())
                sites = Site.objects.filter(**{f"{key}__in":qs})
            elif qs.exists():
                # create a csv file and save it to the zip object
                zf.writestr(f"{key}.csv", qs.explode_values().to_csv_buffer())
                sites = Site.objects.filter(**{f"{key}_logs__in":qs})

            references = references | Publication.objects.filter(sites__in=sites).distinct()
        
        # write references to .bib file
        if references:
            zf.writestr(f'{self.get_object()}.bib', self.references_to_bibtex(references))

        return response

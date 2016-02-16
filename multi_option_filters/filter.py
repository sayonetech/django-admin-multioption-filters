from django.contrib import admin
from django.contrib.admin.utils import get_model_from_relation
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _


class MultipleOptionFilter(admin.FieldListFilter):
    template = 'multi_option_filters/filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = '%s__in' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg)
        super(MultipleOptionFilter, self).__init__(
            field, request, params, model, model_admin, field_path)
        self.request = request

    def expected_parameters(self):
        return [self.lookup_kwarg]

    def choices(self, cl):
        yield {
            'selected': self.lookup_val is None,
            'query_string': cl.get_query_string({}, [self.lookup_kwarg]),
            'display': _('All')
        }
        if self.lookup_val:
            lookup_values = self.lookup_val.split(',')
        else:
            lookup_values = []
        for lookup, title in self.field.flatchoices:

            yield {
                'lookup_kwarg': self.lookup_kwarg,
                'selected': smart_text(lookup) in lookup_values,
                'query_string': lookup,
                'display': title,
            }

    @property
    def other_fields(self):
        query_dict = self.request.GET
        for field in query_dict.iterkeys():
            if field != self.lookup_kwarg:
                valuelist = query_dict.getlist(field)
                for item in valuelist:
                    yield {
                        'lookup_kwarg': field,
                        'value': item
                    }


class MultipleOptionRelatedFieldListFilter(admin.RelatedFieldListFilter):
    template = 'multi_option_filters/filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        other_model = get_model_from_relation(field)
        if hasattr(field, 'rel'):
            rel_name = field.rel.get_related_field().name
        else:
            rel_name = other_model._meta.pk.name
        self.lookup_kwarg = '%s__%s__in' % (field_path, rel_name)
        self.lookup_kwarg_isnull = '%s__isnull' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg)

        self.lookup_val_isnull = request.GET.get(self.lookup_kwarg_isnull)
        self.lookup_choices = field.get_choices(include_blank=False)
        super(admin.RelatedFieldListFilter, self).__init__(
            field, request, params, model, model_admin, field_path)
        if hasattr(field, 'verbose_name'):
            self.lookup_title = field.verbose_name
        else:
            self.lookup_title = other_model._meta.verbose_name
        self.title = self.lookup_title
        self.request = request

    def choices(self, cl):
        yield {
            'selected': self.lookup_val is None and not self.lookup_val_isnull,
            'query_string': cl.get_query_string({},
                [self.lookup_kwarg, self.lookup_kwarg_isnull]),
            'display': _('All'),
        }
        if self.lookup_val:
            lookup_values = self.lookup_val.split(',')
        else:
            lookup_values = []
        for pk_val, val in self.lookup_choices:
            yield {
                'lookup_kwarg': self.lookup_kwarg,
                'selected': smart_text(pk_val) in lookup_values,
                'query_string': pk_val,
                'display': val,
            }

    @property
    def other_fields(self):
        query_dict = self.request.GET
        for field in query_dict.iterkeys():
            if field != self.lookup_kwarg:
                valuelist = query_dict.getlist(field)
                for item in valuelist:
                    yield {
                        'lookup_kwarg': field,
                        'value': item
                    }
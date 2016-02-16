.. |...| unicode:: U+2026   .. ellipsis

===================
django-admin-multioption-filters
===================

Add the option to filter by multiple fields in Django admin.


Install
=======

- add 'multi_option_filters' to your INSTALLED_APPS
- add ``(r'^dynamicforms/', include('dynamicforms.urls'))`` to your ``urls.py``
- In your app's admin.py add
		
		from multi_option_filters.filter import MultipleOptionRelatedFieldListFilter
		
    class BookAdmin(admin.ModelAdmin):
    list_filter = (('author', MultipleOptionRelatedFieldListFilter),)
    list_display = ('__unicode__', 'author')
    class Media:
        js = (
            '/static/multi_option_filters/multi-option-filter-admin.js',
        )
        

.. vim: ft=rst

.. |...| unicode:: U+2026   .. ellipsis

===================
django-admin-multioption-filters
===================

Add the option to filter by multiple fields in Django admin.


Install
=======

- add 'multi_option_filters' to your INSTALLED_APPS

Example Usage
=======

.. code:: python

    # myapp/models.py
    # ============
    class Author(models.Model):
        name = models.CharField('Name', max_length=50)

        def __unicode__(self):
            return '%s' %self.name
        
        class Meta:
            verbose_name = "Author"
            verbose_name_plural = "Authors"
        



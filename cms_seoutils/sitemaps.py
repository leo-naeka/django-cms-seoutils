# -*- coding: utf-8 -*-
from copy import deepcopy

from cms.models import Title
from cms.sitemaps import CMSSitemap
from cms_seoutils.i18n import get_alternate


class CMSI18nSitemap(CMSSitemap):

    def items(self):
        all_titles = Title.objects.public().filter(page__login_required=False)
        for title in all_titles:
            title.alternates = [alt for lang, alt in get_alternate(title.page,
                protocol=self.protocol).iteritems()]
        return all_titles
